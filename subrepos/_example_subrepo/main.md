---
subrepo: <name>
parent: <project-name>     # points to the global spec (../main.md)
status: draft            # draft | active | completed | archived
version: 0.1.0
owner: <owner>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
tags: [<tag1>, <tag2>]
---

# <Sub-repo name> - sub-repo spec

> Spec of **one sub-repo** of the ecosystem. This is a *per-component* view;
> the whole-project view is the global `main.md` at the repo root. Keep this
> file aligned with the global goal.

## Purpose / role in the ecosystem

What this sub-repo does within the larger project, in one or two sentences.

## Goal

What this sub-repo is trying to achieve.

## Scope

- **In scope:** what is built / done here.
- **Out of scope:** what is handled elsewhere (other sub-repos).

## Interfaces with other sub-repos

How this sub-repo connects to the rest of the ecosystem (APIs, contracts,
data, dependencies).

## Code location

The code for this sub-repo lives in a **sibling repo** next to this specs
repo (e.g. `<project>/<name>-code`). Tasks in `tasks/` target that repo.

## Referenced specs

- `tasks/TASK-001-<slug>.md` - one-line description
- `../main.md` - the global (ecosystem) spec
