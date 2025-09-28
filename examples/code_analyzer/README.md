# Example: Codebase Analysis with AILang (yt-dlp)

This example demonstrates how to use **AILang** scripts to analyze a real-world open-source codebase at two levels—first a broad architectural sweep, then a deep dive on the most critical subsystems—and finally synthesize a single, actionable report.

> **Target repository analyzed:** [`yt-dlp/yt-dlp`](https://github.com/yt-dlp/yt-dlp)
> A high-throughput, modular CLI video downloader with hundreds of site extractors, FFmpeg-based post-processing, and a stable plugin/embedding surface.
> We chose it because it’s mature, widely used, and architected around clear adapter boundaries (core engine + extractors + post-processors).

---

## What this example shows

1. **Two-phase analysis workflow**

   * **Phase A (Overview):** Reconstruct the original architectural intent, high-level layering, and confluence of later additions.
   * **Phase B (Specifics):** Inspect the core seams (core engine, extractor/downloader/postprocessor bases, utils, networking/policy, plugin surface) and produce concrete refactor opportunities.

2. **Synthesis step**

   * Combine the phase outputs into a **comprehensive refactor & confluence report**, plus **PR-sized work items** (with gates), draft modules, and CI/test artifacts that a maintainer could act on immediately.

---

## Files in this example

```
/examples/code-analysis-yt-dlp/
├─ code_overview_analyzer.ail          # Phase A: intent-aware, high-level scan
├─ code_specifics_analyzer.ail         # Phase B: specifics & refactor targets
├─ README.md                           # (this file)
└─ files/
   ├─ workplan.md                      # Multi-PR plan (tasks, gates, owners)
   ├─ network_policy_draft.py          # Draft module centralizing networking policy
   ├─ extractor_cookiecutter.md        # Template + rules for new extractors
   ├─ mypy_core_strict.ini             # Strict typing gate for core paths
   ├─ test_matrix.md                   # Matrix for formats/network/PP/errors
   ├─ migration_utils_split.md         # Phased plan to split big utils module
   ├─ error_map.csv                    # Normalized error taxonomy for telemetry
   └─ ci_additions.md                  # CI jobs to enforce the new guardrails
```
## How we ran it (step-by-step)

### 1) Phase A — Run the overview script

Script: `code_overview_analyzer.ail`

**Goal:** Rebuild the project’s architectural model from public signals (entry points, layering, plugin posture, release channels) and assess whether later features “fit” the original spine.

**Result:** The resulting report contained:
* Reconstructed layers (CLI/config → Core → Extractors → Downloaders/Network → Post-processors → Plugins)
* Alignment/confluence score and rationale
* Early recommendations and risk hints (e.g., utils gravity, extractor drift)

### 2) Phase B — Run the specifics script

Script: `code_specifics_analyzer.ail`

**Goal:** Inspect critical seams and produce concrete refactor opportunities with crisp scope and value.

**Focus areas:**

* `YoutubeDL` core orchestration
* `extractor/common.py`, `downloader/common.py`, `postprocessor/common.py`
* `utils` cohesion risks
* Networking (proxy/UA/transport/impersonation)
* IE/PP plugin surface and embedding posture

**Result:** The resulting report included:
* Contracts & typedness status
* Parameterization checks (network, format selection, post-processing)
* Hotspots & tangles
* Test surfaces and rollout safety notes
* Ranked recommendations

### 3) Synthesis — Combine A + B into a report & artifacts

After running both scripts, we asked the AI to merge the outputs into:

* A **comprehensive, top-down report** (high-level to low-level) summarizing strengths, risks, and next steps.
* A **PR-ready workplan**: `./files/workplan.md`
* Implementation helpers:

  * **Draft module**: `./files/network_policy_draft.py`
  * **Extractor template**: `./files/extractor_cookiecutter.md`
  * **Mypy config**: `./files/mypy_core_strict.ini`
  * **Test matrix**: `./files/test_matrix.md`
  * **Migration plan**: `./files/migration_utils_split.md`
  * **Error taxonomy**: `./files/error_map.csv`
  * **CI jobs**: `./files/ci_additions.md`

> The sequence above mirrors a realistic analyst-to-maintainer handoff: first understand the system, then pinpoint change-sets, then hand over a set of ready-to-adopt artifacts and checks.

---

## Why this is powerful

* **Intent-aware**: The overview pass respects the project’s original design and measures later changes against it.
* **Action-first**: The specifics pass goes straight to refactorable seams with ready-to-use artifacts.
* **Repeatable**: Works as a pattern you can reuse on any sufficiently modular repo.
* **Dev-friendly**: Produces PR-sized tasks, not vague advice.

---

**Questions or improvements?**
Open an issue in this example’s folder with your runner’s logs, the target repo, and which artifacts you want to generate automatically (e.g., only the workplan vs. the full pack).
