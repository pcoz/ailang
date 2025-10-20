Here’s a faithful, end-to-end **simulation of your `small_claims.ail` program** running on the scenario:

* **Incident**: London bank customer has been charged **punitive interest** on an overdrawn current account.
* **Goal**: Customer wants **refund/recalculation of interest and charges**, corrections to any credit markers, and a fair ongoing arrangement.

---

# Simulation Transcript (what the AIL program would output)

## Stage 1 — Fact Clarification

**Financial-Rights Advisor**: Quick intake:

* Bank & account: *UK personal current account (London)*.
* What happened: *Overdraft interest charged at a very high rate; possibly different/higher rate for unarranged overdraft; charges feel punitive and unaffordable.*
* What you want: *Refund/recalculation of interest/fees; fair ongoing rate/plan; removal of negative credit markers if caused by the bank’s failings.*
* Evidence available: *Bank statements (last 12–24 months), overdraft T&Cs and rate change notices, any financial difficulty disclosures, complaint history, affordability notes.*
* Regulatory context: **FCA overdraft reforms** (2020) require **simple annual interest with no extra fees** and **no higher price for unarranged vs arranged overdrafts**, plus **Consumer Duty (Principle 12)** on *price & value* and fair outcomes; complaint/escalation via **FOS** after **8 weeks** or deadlock. ([FCA][1])

**Opponent model** (bank): “Process-driven; initial stance: *terms-and-conditions compliance*; sensitivity to **Consumer Duty** scrutiny and **FOS** risk.”

---

## Stage 2 — Strategy (law × persuasion)

* **Legal levers**:

  1. **FCA overdraft reforms (PS19/16; from Apr 2020)** → banks must charge a **single simple annual interest rate**; **no fixed daily/paid-item fees**; **unarranged price can’t exceed arranged**. Evidence of complex or punitive charging post-2020 is a red flag. ([FCA][1])
  2. **Consumer Duty (PRIN 2A)** → outcomes on **price & value**: charges must represent **fair value**; firms must act to deliver **good outcomes** for retail customers. ([handbook.fca.org.uk][2])
  3. **BCOBS (Banking Conduct)** → overdraft information and treatment standards still apply alongside the Duty. ([handbook.fca.org.uk][3])
  4. **Complaints** → firm has **8 weeks** to issue a final response; then **FOS** (free) within **6 months** of final response. ([Financial Ombudsman][4])

* **What we argue**:
  Charges were **excessive and/or poorly explained**, **not fair value** under the **Consumer Duty**, and/or **non-compliant** with 2020 overdraft pricing reforms (e.g., if unarranged was priced higher than arranged, or extra fees persisted). Remedy: **refund of inappropriate interest/fees**, **recalculation**, **affordability support**, **credit file correction**. ([FCA][1])

---

## Stage 3 — 2D Navigation Loop (actions & predicted reactions)

### Move 1 — **Formal complaint** to the bank (calibrated)

**Rationale**: Required first step; frames **Consumer Duty “price & value”** and **overdraft-reform** breaches; moves bank from *T&Cs defense* → *evaluation*.

**Draft to send (essentials)**

```
Subject: Formal complaint – unfair overdraft interest/charges; request for refund & recalculation

Account: [sort code / account]; Overdraft: [arranged limit if any]

I am complaining about punitive and unfair overdraft interest/charges applied to my account. 
Under the FCA’s overdraft reforms (PS19/16, effective April 2020), overdraft pricing must be 
a single simple annual interest rate without additional fees and the unarranged rate cannot 
exceed the arranged rate. Under the FCA Consumer Duty (PRIN 2A – price & value), these 
charges must represent fair value and deliver good customer outcomes.

Please:
1) Provide a full breakdown of all overdraft interest/charges applied since [date].
2) Confirm the arranged vs unarranged rates used and when any changes took effect.
3) Refund/recalculate any charges that exceed the arranged rate, include prohibited fees, 
   or otherwise fail fair value under the Duty. 
4) If I’ve indicated financial difficulty, apply appropriate forbearance and support.
5) Remove any adverse credit markers caused by these failings.

If I don’t receive a satisfactory final response within 8 weeks, I will refer this to the 
Financial Ombudsman Service.
```

(We’ll attach a **schedule of charges** extracted from statements.)
**Reg scaffolding**: overdraft reforms summary; Consumer Duty (PRIN 2A) extract; FOS escalation info. ([FCA][1])

**Predicted reaction**: Bank requests time; offers partial goodwill; asserts “rates disclosed.” Emotional shift: *defensive → evaluation*.

---

### Move 2 — **Evidence pack** (built by the program)

* **Timeline** of rate changes and overdraft usage.
* **Table of all interest/charges** by month (arranged vs unarranged flags).
* **T&Cs & notices** the bank sent you.
* **Any hardship disclosure** → supports forbearance expectations.
* **Comparative check**: Were **unarranged charges higher than arranged**? Any **fixed fees** post-Apr 2020? Are total charges **disproportionate** vs typical balances (fair-value lens)? ([Addleshaw Goddard][5])

