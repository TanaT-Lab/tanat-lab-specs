# Conventions

> Shared conventions so all tasks and agents stay consistent across the
> project. Edit to match the project's reality.

## Naming

- Task files: `TASK-<NNN>-<slug>.md` (zero-padded, hyphenated slug).
- Branches: `feature/<slug>`, `fix/<slug>`, `task/<NNN>-<slug>`.
- Commits: conventional style (`feat:`, `fix:`, `docs:`, `chore:`).

## Process

- One logical change per commit.
- Run linters / typecheck / tests before marking a task done.
- Never force-push or rewrite shared history.

## Sub-repo specific rules

A sub-repo may add stricter rules in its own folder; they apply on top of
these conventions. Example: `subrepos/tanat/constitution.md` (data model,
style, no em dashes, workflow) and `subrepos/tanat/review.md`.

## Definitions

| Term | Meaning |
|------|---------|
| spec | A durable, versioned description of intent (`main.md`, board). Task files are working contracts, not versioned. |
| contract | The explicit input/output of a task (see task template). |

## Model-agnostic note

These specs must stay **independent of any specific model or agent tooling**.
Model behavior and agent roles live in `agents-kit`; this repository holds only
the *what* and *why*, never the *how with a particular model*.
