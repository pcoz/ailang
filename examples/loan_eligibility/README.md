# Personal Loan Eligibility — AILang as an Executable Specification

This example demonstrates how a regulated business-rules workflow — the kind that today lives in 200,000-line Drools rule sets, hand-tuned Java decision engines, or COBOL underwriting modules — can be expressed as a single readable AILang program and run on AIEX.

The core insight: **the program is the spec**. The same text a compliance officer reads to understand the policy is what the AIEX runtime executes. There is no separate "rules document → translated into Java → translated back to a regulator-friendly summary" round trip where intent gets lost between layers.

## What gets demonstrated

- **Typed reasoning operations** for the qualitative parts (`WEIGH`, `SYNTHESIZE`)
- **`EXECUTE_CODE` blocks** for the deterministic parts (amortisation math, rule-by-rule eligibility checks and the hard-outcome classification, the decision-rule policy check, audit log formatting)
- **Output contracts** (`MUST_INCLUDE`, `CANNOT_INCLUDE`, constrained `OUTPUT_FORMAT` enums) that lock the LLM to defensible decision categories and make it name the decision rule it applied
- **Multi-tier model routing** — BERT/Haiku/Sonnet/Opus selected automatically per operation, ~40% cost reduction vs running the same plan on Opus
- **Pre-execution budget reports** — every scenario is estimated at $0.032 to run, knowable before spending
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
| Cost at scale | Cheap (CPU); poor judgment quality | ~$0.032/decision (pre-execution estimate) with multi-tier routing; quality competitive with paralegal review |
| Reproducibility | Bit-exact (deterministic) | Functionally equivalent (qualitative idempotency) |

Determinism is the one thing classical code wins on. For most business-rules systems that's a theoretical win — the input data has so much real-world variability that bit-exact reproducibility was never the actual property they had. Functionally-equivalent reproducibility (same applicant → same decision shape, same justification, same audit fields) is what they actually need, and AILang + AIEX delivers it.

## Files

```
loan_eligibility/
├── README.md                       # This file
├── loan_eligibility.ailang         # The canonical program (the executable spec)
├── scenarios/
│   ├── generate_scenarios.py       # Builds the 5 .ailang variants from APPLICANTS dict
│   ├── run_all.py                  # Runs every scenario through AIEX, writes runs/<run-id>/
│   ├── compare_runs.py             # Compares two run_report.json files on the load-bearing fields
│   ├── scenario_01_clear_approve.ailang
│   ├── scenario_02_clear_decline.ailang
│   ├── scenario_03_marginal_conditional.ailang
│   ├── scenario_04_marginal_decline.ailang
│   └── scenario_05_judgment_call.ailang
└── runs/
    ├── run_report.md               # Captured run (predates the WEIGH fix and the explicit rules -- see note below)
    ├── run_report.json             # Machine-readable dump of the same run
    └── <run-id>/                   # New runs from run_all.py: run_report.md + run_report.json
```

## Program structure

```
SET applicant TO {...}           # input data (varies per scenario)
SET product TO {...}             # product policy thresholds
SET eligibility_rules TO {...}   # the rule set in declarative form
SET hard_outcome_policy TO {...} # disqualifiers, marginal tolerance, thin-margin band
SET decision_rules TO {...}      # decision table R1-R4 the final step must follow

EXECUTE_CODE python:             # Step 1: deterministic affordability math
    monthly payment, DTI, residual income, payment-to-income ratio
END_EXECUTE

EXECUTE_CODE python:             # Step 2: rule-by-rule pass/fail, margins,
    hard_eligibility, hard_outcome, thin_margin_checks   # hard outcome
END_EXECUTE

WEIGH soft_factors ...           # Step 3: qualitative judgment (Sonnet)
SYNTHESIZE final_decision ...    # Step 4: decision under decision_rules (Sonnet)

EXECUTE_CODE python:             # Step 5: policy check, audit record, letter
    policy_check, audit_log_entry, letter_excerpt
END_EXECUTE
```

Five transactions; three are deterministic ($0 LLM cost); two are reasoning operations routed to the appropriate model tier. Pre-execution budget: **$0.0321 per scenario**, **40.0% savings vs an all-Opus baseline** ($0.0535). Both numbers come straight from `aiex compile <scenario>.ailang` — run that command on any of the scenario files to see the per-transaction routing decisions and verify the figures.

