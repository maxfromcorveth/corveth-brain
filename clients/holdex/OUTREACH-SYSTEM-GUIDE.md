# Client Acquisition System: LinkedIn Outreach Playbook

A complete system for setting up manual LinkedIn outreach for B2B clients. This guide covers lead research, messaging, sheet setup, and execution workflow.

---

## Overview

| Aspect | Details |
|--------|---------|
| **Goal** | Book meetings with qualified leads via LinkedIn |
| **Model** | Manual execution (no automation due to ban risk) |
| **Time** | 15-30 min/day |
| **Tools** | Google Sheets, LinkedIn, GitHub |
| **Output** | Qualified meetings booked |

---

## Prerequisites

1. Google account (for Sheets)
2. GitHub account (for documentation)
3. LinkedIn Premium (optional but recommended)
4. 15-30 min/day for execution

---

## Step 1: Lead Research

### Finding Leads

**Method: Competitor & Industry Mining**

1. Identify competitors in your target market
2. Look for their funding, partnerships, press releases
3. Find founders/CEOs on LinkedIn
4. Validate: Do they have budget? Is it a fit?

**Sources Used:**
- Web searches for funding news
- LinkedIn company pages
- Crunchbase, PitchBook
- Industry newsletters

**Example (this campaign):**
- Target: DeFi/RWA founders
- Competitors studied: Alchemy, ConsenSys, Maple Finance, Centrifuge
- Found: 11 validated leads with direct contact info

---

## Step 2: Sheet Setup

### Create Google Sheet

**Link:** https://docs.google.com/spreadsheets/d/16vNgb579V8ufNBYsO3sk5dyvKf2w_QGYC-FxKGZ5nBk

### Columns (Cold Tab)

| Column | Field |
|--------|-------|
| A | Lead First Name |
| B | Lead Last Name |
| C | Company Name |
| D | Company Description |
| E | Contact Name |
| F | Contact Title |
| G | LinkedIn URL |
| H | Email |
| I | First Message |
| J | Follow-up Message |
| K | Breakaway Message |
| L | Sent Date |
| M | Stage |
| N | Results |

### Stage Dropdown Values

Create data validation on Column M:
- New
- Contacted
- Follow-up 1 sent
- Follow-up 2 sent
- Breakaway sent
- Replied
- Qualified
- Booked
- Stale

---

## Step 3: Message Templates

### Core Framework

**Voice:** Founder-to-founder, direct, no fluff
**Length:** Short paragraphs, specific facts
**Tone:** Curious, not pitchy

### First Message Formula

```
Hey [Name],

[Specific achievement/recent news]. [Company] is clearly building something real.

We've been doing this since [year] - [specific project with numbers]. I'm always interested in connecting with teams who've cracked [the angle]. Seems like you have.

Not pitching. Just think we might have useful context. Worth 15 minutes?

[Your Name]
```

### Example Messages

**Chris Yin - Plume Network:**
> Hey Chris,
>
> $150M RWA deployed. World Liberty Financial. You're clearly building something real at Plume.
>
> We've been doing this since 2017 - Clearpool ($650M+ in loans), several other DeFi products - and I'm always interested in connecting with teams who've cracked the institutional angle. Seems like you have.
>
> Not pitching. Just think we might have useful context. Worth 15 minutes?
>
> Vadim

**Sid Powell - Maple Finance:**
> Hey Sid,
>
> Surpassing BUIDL in AUM. Bitwise partnership. You're clearly building something real at Maple.
>
> We've been doing this since 2017 - Clearpool ($650M+ in loans), several other DeFi products - and I'm always interested in connecting with teams who've cracked the institutional angle. Seems like you have.
>
> Not pitching. Just think we might have useful context. Worth 15 minutes?
>
> Vadim

### Follow-up (Day 3-5)

**Formula:** No name, reference what you learned, offer value

> Just bumping this up. Clearpool, which we helped launch, has done $650M+ in loans since going live. What we learned: [insight]. Happy to share more if useful.

