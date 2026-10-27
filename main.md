---
project: TanaT Lab
status: active           # draft | active | completed | archived
version: 0.1.0
owner: TanaT-Lab
created: 2026-10-26
updated: 2026-10-26
tags: [trajectory-analysis, longitudinal-data, deep-learning, care-pathways]
---

# TanaT Lab - global spec

> The **global, whole-project** view. TanaT Lab is an **ecosystem of
> sub-repos** hosted on the [TanaT-Lab](https://github.com/TanaT-Lab) GitHub
> organization; this file summarizes it and points to each sub-repo's own spec.

## Goal

**TanaT Lab** develops methodologies and open-source tools for trajectory
analysis, longitudinal data modeling, and Deep Learning applications, with a
specialized focus on patient care pathways.

## Scope

- **In scope:** the TanaT core library and its satellite repos (shared
  utilities, embeddings, synthetic datasets, public demos).
- **Out of scope:** model or agent tooling (lives in `agents-kit`, not here).

## Context

- The main project is **TanaT** (Temporal Analysis of Trajectories), published
  on PyPI as `tanat`.
- Repos are migrating from `gitlab.inria.fr/tanat` to `github.com/TanaT-Lab`.
- This specs repo was originally TanaT-specific; those specs now live under
  `subrepos/tanat/`.

## Sub-repos

Each sub-repo has its own spec (`main.md` + `tasks/`) under `subrepos/<name>/`.
Code lives in sibling repos next to this specs repo (`TanaT-Lab/<repo>`).

| Sub-repo | Code repo | Role in ecosystem | Spec |
|----------|-----------|-------------------|------|
| `tanat` | [TanaT-Lab/TanaT](https://github.com/TanaT-Lab/TanaT) | Core library for trajectory analysis | `subrepos/tanat/main.md` |
| `tanat-utils` | [TanaT-Lab/tanat-utils](https://github.com/TanaT-Lab/tanat-utils) | Shared utilities for the TanaT ecosystem | `subrepos/tanat-utils/main.md` |
| `tanat-embs` | [TanaT-Lab/tanat-embs](https://github.com/TanaT-Lab/tanat-embs) | WIP: experiments and implementation of embeddings facilities | `subrepos/tanat-embs/main.md` |
| `tanat-synthea` | [TanaT-Lab/tanat-synthea](https://github.com/TanaT-Lab/tanat-synthea) | Synthetic patient journey datasets for longitudinal analysis | `subrepos/tanat-synthea/main.md` |
| `tanat-demo` | [TanaT-Lab/tanat-demo](https://github.com/TanaT-Lab/tanat-demo) | Narrated interactive demos of TanaT (conference showcase) | `subrepos/tanat-demo/main.md` |

`subrepos/_example_subrepo/` is the template for adding a new sub-repo.

## Referenced specs

- `subrepos/tanat/main.md` - core library (constitution, review, testing rules)
- `subrepos/tanat-utils/main.md` - shared utilities
- `subrepos/tanat-embs/main.md` - embeddings
- `subrepos/tanat-synthea/main.md` - synthetic datasets
- `subrepos/tanat-demo/main.md` - demos
- `architecture.md` - how the sub-repos depend on each other
- `conventions.md` - lab-wide conventions