---

### Move 3 — **Negotiation stance**

* Reiterate **Consumer Duty—price & value**: outcome must be **fair value**; complexity or stealth price jumps are problematic. ([handbook.fca.org.uk][6])
* Point to **2020 reforms**: any **unarranged > arranged pricing** or **additional fees** after Apr-2020 is non-compliant. ([Addleshaw Goddard][5])
* Ask for: **full refund/recalculation**, **12-month interest-free plan** (if needed), **credit-file clean-up**, and **written confirmation**.

**Predicted reaction**: Improved offer if non-compliance is clear; otherwise a final response (deadlock). Emotional shift: *evaluation → negotiation_openness*.

---

### Move 4 — **Escalate to FOS** (if unresolved after 8 weeks or on deadlock)

* Submit **complaint form**, attach evidence pack and bank’s final response.
* FOS will look at **what’s fair and reasonable** in light of **FCA rules** (overdraft reforms, Consumer Duty) and **individual circumstances**; remedies can include **refund/recalculation** and **interest on redress**; **free for consumers**. ([Financial Ombudsman][7])

**Predicted reaction**: Bank re-assesses risk; may settle pre-adjudication. Emotional shift: *concern → acceptance*.

---

## Evidence Matrix (program’s working set)

* **Primary**: Full statements (CSV if available), overdraft T&Cs (historic & current), formal notices of rate changes, any hardship correspondence.
* **Derived**: Spreadsheet of charges vs rules (flag *post-Apr 2020* anomalies; highlight **unarranged>arranged** or **extra fees**). ([Addleshaw Goddard][5])
* **Authorities**:
  – FCA **PS19/16 Overdrafts** summary/policy; **no higher price for unarranged**, **simple annual rate**, **no extra fees** (from Apr 2020). ([FCA][1])
  – **Consumer Duty (PRIN 2A)**, particularly **price & value** outcome (fair value). ([handbook.fca.org.uk][2])
  – **BCOBS** overdose/overdraft information obligations. ([handbook.fca.org.uk][3])
  – **Complaints** → **8 weeks** to final response; **FOS** within **6 months**. ([Financial Ombudsman][4])

---

## Risk & Counter-moves (program’s forecast)

* **Bank: “We disclosed the rate.”**
  → Disclosure ≠ **fair value**; **Consumer Duty** assesses **outcomes** (price & value), not just disclosure. ([handbook.fca.org.uk][6])
* **Bank: “It was unarranged—higher rate is normal.”**
  → Since Apr-2020, **unarranged cannot exceed arranged**; any extra fees also banned. ([Addleshaw Goddard][5])
* **Delay tactics**
  → Note **8-week** rule; then **FOS**. ([Financial Ombudsman][4])

---

## Compact Next-Actions Checklist

1. **File the formal complaint** (template above) today; request full breakdowns & T&Cs. ([FCA][8])
2. **Build the charges spreadsheet** (arranged vs unarranged; flag post-2020 issues). ([Addleshaw Goddard][5])
3. **If no satisfactory final response in 8 weeks** (or a poor outcome), **escalate to FOS** within **6 months**. ([Financial Ombudsman][4])
4. If in **financial difficulty**, explicitly say so and request **forbearance**; this engages Duty expectations around **support**. ([handbook.fca.org.uk][2])

---

### Notes

* This is a **simulation of your AIL program’s advisory journey**, not legal advice.
* If you want, I can output the complaint letter and a ready-to-fill **charges schedule** as downloadable Markdown/CSV in a follow-up.

[1]: https://www.fca.org.uk/publications/policy-statements/ps19-16-high-credit-review-overdrafts?utm_source=chatgpt.com "PS19/16: High-Cost Credit Review: Overdraft policy ..."
[2]: https://handbook.fca.org.uk/handbook/prin2a?utm_source=chatgpt.com "PRIN 2A The Consumer Duty - FCA Handbook"
[3]: https://handbook.fca.org.uk/handbook/BCOBS/2/2B.html?utm_source=chatgpt.com "BCOBS 2.2B General information about overdrafts for ..."
[4]: https://www.financial-ombudsman.org.uk/consumers/how-to-complain?utm_source=chatgpt.com "How to complain"
[5]: https://www.addleshawgoddard.com/globalassets/specialisms/financial-regulation/overdrafts-client-briefing.-june-2019.pdf?utm_source=chatgpt.com "FCA FINAL RULES AND FURTHER CONSULTATION"
[6]: https://handbook.fca.org.uk/handbook/PRIN/2A/4.html?utm_source=chatgpt.com "PRIN 2A.4 Consumer Duty: retail customer outcome on price ..."
[7]: https://www.financial-ombudsman.org.uk/consumers/complaints-can-help/banking-and-payments/bank-accounts?utm_source=chatgpt.com "Bank accounts"
[8]: https://www.fca.org.uk/consumers/how-complain?utm_source=chatgpt.com "How to complain"