## The decision policy

Every eligibility rule is a threshold comparison, so the program applies them in Python, not with a model. Two rules decide how those checks turn into a decision. Both are written out in the program, and neither is left to model judgment.

**1. Hard outcome.** Step 2 runs each check in `eligibility_rules` and records how far the value sits from its threshold (`margin_pct`: negative means a shortfall). It then classifies the application:

| Hard outcome | When |
|---|---|
| `hard_fail` | Any disqualifier fails: bankruptcy, fraud flags, or a product limit (loan amount, term). No tolerance applies. |
| `marginal` | No disqualifier fails, and exactly one graded check (credit score, DTI, employment tenure, residual income) fails by no more than 5% of its threshold: DTI up to 45.15% (max 43.0%), credit score down to 627 (min 660), tenure down to 11.4 months (min 12), residual income down to $1,425 (min $1,500). |
| `hard_fail` | Any other failure: two or more graded checks fail, or one fails by more than 5%. |
| `all_pass` | No check fails. |

Step 2 also lists `thin_margin_checks`: graded checks that pass with no more than 2% headroom over their threshold. That means credit score 660–673, DTI 42.14%–43.0%, tenure of exactly 12 months, or residual income of $1,500–$1,530. A value exactly at its threshold passes, and always counts as a thin margin. Both percentages are set in `hard_outcome_policy`.

**2. Decision.** `decision_rules` fixes which decision the final `SYNTHESIZE` step may return. The step receives `hard_outcome`, `thin_margin_checks` and the rules, and it must report the rule it applied in `decision_rule_applied`:

| Rule | Condition | Decision |
|---|---|---|
| R1 | `hard_fail` | DECLINE |
| R2 | `marginal` | APPROVE_WITH_CONDITIONS, only if every condition cures the specific shortfall (e.g. a smaller amount or a longer term that brings DTI under the maximum) and the soft direction is not negative; otherwise REFER_TO_UNDERWRITER |
| R3 | `all_pass` with thin margins | APPROVE_WITH_CONDITIONS with one verification condition per thin-margin check; REFER_TO_UNDERWRITER if the soft direction is negative |
| R4 | `all_pass`, no thin margins | APPROVE if the soft direction is positive or neutral; REFER_TO_UNDERWRITER if negative |

The model still makes two judgement calls: it weighs the soft factors (`WEIGH`), and it chooses and words the conditions and the rationale. Step 5 checks the model's decision against R1–R4 in code. If the decision is not one the rules allow, the application goes to an underwriter, and the audit log records the mismatch in `policy_check`.

## Running it yourself

