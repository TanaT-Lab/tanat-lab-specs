# TanaT Lab specs

Specifications of the **TanaT Lab** ecosystem ([github.com/TanaT-Lab](https://github.com/TanaT-Lab)).
One specs repo drives all the lab's sub-repos. Structure from
[`specs-template`](https://gitlab.inria.fr/dev-studio/specs-template).

Specs live **outside the code repositories** and hold only the *what* and *why*
(model-agnostic). Agent roles and tooling live in `agents-kit`.

## Layout

| Path | Purpose |
|------|---------|
| `main.md` | **Global** spec: the lab, its goal, and the table of sub-repos. |
| `architecture.md` | How the sub-repos depend on each other + lab-wide decisions (ADR). |
| `conventions.md` | Lab-wide naming, git process, definitions. |
| `subrepos/<name>/main.md` | Spec of one sub-repo. |
| `subrepos/<name>/tasks/` | Task board (`README.md`) + `TASK-*.md` of one sub-repo. |
| `subrepos/_example_subrepo/` | Template for a new sub-repo and for a task (`TASK-000-template.md`). |

Sub-repos: `tanat`, `tanat-utils`, `tanat-embs`, `tanat-synthea`, `tanat-demo`.

## Expected local layout

```
TanaT-Lab/
├── specs/            # this repo
├── TanaT/            # code of subrepos/tanat
├── tanat-demo/       # code of subrepos/tanat-demo
└── ...               # other sub-repos, cloned as siblings
```

## Workflow

1. **New sub-repo**: copy `subrepos/_example_subrepo/` to `subrepos/<name>/`,
   fill in `main.md`, add a row in the global `main.md`.
2. **Task creation**: the orchestrator writes one `TASK-<NNN>-<slug>.md` in the
   sub-repo it targets, with explicit `input_contract` and `output_contract`.
   Task files are working files on the orchestrator's machine: not versioned.
3. **Execution**: an atomic coder works in a git worktree of the target code
   repo, fills in the result and flips `status`. Transient files go in
   `tasks/.exchange/` (git-ignored).
4. **Tracking**: each `tasks/README.md` summarizes status. Anything a task
   taught that must outlive it (decision, API finding, open point) is moved
   into the sub-repo's `main.md`; the commits of the code repo are the trace.

## Versioning

- **Versioned**: `main.md`, `architecture.md`, `conventions.md`,
  `subrepos/*/main.md`, `subrepos/*/tasks/README.md` (board), the task template,
  and sub-repo specific rules (e.g. `subrepos/tanat/constitution.md`).
- **Ignored** (`.gitignore`): `TASK-*.md` (except the template), `.exchange/`,
  `logs/`, transient agent state.
