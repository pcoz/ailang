# Personal Loan Eligibility — AILang as an Executable Specification

This example demonstrates how a regulated business-rules workflow — the kind that today lives in 200,000-line Drools rule sets, hand-tuned Java decision engines, or COBOL underwriting modules — can be expressed as a single readable AILang program and run on AIEX.

The core insight: **the program is the spec**. The same text a compliance officer reads to understand the policy is what the AIEX runtime executes. There is no separate "rules document → translated into Java → translated back to a regulator-friendly summary" round trip where intent gets lost between layers.

## What gets demonstrated

- **Typed reasoning operations** for the qualitative parts (`DEDUCE`, `WEIGH`, `SYNTHESIZE`)
- **`EXECUTE_CODE` blocks** for the deterministic parts (amortisation math, audit log formatting)
- **Output contracts** (`MUST_INCLUDE`, `CANNOT_INCLUDE`, constrained `OUTPUT_FORMAT` enums) that lock the LLM to defensible decision categories
- **Multi-tier model routing** — BERT/Haiku/Sonnet/Opus selected automatically per operation, ~88% cost reduction vs all-Opus
- **Pre-execution budget reports** — every scenario costs $0.044 to run, knowable before spending
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

Five transactions; two are deterministic ($0 LLM cost); three are reasoning operations routed to the appropriate model tier. Pre-execution budget: **$0.0441 per scenario**, **87.8% savings vs an all-Opus baseline**. Both numbers come straight from `aiex compile <scenario>.ailang` — run that command on any of the scenario files to see the per-transaction routing decisions and verify the figures.

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

The table below shows the designed *intent* of each scenario alongside the *actual* decision the model produced on a live run. Where the actual differs from the designed outcome, the model leaned conservative — escalating to a human underwriter or adding conditions rather than committing to a hard call. That's the correct behaviour for a real underwriting system, and it's exactly what the contracts allow: the OUTPUT_FORMAT enum includes `REFER_TO_UNDERWRITER` and `APPROVE_WITH_CONDITIONS` precisely so the model can defer when it doesn't have enough signal.

| # | Designed outcome | Actual (live run) | What it stresses |
|---|---|---|---|
| 1 | APPROVE | APPROVE_WITH_CONDITIONS (medium conf) | All hard rules pass with comfortable margins; model added conditions because soft-factor input data was thin |
| 2 | DECLINE | DECLINE (high conf) | Hard disqualifier present (recent bankruptcy); model cites it directly |
| 3 | APPROVE_WITH_CONDITIONS | REFER_TO_UNDERWRITER | Borderline DTI; model escalated rather than commit |
| 4 | DECLINE | REFER_TO_UNDERWRITER | Score passes thresholds but soft factors concerning; model escalated |
| 5 | REFER_TO_UNDERWRITER | APPROVE_WITH_CONDITIONS | Right at every threshold; model resolved with conditions |

Full per-scenario rationales, contributing factors, and customer-letter excerpts are in [`runs/run_report.md`](runs/run_report.md).

**Why the conservative skew?** The WEIGH step's soft-factor inputs in this example are deliberately minimal (one industry tag, one tenure number, etc.). Every scenario produced `soft_factor_direction: neutral` because the model lacked confident signal — which then drove the SYNTHESIZE step toward conditional or escalated decisions rather than confident APPROVE/DECLINE. With richer soft-factor inputs (recent payment history, industry-specific economic context, behavioural CRM signals) the model would discriminate more sharply. This is itself a useful lesson: AILang programs are sensitive to input richness in exactly the way a human underwriter is.

## Reproducing the qualitative idempotency claim

Run `python run_all.py` twice in a row. Compare the two `runs/run_report.json` files. Surface text wording will vary between the runs (LLMs are stochastic); the load-bearing fields — `decision`, `hard_outcome`, `soft_factor_direction`, `confidence`, the conditions list — converge across runs. That convergence is what makes this architecture credible for systems where decisions need to be reproducible-enough for audit, even when they cannot be deterministic in the bit-exact sense.

## Where this would not fit

For honesty: AIEX is not the right substrate for every business-rules workload.

- **Sub-millisecond decisioning** (real-time fraud at >1K TPS): too slow. Each AIEX decision takes seconds, not milliseconds.
- **Regulator-mandated bit-exact replay**: AIEX gives functional equivalence, not bit equivalence. If the regulator demands "given the same inputs, prove the system produces the same bytes", you need classical code (or AIEX as a layer over classical code that handles the deterministic core).
- **No qualitative dimension at all**: if every rule is `(field op constant)`, classical code is cheaper, faster, and easier to verify. AIEX shines when the rules involve genuine judgment.

For everything else — the underwriting, the eligibility, the adjudication, the compliance review work that today eats armies of analysts and 200,000-line rule engines — this approach is a credible alternative.
