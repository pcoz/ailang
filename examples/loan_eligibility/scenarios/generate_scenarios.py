"""Generate runnable scenario .ailang files from the canonical program.

Reads the canonical ``loan_eligibility.ailang``, swaps in each applicant
dict from ``APPLICANTS`` below, writes one complete .ailang file per
scenario into this directory.

Usage::

    python generate_scenarios.py

Re-run any time the canonical program changes; the generated files are
overwritten.
"""

from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).parent
CANONICAL = HERE.parent / "loan_eligibility.ailang"

# Each scenario is named and described.  The ``applicant`` dict is what
# gets substituted into the canonical program's ``SET applicant TO {...}``
# block.  Everything else in the program stays identical so the only
# thing varying between runs is the input data -- exactly what we want
# to demonstrate reproducibility / qualitative idempotency.
APPLICANTS: dict[str, dict] = {
    "scenario_01_clear_approve": {
        # Strong applicant: high credit, low debt, stable employment,
        # established homeowner.  Should produce APPROVE with high
        # confidence and no special conditions.
        "name": "Asha Bhattacharya",
        "age": 42,
        "credit_score": 785,
        "annual_income_usd": 110000,
        "monthly_debt_obligations_usd": 950,
        "employment_status": "full_time",
        "employment_tenure_months": 96,
        "industry": "healthcare",
        "residence_status": "owns_home",
        "requested_loan_amount_usd": 18000,
        "requested_term_months": 48,
        "bankruptcies_last_7_years": 0,
        "fraud_flags": [],
        "months_with_lender": 60,
        "recent_credit_inquiries_6mo": 1,
    },
    "scenario_02_clear_decline": {
        # Weak applicant: low credit, recent bankruptcy = hard
        # disqualifier, high debt load.  Should produce DECLINE with
        # high confidence, citing the bankruptcy as primary cause.
        "name": "Marcus Reilly",
        "age": 29,
        "credit_score": 590,
        "annual_income_usd": 38000,
        "monthly_debt_obligations_usd": 1100,
        "employment_status": "part_time",
        "employment_tenure_months": 5,
        "industry": "retail",
        "residence_status": "rents",
        "requested_loan_amount_usd": 12000,
        "requested_term_months": 60,
        "bankruptcies_last_7_years": 1,
        "fraud_flags": [],
        "months_with_lender": 4,
        "recent_credit_inquiries_6mo": 8,
    },
    "scenario_03_marginal_conditional": {
        # Borderline DTI, otherwise solid.  Hard rules likely produce
        # marginal; soft factors are positive (long tenure, owned home,
        # established lender relationship).  Expected: APPROVE_WITH_
        # CONDITIONS (e.g. shorter term to reduce monthly payment).
        "name": "Priya Sundaram",
        "age": 37,
        "credit_score": 695,
        "annual_income_usd": 64000,
        "monthly_debt_obligations_usd": 1850,
        "employment_status": "full_time",
        "employment_tenure_months": 48,
        "industry": "education",
        "residence_status": "owns_home",
        "requested_loan_amount_usd": 22000,
        "requested_term_months": 60,
        "bankruptcies_last_7_years": 0,
        "fraud_flags": [],
        "months_with_lender": 36,
        "recent_credit_inquiries_6mo": 2,
    },
    "scenario_04_marginal_decline": {
        # Decent score (above min) but multiple soft signals are
        # negative: very recent job, volatile industry exposure (gig
        # economy), 7 inquiries in 6 months suggests credit-shopping
        # distress.  Expected: DECLINE or REFER_TO_UNDERWRITER even
        # though hard rules might pass.
        "name": "Diego Ferreira",
        "age": 31,
        "credit_score": 685,
        "annual_income_usd": 72000,
        "monthly_debt_obligations_usd": 1200,
        "employment_status": "full_time",
        "employment_tenure_months": 3,
        "industry": "rideshare_gig",
        "residence_status": "rents",
        "requested_loan_amount_usd": 15000,
        "requested_term_months": 36,
        "bankruptcies_last_7_years": 0,
        "fraud_flags": [],
        "months_with_lender": 2,
        "recent_credit_inquiries_6mo": 7,
    },
    "scenario_05_judgment_call": {
        # Right at every threshold.  Hard rules will say "marginal".
        # Soft factors are mixed (stable industry, but new to lender,
        # moderate inquiries).  Expected: REFER_TO_UNDERWRITER --
        # this is exactly the kind of edge case where a defensible
        # automated system should escalate rather than guess.
        "name": "Eleanor Whitfield",
        "age": 56,
        "credit_score": 660,
        "annual_income_usd": 58000,
        "monthly_debt_obligations_usd": 1400,
        "employment_status": "full_time",
        "employment_tenure_months": 12,
        "industry": "manufacturing",
        "residence_status": "rents",
        "requested_loan_amount_usd": 20000,
        "requested_term_months": 72,
        "bankruptcies_last_7_years": 0,
        "fraud_flags": [],
        "months_with_lender": 6,
        "recent_credit_inquiries_6mo": 3,
    },
}

