---
id: TASK-000
title: <short task title>
status: open             # open | in_progress | done | needs_review | rejected
parent: main             # or subrepos/<name>/main.md for sub-repo tasks
subrepo: <name>          # the sub-repo this task targets (empty for cross-cutting)
assignee: <orchestrator | coder | human>
model: albert/deepseek-v4-flash-0731   # overridable; agnostic default
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

# TASK-000: <short task title>

> One task = one goal. This file is the **exchange contract** between the
> orchestrator (writer) and the atomic coder (reader/executor). Do not mix
> several goals in one task.

## Goal

The single thing this task must achieve, in one sentence.

## Context

Background needed to do the task. Point to `main.md`, other tasks, or files.

## Input contract

Exactly what the executor **receives**. What is available (repo path, files,
data, previous task outputs).

```yaml
repo: <path>
depends_on: [TASK-001, TASK-002]
inputs:
  - <file or data the executor starts from>
```

## Output contract

Exactly what the executor must **produce and return**, nothing more. Explicit
enough that a stateless coder can complete without asking.

```yaml
artifacts:
  - <file(s) to produce>
contract:
  - <what must be true when done>
returns: <the artifact to hand back>
```

## Steps (suggested)

1. ...
2. ...
3. ...

## Result

> Filled in by the executor. Do not delete the contract above; append the
> outcome below and flip `status` in the front-matter.

### Outcome

<what was actually done>

### Artifacts produced

- <path to produced artifacts>

### Opinion / concerns

<honest senior-coder assessment, if any>

### CLARIFICATION NEEDED

<only if blocked: the precise question that must be answered>