### Breakaway (Day 10)

**Formula:** Short, no pressure, door left open

> Last msg from me on this. But if you ever need help with [area], we're around. Best of luck.

---

## Step 4: SOP for Execution

### Daily Workflow (15-30 min)

1. **Open sheet** → Filter by Stage = "New"
2. **Pick top lead** → Click LinkedIn URL
3. **Click "Connect"** → Paste First Message → Send
4. **Update sheet:**
   - Add today's date in Sent Date (Column L)
   - Change Stage to "Contacted"
5. **Repeat** for remaining leads

### Follow-up Schedule

| Day | Action |
|-----|--------|
| Day 0 | Send First Message |
| Day 3-5 | If no response → Send Follow-up → Update Stage to "Follow-up 1 sent" |
| Day 10 | If no response → Send Breakaway → Update Stage to "Breakaway sent" |
| Day 14+ | If no response → Change Stage to "Stale" |

### Weekly Review (15 min)

1. Check Stage = "Replied" → Prioritize these
2. Note what messages got responses
3. Update Results column with outcome

---

## Step 5: GitHub Documentation

### SOP Document

Create in your repo: `/clients/[client]/SOP-outreach.md`

**Link:** https://github.com/maxfromcorveth/corveth-brain/blob/master/clients/holdex/SOP-outreach.md

### GitHub Issues

Create problems as they arise:

```markdown
## Problem: [Title]

## Context
- What's the issue?

## Solution
- How to resolve

ETA: [Date] | Deliverable: [What]
```

**Example Issues:**
- #652: Outreach volume requires manual execution
- #653: Waiting on LinkedIn profile data

---

## Tools & Resources

### LinkedIn
- Profile: linkedin.com
- Search: Use keywords like "CEO" + "DeFi" + "founder"

### Google Sheets
- Create: sheets.google.com
- Share with team: Click Share → add emails

### GitHub
- Repo: github.com/maxfromcorveth/corveth-brain
- Issues: github.com/holdex/marketing/issues

### Research Sources
- Crunchbase (funding data)
- LinkedIn (founder research)
- Company websites
- Press releases
- Industry newsletters

---

## Skills & Tools Used

This system uses Claude/OpenClaw skills for automation:

### 1. De-AI-ify
Removes AI-generated patterns from messages to sound more human.

- **Repo:** https://github.com/BrianRWagner/ai-marketing-claude-code-skills/tree/main/de-ai-ify
- **Skill:** `/de-ai-ify` - Run on any text to remove jargon, hedge words, corporate buzzwords

### 2. Cold Outreach Sequence
Generates personalized outreach sequences based on research.

- **Repo:** https://github.com/BrianRWagner/ai-marketing-claude-code-skills/tree/main/cold-outreach-sequence
- **Skill:** Uses research + personalization tiers to write messages

### Installation

```bash
# Clone the skills repo
git clone https://github.com/BrianRWagner/ai-marketing-claude-code-skills.git ~/.openclaw/skills/

# Skills will be available automatically
```

---

## Key Lessons

1. **Personalization wins** — Specific facts beat generic templates
2. **Follow-up is crucial** — 80% of responses come after first follow-up
3. **Track everything** — Sheet visibility keeps both sides aligned
4. **Voice matters** — Founder-to-founder sounds different than "agency"
5. **Execution is the bottleneck** — Without sending, nothing happens

---

## Files

| File | Link |
|------|------|
| Sheet (Cold) | https://docs.google.com/spreadsheets/d/16vNgb579V8ufNBYsO3sk5dyvKf2w_QGYC-FxKGZ5nBk |
| SOP | https://github.com/maxfromcorveth/corveth-brain/blob/master/clients/holdex/SOP-outreach.md |
| Spec Doc v2 | https://docs.google.com/document/d/1lmWw9lRx5hEX1e2xtAXRWZoi8UvZq-99qW86IV_lJoQ |

---

*System built: March 2026*
