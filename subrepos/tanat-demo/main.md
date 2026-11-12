---
subrepo: tanat-demo
parent: TanaT Lab        # ../../main.md
status: active           # draft | active | completed | archived
version: 1.0.0
owner: TanaT-Lab
created: 2026-10-26
updated: 2026-11-12
tags: [demo, showcase, conference, static-site]
---

# tanat-demo - sub-repo spec

Narrated, interactive walkthroughs of TanaT for **conference talks**: a player
types real TanaT code step by step, shows its outputs and figures, in sync with
an audio narration. Static site, one demo today, built to host more.

- **Live:** https://tanat-lab.github.io/tanat-demo/
- **Code:** [TanaT-Lab/tanat-demo](https://github.com/TanaT-Lab/tanat-demo)
  (local sibling `../tanat-demo`; history before 2026-10-26 archived at
  `gitlab.inria.fr/tanat/comms/tanat-demo`).
- **Scope:** demo content, player and landing page, output generation, CI and
  Pages. Not TanaT itself (`tanat`) nor dataset generation (`tanat-synthea`).

## Current state (2026-11-10)

One demo, **mimic-clustering** (MIMIC-IV hospital admissions), **4 min 00** of
narration (~4 min 20 wall-clock) in 6 steps: load a CSV into a pool, bar plot,
keep the 64 patients with an emergency admission, align on the first emergency
(T0) shown as a before/after (calendar time beside aligned time), cluster with
a normalized edit distance (3 clusters), one timeline per cluster. The intro
explains MIMIC-IV for non-specialists (2026-11 talk feedback, TASK-015..019).

How it works, in one line per piece:

| Piece | Role |
|---|---|
| `demos/<id>/pipeline.py` | The code shown, written once, in `# %% <id>` blocks. |
| `generate_all.py` | Runs every pipeline: `outputs/outputs.json` (code, output, figure per block) + figures, and `demos/index.json` for the landing. |
| `demos/<id>/config.js` | Staging only: intro notes, stations, audio, which blocks are shown. |
| `demos/<id>/demo.json` | Card metadata (title, subtitle, tags), read by the landing and the player. |
| `demos/<id>/SCRIPT.md` | Narration, one `## section` per audio file; `{#anchor}` marks times for the intro notes. |
| `tools/tts.py` | SCRIPT.md -> mp3 per section + `audio/manifest.json` (durations, anchors); Kokoro-82M on CPU, cached, fails above 4 min 45. |
| `data/` | Versioned CSV, rebuilt exactly by `data/build_csv.py --check`; provenance and licences in `data/README.md`. |
| `.github/workflows/pages.yml` | On PRs and `main`: regenerate outputs, run the tests (incl. headless browser), deploy Pages from `main`. |

Adding a demo = a folder with `pipeline.py`, `demo.json`, `config.js`,
`SCRIPT.md` (see the code repo README).

## Decisions and why

| Topic | Decision | Why |
|---|---|---|
| Content | Follows the TanaT MIMIC tutorials, no extra step. | One reference to maintain; audience sees the documented API. |
| Code | Written once in `pipeline.py`, really executed; the player reads `outputs.json`. | What the audience sees is what ran; no hand-copied outputs to drift. |
| Outputs | Shown as TanaT prints them; only the pipeline's own prints are tuned (3a, 5b). | Filtering TanaT's output would hide what really runs. Verbosity belongs in TanaT (issue drafted). |
| Data | CSV in `data/`, no network at run time. Source: MIMIC-IV Clinical Database Demo 2.2 (PhysioNet), ODbL v1.0, redistributed under the same licence. | Conference rooms have bad Wi-Fi; PhysioNet is the authoritative source. |
| Versions | `tanat==0.10.4`, `polars<2`. | An unpinned `pip install tanat` broke the demo silently; `polars<2` works around a TanaT bug (below). |
| Clustering | Hamming on `admission_type`, normalized edit distance, 3 clusters. | Unnormalized, clusters only sorted patients by number of stays (55/7/1/1). Now: single emergency visit (22 patients), a few stays incl. deaths (24), frequent readmissions (18). |
| Audio | Kokoro-82M, voice `af_heart`, mp3 versioned, regenerated only when the text changes. | Free, local, CPU only, reproducible from the script; replaces a manual TTS website. |
| Duration | Under 5 min; build fails above 4 min 45 of audio; target <= 4 min 30 wall-clock. | Conference slot, with margin for typing and transitions. |
| MIMIC for non-specialists | Intro says what MIMIC-IV is (real, de-identified records, Boston, widely used) and what the open demo holds; notes repeat the key facts. | Talk feedback: the audience did not know the dataset. |
| Alignment before/after | Step 4 draws the cohort in calendar time (TanaT default timeline), then `set_t0`, then the aligned timeline; the two figures side by side (`columns` staging field), `figsize(6, 4.5)` each. | MIMIC shifts dates per patient (2110-2210): calendar time looks scattered, which is exactly why alignment is needed. Default 10x5 figures were unreadable at half width. |
| Framing | One scroll owner (`scrollToY`, one rAF easing loop): step header at the top of the visible area at step start; the typed line kept on a reading line at 55% of the visible height (page only moves down within a block); each output framed fully once decoded; never center something taller than the screen; a manual scroll suspends auto-follow until the next block. Figures capped at 60vh. Columns stack below 1200 px. | Bad framing depending on screen/zoom, then code typed glued to the bottom edge (talk feedback, 2026-11-12: competing `scrollIntoView` calls). `test_player_framing.py` checks 1920x1080, 1280x720, 1024x576 in real time. |
| Controls | In the fixed header on desktop (top-right corner in the intro, icon-only sticky footer on mobile), SVG icons, 3 px narration progress bar, keys Space / arrows / PageUp-PageDown / `r`. | They used to float over the code being typed; emoji render as boxes without an emoji font; a presentation clicker sends PageUp/PageDown. |
| Start | Shown once the intro audio and every figure are loaded, after at least 0.8 s of logo, at most 8 s. | A fixed 1.5 s timer could start the intro with no sound. |
| Final screen | `core/final-view.js`: notebook of every shown block on the left; on the right a clickable workflow of the stations (`api` staging field), last figure, `outro.takeaways` (`{lines}` computed from outputs.json), `pip install tanat` + links. | The 3x2 grid of miniatures was unreadable on a projector. |
| Palette | `ADMISSION_COLORS` runs but is not shown. | Saves screen time. |
| Hosting | GitHub Actions + Pages. | Repos moved to the TanaT-Lab GitHub org. |
| Workflow | Task files not versioned (board is); one PR per task branch on GitHub, merged by the human (since 2026-11-10, TASK-015). | CI (incl. headless browser tests) runs on the PR in a clean environment; the human keeps the last word on `main`, which deploys the site. |

## Known issues

- **TanaT bug, static features on the wrong ids.** `store/base/static.py`
  `add_static()` LEFT JOINs without `maintain_order="left"` then writes by
  position: with polars 2, cluster labels land on the wrong patients (26/64
  right). Pinned `polars<2`; `tests/test_pipeline_labels.py` fails if it comes
  back. Issue drafted for `TanaT-Lab/TanaT`, not posted yet.
- **Legend order** differs between figures and between runs (TanaT orders
  legend entries non-deterministically); visible on the step 4 side by side.
  To report upstream with the verbosity issue.
- **Flaky CI on `import tanat`.** `tanat_utils.check_version` queries PyPI
  (timeout 0.5 s) at import and catches `URLError` but not `TimeoutError` on a
  slow read: test collection crashes (PR #4, 2026-11-12; rerun passed). To
  report upstream with the other TanaT issues; rerun the job meanwhile.
- **Fixed test ports** (8721-8726): two pytest runs at once (parallel coders,
  other sessions) collide with "Address already in use". The real-time
  framing test (~6 min) is load-sensitive. Whole suite ~12-19 min.
- **Stale figures**: `generate_all.py` does not remove figures of blocks that
  no longer exist in `outputs/` (local only; CI starts clean).

## Next (backlog, by priority)

1. Post the TanaT issues (static-feature join, output verbosity, legend
   order).
2. Faster player tests: free ports (port 0), fast typing in tests with checks
   at block ends, so the suite runs in a few minutes and in parallel.
3. Split `core/player.js` (~1100 lines) into ES modules with an explicit state
   machine, UX unchanged (TASK-013). Not before a talk.
4. Once TanaT is fixed: drop `polars<2`; once verbosity exists: quiet the
   progress boxes in 1b and 5b.
5. Option: split `core/styles.css`.
6. A second demo, to prove "adding a demo = a folder" (wave 8, spike
   TASK-024 running). Decided with the human (2026-11-12): the TanaT SWoTTeD
   tutorial, framed as **TanaT bridges tools**, not as "deep learning"
   (SWoTTeD is a tensor decomposition trained with PyTorch). Round trip:
   trajectories in TanaT -> `to_tensor` -> SWoTTeD patterns (figure) -> the
   dominant pattern back into TanaT as a static feature, one timeline per
   pattern. Card: title "From trajectories to tensors", subtitle "Turn care
   pathways into PyTorch-ready tensors, learn temporal patterns with SWoTTeD,
   and bring them back into TanaT."; folder `demos/swotted-patterns/`.
7. Small: tests on port 0; `generate_all.py` clears stale figures.

## Interfaces with other sub-repos

- **Depends on** `tanat` via PyPI (pinned). The pipeline follows the current
  public API; the MIMIC tutorials in `tanat` are the reference.

## Referenced specs

- `tasks/README.md` - task board (history of the 2026-10 refactor: TASK-001..014)
- `../../main.md` - global spec
