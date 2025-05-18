from typing import Dict, List, Any, Optional, Literal, Union
from pydantic import BaseModel, Field
import logging
from enum import Enum
import json
from anthropic import Anthropic

logger = logging.getLogger(__name__)

# Enums for structured choices
class FilterType(str, Enum):
    EQUALS = "equals"
    CONTAINS = "contains"
    EXISTS = "exists"

class FilterOperation(str, Enum):
    AND = "AND"
    OR = "OR"

# Models for structured data
class FilterCondition(BaseModel):
    field: str
    type: FilterType
    value: Optional[str] = None
    operation: FilterOperation = FilterOperation.AND
    include: bool = True

class QueryIntent(BaseModel):
    dataset_info: bool = Field(False, description="Whether to search dataset metadata")
    file_metadata: bool = Field(False, description="Whether to search file metadata")
    file_content: bool = Field(False, description="Whether to search file content")
    summary: bool = Field(False, description="Whether to provide a summary of the content")
    filters: List[FilterCondition] = Field(default_factory=list, description="Filters to apply to the search")
    fields: List[str] = Field(default_factory=list, description="Fields to return in the response")
    is_dataset_related: bool = Field(True, description="Whether the query is related to dataset search")
    needs_clarification: bool = Field(False, description="Whether the query needs clarification")
    clarification_message: Optional[str] = Field(None, description="Message to ask for clarification")
    max_files: int = Field(10, description="Maximum number of files to return (between 5 and 25)")

