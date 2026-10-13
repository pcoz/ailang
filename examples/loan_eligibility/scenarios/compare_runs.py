"""Compare two run_report.json files on the load-bearing decision fields.

This is the check behind the README's "qualitative idempotency" claim:
surface wording is expected to differ between runs, but the structured
fields an auditor relies on should converge.  For each scenario present
in both reports it compares:

  - final_decision.decision
  - hard_eligibility.hard_outcome
  - soft_factors.soft_factor_direction
  - final_decision.confidence
  - final_decision.conditions_if_any  (free text: compared on whether
    conditions were imposed and how many; both lists are printed so a
    human can judge whether they say the same thing)

Usage::

    python compare_runs.py ../runs/<run_a>/run_report.json ../runs/<run_b>/run_report.json

Exit code 0 when every categorical field matches for every scenario,
1 when any differ (or a scenario is missing from one report).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# (label, section, key) -- section is the top-level key in each scenario
# record written by run_all.py.
CATEGORICAL_FIELDS: list[tuple[str, str, str]] = [
    ("decision", "final_decision", "decision"),
    ("hard_outcome", "hard_eligibility", "hard_outcome"),
    ("soft_factor_direction", "soft_factors", "soft_factor_direction"),
    ("confidence", "final_decision", "confidence"),
]


def _load(path: Path) -> dict[str, dict]:
    records = json.loads(path.read_text(encoding="utf-8"))
    return {r["scenario"]: r for r in records}


def _get(record: dict, section: str, key: str):
    return (record.get(section) or {}).get(key)


def _conditions(record: dict) -> list[str]:
    return list(_get(record, "final_decision", "conditions_if_any") or [])


def compare(a: dict[str, dict], b: dict[str, dict]) -> tuple[list[str], int]:
    """Return (report lines, number of mismatches)."""
    lines: list[str] = []
    mismatches = 0
    for scenario in sorted(set(a) | set(b)):
        lines.append(f"\n{scenario}")
        if scenario not in a or scenario not in b:
            lines.append(f"  MISSING from {'A' if scenario not in a else 'B'}")
            mismatches += 1
            continue
        ra, rb = a[scenario], b[scenario]
        for label, section, key in CATEGORICAL_FIELDS:
            va, vb = _get(ra, section, key), _get(rb, section, key)
            mark = "same" if va == vb else "DIFF"
            if va != vb:
                mismatches += 1
            lines.append(f"  {mark:4}  {label:22} A={va!s:26} B={vb!s}")
        ca, cb = _conditions(ra), _conditions(rb)
        same_shape = bool(ca) == bool(cb) and len(ca) == len(cb)
        if not same_shape:
            mismatches += 1
        lines.append(
            f"  {'same' if same_shape else 'DIFF':4}  {'conditions (count)':22} "
            f"A={len(ca):<26} B={len(cb)}"
        )
        for tag, conds in (("A", ca), ("B", cb)):
            for c in conds:
                lines.append(f"          {tag}: {c}")
    return lines, mismatches


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("run_a", type=Path)
    ap.add_argument("run_b", type=Path)
    args = ap.parse_args()

    lines, mismatches = compare(_load(args.run_a), _load(args.run_b))
    print(f"A: {args.run_a}\nB: {args.run_b}")
    print("\n".join(lines))
    print(
        f"\n{'CONVERGED' if mismatches == 0 else 'DIVERGED'}: "
        f"{mismatches} load-bearing field mismatch(es)"
    )
    sys.exit(0 if mismatches == 0 else 1)


if __name__ == "__main__":
    main()
