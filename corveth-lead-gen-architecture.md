# Lead List Generation System - Technical Architecture

## Executive Summary
For Corveth Consulting with ~2000 companies from Crunchbase, here's the recommended architecture:

---

## Workflow Step-by-Step

### Step 1: Company Data (✅ Already Have)
- **Source:** Crunchbase export (~2000 companies)
- **Format:** Company names, industries, funding stages, locations

### Step 2: Website URL Extraction
| Tool | Pros | Cons | Est. Cost |
|------|------|------|-----------|
| **Clearbit** | Accurate, company enrichment | Expensive | $199-499/mo |
| **People Data Labs** | Bulk affordable | Less accurate | $99-299/mo |
| **Scraping (custom)** | Free | Slow, maintenance | $0 + dev time |
| **Domain by Apollo** | Integrated with enrichment | Part of Apollo | Included |

**Recommendation:** Use Apollo's enrichment (covers Step 2 + 3)

### Step 3: Founder/Decision-Maker Enrichment
| Tool | Data Quality | Email Accuracy | LinkedIn | Est. Cost |
|------|--------------|-----------------|----------|-----------|
| **Apollo** | Good | 70-85% | Yes | $39-99/mo |
| **ZoomInfo** | Best | 85-95% | Yes | $500+/mo |
| **Clearbit** | Good | 70-80% | Yes | $199/mo |
| **People Data Labs** | Decent | 60-70% | No | $99/mo |
| **LinkedIn Sales Nav** | Excellent | N/A | Yes | $99/mo |

**Recommendation:** Apollo (best value for startup ICP)

### Step 4: Lead Scoring
**Automated Scoring Options:**
- **ICP Match Score:** Revenue range ($5M-$50M), industry (SaaS/Fintech/AI), location (US/UK/SG), funding stage (Seed-Series B)
- **Tech Stack Scoring:** Use BuiltWith to detect B2B signals (Stripe, HubSpot, AWS)
- **Intent Data:** Apollo provides buying signals (job posts, funding news)

**Scoring Logic (can build in Google Sheets or Make):**
```
Score = (Revenue Fit * 30) + (Industry Match * 25) + (Location * 15) + (Funding Stage * 15) + (Tech Signals * 10) + (Intent Signals * 5)
```

### Step 5: Data Cleaning
- **Dedupe:** Use Remove Duplicates in Sheets or Dedupely ($0-29/mo)
- **Email Validation:** Neverbounce ($99/mo) or Zerobounce ($79/mo)
- **Manual Review:** Flag low-confidence emails for human check

### Step 6: Attio Import Format
Attio accepts CSV with these mappings:
- Company name, domain, industry, size, location
- People: name, email, title, LinkedIn URL
- Custom fields for lead score

### Step 7: Attio API Import
**Attio API Endpoints:**
- `POST /companies` - Create companies
- `POST /people` - Create contacts
- `POST /records` - Link to objects

---

## Recommended Architecture

### Option A: MVP (Quick Build)
```
[Crunchbase CSV] → [Google Sheets] → [Apollo Enrichment] → [Scoring Formula] → [Attio Import]
```
- **Tools:** Google Sheets + Apollo + Manual Attio import
- **Cost:** $39/mo (Apollo)
- **Time:** 2-3 days setup
- **Automation:** Low (manual CSV upload)

### Option B: Semi-Automated (Recommended)
```
[Crunchbase CSV] 
    ↓
[Make.com] ←→ [Apollo API] ←→ [Attio API]
    ↓
[Lead Scoring Module] (in Make or G Sheets)
    ↓
[Attio CRM]
```
- **Tools:** Make ($9-29/mo) + Apollo + Attio
- **Cost:** $48-128/mo
- **Time:** 1-2 weeks
- **Automation:** High

### Option C: Fully Custom (Scale)
```
[Database] → [Python Scripts] → [Multiple APIs] → [Attio]
```
- **Tools:** Custom Python + n8n/self-hosted
- **Cost:** $50-200/mo (APIs) + dev time
- **Time:** 3-4 weeks
- **Automation:** Full

---

## Cost Breakdown (Option B)

| Component | Plan | Monthly Cost |
|-----------|------|--------------|
| Apollo | Team | $79/mo |
| Make | Pro | $29/mo |
| Attio | Business | $49/mo |
| Email Validation (opt) | Zerobounce | $29/mo |
| **Total** | | **$116-186/mo** |

---

## What Can Be Automated Today

| Step | Automation Ready? | Notes |
|------|-------------------|-------|
| Website extraction | ✅ Yes | Apollo/Clearbit |
| People enrichment | ✅ Yes | Apollo API |
| Lead scoring | ✅ Yes | Make formula |
| Deduplication | ✅ Yes | Make/Google |
| Email validation | ⚠️ Partial | Requires verification step |
| Attio import | ✅ Yes | Attio API |
| Data quality check | ❌ No | Needs human review |

---

## MVP Build Plan (5 Days)

**Day 1:** Set up Apollo account, test enrichment on 50 companies
**Day 2:** Build Make scenario (Crunchbase → Apollo → Format)
**Day 3:** Create lead scoring logic in Google Sheets
**Day 4:** Test Attio API import, map fields
**Day 5:** End-to-end test, refine scoring, document process

---

## Potential Bottlenecks

1. **Email accuracy:** Apollo ~75% accuracy; budget for validation service
2. **Rate limits:** Apollo limits API calls (5000/mo on Team plan)
3. **Attio rate limits:** Check API docs for limits
4. **Data freshness:** Re-enrich quarterly (companies change)
5. **LinkedIn scraping:** Against ToS - use Sales Navigator or Apollo

---

## Quick Wins for Corveth

1. **Start with Apollo enrichment** - handles steps 2-3 in one
2. **Use Google Sheets for scoring** - free, flexible
3. **Manual Attio import first** - validate data before automating
4. **Target 500 companies first** - test the workflow before full scale
