# LinkedIn Inbound Lead Management SOP

**Holdex Marketing Team**  
**Issue:** https://github.com/holdex/marketing/issues/659  
**Target Audience:** DeFi/RWA Founders  
**CRM:** Attio

---

## Overview

This SOP defines the process for handling inbound LinkedIn connection requests from DeFi/RWA founders. The goal is to systematize response, qualify opportunities, and convert interest into meetings—no lead falls through the cracks.

**Core Principle:** Every inbound connection is a potential conversation starter. Respond fast, personalize genuinely, and move qualified leads to offer within 48 hours.

---

## The 4-Step Framework

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  DIAGNOSE   │ →  │   BUCKET    │ →  │  QUALIFY    │ →  │   OFFER     │
│  "Who are   │    │  "Where do  │    │  "Is this   │    │  "Here's    │
│   they?"    │    │  they fit?" │    │  a fit?"    │    │  what we    │
│             │    │             │    │             │    │  can do"    │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
     24h               24h               24-48h            Immediate
```

### Step 1: DIAGNOSE (Within 24 hours)

Review their LinkedIn profile and determine:
- **Role:** Founder, Co-founder, CEO?
- **Company:** What are they building? Stage (seed, Series A, etc.)?
- **Context:** Recent posts, content, funding news?
- **Connection note:** Why did they connect? (Check invite message)

### Step 2: BUCKET (Within 24 hours of diagnose)

Assign to one of three buckets:

| Bucket | Criteria | Action |
|--------|----------|--------|
| **HOT** | Active DeFi/RWA founder, recent funding, relevant pain point | Fast-track to qualify |
| **WARM** | Founder adjacent (CTO, Product), growing company, unclear fit | Nurture with value |
| **COLD** | Non-founder, wrong sector, no clear alignment | Add to 45-day rotation |

### Step 3: QUALIFY (Within 24-48 hours)

Ask qualification questions via LinkedIn message (see templates below). Criteria:
- Budget authority or fundraising status
- Timeline (when do they need help?)
- Specific pain point alignment with Holdex services

### Step 4: OFFER (Immediate when qualified)

Present specific next step based on their qualification response:
- Discovery call
- Portfolio/case study share
- Intro to other relevant contact

---

## Attio CRM Integration

### Pipeline View: "Inbound LinkedIn Leads"

Create the following columns in your Attio pipeline:

| Column | Type | Description |
|--------|------|-------------|
| **Lead Name** | Person | Full name |
| **Company** | Company | Their project/company |
| **LinkedIn URL** | Text | Profile link |
| **Bucket** | Single Select | HOT / WARM / COLD |
| **Lead Source** | Single Select | LinkedIn Connection Request |
| **Connection Date** | Date | When they connected |
| **Last Contact Date** | Date | Last message sent |
| **Next Follow-up** | Date | Scheduled follow-up |
| **Status** | Single Select | New / Diagnosed / Qualified / Converted / Archived |
| **Response Count** | Number | Messages exchanged |
| **Notes** | Text | Call context, qualification answers |
| **Rotation Cycle** | Number | 1-3 (see 45-day system) |

### Workflow Triggers

- **New connection received:** Create Attio record, set Status = "New"
- **Diagnosed:** Set Status = "Diagnosed", update Bucket
- **Qualified:** Set Status = "Qualified", schedule next follow-up
- **Converted:** Set Status = "Converted", move to sales pipeline
- **45-day rotation:** When Next Follow-up = today, trigger outreach

---

## 45-Day Rotation System

No lead gets ignored. Every COLD or unresponsive lead enters the rotation.

### How It Works

```
Day 0:  Initial message sent
Day 5:  Follow-up #1 (if no response)
Day 10: Follow-up #2 (if no response)
Day 15: Mark as "No Response" → Archive
Day 45: Rotate back into active queue (if meets re-engagement criteria)
Day 50: Re-engagement message
Day 55: Final follow-up
Day 60: Archive permanently
```

### Rotation Rules

- **Max 3 rotation cycles** before permanent archive
- **Re-engagement criteria:** New funding, new role, relevant content posted
- **Warm leads** stay in rotation but get lower priority
- **HOT leads** never rotate—they get personal outreach until converted or explicitly rejected

### Tracking the Rotation

In Attio, use the **Rotation Cycle** column:
- `0` = New, never contacted
- `1` = First rotation (Day 0-15)
- `2` = Second rotation (Day 45-60)
- `3` = Third rotation (Day 90-105) — final attempt

---

## Message Templates

All messages follow the **de-ai-ify** principle: no jargon, short sentences, specific references, human tone.

### Template 1: Diagnose Message (Initial Response)

**When:** Within 24 hours of new connection  
**Goal:** Acknowledge, reference something specific, open conversation

```
Hey [First Name],

Thanks for the connection — I saw your recent post about [specific topic from their content]. Solid take.

I run growth for Holdex. We work with DeFi and RWA projects on go-to-market and user acquisition.

What brings you to LinkedIn today? Always good to meet fellow builders in the space.