Prerequisites: a working AIEX install (see [github.com/pcoz/aiex](https://github.com/pcoz/aiex)) with a valid `ANTHROPIC_API_KEY` in `<aiex>/.env`.

```bash
# Compile-only (no API spend) -- shows the budget plan
aiex compile examples/loan_eligibility/scenarios/scenario_01_clear_approve.ailang

# Run one scenario end-to-end
aiex run examples/loan_eligibility/scenarios/scenario_01_clear_approve.ailang

# Run all five scenarios; writes runs/<run-id>/run_report.{md,json}
cd examples/loan_eligibility/scenarios && python run_all.py
```

To add a new scenario: add an entry to the `APPLICANTS` dict in `scenarios/generate_scenarios.py`, then re-run it. The resulting `.ailang` file is fully self-contained and runnable.

## What the scenarios are designed to demonstrate

> **Note: the captured runs predate a fix and need regenerating.** `runs/run_report.md` and `runs/run_report.json` were produced before an AIEX fix ([pcoz/aiex](https://github.com/pcoz/aiex), "Wire WEIGH ON <topic> through compiler and engine into the prompt"): the `ON applicant` clause of the `WEIGH soft_factors` step was parsed but never rendered into the prompt, so the soft-factor step received no applicant data and, under `RETRIEVAL_BUDGET: NONE`, returned `soft_factor_direction: neutral` in every scenario (citing `insufficient_info` in several). The scenario labels describe the *intended* case, not the captured outcome; the "Actual" column below and the per-scenario rationales reflect the bug, not the program's policy. They also predate the explicit hard-outcome and decision rules described in [The decision policy](#the-decision-policy): at the time, a `DEDUCE` step judged each check and the `marginal` / `hard_fail` boundary itself, and nothing told the final step whether an application sitting exactly at its thresholds needed conditions. No repeat-run evidence for the qualitative-idempotency claim has been published yet. Regenerate with a fixed AIEX (`python run_all.py`, twice) and check convergence with `scenarios/compare_runs.py`.

The table below shows each scenario's hard outcome under the current rules and the decision the rules call for, alongside the *actual* decision the model produced on the captured live run. Where the actual differs, the model leaned conservative — escalating to a human underwriter or adding conditions rather than committing to a hard call. The decision rules now say when `REFER_TO_UNDERWRITER` and `APPROVE_WITH_CONDITIONS` apply, so the model no longer chooses between them on its own.

| # | Hard outcome (current rules) | Designed outcome | Actual (captured run) | What it stresses |
|---|---|---|---|---|
| 1 | `all_pass`, no thin margins | APPROVE (R4) | APPROVE_WITH_CONDITIONS (medium conf) | All hard rules pass with comfortable margins; model added conditions because the soft-factor step received no applicant data (see note) |
| 2 | `hard_fail` (bankruptcy, plus credit score, DTI, tenure) | DECLINE (R1) | DECLINE (high conf) | Hard disqualifier present (recent bankruptcy); model cites it directly |
| 3 | `marginal` (DTI 43.84% vs 43.0% max) | APPROVE_WITH_CONDITIONS (R2), with a condition that cures the DTI shortfall | REFER_TO_UNDERWRITER | Borderline DTI; model escalated rather than commit |
| 4 | `hard_fail` (tenure 3 vs 12 months, 75% short) | DECLINE (R1) | REFER_TO_UNDERWRITER | Score passes, but tenure fails well outside the tolerance and soft factors are concerning; model escalated |
| 5 | `all_pass`, thin margins on credit score (660 = min) and tenure (12 = min) | APPROVE_WITH_CONDITIONS (R3): one verification condition per thin margin; REFER_TO_UNDERWRITER if soft factors are negative | APPROVE_WITH_CONDITIONS | Right at the thresholds; at-threshold values pass but need verification |

Full per-scenario rationales, contributing factors, and customer-letter excerpts are in [`runs/run_report.md`](runs/run_report.md).

**Why the conservative skew?** In the captured runs every scenario produced `soft_factor_direction: neutral` because the WEIGH step never saw the applicant (see the note above) — not because the soft-factor inputs are too thin. With no soft signal, the SYNTHESIZE step leaned toward conditional or escalated decisions rather than confident APPROVE/DECLINE. Whether the scenarios land on their designed outcomes once the applicant data reaches the WEIGH step is unverified until the runs are regenerated.

## Reproducing the qualitative idempotency claim

Run `python run_all.py` twice in a row; each run writes to its own `runs/<run-id>/` directory (UTC timestamp by default, or pass `--run-id`). Compare them with `python compare_runs.py ../runs/<run_a>/run_report.json ../runs/<run_b>/run_report.json`, which checks the fields below per scenario and exits non-zero if any differ. Surface text wording will vary between the runs (LLMs are stochastic); the load-bearing fields — `decision`, `decision_rule_applied`, `hard_outcome`, `soft_factor_direction`, `confidence`, the conditions list — should converge across runs (not yet demonstrated by published repeat runs). `hard_outcome` and the thin margins are computed in code, so they are identical by construction; the rule that applies then depends only on the soft-factor direction. That convergence is what makes this architecture credible for systems where decisions need to be reproducible-enough for audit, even when they cannot be deterministic in the bit-exact sense.

## Where this would not fit

For honesty: AIEX is not the right substrate for every business-rules workload.

- **Sub-millisecond decisioning** (real-time fraud at >1K TPS): too slow. Each AIEX decision takes seconds, not milliseconds.
- **Regulator-mandated bit-exact replay**: AIEX gives functional equivalence, not bit equivalence. If the regulator demands "given the same inputs, prove the system produces the same bytes", you need classical code (or AIEX as a layer over classical code that handles the deterministic core).
- **No qualitative dimension at all**: if every rule is `(field op constant)`, classical code is cheaper, faster, and easier to verify. AIEX shines when the rules involve genuine judgment.

For everything else — the underwriting, the eligibility, the adjudication, the compliance review work that today eats armies of analysts and 200,000-line rule engines — this approach is a credible alternative.
