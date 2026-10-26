# Architecture

> Ecosystem-level structure: how the TanaT Lab sub-repos depend on each other.
> Sub-repo internals belong in each sub-repo's spec (e.g. the store
> architecture is in `subrepos/tanat/constitution.md`).

## Overview

```
tanat-utils  <--  tanat (TanaT)  <--  tanat-demo
  mixins           core library        consumes the PyPI release
                       ?
              tanat-embs, tanat-synthea   (relations to be documented)
```

- `tanat` depends on `tanat-utils` (`tanat-utils>=0.1.0` in `pyproject.toml`).
- `tanat-demo` depends on the **published** `tanat` (PyPI, pinned version), not
  on the source tree.
- `tanat-embs` and `tanat-synthea`: dependencies not documented yet.

## Decisions

### ADR-001: One specs repo for the whole TanaT Lab

- **Status:** accepted
- **Date:** 2026-10-26
- **Context:** the specs repo was TanaT-specific while the lab now hosts
  several related repos on the TanaT-Lab GitHub organization.
- **Decision:** this repo becomes the lab-wide specs repo, structured from
  `specs-template`; TanaT-specific specs move to `subrepos/tanat/`.
- **Consequences:** each sub-repo gets `subrepos/<name>/main.md` + `tasks/`;
  rules specific to one sub-repo stay in its folder.