Best,
[Your Name]
```

**De-ai-ify notes:**
- "Solid take" replaces "interesting perspective"
- "What brings you to LinkedIn today?" replaces "I wanted to reach out because..."
- Short. Direct. No filler.

---

### Template 2: Qualification Questions

**When:** After diagnose response, within 24 hours  
**Goal:** Understand fit and timeline

```
Hey [First Name],

Quick Qs to see if we can help:

1. What's the main growth challenge you're facing right now?
2. Are you funded, or still in the build phase?
3. When are you looking to ramp up user acquisition?

No pressure — just helps me figure out if it's worth a quick call or if I should point you to some resources.

Best,
[Your Name]
```

**Alternative (if they're clearly a founder):**
```
Hey [First Name],

Congrats on [their recent milestone — funding, launch, etc.]. The RWA space is heating up.

Curious: are you looking for help with marketing now, or is it more of a "when we hit [milestone]" thing?

Either way, happy to chat strategy.

Best,
[Your Name]
```

---

### Template 3: The Offer (After Qualification)

**When:** Immediately after they respond with qualification info  
**Goal:** Propose specific next step

```
Hey [First Name],

That makes sense. Here's what I'd suggest:

If you want to talk strategy, I can do a 20-min discovery call — no pitch, just mapping out what might work for [Company]. We've helped [similar project] do [specific result].

If you'd rather dig in first, I can send over our one-pager on DeFi user acquisition — covers what works, what doesn't, and where most projects mess up.

Up to you. What's your style?

Best,
[Your Name]
```

**When they're clearly ready:**
```
Hey [First Name],

Let's hop on a call. I'll send you a calendar link — 20 mins, we can cover:

- What's working for [their competitors]
- Where most RWA projects get stuck
- Quick wins you could implement this month

[Calendar Link]

Works?

Best,
[Your Name]
```

---

### Template 4: Follow-up #1 (Day 5)

**When:** No response to diagnose message after 5 days  
**Goal:** Gentle nudge, add value

```
Hey [First Name],

Checking in — didn't want this to get lost in your inbox.

If DeFi marketing isn't on your radar right now, no worries. I'll circle back in a bit.

But if you ever want to swap notes on what's working in the space, I'm around.

Best,
[Your Name]
```

---

### Template 5: Follow-up #2 (Day 10)

**When:** No response after Follow-up #1  
**Goal:** Last attempt before archiving

```
Hey [First Name],

One more try — then I'll stop bothering you.

If [specific insight related to their company/sector] is ever relevant, holler.

Otherwise, best of luck with [their current project/launch].

Cheers,
[Your Name]
```

---

### Template 6: Re-engagement (Day 45+)

**When:** Lead in rotation, new activity detected  
**Goal:** Re-open conversation with relevance

```
Hey [First Name],

Saw you [new activity — funding announcement, new hire, post]. Congrats — the RWA space is moving fast.

We actually just wrapped a campaign for [similar project] that got [specific result]. Might be relevant to where you're at now.

Curious if it's worth a conversation?

Best,
[Your Name]
```

---

## Usage Instructions

### Daily Workflow (10 min/day)

1. **Check LinkedIn** for new connection requests (morning)
2. **Pull new requests** → Review profiles → Create Attio records
3. **Send diagnose messages** to all new HOT leads
4. **Check Attio** for leads needing follow-up (Next Follow-up = today)
5. **Send follow-ups** using templates above

### Weekly Review (30 min/week)

1. **Pipeline review:** Check all leads in "New" / "Diagnosed" status
2. **Rotation check:** Move leads through 45-day cycle
3. **Bucket adjustment:** Promote WARM → HOT if new signals appear
4. **Archive cleanup:** Mark unresponsive leads after Day 15 / Day 60

### Key Metrics to Track

| Metric | Target |
|--------|--------|
| Response rate (diagnose message) | >50% |
| Time to first response | <24 hours |
| Qualification rate (HOT → Qualified) | >40% |
| Conversion rate (Qualified → Call booked) | >25% |
| Rotation recovery rate | >15% |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────┐
│  INBOUND LINKEDIN FLOW                                          │
├─────────────────────────────────────────────────────────────────┤
│  NEW CONNECTION → DIAGNOSE (24h) → BUCKET → QUALIFY (48h)     │
│        ↓                                                        │
│   [HOT] ──→ QUALIFY ──→ OFFER ──→ CALL                         │
│   [WARM] ──→ NURTURE ──→ 45-DAY ROTATION                       │
│   [COLD] ──→ 45-DAY ROTATION ──> ARCHIVE                       │
│                                                                 │
│  ATTIO COLUMNS: Status, Bucket, Next Follow-up, Rotation Cycle │
│  RESPONSE SLA: 24 hours                                         │
└─────────────────────────────────────────────────────────────────┘
```

---

## Appendix: De-AI-ify Checklist for Messages

Before sending any message, run through this:

- [ ] Remove: "I hope this finds you well"
- [ ] Remove: "I'd love to..." / "I wanted to reach out because..."
- [ ] Remove: Generic openings ("Hope you're having a great week")
- [ ] Keep: Short sentences (under 20 words)
- [ ] Keep: One specific reference to them
- [ ] Keep: Clear, low-friction question
- [ ] Keep: Your name at the end

---

**Last Updated:** March 2026  
**Owner:** Holdex Marketing Team  
**Review Cycle:** Monthly
