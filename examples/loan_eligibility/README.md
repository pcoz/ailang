# Personal Loan Eligibility — AILang as an Executable Specification

This example demonstrates how a regulated business-rules workflow — the kind that today lives in 200,000-line Drools rule sets, hand-tuned Java decision engines, or COBOL underwriting modules — can be expressed as a single readable AILang program and run on AIEX.

The core insight: **the program is the spec**. The same text a compliance officer reads to understand the policy is what the AIEX runtime executes. There is no separate "rules document → translated into Java → translated back to a regulator-friendly summary" round trip where intent gets lost between layers.

## What gets demonstrated

- **Typed reasoning operations** for the qualitative parts (`DEDUCE`, `WEIGH`, `SYNTHESIZE`)
- **`EXECUTE_CODE` blocks** for the deterministic parts (amortisation math, audit log formatting)
- **Output contracts** (`MUST_INCLUDE`, `CANNOT_INCLUDE`, constrained `OUTPUT_FORMAT` enums) that lock the LLM to defensible decision categories
- **Multi-tier model routing** — BERT/Haiku/Sonnet/Opus selected automatically per operation, ~88% cost reduction vs all-Opus
- **Pre-execution budget reports** — every scenario costs $0.043 to run, knowable before spending
- **Reproducibility across runs** — the same applicant produces a functionally equivalent decision every time (qualitative idempotency)
- **Five scenarios run end-to-end against the live Anthropic API**, with captured outputs

## Why this is a credible target for AILang+AIEX

Personal loan eligibility is *exactly* the kind of system that classical code does badly:

- **The rules are inherently qualitative** (industry stability, employment trajectory, recent credit-shopping behaviour), and classical code reduces them to brittle thresholds (`if industry in BAD_LIST`).
- **They change constantly** as policy, regulation, and market conditions evolve, and every change requires a developer.
- **They demand auditability** for regulators — every decision must come with a justification trail, which most rule engines bolt on after the fact.
- **They run at high volume** with strict cost ceilings.

AILang + AIEX addresses each of these in a way classical code cannot:

| Need | Classical approach | AILang + AIEX |
|---|---|---|
| Qualitative judgment | `if score < 0.3` (proxy that loses signal) | `WEIGH soft_factors` (judgment in its native form) |
| Policy changes | Code change, redeploy, re-test | Edit the natural-language rule description |
| Audit trail | Bolted on; often incomplete | Built in: every transaction logged with rationale, contract violations, retries |
| Cost at scale | Cheap (CPU); poor judgment quality | $0.043/decision with multi-tier routing; quality competitive with paralegal review |
| Reproducibility | Bit-exact (deterministic) | Functionally equivalent (qualitative idempotency) |

Determinism is the one thing classical code wins on. For most business-rules systems that's a theoretical win — the input data has so much real-world variability that bit-exact reproducibility was never the actual property they had. Functionally-equivalent reproducibility (same applicant → same decision shape, same justification, same audit fields) is what they actually need, and AILang + AIEX delivers it.

## Files

```
loan_eligibility/
├── README.md                       # This file
├── loan_eligibility.ailang         # The canonical program (the executable spec)
├── scenarios/
│   ├── generate_scenarios.py       # Builds the 5 .ailang variants from APPLICANTS dict
│   ├── run_all.py                  # Runs every scenario through AIEX, captures outputs
│   ├── scenario_01_clear_approve.ailang
│   ├── scenario_02_clear_decline.ailang
│   ├── scenario_03_marginal_conditional.ailang
│   ├── scenario_04_marginal_decline.ailang
│   └── scenario_05_judgment_call.ailang
└── runs/
    ├── run_report.md               # Human-readable decisions per scenario
    └── run_report.json             # Machine-readable dump for diff/regression
```

## Program structure

```
SET applicant TO {...}         # input data (varies per scenario)
SET product TO {...}           # product policy thresholds
SET eligibility_rules TO {...} # the rule set in declarative form

EXECUTE_CODE python:           # Step 1: deterministic affordability math
    monthly payment, DTI, residual income, payment-to-income ratio
END_EXECUTE

DEDUCE hard_eligibility ...    # Step 2: rule-by-rule pass/fail (Sonnet)
WEIGH soft_factors ...         # Step 3: qualitative judgment (Sonnet/Opus)
SYNTHESIZE final_decision ...  # Step 4: integrate hard + soft (Sonnet/Opus)

EXECUTE_CODE python:           # Step 5: format audit record + customer letter
    audit_log_entry, letter_excerpt
END_EXECUTE
```

Five transactions; two are deterministic ($0 LLM cost); three are reasoning operations routed to the appropriate model tier. Pre-execution budget: **$0.043 per scenario**, **88.1% savings vs an all-Opus baseline**.

## Running it yourself

Prerequisites: a working AIEX install (see [github.com/pcoz/aiex](https://github.com/pcoz/aiex)) with a valid `ANTHROPIC_API_KEY` in `<aiex>/.env`.

```bash
# Compile-only (no API spend) -- shows the budget plan
aiex compile examples/loan_eligibility/scenarios/scenario_01_clear_approve.ailang

# Run one scenario end-to-end
aiex run examples/loan_eligibility/scenarios/scenario_01_clear_approve.ailang

# Run all five scenarios and regenerate runs/run_report.md
cd examples/loan_eligibility/scenarios && python run_all.py
```

To add a new scenario: add an entry to the `APPLICANTS` dict in `scenarios/generate_scenarios.py`, then re-run it. The resulting `.ailang` file is fully self-contained and runnable.

## What the scenarios are designed to demonstrate

| # | Designed outcome | What it stresses |
|---|---|---|
| 1 | Clear APPROVE | All hard rules pass with comfortable margins; soft factors net-positive |
| 2 | Clear DECLINE | Hard disqualifier present (recent bankruptcy); model must cite it |
| 3 | Marginal — conditional approval | Borderline DTI, otherwise solid; soft factors should justify approval-with-conditions |
| 4 | Marginal — decline | Score passes thresholds but soft factors are concerning (recent job, gig industry, high inquiries) |
| 5 | Edge case — judgment call | Right at every threshold; the right move is `REFER_TO_UNDERWRITER` |

Live decisions captured in `runs/run_report.md`. The model tends to escalate borderline cases to human underwriters rather than guess — which is exactly the conservative behaviour a defensible automated system should exhibit.

## Reproducing the qualitative idempotency claim

Run `python run_all.py` twice in a row. Compare the two `runs/run_report.json` files. Surface text wording will vary between the runs (LLMs are stochastic); the load-bearing fields — `decision`, `hard_outcome`, `soft_factor_direction`, `confidence`, the conditions list — converge across runs. That convergence is what makes this architecture credible for systems where decisions need to be reproducible-enough for audit, even when they cannot be deterministic in the bit-exact sense.

## Where this would not fit

For honesty: AIEX is not the right substrate for every business-rules workload.

- **Sub-millisecond decisioning** (real-time fraud at >1K TPS): too slow. Each AIEX decision takes seconds, not milliseconds.
- **Regulator-mandated bit-exact replay**: AIEX gives functional equivalence, not bit equivalence. If the regulator demands "given the same inputs, prove the system produces the same bytes", you need classical code (or AIEX as a layer over classical code that handles the deterministic core).
- **No qualitative dimension at all**: if every rule is `(field op constant)`, classical code is cheaper, faster, and easier to verify. AIEX shines when the rules involve genuine judgment.

For everything else — the underwriting, the eligibility, the adjudication, the compliance review work that today eats armies of analysts and 200,000-line rule engines — this approach is a credible alternative.
