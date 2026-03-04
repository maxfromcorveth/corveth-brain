# Corveth Brain 🧠

Your AI's second brain. A knowledge management system for agentic AI users.

## Architecture: Two Layers

This system uses a **two-layer architecture**:

### Layer 1: Memory (GitHub) — Permanent
- **Purpose:** Knowledge, research, prompts, experiments, learnings
- **Stays forever** — it's the memory of the organization
- **Tool-agnostic** — works with any orchestration tool
- **Location:** This repository (`corveth-brain`)

### Layer 2: Orchestration (Swappable) — Execution
- **Purpose:** Task management, workflows, execution
- **Swappable** — try different tools without losing memory
- **Current:** `tools/mission-control/` (OpenClaw Mission Control)

---

## Why This Works

| Layer | What it does | Changes? |
|-------|--------------|----------|
| **Brain** | Memory, knowledge, learnings | Never changes — stays |
| **Orchestration** | Tasks, workflows, execution | Swap anytime |

**You can:**
- Switch orchestration tools (Mission Control → Notion → ClickUp)
- Brain stays the same — all knowledge preserved
- Try multiple businesses/products without losing context

---

## Quick Start

1. **For Claude/Max's AI:** Read `.claude/instructions.md` first
2. **Capture knowledge:** Use `brain/knowledge/`
3. **Run experiments:** Use `experiments/`
4. **Manage tasks:** Use `tools/mission-control/`

---

## Structure

```
corveth-brain/
├── brain/              # Layer 1: Permanent knowledge
│   ├── prompts/        # Reusable prompt templates
│   ├── knowledge/     # Market research, insights, lessons
│   └── instructions/  # AI-specific rules
├── experiments/       # Tests and validation
│   ├── active/
│   └── completed/
├── tools/             # Layer 2: Orchestration (swappable)
│   └── mission-control/
└── .claude/          # Max's AI-specific config
```

---

## Testing Multiple Products/Services

This system is designed to test offers until one sticks:

1. **Capture learnings** → `brain/knowledge/`
2. **Run experiments** → `experiments/`
3. **Track tasks** → `tools/mission-control/`
4. **Document results** → What worked/didn't

Each test adds to the brain. Knowledge compounds.

---

## Contributing

1. New insight → `brain/knowledge/`
2. New experiment → `experiments/active/`
3. New prompt → `brain/prompts/`
4. Change orchestration → Add to `tools/`

---

*Built for speed. Validated by results. Memory never forgets.*
