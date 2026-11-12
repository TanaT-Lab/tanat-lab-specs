# Tasks

Index and global status of this sub-repo's tasks. Each task is one file:
`TASK-<NNN>-<slug>.md` (template: `../../_example_subrepo/tasks/TASK-000-template.md`),
kept locally and **not versioned**; durable findings go in `../main.md`.

## Status legend

- **open**: defined, not started
- **in_progress**: being executed
- **done**: completed and contract satisfied
- **needs_review**: done, awaiting human/orchestrator review
- **rejected**: closed without completion (reason in the task)

## Board

| Task | Title | Status | Depends on |
|------|-------|--------|------------|
| TASK-001 | Generic block runner (`pipeline.py` -> `outputs.json`) | done (main @ 0cb8d41) | - |
| TASK-002 | Remove dead code from the player and front | done (main @ fc7e21f) | - |
| TASK-003 | POC local TTS with Kokoro on the intro narration | done (voice: af_heart) | - |
| TASK-004 | Fresh GitHub repo `TanaT-Lab/tanat-demo` | done | - |
| TASK-005 | MIMIC `pipeline.py` on TanaT 0.10.4, `tanat==0.10.4` pinned | done (main @ c3dda62) | 001 |
| TASK-006 | Fix the two navigation bugs in `player.js` | done (main @ cb3938c) | 002 |
| TASK-007 | `tools/tts.py`: sections -> mp3, hash cache, durations, 4m45 budget check | done (main @ 7ac0771) | 003 |
| TASK-008 | Player reads `outputs.json`; `config.js` keeps staging only | done (main @ e74fad8) | 005, 006 |
| TASK-009 | GitHub Actions + Pages, CI on PRs | done (main @ b4691b2, site live) | 004, 005 |
| TASK-010 | Rewrite `SCRIPT.md` in sections, 4m20 target, new API (incl. step 1 text) (orchestrator + human) | done (main @ e8a4ba9) | 005 |
| TASK-011 | Generate audio + automatic intro note timings | done (main @ d6f3c79, sonnet) | 007, 010 |
| TASK-012 | Demo manifest `demos/index.json` read by the landing | done (main @ 62ac3ad) | 008 |
| TASK-013 | Split `player.js` into ES modules + explicit state machine | open | 008, 012 |
| TASK-014 | Links GitLab -> GitHub, README update, CSV provenance/licence | done (main @ 34e2ba9) | 009 |
| (option) | Split `styles.css` | open | 013 |
| TASK-015 | Frame the current step and its newest output on any screen size | done (PR #1, main @ 93ed0c1) | - |
| TASK-016 | Step 4: calendar-time timeline before `set_t0` (pipeline + staging, stacked) | done (PR #2, main @ fe5556a) | 015 |
| TASK-017 | Narration: MIMIC explained for non-specialists + step 4 before/after (orchestrator + human) | done (text validated, applied by 018) | - |
| TASK-018 | Regenerate audio, MIMIC intro note, total under 4 min 30, screenshot review | done (PR #3) | 016, 017 |
| TASK-019 | Step 4 before/after side by side (`columns` in staging, stacked on narrow screens) | done (PR #4, main @ 1f8847a) | 016 |
| TASK-020 | Start button shown only when audio + figures are loaded (no fixed timer) | done (PR #5 merged) | - |
| TASK-021 | Player controls in the header + audio progress bar + keyboard shortcuts | done (PR #6 merged) | 020 |
| TASK-022 | Reading-line framing: typed line at a fixed height, no competing scrolls | in_progress (Claude Sonnet after 2 opencode crashes, stacked on 021) | 021 |
| TASK-024 | Spike: SWoTTeD tutorial as a second demo (data, draft pipeline, report) | done (Sonnet; branch task/024-swotted-spike @ ae243ba, not pushed; go with changes; human chose MIMIC as illustration) | - |
| TASK-025 | swotted-patterns: final pipeline (6-step bridge story), card, deps + CI | in_progress (Sonnet, from the spike branch) | 024 |
| TASK-026 | swotted-patterns: `SCRIPT.md` narration (orchestrator + human) | in_progress (draft 509 words, awaiting human) | 025 |
| TASK-027 | swotted-patterns: `config.js` staging, audio, screenshot review, PR | open | 025, 026 |
| TASK-023 | Final screen: notebook (left) + clickable workflow SVG, key messages, CTA (right) | done (PR #7 merged) | 021 |

Waves: 1 = 001-004 / 2 = 005-007 / 3 = 008-009 / 4 = 010-011 / 5 = 012-014 /
6 = 015-018 (2026-11 talk feedback: explain MIMIC, before/after alignment, framing).
7 = 020-023 (2026-11-12 UX pass: start when ready, controls off the content,
reading-line framing, readable final screen); sequential, all touch `core/player.js`.
8 = 024- (2026-11-12: second demo on Deep Learning, from the TanaT SWoTTeD
tutorial; spike first, demo tasks written from its report).
Task specs are written when their wave starts, so their contracts include the
actual outputs of the previous tasks. Waves 1-3 are done; the site is live at
https://tanat-lab.github.io/tanat-demo/ (deployed by CI from `main`).

## Transient exchange

Intermediate exchange between orchestrator and coders goes in
`tasks/.exchange/` (git-ignored). Only this `README.md` is versioned.
