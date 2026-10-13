# Loan Eligibility -- Live Execution Report

> **Superseded -- regenerate.** This run predates an AIEX fix: the `ON applicant` clause of `WEIGH soft_factors` was never rendered into the prompt, so the soft-factor step received no applicant data and returned `neutral` (citing `insufficient_info` in several scenarios). Scenario headings name the intended case, not the outcome below. See the README note.

_Generated: 2026-04-19T06:11:06Z_

Each scenario runs the same `loan_eligibility.ailang` program through AIEX with a different applicant.  The reasoning operations (`DEDUCE`, `WEIGH`, `SYNTHESIZE`) make real LLM calls; the `EXECUTE_CODE` blocks compute deterministically.  Outputs below are captured verbatim from the run.

## Scenario 1 -- Clear APPROVE

**Applicant:** Asha Bhattacharya, credit 785, income $110,000/yr, requesting $18,000 over 48mo

**Computed metrics (deterministic):** monthly payment $473.13, DTI 15.53%, residual income $7743.54

**Hard eligibility outcome:** `all_pass`

**Soft factor direction:** `neutral`

**Final decision: `APPROVE_WITH_CONDITIONS`** (confidence: medium)

_Rationale:_ All hard eligibility checks pass without exception, demonstrating strong quantitative creditworthiness: credit score of 785 against a 660 minimum, DTI of 15.53% well below the 43% ceiling, residual income of $7,743.54 substantially exceeding the $1,500 floor, 96 months of employment tenure, no bankruptcies, no fraud flags, and a loan amount and term both within product limits. The soft factor assessment yields a net-neutral directional signal, meaning no soft factors actively support escalation to decline or referral, but the tenure assessment is flagged as 'weak' and the relationship assessment is 'none', introducing modest incremental uncertainty. The absence of a positive soft factor uplift, combined with the weak tenure and no existing relationship, warrants a conditional approval rather than a clean approval, ensuring additional verification steps are satisfied before funding.

_Conditions:_
  - Verification of employment and income documentation should be completed prior to funding, given the 'weak' tenure soft assessment flag.
  - Confirmation of identity and absence of undisclosed liabilities should be obtained, given that no existing relationship exists to provide supplementary behavioral data.
  - Any material change in the applicant's financial profile between application and funding should trigger re-evaluation against hard eligibility thresholds.

**Customer letter excerpt:**

> Dear Asha Bhattacharya, your loan request is conditionally approved. Conditions: Verification of employment and income documentation should be completed prior to funding, given the 'weak' tenure soft assessment flag.; Confirmation of identity and absence of undisclosed liabilities should be obtained, given that no existing relationship exists to provide supplementary behavioral data.; Any material change in the applicant's financial profile between application and funding should trigger re-evaluation against hard eligibility thresholds.. All hard eligibility checks pass without exception, demonstrating strong quantitative creditworthiness: credit score of 785 against a 660 minimum, DTI of 15.53% well below the 43% ceiling, residual income of $7,743.54 substantially exceeding the $1,500 floor, 96 months of employment tenure, no bankruptcies, no fraud flags, and a loan amount and term both within product limits. The soft factor assessment yields a net-neutral directional signal, meaning no soft factors actively support escalation to decline or referral, but the tenure assessment is flagged as 'weak' and the relationship assessment is 'none', introducing modest incremental uncertainty. The absence of a positive soft factor uplift, combined with the weak tenure and no existing relationship, warrants a conditional approval rather than a clean approval, ensuring additional verification steps are satisfied before funding.

_Transactions: 5 committed, 0 rolled back._

---

## Scenario 2 -- Clear DECLINE

**Applicant:** Marcus Reilly, credit 590, income $38,000/yr, requesting $12,000 over 60mo

**Computed metrics (deterministic):** monthly payment $266.33, DTI 43.15%, residual income $1800.34

**Hard eligibility outcome:** `hard_fail`
  - Failed checks: credit_score_check, dti_check, employment_tenure_check, bankruptcy_disqualifier_check

**Soft factor direction:** `neutral`

**Final decision: `DECLINE`** (confidence: high)

_Rationale:_ The application results in a hard_fail outcome driven by four failed hard eligibility checks, including one absolute hard disqualifier: the applicant has 1 bankruptcy within the last 7 years, against a requirement of 0. This disqualifier alone mandates decline regardless of any other factors. Additionally, the applicant fails three further eligibility criteria: credit score of 590 is below the product minimum of 660; computed DTI of 43.15% exceeds the product maximum of 43.0%; and employment tenure of 5 months is below the 12-month standard minimum, with no applicable exception (the homeownership exception does not apply as the applicant rents). The cumulative weight of these hard failures leaves no pathway to approval or conditional approval.

