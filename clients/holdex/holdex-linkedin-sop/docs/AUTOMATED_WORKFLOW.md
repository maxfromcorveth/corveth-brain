# Automated Lead Processing Workflow

## Holdex LinkedIn Inbound Lead Management — SOP Addendum

---

## Overview

This addendum documents the **automated lead processing workflow** using OpenClaw AI agent. This system augments the manual SOP with automation for lead research, classification, and response generation.

**Current State:** Max (CMO) reviews all processed leads before forwarding to Vadim
**Goal State:** Full autonomy — OpenClaw delivers directly to Vadim within weeks

---

## The Workflow

### Current Flow (with Review)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           LINKEDIN                                         │
│                    Vadim's Connection Requests                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                             VADIM                                           │
│                                                                             │
│  1. Sees new connection request on LinkedIn                                │
│  2. Reviews the profile briefly                                            │
│  3. Forwards to Max: "process: linkedin.com/in/name"                     │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              MAX                                            │
│                                                                             │
│  1. Receives Vadim's message                                               │
│  2. Forwards to OpenClaw: "process: [LinkedIn URL]"                      │
│  3. [WAIT] for OpenClaw to process                                        │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          OPENCLAW                                           │
│                                                                             │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────┐  ┌────────────┐       │
│  │ 1. CAPTURE │  │  2. ENRICH   │  │3. CLASSIFY  │  │4. GENERATE │       │
│  │            │  │              │  │             │  │            │       │
│  │ Parse URL  │  │ Web search  │  │ Apply SOP   │  │ Select     │       │
│  │ Extract    │  │ Company     │  │ framework   │  │ template   │       │
│  │ context    │  │ Project     │  │ Tier 1-4    │  │ Personalize│       │
│  └─────────────┘  └──────────────┘  └─────────────┘  └────────────┘       │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐     │
│  │                    5. DELIVER TO MAX                            │     │
│  │                                                                  │     │
│  │   Telegram message with:                                        │     │
│  │   - Lead summary + research                                     │     │
│  │   - Classification + rationale                                   │     │
│  │   - Pre-written response options                                │     │
│  └─────────────────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              MAX                                            │
│                                                                             │
│  1. Reviews OpenClaw's output                                              │
│  2. Checks: Classification correct? Response appropriate?                  │
│  3. [A] Forward to Vadim (if good)                                         │
│  4. [B] Edit and forward (if needs changes)                                │
│  5. [C] Skip (if not relevant)                                             │
│  6. [D] Request more research (if insufficient info)                      │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                             VADIM                                           │
│                                                                             │
│  1. Receives enriched lead + response from Max                             │
│  2. Copies the personalized message                                         │
│  3. Sends on LinkedIn                                                      │
│  4. Updates Max on outcome                                                │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Roles & Responsibilities

### Vadim (CEO)

| Action | Description |
|--------|-------------|
| **Monitor LinkedIn** | Check for new connection requests |
| **Forward leads** | Send to Max with profile URL |
| **Execute** | Copy response and send on LinkedIn |
| **Report outcomes** | Tell Max what happened (meeting booked, no response, etc.) |

### Max (CMO)

| Action | Description |
|--------|-------------|
| **Relay leads** | Forward Vadim's requests to OpenClaw |
| **Review output** | Check classification, response quality |
| **Approve/Edit** | Forward to Vadim or adjust |
| **Train agent** | Refine OpenClaw prompt based on errors |
| **Track metrics** | Monitor conversion rates |

### OpenClaw (AI Agent)

| Action | Description |
|--------|-------------|
| **Research** | Find info on lead's background, company, project |
| **Classify** | Apply SOP tier framework |
| **Generate** | Create personalized response |
| **Deliver** | Send formatted output to Max |

---

## Communication Templates

### Vadim → Max (Forward Lead)

**Message:**
```
process: linkedin.com/in/johndoe
```

or with context:
```
process: linkedin.com/in/johndoe - seems to be building a DeFi lending protocol
```

### Max → OpenClaw (Request Processing)

**Message:**
```
process: linkedin.com/in/johndoe
```

### OpenClaw → Max (Deliver Result)

See OPENCLAW_PROMPT.md for exact format. Summary:

