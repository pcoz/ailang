# yt-dlp Refactor & Architecture Confluence Report

## 0) Executive summary (high-level feedback)

**Overall verdict:** The project’s original “engine + adapters” architecture is solid and has aged well. The most significant evolutions—pluginization, multi-channel releases, and browser/transport impersonation—enhance the core model rather than fight it. The main risks now are *entropy* (a large adapter surface with stylistic drift) and *gravity* (an ever-growing `utils` that can become a tangled hub). Both are tractable with a handful of targeted refactors and guardrails.

**What to do next (big rocks):**

1. **Split `utils` by concern** (io, net, path, str, time, compat) with a measured deprecation plan.
2. **Centralize network behavior** behind a **NetworkPolicy** module; stop leaking per-extractor hacks.
3. **Preflight FFmpeg invariants** to reduce post-processing failures and improve UX.
4. **Strengthen typing** on core seams and ship `py.typed` with CI checks.
5. **Standardize new extractors** with a cookiecutter and lint rules to curb divergence.
6. **Unify error taxonomy** for clearer retries, telemetry, and issue triage.

**Impact:** Less coupling, fewer flake points, more predictable networking, cleaner post-proc failure modes, faster extractor development, and safer rollouts (you already have nightly/master/stable).

---

## 1) Original intent & current shape (context)

**Intent:** A modular CLI downloader with:

* A **core orchestrator** (`YoutubeDL`) that drives extraction → selection → download → post-proc.
* A **large, fast-moving adapter surface** (site-specific **extractors**).
* **Downloaders/network adapters** (requests, websockets, curl-impersonation).
* **Post-processors** wrapped around FFmpeg and metadata steps.
* A **plugin posture** (IE/PP) plus an **embedding API** so the core can be reused.
* **Multi-channel releases** (nightly/master/stable) to update extractors quickly without destabilizing the core.

**Assessment:** Later features (plugins, impersonation, release channels) are congruent with the original model. Alignment score (from the overview scan): **0.86**.

---

## 2) Strengths & risks (program-level)

### Strengths

* **Extensible spine:** Clear IE/PP contracts; embedding via params; proven FFmpeg integration.
* **Operational maturity:** Multi-channel release strategy already decouples velocity from stability.
* **Community surface:** The adapter model scales contributor input without hard-forking the core.

### Risks

* **`utils` gravity:** Too many helpers in one place invite import cycles and opaque coupling.
* **Policy leakage:** Network choices (proxies, impersonation, UA) sometimes drift close to extractors.
* **PP edge cases:** Stream-copy/concat/remux failures frustrate users and look like extractor bugs.
* **Extractor drift:** Many small modules can diverge in style and quality without a standard kit.

---

## 3) Recommendations (target state)

1. **Decompose `utils`** into cohesive modules: `utils.io`, `utils.net`, `utils.path`, `utils.str`, `utils.time`, `utils.compat`. Keep `utils.py` as a re-export shim with deprecation warnings; remove in N+2.
2. **NetworkPolicy hub**: one module decides proxy normalization, UA selection, transport (`requests`/`curl_cffi`/`websockets`), and impersonation on/off per site. Extractors consult it; they do not hand-roll network behavior.
3. **FFmpeg invariants preflight**: verify container & codec compatibility for concat/remux, and check tool availability. Fail fast with clear guidance (point to curated builds where relevant).
4. **Typed core & `py.typed`**: add type hints to `YoutubeDL`, IE/PP base classes, NetworkPolicy, and key helpers. Enforce with `mypy` for core paths in CI.
5. **Extractor cookiecutter + lint kit**: provide a template and shared helpers (pagination, m3u8/mpd parsing, auth, JSON handling). Reinforce with ruff/flake8 rules.
6. **Unified error map**: normalize error families (Extractor vs Network vs Post-Proc vs Expected/Unavailable) into structured categories with retry hints and telemetry tags.

---

