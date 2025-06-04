import os
import base64
import json
import re
from typing import Dict, List, Any
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.adk.agents import Agent
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def get_gmail_service():
    """Create Gmail API service using OAuth2 credentials."""
    try:
        credentials = Credentials(
            token=None,
            refresh_token=os.getenv('GOOGLE_REFRESH_TOKEN'),
            token_uri='https://oauth2.googleapis.com/token',
            client_id=os.getenv('GOOGLE_CLIENT_ID'),
            client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
            scopes=['https://www.googleapis.com/auth/gmail.readonly']
        )
        
        service = build('gmail', 'v1', credentials=credentials)
        return service
    except Exception as e:
        return None


def get_unread_emails() -> Dict[str, Any]:
    """Fetch unread emails from Gmail."""
    try:
        service = get_gmail_service()
        if not service:
            return {
                "status": "error",
                "error_message": "Failed to authenticate with Gmail. Please check your credentials."
            }
        
        # Get unread messages
        results = service.users().messages().list(
            userId='me', 
            q='is:unread',
            maxResults=10  # Limit to 10 most recent unread emails
        ).execute()
        
        messages = results.get('messages', [])
        
        if not messages:
            return {
                "status": "success",
                "message": "No unread emails found.",
                "email_count": 0,
                "emails": []
            }
        
        emails = []
        for msg in messages:
            # Get full message details
            message = service.users().messages().get(
                userId='me', 
                id=msg['id'],
                format='full'
            ).execute()
            
            # Extract email details
            payload = message['payload']
            headers = payload.get('headers', [])
            
            # Get sender, subject, and date
            sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
            date = next((h['value'] for h in headers if h['name'] == 'Date'), 'Unknown')
            
            # Get email body
            body = extract_email_body(payload)
            
            emails.append({
                "id": msg['id'],
                "sender": sender,
                "subject": subject,
                "date": date,
                "body": body[:500] + "..." if len(body) > 500 else body  # Truncate long emails
            })
        
        return {
            "status": "success", 
            "email_count": len(emails),
            "emails": emails
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error fetching emails: {str(e)}"
        }


def extract_email_body(payload):
    """Extract email body from Gmail API payload."""
    body = ""
    
    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain':
                if 'data' in part['body']:
                    body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                    break
            elif part['mimeType'] == 'text/html':
                if 'data' in part['body']:
                    html_body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                    # Simple HTML to text conversion
                    body = re.sub('<[^<]+?>', '', html_body)
                    break
    else:
        if payload['mimeType'] == 'text/plain' and 'data' in payload['body']:
            body = base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8')
    
    return body.strip()


def escape_markdown(text: str) -> str:
    """Escape special characters for Telegram Markdown."""
    # Characters that need escaping in Telegram Markdown
    escape_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    
    for char in escape_chars:
        text = text.replace(char, f'\\{char}')
    
    return text


def create_telegram_safe_summary(emails_data) -> str:
    """Create a Telegram-safe email summary without problematic formatting."""
    try:
        # Parse the emails data if it's a string
        if isinstance(emails_data, str):
            try:
                emails_info = json.loads(emails_data)
            except:
                emails_info = {"emails": [], "email_count": 0}
        else:
            emails_info = emails_data
        
        emails = emails_info.get("emails", [])
        email_count = emails_info.get("email_count", 0)
        
        if email_count == 0:
            return "📧 No unread emails found!"
        
        # Create plain text summary for Telegram
        summary = f"📧 EMAIL SUMMARY ({email_count} unread emails)\n\n"
        
        for i, email in enumerate(emails, 1):
            # Clean text for Telegram
            subject = email['subject'].replace('*', '').replace('_', '').replace('[', '').replace(']', '')
            sender = email['sender'].replace('*', '').replace('_', '').replace('<', '').replace('>', '')
            
            summary += f"{i}. {subject}\n"
            summary += f"From: {sender}\n"
            summary += f"Date: {email['date']}\n"
            
            # Create a brief summary of the email body
            body = email['body']
            if len(body) > 100:
                body_summary = body[:100] + "..."
            else:
                body_summary = body
            
            # Clean body text
            body_summary = body_summary.replace('*', '').replace('_', '').replace('[', '').replace(']', '')
            
            summary += f"Preview: {body_summary}\n"
            summary += "-" * 40 + "\n\n"
        
        return summary
        
    except Exception as e:
        return f"Error creating summary: {str(e)}"