```
🔥 HOT LEAD ALERT

👤 Name: [Name]
💼 Title: [Title]
🏢 Company: [Company]
📊 Project: [Project]
🔍 Sector: [Sector]

📋 Research Summary:
• [Finding 1]
• [Finding 2]

✅ Classification: HOT
📝 Rationale: [Why]

---
📝 RESPONSE:
[Full message]

---
[A] Forward to Vadim
[B] Edit and forward
[C] Skip
[D] More research
```

im (Forward Approved### Max → Vad)

**Option A — Forward as-is:**
```
Here's the processed lead. Ready to send.

[OpenClaw's full response]
```

**Option B — With edits:**
```
Edited version (changes in bold):

[Response with edits]

---
Original for reference:
[Original OpenClaw response]
```

---

## Quality Assurance

### Max's Review Checklist

Before forwarding to Vadim, verify:

- [ ] **Classification correct?** Matches SOP criteria
- [ ] **Research complete?** Key findings present
- [ ] **Response personalized?** References their specific project
- [ ] **Template appropriate?** Right tier = right template
- [ ] **No errors?** Names, facts, grammar correct

### Common Errors to Catch

| Error Type | Example | Fix |
|------------|---------|-----|
| Wrong classification | Classifying investor as Hot | Apply criteria correctly |
| Generic response | "Thanks for connecting" without specifics | Add 3+ personalizations |
| Wrong sector | Calling RWA project "DeFi" | Verify sector in research |
| Missing info | No funding stage | Note as "Unknown" |
| Template mismatch | Using Hot template for Warm lead | Match tier to template |

---

## Training the Agent

When OpenClaw makes mistakes, improve the agent:

### Process

1. **Identify error** — Catch mistake during review
2. **Note the issue** — Write down what went wrong
3. **Correct it** — Make the edit yourself
4. **Feed back** — Tell OpenClaw what was wrong and the correct approach

### Example Feedback

**OpenClaw output:**
- Classification: HOT
- But lead is an investor, not a founder

**Max's feedback:**
```
⚠️ CLASSIFICATION ERROR

This lead is an INVESTOR, not a founder. Should be NURTURE tier.

Correction: Change classification to NURTURE, use investor template instead of founder template.

Tip: Look for words like "investing", "fund", "portfolio" in their bio. Founders typically say "building", "founder", "CEO".
```

---

## Progression to Autonomy

### Phase 1: Current (Weeks 1-2)
- Max reviews all OpenClaw outputs
- Error rate: Expected 20-30%
- Focus: Catch errors, train agent

### Phase 2: Spot Check (Weeks 3-4)
- Max reviews 50% of outputs randomly
- Error rate: Expected 10-15%
- Focus: Build confidence

### Phase 3: Light Review (Weeks 5-6)
- Max reviews only HOT leads
- Error rate: Expected 5-10%
- Focus: High-value only

### Phase 4: Full Autonomy (Week 7+)
- OpenClaw delivers directly to Vadim
- Max monitors metrics only
- Error rate: Expected <5%

---

## Metrics to Track

| Metric | Target | Review |
|--------|--------|--------|
| OpenClaw error rate | <20% initially, <5% eventually | Weekly |
| Classification accuracy | >80% | Weekly |
| Response quality score | Good/Acceptable/Poor | Weekly |
| Vadim's send rate | >80% of HOT leads | Weekly |
| Time to process lead | <5 minutes | Weekly |

---

## Troubleshooting

### OpenClaw not responding?

1. Check message format: Use `"process: [URL]"`
2. Try again: Sometimes agent gets stuck
3. Escalate to Max if repeated failures

### Poor quality output?

1. Note specific issues
2. Edit the response yourself
3. Provide detailed feedback to agent
4. Update OPENCLAW_PROMPT.md if systemic

### Vadim not receiving leads?

1. Check Max is forwarding promptly
2. Verify Telegram delivery
3. Check OpenClaw is messaging the right person

---

## Document Links

| Document | Purpose |
|----------|---------|
| `README.md` | Main SOP with classification, workflow |
| `OPENCLAW_PROMPT.md` | Detailed agent instructions |
| `QUICK_START.md` | Fast onboarding |
| `templates/TEMPLATE_LIBRARY.md` | Response templates |
| `ATTIO_SETUP_GUIDE.md` | CRM integration |

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | March 2026 | Initial workflow with Max review |

---

*This workflow evolves. Review and update weekly as the agent improves.*
