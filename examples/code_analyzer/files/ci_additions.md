# CI additions
- Add mypy job using mypy_core_strict.ini for core paths.
- Add cycle-check job (e.g., `pip install pycycle` or custom).
- Add matrix job running NetPolicy tests for transports/proxies.
- Emit structured logs for error_map categories for flaky test triage.
