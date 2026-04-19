# AILang Evolution: v0.8.0 through v0.8.2

**Date:** 2026-04-16
**Author:** Pinchas Chalk

---

## 1. Background

AILang is a programming language designed for AI reasoning operations. Rather than treating an LLM as a black-box text generator, AILang gives programmers explicit control over *how* the model reasons: what type of reasoning to apply, at what depth, with what constraints, and drawing on how much external knowledge.

The theoretical foundation comes from the LLM Reasoning Router research ([github.com/pcoz/llm-reasoning-router](https://github.com/pcoz/llm-reasoning-router)), which demonstrated that different reasoning types activate fundamentally different neuron populations inside large language models. The key finding was that neuron overlap between reasoning types ranges from just 25% to 75% -- meaning that when you ask a model to "think about something" without specifying the reasoning type, it activates far more neurons than necessary, because it hedges across multiple reasoning strategies simultaneously.

This created a concrete opportunity: if reasoning-type awareness became a first-class construct in AILang, programs could direct the model to activate only the neurons needed for each specific reasoning operation, yielding both efficiency gains and higher-quality output.

The evolution from v0.8.0 through v0.8.2 represents three rapid iterations that turned this insight into a tested, validated language specification. Each version was driven by anomalies and gaps discovered in the previous version's test results. All tests were executed by Claude Opus 4.6 self-executing as the AILang engine.

---

## 2. v0.8.0 -- Typed Reasoning Operations

### What Changed

AILang v0.7.1 had a single undifferentiated keyword, `INTELLIGENTLY`, for all reasoning operations, along with four style modifiers (`CREATIVELY`, `ADAPTIVELY`, `CONTEXTUALLY`, and standard). Version 0.8.0 replaced `INTELLIGENTLY` with six typed reasoning operations:

| Operation | Purpose |
|---|---|
| **RETRIEVE** | Factual lookup -- find and return known information |
| **COMPARE** | Side-by-side evaluation of options against criteria |
| **TRACE** | Causal chain analysis -- follow cause-to-effect or effect-to-cause |
| **DEDUCE** | Logical inference from premises using formal rules |
| **SYNTHESIZE** | Integrate multiple inputs into a unified recommendation |
| **WEIGH** | Evaluate competing authorities, evidence, or expert opinions |

The original style modifiers (`CREATIVELY`, `ADAPTIVELY`, `CONTEXTUALLY`) were retained as an orthogonal second axis. This gave programs a two-dimensional control surface: *what* type of reasoning to perform (operation) and *how* to approach it (style).

### Why

The reasoning router research proved that what differs at the neuron level is the *type* of reasoning operation (weighing authority vs. deducing from premises vs. tracing cause-and-effect), not the style or attitude of the reasoning. Style and operation type are orthogonal axes that v0.7.1's single `INTELLIGENTLY` keyword conflated into one.

### Test Results (Tests 01-04)

Four tests validated the typed reasoning model:

**Neuron activation savings per typed operation:**

| Operation | Estimated Neurons (Typed) | Estimated Neurons (Untyped) | Savings |
|---|---|---|---|
| RETRIEVE | ~865 | ~1,531 | **43.5%** |
| COMPARE | ~1,050 | ~1,531 | **31.4%** |
| TRACE | ~1,100 | ~1,531 | **28.1%** |
| DEDUCE | ~1,200 | ~1,531 | **21.6%** |
| SYNTHESIZE | ~1,400 | ~1,531 | **8.6%** |
| WEIGH | ~1,531 | ~1,531 | **0%** |

Average savings: ~22%. Best case (RETRIEVE): 43.5%. These fell within the 25-47% range predicted by the reasoning router research.

**Key findings:**

- **RETRIEVE was the biggest efficiency win** -- 43.5% neuron savings and 94% token reduction for factual lookups. Simple lookups need the fewest neurons.
- **SUPPRESS was discovered to be a safety mechanism, not just an optimization.** Reality Context `REASONING_PROFILE` directives with `SUPPRESS` prevented harmful reasoning in domain-specific contexts. For example, in an HR/Legal context, suppressing TRACE prevented causal speculation about an employee's personal life (a liability risk).
- **Typed TRACE went deeper than untyped.** Untyped TRACE produced event-level descriptions ("firmware update"); typed TRACE produced mechanism-level root causes ("heartbeat timing mismatch"). Committing fully to the TRACE reasoning circuit produced qualitatively deeper analysis.
- **Style modifiers confirmed as genuinely orthogonal.** Changing the style on the same operation produced meaningfully different outputs; changing the operation with the same style activated different reasoning strategies. The two-axis model was architecturally sound.
- **The six operations composed naturally into pipelines:** RETRIEVE, COMPARE, WEIGH, DEDUCE, TRACE, SYNTHESIZE -- each operation's output feeding the next.

---

## 3. v0.8.1 -- Six Deduced Improvements

### What Changed

Six new features were added, each deduced from specific anomalies observed in v0.8.0 test data:

| Feature | Description |
|---|---|
| **DEPTH axis** | Four levels (SHALLOW / STANDARD / DEEP / EXHAUSTIVE) controlling compute investment independently of operation type and style |
| **EMIT_DIGEST** | Produces compressed summaries of operation outputs for pipeline consumption |
| **REASONING_CONTEXT** | Accumulator blocks that automatically wire digests between pipeline steps |
| **CONSTRAIN** | Graduated restriction (e.g., "TRACE only documented records") vs. binary SUPPRESS |
| **THEN chains** | Atomic compound operations (e.g., `RETRIEVE THEN DEDUCE`) with automatic RESULT propagation |
| **WITHOUT_RETRIEVAL** | Modifier that skips the retrieval neuron layer for pure-premise reasoning |

Additionally: `ADAPTIVELY` was reclassified as a dynamic routing modifier (not just a style), and explicit precedence rules were added for cases where auto-classification conflicts with `REALITY_CONTEXT`.

### Why Each Feature Was Needed

Each feature traced directly to a v0.8.0 test anomaly:

- **WEIGH had 0% neuron savings** -- analysis revealed that WEIGH subsumes RETRIEVE as a base layer (it retrieves before weighing). This meant retrieval was always activated even when unnecessary, leading to the `WITHOUT_RETRIEVAL` modifier.
- **SYNTHESIZE re-read all prior outputs** -- in pipeline scenarios, SYNTHESIZE re-parsed the full output of every prior step. This led to `EMIT_DIGEST` (compressed summaries) and `REASONING_CONTEXT` (automatic accumulation).
- **SUPPRESS was binary** -- it was on or off. In domains like law and medicine, a middle ground was needed: restrict reasoning to documented evidence without eliminating the reasoning type entirely. This led to `CONSTRAIN`.
- **No multi-operation chaining** -- sequential operations required manual variable wiring. This led to `THEN` chains with automatic `RESULT` propagation.
- **Untyped TRACE produced different depth than typed** -- the depth difference suggested depth was a controllable axis independent of type and style. This led to the `DEPTH` axis.
- **Auto-classification could conflict with REALITY_CONTEXT** -- when `INTELLIGENTLY` auto-classified an operation type but the active `REALITY_CONTEXT` had different `REASONING_PROFILE` settings, there was no rule for which took precedence. This led to explicit precedence rules.

### Test Results (Tests 05-09)

Five tests validated all six features:

**Test 05 -- WITHOUT_RETRIEVAL:**

| Metric | Standard DEDUCE | DEDUCE WITHOUT_RETRIEVAL | Delta |
|---|---|---|---|
| Neurons activated | ~1,200 | ~335 | **-72%** |
| Conclusion reached | termination_unlawful | termination_unlawful | Same |
| Inference steps | 6 | 6 | Same |
| External knowledge | 4 case law citations | Zero | Clean isolation |

The 72% neuron reduction was the largest single-feature efficiency gain in the entire AILang specification. An unexpected finding: the retrieval run added case law citations that *strengthened* the analysis but were not *necessary* for the conclusion, confirming that the retrieval layer is genuinely optional when premises are self-contained.

**Test 06 -- DEPTH axis:**

| Depth Level | Token Output | Root Cause Found |
|---|---|---|
| SHALLOW | ~75 | Phishing email (immediate trigger) |
| STANDARD | ~190 | Phishing + 5 enabling failures |
| DEEP | ~385 | Phishing + systemic weaknesses |
| EXHAUSTIVE | ~660 | Culture of security policy non-enforcement |

Token counts increased monotonically. All four depths converged on the same entry point, but EXHAUSTIVE identified a deeper organizational root cause ("systemic culture of security policy non-enforcement") that shallower passes missed entirely.

**Test 07 -- EMIT_DIGEST + REASONING_CONTEXT:**

A six-step pipeline (RETRIEVE, COMPARE, WEIGH, TRACE, DEDUCE, SYNTHESIZE) produced 2,680 tokens of full output compressed to 490 tokens of digests -- a 5.5:1 compression ratio. SYNTHESIZE consumed ~400 tokens of accumulated digests instead of ~2,120 tokens of full outputs, an **80% reduction** in input processing with zero critical information lost.

**Test 08 -- CONSTRAIN vs. SUPPRESS:**

In a medical malpractice scenario:

| Dimension | SUPPRESS TRACE | CONSTRAIN TRACE | Unrestricted TRACE |
|---|---|---|---|
| Causal links found | 0 | 5 (documented only) | 7 (mixed evidence) |
| Speculative claims | 0 | 0 | 4 hypotheses |

All three reached the same factual conclusion (standard of care breached) through fundamentally different reasoning paths. CONSTRAIN filled the gap essential for domains like law and medicine: documented causal chains without speculation.

**Test 09 -- THEN chaining:**

Two-step and three-step chains executed correctly with proper RESULT propagation. A three-step chain (RETRIEVE, WEIGH, SYNTHESIZE) demonstrated correct RESULT overwrite behavior at each step. THEN chains produced 36% fewer program statements compared to manual variable piping.

**Aggregate pipeline improvement:**

Applying all v0.8.1 features to a six-step analysis pipeline:

| Step | v0.8.0 Neurons | v0.8.1 Neurons | Savings |
|---|---|---|---|
| RETRIEVE | 865 | 865 | 0% (baseline) |
| COMPARE | 1,050 | 185 | **82%** |
| WEIGH | 1,531 | 666 | **57%** |
| TRACE | 1,100 | 235 | **79%** |
| DEDUCE | 1,200 | 335 | **72%** |
| SYNTHESIZE | 1,400 | 535 | **62%** |
| **Total** | **7,146** | **2,821** | **60.5%** |

Best-case savings jumped from 43.5% (v0.8.0) to 82% (COMPARE WITHOUT_RETRIEVAL). Aggregate pipeline savings went from 22% to 60.5%. Combined with the 80% SYNTHESIZE input reduction via the digest pipeline, the efficiency gains were substantial.

---

## 4. v0.8.2 -- Fine-Tuning

### What Changed

Three refinements based on v0.8.1 test data:

| Feature | Before (v0.8.1) | After (v0.8.2) |
|---|---|---|
| Retrieval control | Binary `WITHOUT_RETRIEVAL` (on/off) | Graduated `RETRIEVAL_BUDGET` with four levels: NONE / MINIMAL / STANDARD / FULL |
| Depth levels | 4 levels (SHALLOW / STANDARD / DEEP / EXHAUSTIVE) | 5 levels -- added **THOROUGH** between STANDARD and DEEP |
| Feature interactions | Informal, unspecified | Formal specification in **Appendix D** with 8 interaction rules |

### Why Each Change Was Needed

- **WITHOUT_RETRIEVAL was too coarse.** Binary on/off meant either full retrieval or none. In practice (e.g., international trade compliance), operations often need basic terminology resolution without full regulatory context injection. `RETRIEVAL_BUDGET` gives four graduated levels of retrieval control.
- **The gap between STANDARD and DEEP was too large.** STANDARD produced ~190 tokens and DEEP produced ~385 tokens, with a significant content gap between them. Many use cases needed the "second-order why" (contributing factors, secondary causes) without the full mechanism-level analysis of DEEP. `THOROUGH` fills this gap.
- **No specification of how features interact.** With six typed operations, four (now five) depth levels, graduated retrieval budgets, CONSTRAIN, THEN chains, REASONING_CONTEXT, and ADAPTIVELY all available simultaneously, compound usage needed formal interaction rules. Appendix D codified 8 rules covering combinations like ADAPTIVELY+DEPTH, RETRIEVAL_BUDGET+THEN, CONSTRAIN+REASONING_CONTEXT, and others.

### Test Results (Tests 10-12)

Three tests validated all three changes:

**Test 10 -- RETRIEVAL_BUDGET graduated control:**

Three runs of `DEDUCE tariff_applicability` (international trade compliance -- Canadian steel to US) with identical premises, differing only in RETRIEVAL_BUDGET:

| Metric | NONE | MINIMAL | STANDARD |
|---|---|---|---|
| Terminology gaps | 7 | 3 | 0 |
| External knowledge items | 0 | Basic definitions only | Full regulatory context |
| Confidence level | Low | Moderate | High |
| Conclusion | insufficient_information | partially_applicable | no_tariffs_exempt (0% duty) |
| Estimated neurons | ~335 | ~535 | ~1,200 |

Monotonic enrichment validated across all dimensions. The trade compliance scenario was particularly effective because it required precise terminology (LTFV, de minimis threshold, ad valorem duty rates) that NONE couldn't resolve, MINIMAL could define, and STANDARD could apply with real regulatory context.

**Test 11 -- DEPTH: THOROUGH (fifth depth level):**

All five depth levels applied to a hospital EHR outage TRACE:

| Depth | Est. Tokens | Key Content |
|---|---|---|
| SHALLOW | ~98 | Immediate trigger, 3-link chain |
| STANDARD | ~187 | Evidence at each step, 4 key failures |
| THOROUGH | ~365 | +5 contributing factors, +4 secondary causes |
| DEEP | ~548 | +mechanism-level detail, +4 systemic vulnerabilities |
| EXHAUSTIVE | ~892 | +3 distinct causal chains, +6 counterfactuals, +7 unexplored hypotheses |

Token counts and content depth both increased monotonically. THOROUGH correctly occupied the space between STANDARD and DEEP: it provided the "second-order why" (e.g., maintenance schedule hadn't been updated after clinic hours were extended, connection pools were sized for pre-expansion traffic) without the full mechanism-level analysis of DEEP. In practical terms, THOROUGH gives enough detail for a corrective action plan without the cost of a full multi-pass analysis.

**Test 12 -- Cross-feature interactions (8 dimensions):**

Three stress-test scenarios exercised all 8 interaction rules from Appendix D:

| Interaction Dimension | Tested In | Result |
|---|---|---|
| ADAPTIVELY + DEPTH adjustment range | Scenarios A, C | **PASS** |
| RETRIEVAL_BUDGET compliance | Scenarios A, B, C | **PASS** |
| REASONING_CONTEXT digest behavior | Scenarios B, C | **PASS** |
| CONSTRAIN enforcement | Scenarios A, B | **PASS** |
| SUPPRESS enforcement | Scenario A | **PASS** |
| THEN chain single digest | Scenario B | **PASS** |
| Person cognitive routing | Scenario C | **PASS** |
| Reality context precedence | Scenarios A, B | **PASS** |

Notable validations:
- ADAPTIVELY correctly adjusted depth within a one-level range above/below the base DEPTH setting (high-evidence steps got DEEP, low-evidence steps got STANDARD, when base was THOROUGH).
- THEN chains correctly produced exactly one digest from the final operation, not one per step.
- CONSTRAIN applied only to the specified operation type, not bleeding into other operations in the same pipeline.
- Person entity cognitive routing correctly used `PRIMARY_REASONING` and `SECONDARY_REASONING` from cognitive profiles.

---

## 5. Cumulative Impact

The following table summarizes the progression from v0.7.1 (baseline) through v0.8.2:

| Metric | v0.7.1 (Baseline) | v0.8.0 | v0.8.1 | v0.8.2 |
|---|---|---|---|---|
| **Reasoning differentiation** | Style only (4 modifiers) | 6 typed operations + style | + DEPTH axis, EMIT_DIGEST, CONSTRAIN, THEN chains, REASONING_CONTEXT | + RETRIEVAL_BUDGET graduated, THOROUGH depth, formal interaction spec |
| **Best-case neuron savings** | 0% | 43.5% | 82% | 82% (same ceiling, finer control) |
| **Practical pipeline savings** | 0% | 22% | 60.5% | 60.5%+ with graduated retrieval |
| **Depth control** | None | None | 4 levels | 5 levels (THOROUGH fills gap) |
| **Retrieval control** | None | None | Binary (on/off) | 4 levels (NONE / MINIMAL / STANDARD / FULL) |
| **Feature interaction spec** | N/A | N/A | Informal | Formal (Appendix D, 8 rules) |
| **Cross-feature validation** | N/A | N/A | N/A | 8 interaction dimensions tested |
| **Total tests executed** | -- | 4 (all pass) | 5 (all pass) | 3 (all pass) |

The trajectory across these three versions is clear: v0.8.0 proved that typed reasoning operations work and deliver measurable efficiency gains. v0.8.1 nearly tripled the pipeline savings (22% to 60.5%) by adding features deduced from v0.8.0's test anomalies. v0.8.2 replaced binary controls with graduated ones and formalized all feature interactions, completing the specification to the point where every feature combination has defined behavior and has been tested.

---

## 6. What Led to AIEX

The twelve tests across v0.8.0-v0.8.2 validated that AILang's features are well-specified and interact correctly. Every test passed. Neuron savings, depth control, retrieval budgets, constraint mechanisms, pipeline digest compression, and cross-feature interactions all behaved as the specification predicted.

This raised the natural next question: **how do you actually execute these programs?**

AILang specifies *what* reasoning to perform and *how* to constrain it, but a specification alone does not run programs. The test results themselves pointed toward the execution model. The v0.8.2 test summary explicitly recommended that RETRIEVE and COMPARE operations could be routed to BERT-class models instead of full generative LLMs, reducing cost by ~60% and latency by ~80% for lightweight operations while reserving larger models for complex reasoning.

This insight led to the **[AIEX (AI Execution) framework](https://github.com/pcoz/aiex)** -- a COBOL-inspired execution language that makes the theoretical neuron savings real through multi-model routing:

| AILang Operation | AIEX Execution Target | Rationale |
|---|---|---|
| RETRIEVE, COMPARE | BERT-class models | Lightweight operations that don't need generative capabilities |
| TRACE, DEDUCE | Sonnet-class models | Medium-complexity reasoning with good cost/quality balance |
| WEIGH, SYNTHESIZE | Opus-class models | Complex multi-factor reasoning requiring the largest models |

AIEX transforms AILang from a theoretical specification into an executable system where the typed reasoning operations map directly to concrete model routing decisions, and the neuron savings predicted by the reasoning router research become real cost and latency savings in production deployments.

---

*This document covers AILang's evolution through the v0.8.x series. For the full test results, see the test_results/SUMMARY.md files in each version's directory. For the reasoning router research that underpins the typed operation model, see [github.com/pcoz/llm-reasoning-router](https://github.com/pcoz/llm-reasoning-router).*
