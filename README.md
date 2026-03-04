# Corveth Brain 🧠

Your AI's second brain. A knowledge management system for agentic AI users.

---

## ⚠️ IMPORTANT: Two Modes

Before we work, **specify which mode**:

| Mode | Command | What it covers |
|------|---------|----------------|
| **Consulting** | "Working on Consulting" | Client work (Holdex, future clients) |
| **Products** | "Working on Products" | Product testing (Corveth Brain, etc.) |

**Without mode specified → I will ask "Which mode?"**

---

## Architecture

### Layer 1: Memory/Brain (GitHub) — Permanent
- Knowledge, research, prompts, learnings
- Stays forever — source of truth

### Layer 2: Orchestration (Swappable)
- Task management, execution
- Can swap tools without losing memory

---

## Structure

```
corveth-brain/
├── .claude/                 # AI instructions
│   ├── consulting.md        # Client work mode
│   ├── products.md          # Product mode
│   ├── default.md           # Default rules
│   ├── context.md           # Current business state
│   └── tasks.md             # Current tasks
│
├── brain/                   # Shared knowledge (both modes OK)
│   ├── prompts/
│   └── knowledge/
│
├── clients/                # Consulting stream ⚠️
│   └── holdex/            # Current client
│       ├── context/       # Private client info
│       ├── knowledge/
│       └── tasks/
│
├── products/               # Products stream ⚠️
│   └── corveth-brain/     # Current product
│
└── experiments/            # Both modes use
    ├── active/
    └── completed/
```

---

## Guardrails

| Action | Rule |
|--------|------|
| Send message | Confirm mode + recipient first |
| Create file in `clients/` | Verify Consulting mode |
| Client secrets | Only in `clients/[name]/context/` |
| Products | Never mix client info |
| Priority | Consulting > Products |

---

## How to Work With Me

1. **You:** Specify mode ("Working on Consulting" or "Products")
2. **Me:** Read appropriate `.claude/[mode].md`
3. **Me:** Confirm and proceed
4. **External actions:** Always confirm before doing

---

## Current Status

**Consulting (Priority):**
- Holdex: Waiting on LinkedIn access → then launch outreach

**Products:**
- Corveth Brain: V1 built, need GTM validation

---

*Built for speed. Validated by results. Memory never forgets.*
