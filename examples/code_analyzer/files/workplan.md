# yt-dlp Refactor Workplan (Specifics)
Generated: 2025-09-28 08:39 UTC

This plan slices the recommended changes into tractable PRs with clear owners, entry/exit criteria, and test gates.

## Legend
- **Area**: Subsystem touched
- **Type**: refactor / feature / infra
- **Risk**: low / medium / high
- **Gate**: tests and checks required before merge

---
## PR-1 — Decompose utils into cohesive modules
**Area:** utils → utils.io, utils.net, utils.path, utils.str, utils.time, utils.compat  
**Type:** refactor | **Risk:** medium

**Rationale:** Reduce centrality/import cycles; increase cohesion.

**Tasks**
- Identify call graph to determine clusters (io/net/str/time/path/compat).
- Create new modules; move functions with minimal churn; keep import shims in `utils.py` (deprecation warnings).
- Add `from yt_dlp.utils import X` compatibility layer (release N deprecates; N+2 removes).

**Gate**
- Unit tests updated/added for each module.
- No circular imports (scripted check).
- Bench smoke vs master within ±2%.

**Owner:** Core maintainers
**ETA (dev-days):** 3–5
**Exit Criteria:** Deprecated imports logged; docs updated.
---
## PR-2 — NetworkPolicy hub
**Area:** networking  
**Type:** refactor | **Risk:** medium

**API Sketch**
```python
class NetworkPolicy:
    def resolve_proxy(self, url, opts) -> str | None: ...
    def user_agent(self, site_hint: str|None) -> str: ...
    def should_impersonate(self, site_hint: str|None) -> bool: ...
    def transport(self, opts) -> Literal["requests","curl_cffi","websockets"]:
        ...
```
**Tasks**
- Centralize scheme validation, proxy selection, TLS/JA3/curl_cffi impersonation toggles.
- Replace per-extractor hacks; provide helpers callable from IE base.

**Gate**
- Matrix tests: requests vs curl_cffi vs websockets.
- Proxy/no-proxy; invalid-scheme; IPv6; TOR (if supported).

**Owner:** Net subteam
**ETA:** 4–6
---
## PR-3 — FFmpeg invariants preflight
**Area:** postprocessor  
**Type:** quality | **Risk:** low

**Checks**
- container compatibility for `--remux-video`
- concat stream compatibility (codec/profile/level)
- existence/exec of ffmpeg/ffprobe (prefer yt-dlp patched builds)

**Gate**
- Golden tests with failing fixtures converted to clean errors and guidance.

**ETA:** 2
---
## PR-4 — Typed core + py.typed
**Area:** core+utils  
**Type:** infra | **Risk:** low

**Tasks**
- Add typing to `YoutubeDL`, base classes, NetworkPolicy.
- Include `py.typed` and mypy config with strict mode for core paths.

**Gate**
- CI runs mypy; zero errors on core paths.

**ETA:** 2–3
---
## PR-5 — Extractor cookiecutter + lint kit
**Area:** extractors  
**Type:** DX | **Risk:** low

**Tasks**
- Cookiecutter template: files, tests, style, `REAL_EXTRACT` guidance.
- Flake8/ruff rules and shared helpers for pagination, m3u8/mpd, auth.

**Gate**
- Create one new IE with kit; pass CI; doc page published.

**ETA:** 2
---
## PR-6 — Unified Error Map
**Area:** errors/telemetry  
**Type:** infra | **Risk:** low

**Result**
- Map: ExtractorError, DownloadError/NetworkError, PostProcessingError, UnavailableVideoError → common categories + retry hints.

**Gate**
- Structured logging fields present; docs for issue templates updated.

**ETA:** 1–2