## 4) Workplan (PR-sized, owner-friendly)

A full PR roadmap is prepared for you:

* **PR-1 — Decompose utils** (risk: medium): phased split + re-export shims + deprecation plan; cycle checks; perf smoke must remain within ±2%.
* **PR-2 — NetworkPolicy hub** (risk: medium): introduce new API; route proxy/scheme/UA/transport/impersonation decisions through it; add a transport/proxy test matrix.
* **PR-3 — FFmpeg preflight** (risk: low): add invariant checks; improve errors and guidance; golden tests with known failing fixtures.
* **PR-4 — Typed core + `py.typed`** (risk: low): strict mypy for core paths; zero errors gate in CI.
* **PR-5 — Extractor cookiecutter + lint kit** (risk: low): standard template + tests; shared helpers; documentation page.
* **PR-6 — Unified Error Map** (risk: low): structured codes, retryability flags, and logging fields; align issue templates with categories.

👉 Download the detailed PR breakdown (tasks, gates, owners, exit criteria):
**[workplan.md](sandbox:/mnt/data/workplan.md)**

---

## 5) Detailed findings by subsystem (low-to-mid level)

### 5.1 Core orchestration (`YoutubeDL`)

* **Observations**

  * High fan-in/out: options plumbing, progress/logging, request direction, and overall flow control.
  * Embedding contract and params object are the primary extension seam.
* **Actions**

  * Add types to public methods and key data structures (formats, infos).
  * Ensure calls to network stack go through NetworkPolicy (not ad-hoc).
  * Emit structured error categories for uniform telemetry.

### 5.2 Extractors (IE base & modules)

* **Observations**

  * Base class does heavy lifting; modules can drift stylistically.
  * Network details occasionally bleed into IEs (e.g., UA/proxy tweaks).
* **Actions**

  * Provide **cookiecutter** and shared helpers for common patterns.
  * Enforce “no ad-hoc UA/proxy”—must call NetworkPolicy.
  * Add type hints to base IE methods and common return dicts.

Template & rules: **[extractor_cookiecutter.md](sandbox:/mnt/data/extractor_cookiecutter.md)**

### 5.3 Downloaders / Networking

* **Observations**

  * Multiple transports (`requests`, `curl_cffi`, websockets) with evolving impersonation needs.
  * Proxy strings without explicit schemes can be ambiguous; policy lives too low.
* **Actions**

  * Introduce **NetworkPolicy** and move scheme validation & proxy normalization into it.
  * Add a table-driven transport decision (feature flags, site hints).
  * Test matrix across transports, proxies (http/https/socks), IPv4/IPv6, and failure modes.

Starter module: **[network_policy_draft.py](sandbox:/mnt/data/network_policy_draft.py)**
Test matrix: **[test_matrix.md](sandbox:/mnt/data/test_matrix.md)**

### 5.4 Post-processors (FFmpeg, metadata)

* **Observations**

  * PP errors (concat/remux) are common and confusing; curated builds exist for known issues.
* **Actions**

  * Add **preflight invariants**: container/codec/profile/level compatibility; detect stream-copy hazards; explicit “upgrade/build” guidance if needed.
  * Golden tests: representative remux/concat subtasks.

### 5.5 Shared helpers (`utils`)

* **Observations**

  * High centrality, broad surface, rising cycle risk.
* **Actions**

  * Execute the **utils split** with re-exports and a deprecation window.
  * Introduce ownership per submodule and small READMEs to keep cohesion.

Migration plan: **[migration_utils_split.md](sandbox:/mnt/data/migration_utils_split.md)**

---

## 6) Error taxonomy & telemetry (implementation-level)

Standardize into structured categories with retry hints:

