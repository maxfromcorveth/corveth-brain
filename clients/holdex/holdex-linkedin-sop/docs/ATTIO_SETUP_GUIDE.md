# Attio CRM Setup Guide

## LinkedIn Lead Management System Integration

---

## Overview

This guide provides step-by-step instructions for setting up Attio to support the LinkedIn Inbound Lead Management SOP. Since Holdex already has Attio configured, this guide focuses on the customizations needed specifically for this system.

### Prerequisites

- Access to Attio with admin or editor permissions
- Existing Attio account for Holdex
- Basic understanding of Attio's data model

---

## Step 1: Create Custom Fields

Navigate to **Settings → Data Model → People** (or Contacts) and create the following custom fields:

### Lead Classification Fields

| Field Name | Type | Options | Description |
|------------|------|---------|-------------|
| Lead Tier | Single Select | Hot, Warm, Nurture, Pass | Classification based on SOP framework |
| Lead Source | Single Select | LinkedIn Inbound, LinkedIn Outbound, Referral, Event, Outbound, Other | How the lead was acquired |

### Project Information Fields

| Field Name | Type | Options | Description |
|------------|------|---------|-------------|
| Project Name | Text | — | Name of the lead's project or company |
| Project Stage | Single Select | Idea, Pre-Seed, Seed, Series A, Series B+ | Current funding/development stage |
| Project Sector | Multi-select | DeFi, RWA, Infrastructure, L1/L2, DAO, Gaming, NFT, Tools, Other | Web3 sector focus |
| Project Description | Long Text | — | Brief description of what they're building |

### LinkedIn Specific Fields

| Field Name | Type | Options | Description |
|------------|------|---------|-------------|
| LinkedIn Profile URL | URL | — | Direct link to their LinkedIn profile |
| LinkedIn Connection Date | Date | — | When the connection was made |
| Initial Message Sent | Checkbox | Yes/No | Whether first outreach was sent |

### Activity Tracking Fields

| Field Name | Type | Options | Description |
|------------|------|---------|-------------|
| Last Contact Date | Date | — | Most recent outreach date |
| Last Contact Type | Single Select | Initial Message, Follow-up, Meeting Request, Call, Email | Type of last interaction |
| Next Action | Long Text | — | What needs to happen next |
| Next Action Date | Date | — | When the next action should occur |
| Days Since Last Contact | Formula | — | Calculated: Today - Last Contact Date |

### Deal Information Fields

| Field Name | Type | Options | Description |
|------------|------|---------|-------------|
| Potential Deal Value | Currency | — | Estimated deal size |
| Deal Type | Single Select | Co-building, Advisory, Consulting, Partnership, Investment | Type of potential engagement |
| Interest Level | Single Select | High, Medium, Low | CMO-assessed interest level |

---

## Step 2: Configure Pipeline Stages

Navigate to **Settings → Pipelines** and create or modify a pipeline called "Web3 Partnerships" (or use an existing pipeline).

### Recommended Stages

| Stage | Description | Color | Probability |
|-------|-------------|-------|-------------|
| New | Just classified, needs initial outreach | Gray | 0% |
| Responded | Lead has responded to outreach | Blue | 20% |
| Qualified | Confirmed fit, needs meeting | Yellow | 40% |
| Meeting Booked | Discovery call scheduled | Orange | 60% |
| Meeting Completed | Initial call held | Purple | 75% |
| Opportunity | Valid pipeline opportunity | Green | 50% |
| Closed Won | Successfully partnered | Dark Green | 100% |
| Closed Lost | No partnership formed | Red | 0% |

### Stage Entry/Exit Rules

| Stage | Entry Criteria | Exit Criteria |
|-------|---------------|---------------|
| New | Lead classified and logged | Initial message sent |
| Responded | Lead replied to message | Qualification complete |
| Qualified | Meeting requested or strong interest | Meeting booked |
| Meeting Booked | Calendar invite confirmed | Meeting held |
| Meeting Completed | Call finished, notes added | Opportunity confirmed or closed |
| Opportunity | Both parties interested in proceeding | Deal won or lost |
| Closed Won | Contract signed | — |
| Closed Lost | Explicit decline or 3+ no-responses | — |

