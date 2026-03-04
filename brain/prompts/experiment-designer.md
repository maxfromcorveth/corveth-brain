# Experiment Designer Prompt

Use this to design valid experiments.

## Template

```
## Experiment: [NAME]

### Hypothesis
[What you think will happen]

### What to Test
[Specific thing being tested]

### Success Metric
[How you'll measure success]

### Setup
[What you need to run it]
- Tool:
- Audience:
- Duration:

### Execution Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Expected Outcome
[What success looks like]

### Failure Criteria
[What means it didn't work]

### Timebox
[Max time to run]
```

---

## Example: LinkedIn Outreach Test

```
## Experiment: LinkedIn Cold Outreach Test

### Hypothesis
Personalized messages mentioning specific company details will get higher response than generic templates.

### What to Test
Company-specific personalization vs generic templates

### Success Metric
Response rate > 10%

### Setup
- Tool: LinkedIn + Minimax-generated messages
- Audience: 10 leads from European B2B SaaS list
- Duration: 1 week

### Execution Steps
1. Pick 10 leads with good data
2. Write 5 personalized, 5 generic (randomized)
3. Send connection requests with messages
4. Track responses after 7 days

### Expected Outcome
Personalized: 3+ responses
Generic: 0-1 responses

### Failure Criteria
No meaningful difference between groups

### Timebox
14 days max
```