**Customer letter excerpt:**

> Dear Marcus Reilly, we are unable to approve your loan request at this time. The application results in a hard_fail outcome driven by four failed hard eligibility checks, including one absolute hard disqualifier: the applicant has 1 bankruptcy within the last 7 years, against a requirement of 0. This disqualifier alone mandates decline regardless of any other factors. Additionally, the applicant fails three further eligibility criteria: credit score of 590 is below the product minimum of 660; computed DTI of 43.15% exceeds the product maximum of 43.0%; and employment tenure of 5 months is below the 12-month standard minimum, with no applicable exception (the homeownership exception does not apply as the applicant rents). The cumulative weight of these hard failures leaves no pathway to approval or conditional approval. You are welcome to reapply after addressing the cited factors.

_Transactions: 5 committed, 0 rolled back._

---

## Scenario 3 -- Marginal: conditional approval

**Applicant:** Priya Sundaram, credit 695, income $64,000/yr, requesting $22,000 over 60mo

**Computed metrics (deterministic):** monthly payment $488.27, DTI 43.84%, residual income $2995.07

**Hard eligibility outcome:** `marginal`
  - Failed checks: dti_check

**Soft factor direction:** `neutral`

**Final decision: `REFER_TO_UNDERWRITER`** (confidence: medium)

_Rationale:_ The application presents a marginal hard eligibility outcome driven by a single failing check: DTI of 43.84% exceeds the product maximum of 43.00% by 0.84 percentage points. All other hard eligibility criteria pass, including credit score (695 vs. 660 minimum), residual income ($2,995.07 vs. $1,500.00 minimum), employment tenure (48 months vs. 12-month minimum), and all disqualifier checks (bankruptcy, fraud). Because DTI is classified as a non-disqualifier eligibility criterion resulting in a marginal rather than hard-fail outcome, and because the soft factor assessment is effectively indeterminate due to insufficient source data, automated approval or decline cannot be responsibly rendered. The marginal DTI breach combined with neutral-to-weak soft factor signals and an absence of meaningful relationship or risk-trajectory data warrants human underwriter review to make a fully informed credit judgment.

_Conditions:_
  - Underwriter should verify whether any documented reduction in recurring obligations could bring DTI to or below the 43.00% threshold prior to funding
  - Underwriter should assess whether the strong residual income figure ($2,995.07) and healthy inquiry velocity are sufficient compensating factors to offset the marginal DTI breach
  - Underwriter should obtain and evaluate the source data underlying the soft factor assessments (industry, tenure, relationship, risk trajectory) before rendering a final decision, as the soft factor module reported insufficient_info
  - If approved, underwriter should consider whether any loan structuring adjustments (e.g., reduced loan amount or adjusted term) could bring DTI within product guidelines

**Customer letter excerpt:**

> Dear Priya Sundaram, your application has been forwarded to a senior underwriter for individual review. We will be in touch within 3 business days.

_Transactions: 5 committed, 0 rolled back._

---

## Scenario 4 -- Marginal: decline despite OK score

**Applicant:** Diego Ferreira, credit 685, income $72,000/yr, requesting $15,000 over 36mo

**Computed metrics (deterministic):** monthly payment $497.5, DTI 28.29%, residual income $4302.5

**Hard eligibility outcome:** `marginal`
  - Failed checks: employment_tenure_check

**Soft factor direction:** `neutral`

**Final decision: `REFER_TO_UNDERWRITER`** (confidence: medium)

_Rationale:_ Diego Ferreira achieves a 'marginal' hard eligibility outcome, passing 7 of 8 checks but failing the employment tenure requirement (3 months actual vs. 12 months minimum). This single failure is a standard eligibility rule rather than an absolute hard disqualifier, and the homeownership exception that could have offset the tenure shortfall does not apply given his renter status. The remaining hard factors are solidly within product limits — credit score (685), DTI (28.29%), and residual income ($4,302.50) all provide meaningful buffer above their respective thresholds. However, because the soft-factor analysis was unable to produce a meaningful weighted evaluation due to insufficient source data (returning only schema-default neutral values), the overall risk picture cannot be fully resolved by automated scoring alone. The combination of a marginal hard outcome and an unresolvable soft-factor assessment makes referral to a human underwriter the appropriate disposition, as the underwriter can apply judgment to the tenure exception question and gather any missing soft-factor evidence.

_Conditions:_
  - Underwriter must make a specific determination on whether any exception to the 12-month employment tenure requirement is warranted given the applicant's other strong financial indicators (low DTI, high residual income buffer)
  - Underwriter should obtain and evaluate employment verification documentation to confirm the 3-month tenure figure and assess the stability of the current employer and role
  - Underwriter should gather the soft-factor source data that was unavailable at automated scoring stage — specifically: industry/employer forward-looking stability indicators, any relationship history, and a validated inquiry velocity count — before finalising the decision
  - If an exception is granted, underwriter must document the specific compensating factors relied upon (e.g., residual income strength, low DTI) in accordance with the institution's exception policy