---

## Step 3: Create Lists (Views)

Create the following list views in Attio for efficient lead management:

### Active Lists

| List Name | Filter Criteria | Purpose |
|-----------|----------------|---------|
| **Hot Leads (Tier 1)** | Lead Tier = Hot | Immediate priority |
| **Today's Follow-ups** | Next Action Date = Today | Daily action items |
| **This Week's Follow-ups** | Next Action Date ≤ 7 days from today | Weekly planning |
| **Stale Leads (14+ days)** | Days Since Last Contact > 14 AND Stage not in (Closed Won, Closed Lost) | Leads needing attention |
| **Meeting Booked This Month** | Stage = Meeting Booked | Upcoming meetings |
| **Rotation: Current Segment** | Rotation Segment = [Current Segment] | Segment-focused review |

### Segment-Specific Lists

Create lists for each rotation segment:

- DeFi Protocols Active
- RWA Projects Active
- Infrastructure Active
- Layer 1/2 Chains Active
- DAOs & Governance Active
- Web3 Tools & Apps Active
- Investors Active
- Ecosystem Players Active
- Warm Leads Pool

---

## Step 4: Set Up Tasks

Create task templates for recurring actions:

| Task Name | Related To | Due Date | Assignee | Description |
|-----------|------------|----------|----------|-------------|
| Initial Outreach (Tier 1) | Lead | Same day as created | Vadim | Send Tier 1 response template |
| Initial Outreach (Tier 2) | Lead | Within 3 days | Vadim | Send Tier 2 response template |
| Initial Outreach (Tier 3) | Lead | Within 7 days | Vadim | Send Tier 3 response template |
| Follow-up Day 3 | Lead | 3 days after last contact | Vadim | Send Day 3 follow-up |
| Follow-up Day 7 | Lead | 7 days after last contact | Vadim | Send Day 7 follow-up |
| Weekly Pipeline Review | — | Every Monday | CMO | Review pipeline health |
| Segment Rotation Check | — | Every 5 days | CMO | Confirm segment rotation |

---

## Step 5: Create Automation Rules

Since Vadim prefers manual over automation (to protect the LinkedIn account), keep automations minimal. Set up only these low-risk rules:

### Task Creation Automations

| Trigger | Condition | Action | Risk Level |
|---------|-----------|--------|------------|
| Lead created | Lead Tier = Hot | Create task: "Priority Outreach" | Low |
| Lead created | Lead Tier = Warm | Create task: "Nurture Sequence" | Low |
| Stage changed to Responded | — | Create task: "Qualify Lead" | Low |
| Stage changed to Qualified | — | Create task: "Book Meeting" | Low |

### Reminder Automations

| Trigger | Condition | Action | Risk Level |
|---------|-----------|--------|------------|
| 7 days passed | Stage = Responded AND Lead Tier = Hot | Create task: "Follow-up Day 7" | Low |
| 14 days passed | Stage not in (Closed Won, Closed Lost) | Create task: "Review Stale Lead" | Low |

**Important**: Do not create automations that send LinkedIn messages directly. All outreach must be manual to protect the account.

---

## Step 6: Create Reports

Set up the following reports for weekly and monthly reviews:

### Weekly Metrics Report

| Metric | Description |
|--------|-------------|
| Connection Request Volume | Total new leads created this week |
| Tier Distribution | Breakdown by Lead Tier |
| Response Rate | % of leads that responded |
| Meeting Booking Rate | % of Qualified that became Meeting Booked |
| Pipeline by Stage | Count in each stage |
| Segment Progress | % complete of current segment |

### Monthly Performance Report

| Metric | Description |
|--------|-------------|
| Tier 1 Conversion Rate | % of Tier 1 that became meetings |
| Pipeline Velocity | Average days from New to Meeting Booked |
| Closed Won Deals | Number of successful partnerships |
| Rotation Completion | Segments completed this month |
| Top Sectors | Most common project sectors |

---

## Step 7: Integration with LinkedIn

### Manual Logging Process

Since we're avoiding automated LinkedIn integration (to protect the account), follow this manual process:

