# Migration Plan — utils split

## Phase 0 — Inventory
- Generate import graph; cluster functions by concern.
- Design new module boundaries.

## Phase 1 — Introduce modules
- Create `yt_dlp/utils/` package with submodules.
- Move functions; keep `utils.py` re-export shims + deprecation warnings.

## Phase 2 — Internal adoption
- Update intra-repo imports to new modules.
- CI: run cycle-checker; mypy on core; full tests.

## Phase 3 — Public deprecation
- Document deprecations in README/CHANGELOG.
- N+2 release removes shims.

Rollback: keep a branch that preserves pre-split layout; revert by re-export mapping.
