# ADK Multi-Agent Project

This project contains multiple Google ADK agents that can be deployed together on a single Render service.

## 🔒 Security Notice

**IMPORTANT**: Never commit `.env` files to git! They contain sensitive API keys.
- Use `.env.template` files as examples
- Add actual values to your local `.env` files  
- The `.gitignore` file prevents accidental commits

## Agents

### 1. Weather & Time Agent (`multi_tool_agent`)
- Get current weather for cities
- Get current time for cities
- Supports New York (expandable)

### 2. Email Summary Agent (`email_summary_agent`)
- Reads unread emails from Gmail
- Creates summaries of emails
- Sends summaries to Telegram
- Automated email monitoring

## Setup & Configuration

### Prerequisites
- Google Cloud Console account
- Telegram Bot Token
- Supabase PostgreSQL database (for session persistence)

### Environment Variables

#### For Weather Agent
Copy `multi_tool_agent/.env.template` to `multi_tool_agent/.env` and fill in:

```env
# Google AI Configuration
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_api_key_here
```

#### For Email Summary Agent
Create `email_summary_agent/.env` with:

```env
# Google Gmail API Credentials
GOOGLE_CLIENT_ID=your_google_client_id_here
GOOGLE_CLIENT_SECRET=your_google_client_secret_here
GOOGLE_REFRESH_TOKEN=your_google_refresh_token_here

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_telegram_chat_id_here

# Gmail Configuration
GMAIL_ADDRESS=your_email@gmail.com
```

### Getting Google Gmail API Credentials

1. **Enable Gmail API**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select existing
   - Enable Gmail API
   - Go to "Credentials" → "Create Credentials" → "OAuth 2.0 Client IDs"
   - Set application type as "Desktop application"
   - Download the credentials JSON

2. **Get Refresh Token**:
   ```bash
   # Install Google Auth Library
   pip install google-auth-oauthlib
   
   # Use the OAuth2 flow to get refresh token
   # This is a one-time setup process
   ```

### Getting Telegram Bot Token

1. **Create Bot**:
   - Message @BotFather on Telegram
   - Send `/newbot`
   - Follow instructions to create your bot
   - Copy the bot token

2. **Get Chat ID**:
   - Send a message to your bot
   - Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
   - Find your chat ID in the response

## Local Development

### Run Single Agent
```bash
# Activate environment
conda activate adk

# Run weather agent only
adk web multi_tool_agent

# Run email agent only  
adk web email_summary_agent
```

### Run All Agents
```bash
# Run all agents together
adk web

# Or run as API server
adk api_server --host 0.0.0.0 --port 8000
```

## Deployment on Render

### Setup
1. **Environment Variables** (in Render dashboard):
   ```
   DATABASE_URL=postgresql://postgres.yejndpbgsguimsnjsxiu:ETHN_hnt523@aws-0-us-east-2.pooler.supabase.com:5432/postgres
   GOOGLE_API_KEY=your_google_api_key
   GOOGLE_CLIENT_ID=your_google_client_id
   GOOGLE_CLIENT_SECRET=your_google_client_secret  
   GOOGLE_REFRESH_TOKEN=your_google_refresh_token
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   TELEGRAM_CHAT_ID=your_telegram_chat_id
   ```

2. **Build Command**: `pip install -r requirements.txt`

3. **Start Command**: `adk api_server --session_db_url=$DATABASE_URL --host 0.0.0.0 --port $PORT`

### API Endpoints

After deployment, your agents will be available at:

```
# Weather Agent
POST https://your-app.onrender.com/apps/multi_tool_agent/users/u_123/sessions/s_123

# Email Agent  
POST https://your-app.onrender.com/apps/email_summary_agent/users/u_123/sessions/s_456
```

## Usage Examples

### Weather Agent
```bash
curl -X POST https://your-app.onrender.com/run_sse \
  -H "Content-Type: application/json" \
  -d '{
    "appName": "multi_tool_agent",
    "userId": "u_123",
    "sessionId": "s_123", 
    "newMessage": {
      "role": "user",
      "parts": [{"text": "What's the weather in New York?"}]
    },
    "streaming": false
  }'
```

### Email Agent
```bash
curl -X POST https://your-app.onrender.com/run_sse \
  -H "Content-Type: application/json" \
  -d '{
    "appName": "email_summary_agent",
    "userId": "u_123",
    "sessionId": "s_456",
    "newMessage": {
      "role": "user", 
      "parts": [{"text": "Check my unread emails and send summary to Telegram"}]
    },
    "streaming": false
  }'
```

## Features

- ✅ **Multi-Agent Architecture**: Multiple specialized agents in one deployment
- ✅ **Persistent Sessions**: PostgreSQL storage via Supabase
- ✅ **Auto-scaling**: Render handles scaling automatically
- ✅ **Email Integration**: Gmail API for reading emails
- ✅ **Telegram Notifications**: Automated messaging
- ✅ **Production Ready**: Error handling, logging, monitoring

## Dependencies

- `google-adk==1.1.1` - Google Agent Development Kit
- `psycopg2-binary>=2.9.0` - PostgreSQL driver
- `google-auth>=2.0.0` - Google authentication
- `google-api-python-client>=2.0.0` - Gmail API client
- `requests>=2.25.0` - HTTP requests for Telegram

## License

MIT License 