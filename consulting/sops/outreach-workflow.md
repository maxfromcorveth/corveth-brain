# Client Acquisition System: Corveth LinkedIn Outreach

A complete system for setting up manual LinkedIn outreach for Corveth Consulting. Based on the Holdex outreach system — adapted for RevOps consulting with Corveth's ICP voice.

---

## Overview

| Aspect | Details |
|--------|---------|
| **Goal** | Book meetings with SaaS founders who need RevOps help |
| **Model** | Manual execution (no automation due to LinkedIn ban risk) |
| **Time** | 15-30 min/day |
| **Tools** | Google Sheets, LinkedIn, GitHub |
| **Output** | Qualified meetings booked |

---

## ICP (Ideal Customer Profile)

| Attribute | Details |
|-----------|---------|
| **Role** | Founder, CEO, CRO, VP Revenue |
| **Company** | B2B SaaS, 11-200 employees |
| **Funding** | Seed, Series A, Series B |
| **Pain Points** | "Flying blind", CRM is a mess, can't forecast, sales/marketing misalignment |
| **Industry** | SaaS, Fintech, DevTools, MarTech |

---

## Step 1: Lead Research

### Sources

- Your Crunchbase company list (~2000 companies)
- LinkedIn company pages
- Company websites
- Press releases, funding news

### Enrichment

When you need fresh leads:
1. Open your company list (from Crunchbase)
2. Find founder/CEO on LinkedIn
3. Validate: Do they fit ICP? Do they have budget?
4. Add to sheet

---

## Step 2: Sheet Setup

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
- Do Not Contact

### Template Tab

Store your message templates here for easy copy/paste.

---

## Step 3: Message Templates

### Corveth Voice

- **Tone:** Founder-to-founder, direct, slightly irreverent
- **What founders say:** "flying blind", "CRM is a mess", "two truths, zero alignment"
- **What we say:** Match their language, throw shade at typical consultants
- **Length:** Short paragraphs, specific facts
- **Not:** Corporate, pitchy, consultant-speak

### First Message Formula

```
Hey [Name],

Saw [recent news/funding/announcement]. Looks like [Company] is [what they're building or achieving].

Quick context: I've been in revenue operations for [X years]. Built marketing for companies that actually scaled. Here's what I know: most founders fly blind because their CRM is a mess and sales + marketing can't agree on anything.

Not pitching. Just curious if any of that resonates. If it does, happy to share what I've seen work.

[Your Name]
```

### Example Messages

**Founder at Series A SaaS:**
> Hey [Name],
>
> $12M Series A. Solid round. Looks like [Company] is scaling.
>
> Quick context: I've been in revenue operations for years. Built marketing for companies that actually scaled. Here's what I know: most founders fly blind because their CRM is a mess and sales + marketing can't agree on anything.
>
> Not pitching. Just curious if any of that resonates. If it does, happy to share what I've seen work.
>
> Max

**Founder at Seed-stage:**
> Hey [Name],
>
> Just saw [Company] came out of stealth / raised seed / launched. Interesting space.
>
> Quick context: I've been in revenue operations for years. Built marketing for companies that actually scaled. Here's what I know: most founders fly blind because their CRM is a mess and sales + marketing can't agree on anything.
>
> Not pitching. Just curious if any of that resonates. If it does, happy to share what I've seen work.
>
> Max

### Follow-up (Day 3-5)

**Formula:** Reference what you noticed, offer a specific insight

> Just bumping this up.
>
> One thing I've noticed with [Company's stage] — the revenue operations piece usually becomes a headache around now. Forecasting gets fuzzy, CRM turns into a data graveyard, and suddenly you can't explain to the board where revenue is coming from.
>
> If any of that sounds familiar, happy to chat. No pitch — just context from someone who's been there.

### Breakaway (Day 10)

**Formula:** Short, no pressure, door left open

> Last msg from me on this.
>
> If revenue operations ever becomes a headache — forecasting, CRM, alignment between sales and marketing — I'm around. Not a typical consultant who hands you a PDF and vanishes.
>
> Best of luck with [Company].

---

## Step 4: SOP for Execution

### Daily Workflow (15-30 min)

1. **Open sheet** → Filter by Stage = "New"
2. **Pick top lead** → Click LinkedIn URL
3. **Personalize the message** — Add 1-2 specific details about their company
4. **Click "Connect"** → Paste First Message → Send
5. **Update sheet:**
   - Add today's date in Sent Date (Column L)
   - Change Stage to "Contacted"
6. **Repeat** for remaining leads (aim for 10-20/day)

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
4. Personalize your templates based on what works

---

## Step 5: GitHub Documentation

### SOP Location

`/consulting/sops/outreach-workflow.md`

### Issue Tracking

Track progress in GitHub:
- Issue #12: Write outreach sequences
- Issue #8: Source target companies list (close when list saved)
- Issue #4: Automate Consulting Lead Gen (parent goal)

---

## Tools & Resources

### Skills for Message Creation

- **De-AI-ify:** Remove AI-generated patterns from copy
  - https://github.com/BrianRWagner/ai-marketing-claude-code-skills/tree/main/de-ai-ify
- **Cold Outreach Sequence:** Generate personalized outreach messages
  - https://github.com/BrianRWagner/ai-marketing-claude-code-skills/tree/main/cold-outreach-sequence

### LinkedIn
- Profile: linkedin.com
- Search: Use keywords like "CEO" + "SaaS" + "founder"

### Google Sheets
- Create: sheets.google.com
- Share with team: Click Share → add emails

### GitHub
- Repo: github.com/maxfromcorveth/corveth-brain
- Issues: For tracking progress

### Research Sources
- Crunchbase (funding data)
- LinkedIn (founder research)
- Company websites
- Press releases
- Industry newsletters

---

## Key Lessons

1. **Personalization wins** — Specific facts beat generic templates
2. **Follow-up is crucial** — 80% of responses come after first follow-up
3. **Track everything** — Sheet visibility keeps progress clear
4. **Voice matters** — Founder-to-founder sounds different than "agency"
5. **Execution is the bottleneck** — Without sending, nothing happens

---

## Files

| File | Location |
|------|----------|
| This SOP | `consulting/sops/outreach-workflow.md` |
| ICP Research | `consulting/icp-language-research.md` |
| Company List | Your Google Sheet from Crunchbase |

---

## Next Steps

1. Create your Google Sheet (copy the columns above)
2. Add your first batch of leads (20-50 to start)
3. Personalize message templates for your voice
4. Start sending: 10-20/day
5. Track responses, iterate

---

*System built: March 2026*
*For: Corveth Consulting lead generation*
