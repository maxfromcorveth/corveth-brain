# Google OAuth Setup for OpenClaw Agents

This guide explains how to set up Google APIs for an OpenClaw agent to access Google Drive, Sheets, and Docs.

---

## Overview

To use Google APIs (Drive, Sheets, Docs) with an OpenClaw agent, you need:
1. A Google Cloud project with APIs enabled
2. An OAuth 2.0 client (Desktop app type recommended)
3. A refresh token for the Google account that will be used

---

## Step 1: Create Google Cloud Project

1. Go to Google Cloud Console (https://console.cloud.google.com/)
2. Create a new project (or use existing)
3. Note the Project ID (e.g., openclaw-seldon)

---

## Step 2: Enable Required APIs

For the project, enable these APIs:
- Google Drive API: https://console.developers.google.com/apis/api/drive.googleapis.com
- Google Sheets API: https://console.developers.google.com/apis/api/sheets.googleapis.com
- Google Docs API: https://console.developers.google.com/apis/api/docs.googleapis.com

Click Enable for each.

---

## Step 3: Create OAuth Client (Desktop App)

1. Go to APIs & Services → Credentials
2. Click + Create Credentials → OAuth client ID
3. Select Desktop app (recommended — works with localhost redirect)
4. Name it (e.g., "OpenClaw Agent")
5. Download the JSON or copy:
   - Client ID (ends in .apps.googleusercontent.com)
   - Client Secret

---

## Step 4: Get Refresh Token

Run this on the machine where the agent runs (must have a browser):

```python
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/docs'
]

# REPLACE THESE WITH YOUR CLIENT'S CREDENTIALS
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'

client_config = {
    'installed': {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uris': ['http://localhost'],
        'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
        'token_uri': 'https://oauth2.googleapis.com/token'
    }
}

flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
creds = flow.run_local_server(port=0)

# Save refresh token to file
print(creds.refresh_token)
```

Important:
- When the browser opens, sign in with the Google account you want the agent to use
- Copy the refresh token output

---

## Step 5: Save Credentials for Agent

Create a credentials file at:
`/root/.openclaw-[AGENT_NAME]/credentials/google-oauth.json`

With this content:
```json
{
    "scopes": [
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/docs",
        "https://www.googleapis.com/auth/spreadsheets"
    ],
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET",
    "refresh_token": "YOUR_REFRESH_TOKEN",
    "token_uri": "https://oauth2.googleapis.com/token"
}
```

---

## Troubleshooting

### redirect_uri_mismatch
- If using Desktop app: ensure http://localhost is in redirect URIs
- If using Web app: add https://developers.google.com/oauthplayground/ to redirect URIs

### Test user errors
- Add the Google account as a test user in OAuth consent screen → Test users
- Or publish the app (make it available to all users)

### Token expired
- Refresh tokens don't expire (unless revoked)
- If needed, re-run Step 4 to get a new token