# Matches the canonical program's ``SET applicant TO { ... }`` block,
# spanning newlines.  The non-greedy `.*?` plus the closing `\n}` keeps
# it from eating subsequent SET blocks.
APPLICANT_BLOCK_RE = re.compile(
    r"SET applicant TO \{.*?\n\}",
    re.DOTALL,
)


def applicant_to_ailang(applicant: dict) -> str:
    """Render an applicant dict as an AILang object literal.

    AILang's object literal syntax overlaps with JSON-ish notation: keys
    are bare identifiers (no quotes), strings are double-quoted, lists
    use square brackets.  We use that subset directly rather than going
    through ``json.dumps`` because JSON would quote the keys.
    """
    lines = ["SET applicant TO {"]
    keys = list(applicant.keys())
    for i, key in enumerate(keys):
        value = applicant[key]
        if isinstance(value, str):
            rendered = f'"{value}"'
        elif isinstance(value, list):
            # Only str-list values appear in our schema (e.g. fraud_flags).
            elems = ", ".join(f'"{x}"' for x in value)
            rendered = f"[{elems}]"
        else:
            rendered = str(value)
        comma = "," if i < len(keys) - 1 else ""
        lines.append(f"    {key}: {rendered}{comma}")
    lines.append("}")
    return "\n".join(lines)


def main() -> None:
    canonical_text = CANONICAL.read_text(encoding="utf-8")
    if not APPLICANT_BLOCK_RE.search(canonical_text):
        raise RuntimeError(
            "Could not find the SET applicant block in the canonical program. "
            "Has the structure of loan_eligibility.ailang changed?"
        )
    for name, applicant in APPLICANTS.items():
        new_block = applicant_to_ailang(applicant)
        # Inject a header comment so each generated file is self-describing
        # at a glance -- the scenario name, applicant headline data.
        header = (
            f"# ============================================================\n"
            f"# Generated scenario: {name}\n"
            f"# Applicant: {applicant['name']}, "
            f"credit={applicant['credit_score']}, "
            f"income=${applicant['annual_income_usd']:,}/yr, "
            f"requesting ${applicant['requested_loan_amount_usd']:,} "
            f"over {applicant['requested_term_months']}mo\n"
            f"# Generated by scenarios/generate_scenarios.py -- do not edit\n"
            f"# ============================================================\n"
        )
        new_text = APPLICANT_BLOCK_RE.sub(new_block, canonical_text, count=1)
        # Place the generation header right after the AILang version line.
        new_text = new_text.replace(
            "#ailang v0.8.2\n",
            f"#ailang v0.8.2\n{header}",
            1,
        )
        out = HERE / f"{name}.ailang"
        out.write_text(new_text, encoding="utf-8")
        print(f"wrote {out.relative_to(HERE.parent)}")


if __name__ == "__main__":
    main()
