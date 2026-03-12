# Corveth Attio CRM Setup Guide

## Current State
- **API Key**: ✅ Configured and working
- **Objects available**: Companies, Deals, People
- **Custom attributes**: None yet (need to create)
- **Lists**: Empty

---

## Step 1: Create Custom Attributes for People

Go to Attio → People → Add these custom fields:

| Field | Type | Options | Purpose |
|-------|------|---------|---------|
| **Lead Tier** | Single Select | Hot, Warm, Nurture, Pass | Classification |
| **Lead Source** | Single Select | LinkedIn, Outreach, Referral, Website, Other | How they found us |
| **LinkedIn Profile** | URL | — | Profile link |
| **Company Website** | URL | — | Their company site |
| **Revenue Range** | Single Select | $0-1M, $1-5M, $5-10M, $10-50M, $50M+ | Company size |
| **Last Contact Date** | Date | — | Track outreach |
| **Next Action** | Text | — | What to do next |
| **Next Action Date** | Date | — | When to do it |
| **Outreach Stage** | Single Select | New, Contacted, Follow-up 1, Follow-up 2, Breakaway, Replied, Qualified, Meeting Booked, Closed Won, Closed Lost | Pipeline |

---

## Step 2: Create "Corveth Leads" List

1. Go to Attio → Lists → Create new list
2. Name: **Corveth Leads**
3. Parent object: **People**
4. Add list-specific attributes:
   - **Priority** (Single Select: High, Medium, Low)
   - **Notes** (Text)

---

## Step 3: Connect to LinkedIn (Manual for Now)

Since LinkedIn API is restrictive:
1. Export leads from LinkedIn Sales Navigator
2. Import via Attio UI or API
3. Or use the sheet → API workflow

---

## API Usage for Automation

### Add a new lead:
```bash
curl -X POST "https://api.attio.com/v2/objects/people/records" \
  -H "Authorization: Bearer YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": {"first_name": "John", "last_name": "Doe"},
    "email_addresses": [{"address": "john@company.com"}],
    "lead_tier": {"value": "Warm"},
    "lead_source": {"value": "LinkedIn"},
    "linkedin_profile": {"url": "https://linkedin.com/in/johndoe"}
  }'
```

### Update lead stage:
```bash
curl -X PATCH "https://api.attio.com/v2/objects/people/records/RECORD_ID" \
  -H "Authorization: Bearer YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "outreach_stage": {"value": "Contacted"},
    "last_contact_date": {"value": "2026-03-12"}
  }'
```

---

## Next Steps for Automation

1. **Create attributes** (you do in UI)
2. **I can then**:
   - Auto-create leads from outreach
   - Track stage progression
   - Create follow-up tasks
   - Generate pipeline reports

---

## Want Me to Create the Attributes via API?

I can create the custom fields programmatically. Just confirm and I'll:
1. Create `lead_tier` select attribute
2. Create `lead_source` select attribute  
3. Create `outreach_stage` select attribute
4. Create the other fields (URL, date, text)

Want me to do that?