**Customer letter excerpt:**

> Dear Diego Ferreira, your application has been forwarded to a senior underwriter for individual review. We will be in touch within 3 business days.

_Transactions: 5 committed, 0 rolled back._

---

## Scenario 5 -- Edge case: judgment call

**Applicant:** Eleanor Whitfield, credit 660, income $58,000/yr, requesting $20,000 over 72mo

**Computed metrics (deterministic):** monthly payment $389.96, DTI 37.03%, residual income $3043.37

**Hard eligibility outcome:** `all_pass`

**Soft factor direction:** `neutral`

**Final decision: `APPROVE_WITH_CONDITIONS`** (confidence: medium)

_Rationale:_ All eight hard eligibility checks pass with no failed checks, satisfying every mandatory threshold: credit score meets the minimum exactly (660 >= 660), DTI is within the maximum (37.03% <= 43.0%), employment tenure meets the minimum (12 months >= 12 months), residual income exceeds the minimum ($3,043.37 >= $1,500.00), no bankruptcy disqualifier, no fraud flags, loan amount within product limit ($20,000 <= $50,000), and term within product limit (72 months <= 84 months). The hard outcome is unambiguously 'all_pass', which supports approval. However, the soft factor analysis is materially incomplete: the soft_factors module explicitly states 'insufficient_info' and acknowledges that no source data, claims, or evidence were provided to evaluate forward payment capacity, relationship value, or risk trajectory. The only assessable soft signals are a 'weak' tenure assessment and a 'none' relationship assessment, both of which introduce modest incremental risk. The inquiry velocity assessment is 'healthy' and the industry assessment is 'neutral', providing partial offset. Because the hard outcome fully supports approval but the soft factor layer is substantively unresolved, a clean APPROVE cannot be issued with high confidence. Conditions are imposed to compensate for the soft factor data gap and the marginally thin credit profile (score at the floor, DTI near the upper range).

_Conditions:_
  - Verification of employment and income documentation (e.g., recent pay stubs, employer confirmation, or equivalent) to substantiate the residual income and tenure figures before disbursement, given the tenure assessment is 'weak' and tenure is at the minimum threshold
  - Completion of a full soft factor evaluation with actual source data, claims, and evidence supplied to the soft_factors module; if the completed soft factor assessment returns a 'negative' direction, the file must be referred to an underwriter before proceeding
  - Confirmation that no material changes to employment status, income, or outstanding obligations have occurred since the application date, given the thin margin between actual DTI (37.03%) and the maximum (43.0%)

**Customer letter excerpt:**

> Dear Eleanor Whitfield, your loan request is conditionally approved. Conditions: Verification of employment and income documentation (e.g., recent pay stubs, employer confirmation, or equivalent) to substantiate the residual income and tenure figures before disbursement, given the tenure assessment is 'weak' and tenure is at the minimum threshold; Completion of a full soft factor evaluation with actual source data, claims, and evidence supplied to the soft_factors module; if the completed soft factor assessment returns a 'negative' direction, the file must be referred to an underwriter before proceeding; Confirmation that no material changes to employment status, income, or outstanding obligations have occurred since the application date, given the thin margin between actual DTI (37.03%) and the maximum (43.0%). All eight hard eligibility checks pass with no failed checks, satisfying every mandatory threshold: credit score meets the minimum exactly (660 >= 660), DTI is within the maximum (37.03% <= 43.0%), employment tenure meets the minimum (12 months >= 12 months), residual income exceeds the minimum ($3,043.37 >= $1,500.00), no bankruptcy disqualifier, no fraud flags, loan amount within product limit ($20,000 <= $50,000), and term within product limit (72 months <= 84 months). The hard outcome is unambiguously 'all_pass', which supports approval. However, the soft factor analysis is materially incomplete: the soft_factors module explicitly states 'insufficient_info' and acknowledges that no source data, claims, or evidence were provided to evaluate forward payment capacity, relationship value, or risk trajectory. The only assessable soft signals are a 'weak' tenure assessment and a 'none' relationship assessment, both of which introduce modest incremental risk. The inquiry velocity assessment is 'healthy' and the industry assessment is 'neutral', providing partial offset. Because the hard outcome fully supports approval but the soft factor layer is substantively unresolved, a clean APPROVE cannot be issued with high confidence. Conditions are imposed to compensate for the soft factor data gap and the marginally thin credit profile (score at the floor, DTI near the upper range).

_Transactions: 5 committed, 0 rolled back._

---