class PydanticAIQueryIntentExtractor:
    def __init__(self, claude_api_key, metadata_fields=None):
        self.client = Anthropic(api_key=claude_api_key)
        self.metadata_fields = metadata_fields or []
        
    def extract_query_intent(self, query: str) -> Dict[str, Any]:
        """Extract search intent from user query to determine which indexes to search using Pydantic AI"""
        
        # Default intent for fallback
        default_intent = QueryIntent(
            dataset_info=False,
            file_metadata=False,
            file_content=False,
            summary=False,
            fields=[],
            filters=[],
            is_dataset_related=True,
            needs_clarification=False,
            clarification_message=None,
            max_files=10
        )
        
        try:
            # Build the prompt for query intent extraction
            prompt = self._build_intent_extraction_prompt(query)
            
            # Call Claude to extract structured intent
            response = self.client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1000,
                temperature=0,
                system="""You are a helpful AI assistant that extracts structured information from user queries about datasets.
                You should respond with valid JSON that matches the structure defined in the prompt.
                Extract the most accurate intent possible from the query.""",
                messages=[{"role": "user", "content": prompt}]
            )
            
            # Extract JSON from the response
            extracted_json = self._extract_json_from_response(response.content[0].text)
            
            if not extracted_json:
                logger.warning("Failed to extract JSON from response")
                return default_intent.model_dump()
            
            # Parse and validate the extracted JSON
            try:
                # Ensure max_files is between 5 and 25
                if "max_files" in extracted_json:
                    extracted_json["max_files"] = max(5, min(25, extracted_json["max_files"]))
                
                # Apply fallback heuristics for content requests
                extracted_json = self._apply_content_request_heuristics(query, extracted_json)
                
                # Validate with Pydantic model
                intent = QueryIntent(**extracted_json)
                
                # Special handling for non-dataset related queries
                if not intent.is_dataset_related:
                    logger.info("Query not related to dataset search")
                    return {
                        "dataset_info": False,
                        "file_metadata": False,
                        "file_content": False,
                        "summary": False,
                        "filters": [],
                        "is_dataset_related": False,
                        "needs_clarification": True,
                        "clarification_message": "Your question doesn't appear to be related to searching the dataset. Please try a query about the dataset content or metadata.",
                        "max_files": 5
                    }
                
                # Ensure there's a clarification message if clarification is needed
                if intent.needs_clarification and not intent.clarification_message:
                    intent.clarification_message = "Could you provide more details about what you're looking for in the dataset?"
                
                return intent.model_dump()
                
            except Exception as e:
                logger.error(f"Error validating query intent: {str(e)}")
                return default_intent.model_dump()
                
        except Exception as e:
            logger.error(f"Error extracting query intent: {str(e)}")
            return default_intent.model_dump()
    
    def _build_intent_extraction_prompt(self, query: str) -> str:
        """Build the prompt for extracting query intent using Pydantic AI"""
        
        prompt = f"""Analyze the following user query about a dataset and determine the search intent.
Query: "{query}"

First, determine if the query is related to dataset search or if it's a general question or unrelated to datasets.

IMPORTANT INSTRUCTIONS:
1. For dataset overview requests (e.g., "tell me about this dataset", "what's in this dataset"):
   - Start with a clear introduction about the dataset
   - Include key metadata
   - Keep the response concise but informative

If the query is related to dataset search, determine which of these data sources should be searched:
1. "dataset_info" - Dataset metadata (name, status, total_size, total_files, etc.)
2. "file_metadata" - File metadata (filename, filepath, access information)
3. "file_content" - The actual content of files in the dataset

IMPORTANT: Set file_content to true if the user:
- Asks to "provide", "display", "show", "view", "summarize", "read", or otherwise access the CONTENT of a file.
- Asks for "content of" a file
- Asks to "show" or "display" file content
- Asks to "read" a file
- Asks for "what's in" a file
- Asks for "text" or "contents" of a file

Next, determine how many files would be needed to properly answer this query:
- For general questions about the dataset, 5-10 files may be sufficient
- For questions about specific files, include those specific files
- For broad questions requiring representative content, include more files (up to 25)
- The minimum is 5 files and maximum is 25 files

IMPORTANT: Pay special attention to general file listing queries:
- If the user asks to "list files", "list all files", "show me files", etc., with no specific criteria, this should be treated as a general file listing request
- For general file listing requests, DO NOT add any specific filename filters
- If the user asks to "list random files" or "show me some files", this should also be treated as a general listing without filename filters

IMPORTANT: Extract any filters mentioned in the query. Pay close attention to:
- If the user asks about a specific filename (like "filename X" or "file named X"), create a filter with field="filename", type="contains", value=X
- If the user mentions specific paths, departments, or other metadata fields, create appropriate filters

IMPORTANT: Content and Summary Handling:
- If a specific filename is mentioned in the query, ALWAYS set file_content=true since we're dealing with a single file
- If the user asks to "show", "display", "read", "view", "provide", or "get" content, set file_content=true
- If the user asks about "what's in" or "what does it contain", set file_content=true
- By default, when file_content=true, also set summary=true
- ONLY set summary=false if the user explicitly asks for "full content", "complete text", or "entire content"
- If the user asks for a "summary", "overview", "key points", or "main ideas", keep summary=true

For each filter, determine:
- field: The field to filter on (e.g., {', '.join(self.metadata_fields)})
- type: How to filter ("equals", "contains", "exists")
- value: The value to filter by. For "exists" type, value should be null
- operation: How this filter combines with others ("AND" or "OR")
- include: Whether to perform include or exclude the filter in the query

Examples of filters:
1. "Show me files with Risk in the filename" -> {{"field": "filename", "type": "contains", "value": "Risk", "operation": "AND", "include": true}}
2. "Summarize the content of the file Risk20140318.pdf" -> {{"field": "filename", "type": "contains", "value": "Risk20140318.pdf", "operation": "AND", "include": true}}

Respond with a JSON object in the following format:
{{
    "dataset_info": boolean,
    "file_metadata": boolean,
    "file_content": boolean,
    "summary": boolean,
    "filters": [
        {{
            "field": string,
            "type": "equals" | "contains" | "exists",
            "value": string or null,
            "operation": "AND" | "OR",
            "include": boolean
        }}
    ],
    "is_dataset_related": boolean,
    "needs_clarification": boolean,
    "clarification_message": string or null,
    "fields": [string],
    "max_files": number  // Between 5 and 25
}}

Only include filters and fields that are needed to answer the query.
"""
        return prompt
    
    def _extract_json_from_response(self, response_text: str) -> Dict[str, Any]:
        """Extract JSON from Claude's response"""
        try:
            # Try to parse the entire response as JSON first
            return json.loads(response_text)
        except json.JSONDecodeError:
            # If that fails, try to extract JSON using regex
            import re
            json_match = re.search(r'(\{.*\})', response_text, re.DOTALL)
            if json_match:
                try:
                    return json.loads(json_match.group(1))
                except json.JSONDecodeError:
                    logger.warning(f"Failed to parse extracted JSON: {json_match.group(1)}")
                    return {}
            return {}
    
    def _apply_content_request_heuristics(self, query: str, extracted_json: Dict[str, Any]) -> Dict[str, Any]:
        """Apply heuristics to ensure content requests are properly handled"""
        
        query_lower = query.lower()
        
        # CONTENT REQUEST FALLBACK: Force file_content to true for content display requests
        content_keywords = ["content", "text", "document", "what's in", "what is in"]
        action_keywords = ["display", "show", "view", "summarize", "read", "get", "extract", "tell me about", "tell about"]
        
        has_content_keyword = any(keyword in query_lower for keyword in content_keywords)
        has_action_keyword = any(keyword in query_lower for keyword in action_keywords)
        has_file_mention = "file" in query_lower or any(ext in query_lower for ext in [".pdf", ".docx", ".txt", ".xlsx"])
        
        # Check for "tell me about [filename]" pattern
        import re
        tell_about_file_pattern = re.search(r'tell\s+(?:me\s+)?about\s+([\w\s\-.,]+\.(?:pdf|docx|txt|xlsx))', query_lower)
        
        # If query looks like a content request but LLM didn't set file_content to true
        if (has_content_keyword or 
            (has_action_keyword and has_file_mention) or 
            tell_about_file_pattern) and not extracted_json.get("file_content", False):
            logger.info(f"Forcing file_content to True based on query keywords: '{query}'")
            extracted_json["file_content"] = True
            # Also ensure file_metadata is True since we need it to get file IDs
            extracted_json["file_metadata"] = True
            
            # By default, we want to summarize content
            if "summary" not in extracted_json:
                extracted_json["summary"] = True
            
            # Unless user explicitly asks for full content
            full_content_indicators = ["full content", "complete text", "entire content", "full text", "verbatim"]
            if any(indicator in query_lower for indicator in full_content_indicators):
                extracted_json["summary"] = False
        
        # FILENAME FILTER FALLBACK: If user explicitly mentions a filename but no filters were extracted
        if not extracted_json.get("filters") and "filename" in query_lower:
            # Try to extract filename using simple pattern matching
            filename_patterns = [
                r'filename\s+(?:that\s+)?contains\s+([^\s.,]+)',
                r'filename\s+([^\s.,]+)',
                r'file\s+named\s+([^\s.,]+)',
                r'file\s+([^\s.,]+\.(?:pdf|csv|txt|xlsx|docx|html))'
            ]
            
            for pattern in filename_patterns:
                match = re.search(pattern, query_lower, re.IGNORECASE)
                if match:
                    filename_value = match.group(1)
                    logger.info(f"Fallback filename filter extracted: {filename_value}")
                    if "filters" not in extracted_json:
                        extracted_json["filters"] = []
                    extracted_json["filters"].append({
                        "field": "filename",
                        "type": "contains",
                        "value": filename_value,
                        "operation": "AND",
                        "include": True
                    })
                    break
                    
        return extracted_json
    
    def _standardize_llm_response(self, response_text: str) -> str:
        """Clean and standardize LLM response for consistent parsing"""
        # Remove any triple backticks and json indicators from the response
        cleaned_text = response_text.replace("```json", "").replace("```", "").strip()
        return cleaned_text


# Example usage
def example_usage():
    # Initialize the extractor
    metadata_fields = [
        "filename", "filepath", "file_size", "last_modified",
        "department", "document_type", "status", "owner",
        "access_level", "created_date"
    ]
    
    extractor = PydanticAIQueryIntentExtractor(
        claude_api_key="your_api_key_here",
        metadata_fields=metadata_fields
    )
    
    # Example queries
    queries = [
        "Show me all files in the dataset",
        "What's in the Risk20140318.pdf file?",
        "Display files with Risk in the filename",
        "List files created before 2023",
        "Tell me about this dataset",
        "What time is it?",
        "Show me the content of the financial report from 2023"
    ]
    
    for query in queries:
        intent = extractor.extract_query_intent(query)
        print(f"\nQuery: {query}")
        print(f"Intent: {json.dumps(intent, indent=2)}")


if __name__ == "__main__":
    example_usage()