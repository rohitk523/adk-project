# 🎬 YouTube Short Maker Agent

This agent creates YouTube Shorts by combining background video with AI-generated voiceover and uploads them to YouTube automatically.

## 🔄 **Complete Pipeline Flow**

```
📁 Input Video + 📝 Transcript
           ↓
🎬 Video Processing (9:16 format, max 60s)
           ↓
🎤 Text-to-Speech Generation (OpenAI)
           ↓
🎞️ Audio + Video Combination (FFmpeg)
           ↓
📤 YouTube Upload (YouTube Data API)
           ↓
✅ Published YouTube Short
```

## 🚀 **Quick Start**

### 1. **Prerequisites**
```bash
# Install FFmpeg (required for video processing)
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

### 2. **API Setup**

#### **OpenAI API** (for Text-to-Speech)
1. Get API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Add `OPENAI_API_KEY` to environment

#### **YouTube Data API v3** (for uploading)
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create/select project → Enable YouTube Data API v3
3. Create OAuth 2.0 credentials (Desktop Application)
4. Get refresh token using OAuth flow

#### **Google AI API** (for agent model)
1. Get API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### 3. **Environment Setup**
```bash
# Copy environment template
cp youtube_short_maker/env_template.txt youtube_short_maker/.env

# Edit with your credentials
nano youtube_short_maker/.env
```

### 4. **Run the Agent**
```bash
# Activate ADK environment
conda activate adk

# Start the YouTube short maker agent
adk web youtube_short_maker
```

## 🎯 **Usage Examples**

### **Via Web Interface** (http://localhost:8000)
Ask the agent:
```
"Create a YouTube Short with this video file: /path/to/video.mp4 
and this transcript: 'Welcome to my channel! Today I'll show you 
how to make amazing content with AI tools.'"
```

### **Via API**
```bash
curl -X POST http://localhost:8000/run_sse \
  -H "Content-Type: application/json" \
  -d '{
    "appName": "youtube_short_maker",
    "userId": "u_123",
    "sessionId": "s_123",
    "newMessage": {
      "role": "user",
      "parts": [{
        "text": "Create a YouTube Short with video '/Users/me/background.mp4' and transcript 'Hello everyone! Welcome to my AI-powered content creation tutorial!'"
      }]
    },
    "streaming": false
  }'
```

## 🛠️ **Individual Functions**

### **1. Process Background Video**
```python
# Convert any video to YouTube Shorts format (9:16, max 60s)
process_background_video("/path/to/video.mp4", duration=45)
```

### **2. Generate Text-to-Speech**
```python
# Convert text to speech using OpenAI TTS
generate_tts_audio("Your script here", voice="alloy")
```

**Available Voices:**
- `alloy` - Neutral, balanced
- `echo` - Male voice
- `fable` - British accent
- `onyx` - Deep male voice
- `nova` - Female voice
- `shimmer` - Soft female voice

### **3. Combine Audio + Video**
```python
# Merge processed video with TTS audio
combine_audio_video("processed_video.mp4", "voiceover.mp3", "My YouTube Short")
```

### **4. Upload to YouTube**
```python
# Upload final video to YouTube
upload_to_youtube("final_short.mp4", "Amazing AI Short", "Created with AI", ["shorts", "ai"])
```

### **5. Complete Pipeline**
```python
# Run entire pipeline at once
create_youtube_short(
    video_path="/path/to/video.mp4",
    transcript="Your script here",
    title="My AI-Generated Short",
    description="Created automatically with AI",
    voice="nova",
    tags=["ai", "automation", "shorts"]
)
```

## 📋 **Required Environment Variables**

```env
# OpenAI API (for Text-to-Speech)
OPENAI_API_KEY=your_openai_api_key_here

# YouTube Data API v3 (for uploading)
YOUTUBE_CLIENT_ID=your_youtube_oauth_client_id_here
YOUTUBE_CLIENT_SECRET=your_youtube_oauth_client_secret_here
YOUTUBE_REFRESH_TOKEN=your_youtube_refresh_token_here

# Google AI API (for agent model)
GOOGLE_API_KEY=your_google_ai_api_key_here

