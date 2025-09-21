# AILang

A natural language programming system designed for execution by AI systems.

## What is AILang?

AILang is a programming language that uses structured English instead of traditional programming syntax. Programs are written in controlled natural language that AI systems can directly interpret and execute without compilation.

## The Core Paradigm

Traditional programming translates human intent through artificial syntax, compilation, and machine code. AILang inverts this model by recognizing that modern AI systems can directly process human logical intent expressed in natural language.

AILang operates on a **hybrid architecture**:

* **Deterministic Layer**: Core operations (variables, control flow, I/O) execute identically every time, providing reliability.
* **Intelligent Layer**: Specific constructs delegate decision-making to AI intelligence, using deterministic data and program state as context.
* **Mathematical Layer**: Exact symbolic math and high-precision numerical methods for domains that require provable correctness and stable computation.

## How AILang Works

AILang uses a **Retrieval-Augmented Generation (RAG)** execution model: the complete language specification is attached to the AI system as a knowledge base. During execution, the AI retrieves exact behavioral definitions for each construct, enforcing consistency on deterministic operations while allowing bounded intelligence where explicitly permitted.

### Execution Environments

1. **AI Web Interface** — author and run programs interactively.
2. **API Integration** — submit AILang programs programmatically for system integration.

### RAG Integration Requirements (Summary)

* Load the **entire** specification into the AI’s retrieval system before execution.
* For each instruction, retrieve its definition and enforce consistency on deterministic constructs.
* Distinguish deterministic vs. intelligent operations and respect defined boundaries.

## Why AILang for Production

The spec’s RAG-backed rules turn AI from a creative but unpredictable system into a reliable computational processor operating within **known boundaries**—appropriate for production use.

## Language Highlights

* **Readable, dual-style syntax**: Controlled natural language (`SET`, `LET`, `GET`, `SEND`) plus familiar operators (`=`, `<<`, `>>`).

* **Data & State**: Dynamic typing; dot-notation property access; nested and dynamic keys; accumulation helpers (`ADD`, `INCREMENT`, `APPEND`).

* **Operators & Expressions**: Arithmetic, comparison, logical, and text operators with deterministic evaluation.

* **I/O with streams**: Deterministic input/output via `GET/SEND` and `<<`/`>>` with chainable streams.

* **Control Flow**: `IF/ELSE`, `WHILE`, `FOR EACH`, `REPEAT`, and `MATCH/CASE`.

* **Procedures & Functions**: `DO` blocks; `DEFINE PROCEDURE` and `CALL` with parameters/returns.

* **Object Management**: Object definition, instantiation, and dot-notation method access.

* **Intelligent Programming**:

  * Invoke AI with `INTELLIGENTLY`, `CREATIVELY`, `ADAPTIVELY`, `CONTEXTUALLY`.
  * Bound scope with `MUST_INCLUDE`, `CANNOT_INCLUDE`, `OUTPUT_FORMAT`, `MAX_SCOPE`.
  * Use gap-filling `...` and smart defaults to indicate where AI can adapt.

* **Confidence & Qualitative Spectrum**: Declare confidence levels; treat observable vs. interpretive assessments differently, with action authority tied to confidence.

* **Mathematical Layer**:

  * **Contexts**: `MATHEMATICAL_CONTEXT` for domain (`real|complex|quaternion|tensor`), precision, and constraints.
  * **Symbolic & Numeric**: Algebra, calculus (differentiate/integrate), sums/products, Fourier analysis, linear algebra, optimization.
  * **Complex Numbers & `i`**: Explicit domain rules and promotion; Euler/trig forms; residues and contour integration.
  * **Vectors/Tensors/Quaternions** and advanced applications across physics, signals, control, ML, and finance.
  * **Execution Guarantees**: Precision, stability, domain enforcement, verification.

* **State-Aware Boundaries & Safety**: Rate limits, progressive authorization, cascade prevention, and compositional limits to keep systems safe.

* **Error Handling**: Deterministic `TRY/CATCH/FINALLY` and `INTELLIGENTLY_HANDLE` for bounded recovery.

## Getting Started

1. **Attach the specification** (`AILang_Specification.md`) to your AI system’s knowledge base.
2. **Write your program** using the constructs above.
3. **Execute** via:

   * **AI Web Interface**: paste your program into a conversational session.
   * **API Integration**: submit programs via API.

During execution, deterministic rules are enforced; bounded intelligence is applied only where your code explicitly requests it.

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
MATCH doc.type WITH:
    CASE "invoice":
        PROCESS invoice_handler WITH doc
    CASE "letter":
        PROCESS letter_handler WITH doc
    DEFAULT:
        LOG "Unhandled document type"
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
  CONFIRM WITH user: "Proceed?" 
  WAIT for_confirmation BEFORE proceeding
END_IF
```

### Mathematical Context & Complex Numbers

```ailang
MATHEMATICAL_CONTEXT:
  DOMAIN: complex
  PRECISION: symbolic
END_CONTEXT

SET z TO 3 + 4*i
ASSERT |z| EQUALS 5
INTEGRATE f(x) = e^(i*x) FROM 0 TO pi WITH_RESPECT_TO x
```

## Worked Example

The repository includes practical examples demonstrating hybrid deterministic–intelligent capabilities. Provide the specification and the program to an AI system along with any required input documents.

* **Rent Increase Negotiation** (`examples/negotiate_rent_increase/`): Deterministically parses inputs and data; intelligently assesses fairness and crafts communication; adapts across negotiation loops; and handles errors within safety constraints.

## Repository Contents

* `AILang_Specification.md` — Complete language specification and usage guide
* `README.md` — This overview document
* `examples/` — Example AILang programs and supporting files

---

**Author**: Edward Chalk ([fleetingswallow.com](https://fleetingswallow.com))

**Version**: 0.3

**License**: MIT


