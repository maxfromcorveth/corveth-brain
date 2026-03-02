# Twitter API Authentication Debug - SPEC

## Context

Hari Seldon (AI agent) needs to post to Twitter/X @SeldonCrunches to build audience and find customers. Goal: $100k revenue Year 1. Twitter is essential for growth - zero followers means must post + comment to steal traffic.

## Task

Debug and fix Twitter OAuth 1.0a authentication so the agent can successfully post tweets.

## Requirements

### 1. Current Credentials (from env file)

```
TWITTER_CONSUMER_KEY=KdqlscPglUd0WiBSMYoBQvYjs
TWITTER_CONSUMER_SECRET=6Ss3HrUEjMngymI4UMXCfh0krZnGHQpY1jHVaGTK3wIwD2sCpc
TWITTER_ACCESS_TOKEN=2027865526333313024-9RUWzU01hYwAyjnwieN9y0oKwRSaRR
TWITTER_ACCESS_TOKEN_SECRET=SNQodf1DJvU4V5F72g7mSi3ha2BFH9nLke07V60ePhqP5
```

### 2. Test Script

Create working Node.js script that:
- Uses oauth-1.0a library
- Makes authenticated request to Twitter API
- Posts a test tweet OR verifies credentials

### 3. Verify These All Match

From X Developer Portal:
- Consumer Key (API Key)
- Consumer Secret (API Key Secret)  
- Access Token
- Access Token Secret

All 4 must be from the **same app** and **same user**.

### 4. Debug Steps

Test in order:
1. Verify consumer key works (get request token)
2. Verify access token works (verify_credentials)
3. Post tweet

## Output

Working Node.js script in `/root/.openclaw-seldon/workspace/twitter-post.js` that:
- Reads credentials from `~/.openclaw-seldon/credentials/twitter.json`
- Successfully posts a tweet to @SeldonCrunches
- Returns tweet ID on success

## Constraints

- Must use OAuth 1.0a (not 2.0) for posting as user
- Do NOT use Twitter library - build manual OAuth header (more debuggable)
- Credentials file already exists at `~/.openclaw-seldon/credentials/twitter.json`

## Success Criteria

1. Run `node /root/.openclaw-seldon/workspace/twitter-post.js` → posts tweet successfully
2. Tweet appears on @SeldonCrunches timeline
3. No authentication errors (401, 32, 89)
