# Twitter API Debug & Fix - SPEC

## Context

Hari Seldon needs working Twitter API to post tweets. Goal: $100k revenue Year 1. Current status: Authentication works (verified via Python) but posting returns 403 "subset of X API V2 endpoints" - meaning free tier may not allow posting.

## Task

Debug Twitter API posting issue and get tweet posting working.

## Requirements

### 1. Current Working Credentials
File: `~/.openclaw-seldon/credentials/twitter.json`
```
consumer_key: UQWD7iH05matO3cCJIFuhYqWA
consumer_secret: lc1ufanxEZJLe6sFCzs2CLu1DYga0i1PvGaInK2dCs3dn68Vs7
access_token: 2027865526333313024-QzqUr4c4iErg4i2ZHv3aZ8qLhbTKXi
access_token_secret: W1A3QRV3e2cQO1JHTIVnGOpLfIv5CaN7bC8dXMS9J1KYf
```

### 2. Current Test Results
- `api.verify_credentials()` → ✅ SUCCESS
- `api.update_status()` → ❌ 403 Forbidden ("subset of X API V2 endpoints")

### 3. What to Test

#### Test A: Verify App Permissions
Check if the app has "Read and Write" permissions in X Developer Portal:
- Go to: https://developer.x.com/en/portal/dashboard
- Select app: 2028289947099099136SeldonCrunc
- Find "User authentication settings" or "App permissions"
- Confirm permissions = Read and Write (not Read-only)

#### Test B: Try Different Endpoints
Test these endpoints with the credentials:
1. `POST /2/tweets` (v2 JSON)
2. `POST /1.1/statuses/update.json` (v1.1 URL-encoded)
3. Check if oauth/request_token works (it should - proves consumer key is valid)

#### Test C: Check Rate Limits
Make request to see if we're hitting any limits:
- GET /2/users/me (check account status)
- Check response headers for rate limit info

### 4. Environment Info
- OS: Linux
- Node.js: v22.22.0
- Python: 3.12
- Working: tweepy library, oauth-1.0a library

## Output

Working Node.js or Python script in `/root/.openclaw-seldon/workspace/` that:
1. Successfully posts a tweet to @SeldonCrunches
2. Returns tweet ID on success

## Constraints
- Use OAuth 1.0a (not 2.0) - we have the tokens already
- Do NOT use Twitter library - use raw HTTP requests for debugging
- Print all HTTP status codes and response bodies

## Success Criteria
1. Run script → tweet posted to @SeldonCrunches
2. No 403 errors
3. Tweet visible on timeline