1. **When receiving a connection request**:
   - Review on LinkedIn
   - Apply classification using SOP
   - Create lead in Attio with all relevant fields

2. **When sending a message**:
   - Send manually on LinkedIn
   - Log in Attio: Create a "Note" with date, message type, and content

3. **When receiving a response**:
   - Respond on LinkedIn
   - Update Attio: Add "Note" and update Stage

4. **When booking a meeting**:
   - Create calendar event
   - Update Attio: Change Stage to "Meeting Booked", add meeting date

### No-Code Integration Options (Optional)

If you later want to explore light automation, consider these options:

| Option | Description | Risk Level |
|--------|-------------|------------|
| Zapier (Webhooks) | Trigger task creation on external events | Medium |
| Make (Integromat) | Sync data between platforms | Medium |
| Browser Extensions | Manual copy-paste helpers | Low |

**Warning**: Avoid any tool that requires LinkedIn OAuth credentials or claims to automate LinkedIn messaging. These violate LinkedIn's Terms of Service and can result in account bans.

---

## Step 8: Daily Usage Workflow

### Morning Routine (15 minutes)

1. Open Attio and go to **Today's Follow-ups** list
2. Complete each task (send LinkedIn messages manually)
3. After sending, update the lead record:
   - Update "Last Contact Date" to today
   - Add a Note with what was sent
   - Update "Next Action Date" if follow-up needed

4. Check LinkedIn for new connection requests
5. For each new request:
   - Apply classification
   - Create new lead in Attio
   - Set appropriate "Next Action Date"

### Weekly Review (30 minutes)

1. Go to **Stale Leads (14+ days)** list
2. Review each lead and determine:
   - Send another follow-up
   - Move to Nurture stage
   - Mark as Closed Lost

3. Review **Pipeline by Stage** for accuracy
4. Check **Rotation: Current Segment** for completeness
5. Generate weekly metrics report

---

## Step 9: Data Quality Guidelines

To maintain accurate data in Attio:

### Required Fields for Every Lead

- [ ] Name
- [ ] LinkedIn Profile URL
- [ ] Lead Tier
- [ ] Lead Source
- [ ] Rotation Segment
- [ ] Stage
- [ ] Next Action Date

### Update Frequency

| Field | Update When |
|-------|-------------|
| Stage | After any meaningful interaction |
| Last Contact Date | After sending or receiving a message |
| Next Action Date | After setting a follow-up reminder |
| Notes | After every interaction |
| Project Information | When new information is learned |

### Data Validation Rules

- Next Action Date should always be in the future (or today)
- Leads in Closed Won/Lost should have a "Loss/Win Reason" note
- All Hot leads should have a response within 24 hours

---

## Step 10: Troubleshooting Common Issues

### Issue: Leads don't appear in expected lists

**Solution**: Check that the lead's fields match the list filters exactly. Common issues include:

- Misspelled segment name
- Lead Tier not set
- Stage not updated

### Issue: Can't find a lead

**Solution**: Use global search (Cmd+K) to search by name, company, or LinkedIn URL.

### Issue: Tasks not creating automatically

**Solution**: Verify the automation rules are active in Settings → Automations. Check that trigger conditions are met.

### Issue: Pipeline stages not flowing correctly

**Solution**: Ensure each stage has clear entry criteria and that the team understands when to move leads.

---

## Quick Start Checklist

Use this checklist when first setting up the system:

- [ ] Create all custom fields (Step 1)
- [ ] Configure pipeline stages (Step 2)
- [ ] Create list views (Step 3)
- [ ] Set up task templates (Step 4)
- [ ] Review automation rules (Step 5)
- [ ] Create reports (Step 6)
- [ ] Train team on daily workflow (Step 8)
- [ ] Establish data quality standards (Step 9)
- [ ] Process first batch of leads
- [ ] Review and optimize after 30 days

---

## Support

For Attio-specific questions:

- Attio Help Center: help.attio.com
- Attio Support: support@attio.com

For questions about this SOP:

- Refer to the main README.md
- Contact the CMO

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | March 2026 | MiniMax Agent | Initial setup guide |
