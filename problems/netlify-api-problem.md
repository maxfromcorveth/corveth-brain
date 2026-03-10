# Problem Brief: Netlify API Deployment

## The Problem
Netlify API creates sites successfully (201 response) but deployed content returns 404.

## What Works
- ✅ API key valid - sites created
- ✅ File upload accepted
- ✅ Site claimed

## What's Broken
- ❌ Content returns 404 on all URLs
- ❌ Deployments stuck in "new" state, never process to "ready"

## Root Cause
Netlify's API is designed for Git-based deployments. Direct file upload requires:
1. Build system to process (Netlify doesn't do this via API)
2. Or need to upload to correct path with proper headers

## Attempted Solutions
| Method | Result |
|--------|--------|
| Direct file upload | 404 |
| multipart form | 404 |
| JSON files | 404 |
| tar.gz upload | 404 |
| ZIP upload | 404 |

## Solutions That Work (Manual)
1. **Netlify Drop** - Drag file to web interface ✓
2. **Netlify CLI** - `netlify deploy --prod` (not tried yet)

## What Would Fix API
1. **Netlify CLI** - Install and use CLI instead of API
2. **Build step** - Add build configuration (netlify.toml)
3. **Git integration** - Push to Git, Netlify auto-deploys

## Recommended Fix
Install Netlify CLI:
```bash
npm install -g netlify-cli
netlify deploy --prod --dir=.
```

This should work because CLI handles the build system that API doesn't.

## Status
🔴 BLOCKED - Need CLI installation or manual deployment