def create_email_summary(emails_data: str) -> Dict[str, Any]:
    """Create a summary of unread emails."""
    try:
        # Parse the emails data if it's a string
        if isinstance(emails_data, str):
            try:
                emails_info = json.loads(emails_data)
            except:
                emails_info = {"emails": [], "email_count": 0}
        else:
            emails_info = emails_data
        
        emails = emails_info.get("emails", [])
        email_count = emails_info.get("email_count", 0)
        
        if email_count == 0:
            summary = "📧 No unread emails found!"
        else:
            summary = f"📧 **Email Summary** ({email_count} unread emails)\n\n"
            
            for i, email in enumerate(emails, 1):
                summary += f"**{i}. {email['subject']}**\n"
                summary += f"From: {email['sender']}\n"
                summary += f"Date: {email['date']}\n"
                
                # Create a brief summary of the email body
                body = email['body']
                if len(body) > 100:
                    body_summary = body[:100] + "..."
                else:
                    body_summary = body
                
                summary += f"Preview: {body_summary}\n"
                summary += "─" * 40 + "\n\n"
        
        return {
            "status": "success",
            "summary": summary,
            "email_count": email_count
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error creating summary: {str(e)}"
        }


def send_to_telegram(message: str) -> Dict[str, Any]:
    """Send email summary to Telegram with improved error handling."""
    try:
        bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        chat_id = os.getenv('TELEGRAM_CHAT_ID')
        
        if not bot_token or not chat_id:
            return {
                "status": "error",
                "error_message": "Telegram bot token or chat ID not configured."
            }
        
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        
        # First, try sending with no parse mode (plain text)
        data = {
            "chat_id": chat_id,
            "text": message
        }
        
        response = requests.post(url, data=data)
        
        if response.status_code == 200:
            return {
                "status": "success",
                "message": "Email summary sent to Telegram successfully!"
            }
        else:
            # If plain text fails, try with just the basic info
            simple_message = f"📧 You have unread emails in your inbox!\n\nCheck your email client for details."
            
            simple_data = {
                "chat_id": chat_id,
                "text": simple_message
            }
            
            fallback_response = requests.post(url, data=simple_data)
            
            if fallback_response.status_code == 200:
                return {
                    "status": "success",
                    "message": "Simplified email notification sent to Telegram successfully!"
                }
            else:
                return {
                    "status": "error",
                    "error_message": f"Failed to send to Telegram: {response.text}"
                }
            
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error sending to Telegram: {str(e)}"
        }


def check_and_send_email_summary() -> Dict[str, Any]:
    """Main function to check unread emails and send summary to Telegram."""
    try:
        # Get unread emails
        emails_result = get_unread_emails()
        
        if emails_result["status"] == "error":
            return emails_result
        
        # Create Telegram-safe summary
        telegram_summary = create_telegram_safe_summary(emails_result)
        
        # Send to Telegram
        telegram_result = send_to_telegram(telegram_summary)
        
        return {
            "status": "success",
            "message": f"Processed {emails_result['email_count']} unread emails and sent summary to Telegram.",
            "email_count": emails_result["email_count"],
            "telegram_status": telegram_result["status"]
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error in email summary process: {str(e)}"
        }


root_agent = Agent(
    name="email_summary_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent that reads unread emails, creates summaries, and sends them to Telegram."
    ),
    instruction=(
        "You are a helpful email assistant that can check unread emails, create summaries, "
        "and send notifications to Telegram. You can also get individual email details or "
        "send custom messages to Telegram."
    ),
    tools=[
        get_unread_emails,
        create_email_summary,
        send_to_telegram,
        check_and_send_email_summary
    ],
) 