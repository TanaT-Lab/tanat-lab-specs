# Tasks

Index and global status of all tasks. Update this as tasks move through their
lifecycle. Each task is one file: `TASK-<NNN>-<slug>.md`.

## Status legend

- **open** - defined, not started
- **in_progress** - being executed
- **done** - completed and contract satisfied
- **needs_review** - done, awaiting human/orchestrator review
- **rejected** - closed without completion (reason in the task)

## Board

| Task | Title | Status | Depends on |
|------|-------|--------|------------|
| TASK-001 | <title> | open | - |

## Transient exchange

Intermediate exchange between orchestrator and coders goes in
`tasks/.exchange/` - **git-ignored**, not part of the durable record. The
`TASK-*.md` files are git-ignored too: only this board is versioned, and what
a task teaches (decisions, findings) goes into `../main.md`.