# Database (for persistence)
DATABASE_URL=your_postgresql_database_url_here
```

## 🎥 **Video Specifications**

**Input Video Requirements:**
- Any format supported by FFmpeg (MP4, AVI, MOV, etc.)
- Any resolution/aspect ratio (will be converted)
- Any duration (will be trimmed to 60s max)

**Output Video Specs:**
- **Aspect Ratio**: 9:16 (vertical)
- **Resolution**: 1080x1920 (YouTube Shorts optimal)
- **Duration**: Max 60 seconds
- **Format**: MP4 (H.264 + AAC)
- **Bitrate**: 2Mbps video, 128kbps audio

## 🔧 **Advanced Configuration**

### **Custom Video Duration**
```python
# Create 30-second short instead of 60
process_background_video("video.mp4", duration=30)
```

### **Custom Voice Selection**
```python
# Use different TTS voice
generate_tts_audio("Script", voice="onyx")  # Deep male voice
```

### **Privacy Settings**
```python
# Upload as private/unlisted
upload_to_youtube("video.mp4", "Title", "Description", privacy="private")
```

### **Custom Tags & Categories**
```python
upload_to_youtube(
    "video.mp4", 
    "Title",
    "Description", 
    tags=["tech", "ai", "tutorial", "automation"],
    category_id="27"  # Education category
)
```

## 🚨 **Error Handling**

The agent handles common issues:
- **Missing credentials**: Clear error messages
- **Video processing failures**: FFmpeg error details
- **TTS failures**: OpenAI API error handling
- **Upload failures**: YouTube API error responses
- **Partial successes**: Video created but upload failed

## 📊 **Output Examples**

**Successful Creation:**
```json
{
  "status": "success",
  "message": "YouTube Short created and uploaded successfully!",
  "video_url": "https://www.youtube.com/watch?v=abc123",
  "video_id": "abc123",
  "final_video_path": "youtube_short_20241220_143052.mp4"
}
```

**Partial Success:**
```json
{
  "status": "partial_success", 
  "message": "YouTube Short created but upload failed",
  "final_video_path": "youtube_short_20241220_143052.mp4",
  "error": "YouTube API authentication failed"
}
```

## 🎨 **Content Ideas**

Perfect for creating:
- **Educational content** (tutorials, tips)
- **Motivational quotes** with background visuals
- **Product demonstrations** 
- **News summaries** with stock footage
- **AI-generated stories** with ambient video
- **Podcast highlights** with visualizations

## 🔐 **Security Notes**

- Never commit `.env` files to git
- Store API keys securely in environment variables
- Use refresh tokens (not access tokens) for YouTube API
- Consider using separate Google Cloud projects for different environments

## 🏗️ **Multi-Agent Architecture**

This agent can be easily extended to a multi-agent system:

**Potential Specialized Agents:**
- `video_processor_agent` - Video manipulation only
- `tts_generator_agent` - Text-to-speech only  
- `youtube_uploader_agent` - Upload management only
- `content_optimizer_agent` - SEO optimization for titles/descriptions

**Current Single-Agent Benefits:**
- ✅ Simpler setup and maintenance
- ✅ Fewer dependencies between services
- ✅ Easier error handling and debugging
- ✅ Single point of configuration

## 🚀 **Deployment on Render**

Add to existing multi-agent deployment:

```bash
# Environment variables in Render
OPENAI_API_KEY=your_key
YOUTUBE_CLIENT_ID=your_id
YOUTUBE_CLIENT_SECRET=your_secret  
YOUTUBE_REFRESH_TOKEN=your_token
```

**Start command:**
```bash
adk api_server --session_db_url=$DATABASE_URL --host 0.0.0.0 --port $PORT
```

The agent will be available at:
```
POST https://your-app.onrender.com/apps/youtube_short_maker/users/u_123/sessions/s_123
```

## 📈 **Performance Tips**

- **Optimize video size**: Use shorter clips for faster processing
- **Batch processing**: Process multiple shorts in sequence
- **Async operations**: All I/O operations are handled asynchronously
- **Error recovery**: Failed uploads can be retried manually
- **Resource management**: Temporary files are cleaned up automatically 