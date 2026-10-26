---
subrepo: tanat
parent: TanaT Lab        # ../../main.md
status: active           # draft | active | completed | archived
version: 0.1.0
owner: TanaT-Lab
created: 2026-10-26
updated: 2026-10-26
tags: [core, library, python]
---

# TanaT - sub-repo spec

> Spec of the **TanaT core library**. The rules that govern its code are in
> `constitution.md`; this file only places it in the ecosystem.

## Purpose / role in the ecosystem

Core library for trajectory analysis (Temporal Analysis of Trajectories):
an extensible Python library for temporal sequence analysis, with a primary
focus on patient care pathways. Published on PyPI as `tanat`.

## Goal

Provide well-established temporal analysis features (sequences, trajectories,
criteria, T0 alignment, metrics, clustering, visualization) with a clear,
flexible and explicit code syntax.

## Scope

- **In scope:** data model (Entity, Sequence, Trajectory, Pool), store layer,
  criteria, zeroing, metrics, clustering, visualization, dataset access,
  user documentation and tutorials.
- **Out of scope:** generic utilities (`tanat-utils`), embeddings
  (`tanat-embs`), synthetic data generation (`tanat-synthea`), public demos
  (`tanat-demo`).

## Interfaces with other sub-repos

- **Depends on** `tanat-utils` (`tanat-utils>=0.1.0`): mixins such as
  `Cachable`, `CachableSettings`, `Registrable` (see `constitution.md`).
- **Consumed by** `tanat-demo` through the PyPI release (pinned version).
  Breaking API changes must be reflected in the demo.

## Code location

`TanaT-Lab/TanaT` (local sibling: `../TanaT`).

## Specs in this folder

- `constitution.md` - mandatory rules: data model, store architecture, style, workflow
- `review.md` - code review specification
- `testing.md` - test strategy (pytest + syrupy)
- `feature-template.md` + `features/` - feature specs (`features/<name>/spec.md`, `tasks.md`)
- `minify_specs.py` - builds `features/<name>/context.min.md` (run from this folder)
- `tasks/README.md` - task board (lab-wide `TASK-*.md` workflow)

> Two task workflows coexist for now: the historical `features/` workflow and
> the lab-wide `tasks/TASK-*.md` workflow. To be reconciled.
