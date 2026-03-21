# Holdex Lead Enrichment — Claude Code + Brave Search

## What This Does
Takes your 281 companies CSV and finds the CEO/Founder LinkedIn URL for each one using Claude Code with Brave Search MCP.

## Setup (5 minutes)

### Step 1: Get a Brave Search API Key (free)
1. Go to https://brave.com/search/api
2. Create an account
3. Under "Subscriptions", pick the free plan (2,000 queries/month)
4. Go to "API Keys" → "Add API Key"
5. Copy the key

### Step 2: Install Node.js (if you don't have it)
```bash
# Check if you have it
node --version

# If not, install via nvm (recommended)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
nvm install 20
```

### Step 3: Install Claude Code (if you don't have it)
```bash
npm install -g @anthropic-ai/claude-code
```

### Step 4: Add Brave Search MCP to Claude Code
```bash
claude mcp add brave-search \
  -e BRAVE_API_KEY=YOUR_KEY_HERE \
  -- npx -y @modelcontextprotocol/server-brave-search
```
Replace `YOUR_KEY_HERE` with your actual Brave API key.

### Step 5: Verify it works
```bash
claude "Use brave_web_search to find who is the CEO of Ondo Finance"
```
You should see Claude search and return "Nathan Allman" or similar.

## Run the Enrichment

### Option A: Interactive (recommended first time)
```bash
cd enrich-project
claude
```
Then say:
```
Read the CLAUDE.md instructions, then process all companies in input/leads.csv. 
Start from wherever progress.txt left off (or from the beginning if no progress file).
Work in batches of 10. After each batch, save progress.
```

### Option B: Headless / autonomous
```bash
cd enrich-project
claude -p "Read CLAUDE.md and execute the full enrichment pipeline on input/leads.csv. Process all 281 companies, save results to output/enriched_leads.csv, track progress in output/progress.txt. Work autonomously until complete."
```

### Option C: If you get rate limited on Brave free tier
The free tier is 2,000 queries/month at 1 req/sec. At ~2 queries per company, 281 companies = ~560 queries. You're well within limits, but if you hit throttling:
```bash
# Process in smaller chunks
claude -p "Read CLAUDE.md. Process rows 1-50 from input/leads.csv only."
# Wait a bit, then:
claude -p "Read CLAUDE.md. Resume from progress.txt and process the next 50."
```

## After Enrichment

Your output will be in `output/enriched_leads.csv` with:
- company_name, website, vertical, description
- contact_name, contact_title, contact_linkedin
- enrichment_confidence (A/B/C/D)

### Check your hit rate
```bash
# Quick stats
claude -p "Read output/enriched_leads.csv and tell me: total rows, confidence A count, B count, C count, D count, and overall hit rate (A+B as percentage of total)"
```

### If hit rate is below 70%
Come back to Claude.ai chat and say "hit rate was X%, need to source more companies to fill the gap" — I'll run a second sourcing batch.

## File Structure
```
enrich-project/
├── CLAUDE.md              # Instructions for Claude Code
├── README.md              # This file
├── input/
│   └── leads.csv          # Your 281 companies (cleaned, no portfolio)
└── output/
    ├── enriched_leads.csv  # Results (created by Claude Code)
    ├── progress.txt        # Resume tracking (created by Claude Code)
    └── errors.log          # Any failures (created by Claude Code)
```

## Troubleshooting

**"tool not found" error**: Brave MCP not connected. Run `claude mcp list` to check, then re-add if needed.

**Rate limiting**: Wait 60 seconds, resume. Or upgrade Brave to Base plan ($3/mo) for 15K queries.

**Bad results**: Some early crypto projects have very thin web presence. Confidence D leads need manual LinkedIn searching — but that's expected for ~15-20% of web3 startups.