| Code | Name                  | Retryable | Category  | Notes                                     |
| ---- | --------------------- | --------- | --------- | ----------------------------------------- |
| E100 | ExtractorError        | false     | extractor | Site structure change/unsupported         |
| E200 | NetworkError          | true      | network   | Use backoff; consider transport switch    |
| E210 | HTTP403               | true      | network   | Try impersonation/proxy via NetworkPolicy |
| E300 | PostProcessingError   | false     | postproc  | FFmpeg failure; check invariants          |
| E400 | UnavailableVideoError | false     | expected  | Geo/DRM/unpublished                       |

CSV for CI/log parsers: **[error_map.csv](sandbox:/mnt/data/error_map.csv)**

---

## 7) Testing & CI (gates you can copy-paste)

* **Mypy gate** for core paths (strict), ship `py.typed`.
* **Cycle check** (prevents utils regressions).
* **NetworkPolicy matrix**: transports × proxies × headers × IP families.
* **PP golden tests** for remux/concat invariants.

Configs/snippets:

* **[mypy_core_strict.ini](sandbox:/mnt/data/mypy_core_strict.ini)**
* **[test_matrix.md](sandbox:/mnt/data/test_matrix.md)**
* **[ci_additions.md](sandbox:/mnt/data/ci_additions.md)**

---

## 8) Rollout & risk management (operational)

* **Use your channels**: land structural changes in `master`/`nightly` with strong CI and telemetry; promote to `stable` once green.
* **Deprecation schedule**: `utils` re-exports for N and N+1; removal in N+2; changelog + warnings in place.
* **Rollback**: keep a branch that preserves pre-split `utils.py`; reverting becomes a single mapping change.

---

## 9) Artifacts index (everything in one place)

* Findings JSON (specific scan): **[refactor_specific_findings.json](sandbox:/mnt/data/refactor_specific_findings.json)**
* High-level overview JSON: **[refactor_overview.json](sandbox:/mnt/data/refactor_overview.json)**
* Workplan: **[workplan.md](sandbox:/mnt/data/workplan.md)**
* NetworkPolicy draft: **[network_policy_draft.py](sandbox:/mnt/data/network_policy_draft.py)**
* Extractor template & rules: **[extractor_cookiecutter.md](sandbox:/mnt/data/extractor_cookiecutter.md)**
* Mypy config: **[mypy_core_strict.ini](sandbox:/mnt/data/mypy_core_strict.ini)**
* Test matrix: **[test_matrix.md](sandbox:/mnt/data/test_matrix.md)**
* Utils split migration plan: **[migration_utils_split.md](sandbox:/mnt/data/migration_utils_split.md)**
* Error map CSV: **[error_map.csv](sandbox:/mnt/data/error_map.csv)**
* CI additions: **[ci_additions.md](sandbox:/mnt/data/ci_additions.md)**

---

## 10) Appendix A — NetworkPolicy API sketch (for clarity)

```python
class NetworkPolicy:
    def resolve_proxy(self, url, opts) -> str | None: ...
    def user_agent(self, site_hint: str | None) -> str: ...
    def should_impersonate(self, site_hint: str | None) -> bool: ...
    def transport(self, opts) -> Literal["requests", "curl_cffi", "websockets"]: ...
```

**Notes:**

* Enforce explicit schemes in proxies (no silent `http://` defaulting).
* Site-hint gates impersonation; global flag as fallback.
* Extractors pass only hints and headers; *no direct transport choices*.

---

## 11) Appendix B — Utils split migration (phases)

* **Phase 0 — Inventory**: generate import graph; cluster by concern.
* **Phase 1 — Introduce modules**: move functions; re-export in `utils.py`; start deprecation warnings.
* **Phase 2 — Internal adoption**: update intra-repo imports; add cycle checker; keep perf steady.
* **Phase 3 — Public deprecation**: document in README/CHANGELOG; remove in N+2.

---

### Closing note

You don’t need a big-bang. Ship the **NetworkPolicy** and **FFmpeg preflight** first (fast wins and visible stability), then do the **utils** split under a deprecation umbrella, while **typing**, **error taxonomy**, and the **extractor kit** raise the reliability floor across the codebase.
