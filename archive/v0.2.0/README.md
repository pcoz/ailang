# AILang

A natural language programming system designed for execution by AI systems.

## What is AILang?

AILang is a programming language that uses structured English instead of traditional programming syntax. Programs are written in controlled natural language that AI systems can directly interpret and execute without compilation.

## The Core Paradigm

Traditional programming requires translating human intent through artificial syntax, compilation, and machine code execution. AILang inverts this model by recognizing that modern AI systems are sophisticated computational engines capable of directly processing human logical intent expressed in natural language.

AILang operates on a **hybrid deterministic–intelligent architecture**:

* **Deterministic Layer**: Core operations (variables, control flow, I/O) execute identically every time, providing reliability.
* **Intelligent Layer**: Specific constructs delegate decision-making to AI intelligence, using deterministic data as context.

This means programs can have both predictable computational behavior and intelligent adaptability where explicitly designed.

## How AILang Works

AILang uses a **Retrieval-Augmented Generation (RAG) execution model**. The complete language specification serves as a knowledge base that the AI system references during program execution. This ensures consistent interpretation of instructions while allowing intelligent decision-making within defined boundaries.

The AI retrieves exact behavioral definitions for each language construct, transforming from an unpredictable creative system into a reliable computational processor that follows precise rules while retaining intelligent adaptability where explicitly permitted.

## Production-Ready AI

The major advantage of AILang is that it enables AI to be used in production environments by constraining AI operations to **known boundaries**. Traditional AI systems are unpredictable and cannot be responsibly deployed in production because their outputs are random and unreliable.

AILang solves this through its RAG architecture: the AI retrieves exact behavioral definitions from the specification, ensuring deterministic operations behave consistently while allowing intelligent adaptation only where explicitly permitted. This transforms AI from an unpredictable creative system into a reliable computational processor that operates within defined constraints.

## Language Highlights

* **Readable, dual-style syntax**: Controlled natural language (`SET`, `LET`, `GET`, `SEND`) and familiar operators (`=`, `<<`, `>>`) for assignment and stream-based I/O.
* **Control flow & branching**: `IF/ELSE`, loops, and `MATCH/CASE` for multi-way pattern matching.
* **State & data**: Variables, dynamic property access, nested structures, and state accumulation.
* **Intelligent programming**:

  * Invoke AI with explicit modes such as `INTELLIGENTLY`, `CREATIVELY`, `ADAPTIVELY`, and `CONTEXTUALLY`.
  * Constrain scope and outputs with `MUST_INCLUDE`, `CANNOT_INCLUDE`, `OUTPUT_FORMAT`, `MAX_SCOPE`.
  * Use gap-filling (`...`) to indicate where AI should apply intelligence within deterministic scaffolding.
* **Safety & reliability**:

  * Confidence levels on intelligent actions (e.g., `high | moderate | low`) and qualitative distinctions between observable vs. interpretive assessments.
  * State-aware execution boundaries and cascade-prevention guards to stop runaway operations.
  * Progressive authorization that adjusts action authority based on observed success rates.
* **Error handling**:

  * Deterministic `TRY/CATCH/FINALLY` patterns.
  * `INTELLIGENTLY_HANDLE` for bounded, objective-driven recovery while preserving context.

## Getting Started

To understand how to write AILang programs, see `AILang_Specification.md`. The specification contains:

* Complete syntax and language constructs
* Data types and operators
* Control flow structures
* Input/output operations with stream operators
* Intelligent programming constructs and confidence levels
* State-aware dynamic boundaries and safety controls
* Detailed examples and use cases
* Implementation guidelines for AI systems

## How You Use AILang

1. **Attach the specification**: Provide `AILang_Specification.md` to your AI system as a knowledge base.
2. **Write your program**: Author AILang code using the syntax and constructs defined in the spec.
3. **Execute** via either:

   * **AI Web Interface**: Paste your AILang program into conversational AI (e.g., ChatGPT, Claude).
   * **API Integration**: Submit AILang programs programmatically through API calls.

During execution, the AI follows deterministic rules for core operations and applies bounded intelligence only where your code explicitly requests it.

## Code Examples

### Variables & Stream I/O

```ailang
# Assignment styles
SET username TO "Alice"
LET age BE 25
email = "alice@example.com"

# Stream I/O
user_input << console
processed_data >> "output.txt"
```

### Pattern Matching

```ailang
MATCH doc.type:
  CASE "invoice":   PROCESS invoice_handler WITH doc
  CASE "letter":    PROCESS letter_handler WITH doc
  CASE "unknown":   LOG "Unhandled document type"
END_MATCH
```

### Intelligent Operations with Boundaries

```ailang
INTELLIGENTLY draft_reply WITH:
  MUST_INCLUDE: [greeting, solution, next_steps]
  CANNOT_INCLUDE: [personal_opinions, guarantees]
  OUTPUT_FORMAT: professional_email
  MAX_SCOPE: current_issue_only
END
```

### Confidence-Based Execution

```ailang
INTELLIGENTLY assess_risk WITH:
  OUTPUT: risk_level
  CONFIDENCE_LEVEL: [high|moderate|low]
END

IF confidence_level < high THEN:
  CONFIRM WITH user BEFORE proceeding
END_IF
```

### State-Aware Limits

```ailang
SET daily_limit TO 100
SET current_count TO 0

FOR each request IN queue:
  IF current_count >= daily_limit THEN:
    DEFER request TO tomorrow
  ELSE:
    PROCESS request
    INCREMENT current_count BY 1
  END_IF
END_FOR
```

## Worked Example

This repository includes practical examples demonstrating AILang's hybrid deterministic–intelligent capabilities. Provide the specification and the program to an AI system along with any required input documents.

* **Rent Increase Negotiation** (`examples/negotiate_rent_increase/`): Demonstrates a full workflow that

  * Deterministically retrieves tenant details, parses notices, and gathers market/inflation data.
  * Intelligently assesses fairness, affordability, and negotiation leverage.
  * Adaptively generates counter-offer emails and reports, with conditional loops for ongoing negotiations.
  * Handles errors intelligently while maintaining privacy and legal compliance.

  The example folder includes:

  * `negotiate_rent_increase.ailang`
  * Inputs: `landlord_email.pdf`, `tenant_details.json`, `local_rent_data.json`, `cost_of_living_index.json`, `tenant_rights_laws.md`
  * Outputs (generated): `counteroffer_email_to_landlord.txt`, `negotiation_report.json`

## Repository Contents

* `AILang_Specification.md` — Complete language specification and usage guide
* `README.md` — This overview document
* `examples/` — Example AILang programs and supporting files

---

**Author**: Edward Chalk ([fleetingswallow.com](https://fleetingswallow.com))
**Version**: 0.2
**License**: MIT
