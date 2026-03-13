# Holdex ICP Scoring System Design

## ICP JSON Created
See: `consulting/holdex-icp.json`

## For the AI Agent Prompt

```
Design a complete ICP scoring system for Holdex (Web3 marketing agency).

## ICP Reference
See attached: holdex-icp.json

## Current Problem
We have 2,034 LinkedIn connections but simple keyword matching gives inaccurate results.

## What We Need

### 1. Lead Enricher Skill
Design a skill that:
- Input: LinkedIn profile URL
- Process: Visit profile + company website, extract data
- Output: Structured lead data

### 2. ICP Scorer Skill
Design a skill that:
- Input: Enriched lead data
- Process: Compare against ICP criteria
- Output: Score 0-100 with breakdown

### 3. Signal Finder Skill
Design a skill that:
- Input: Company website URL
- Process: Find buying signals
- Output: Signal list with priority

## Key Questions
1. How to handle missing data in scoring?
2. What weights make sense for Web3?
3. How to automate enrichment at scale?

## Deliverable
- Skill structures (input/process/output)
- Scoring logic
- Recommendations for automation
```
