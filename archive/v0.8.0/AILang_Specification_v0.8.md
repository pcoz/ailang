**AILang: Complete Language Specification**

**Version 0.8.0**

**Author**: Edward Chalk (fleetingswallow.com)

---

## Introduction

AILang is a natural language programming system designed for execution by AI systems. It allows users to write computational logic using structured English that AI can reliably interpret and execute. AILang programs are written in controlled natural language that balances human readability with computational precision. Unlike traditional programming languages, AILang is executed directly by AI systems using this specification as a reference guide.

AILang serves as both a production language for AI-executed programs and a rapid prototyping tool that can later be converted to traditional programming languages when needed.

### What's New in v0.8.0

Version 0.8.0 integrates insights from the [LLM Reasoning Router](https://github.com/pcoz/llm-reasoning-router) project, which demonstrated that different reasoning types activate fundamentally different neuron populations in large language models (25-75% non-overlap between types). The previous specification treated intelligent operations as a monolithic capability with stylistic modifiers (INTELLIGENTLY, CREATIVELY, ADAPTIVELY, CONTEXTUALLY) that did not map to actual computational differences inside the AI engine. Version 0.8.0 makes reasoning operation type a first-class language construct.

**Key changes from v0.7.1:**

1. **Reasoning Operations** — Six typed reasoning verbs (WEIGH, DEDUCE, TRACE, COMPARE, SYNTHESIZE, RETRIEVE) replace undifferentiated INTELLIGENTLY as the primary axis for intelligent operations
2. **Style Modifiers** — CREATIVELY, ADAPTIVELY, CONTEXTUALLY become an orthogonal secondary axis that can modify any reasoning operation
3. **Auto-Classification** — When INTELLIGENTLY is used as a fallback, the engine auto-classifies the appropriate reasoning type using linguistic pattern matching
4. **Reasoning Routing Architecture** — A new section explains the neuron-level basis for the reasoning type taxonomy and the performance benefits of typed operations
5. **REASONING_PROFILE in Reality Contexts** — Reality contexts can now specify primary, secondary, and suppressed reasoning types
6. **Workflow Patterns** — ASSESS/EXPLORE/DECIDE reframed as composable workflow patterns that use typed reasoning operations
7. **Extension framework updates** — Person entities and Matter entities gain reasoning-type-aware interfaces

---

## Technical Foundation and Architecture

### The AI as a CPU

Traditional programs operate on a rigid hierarchy: human intent must be translated through programming languages, compiled into machine code, and executed by silicon processors that understand only binary operations. AILang inverts this model entirely by recognizing that modern AI systems are themselves sophisticated computational engines capable of directly processing human logical intent.

The breakthrough insight is that we don't need to translate these operations into an artificial syntax—the AI can process them directly in the language humans naturally use to describe logical procedures.

### Execution Environment

AILang programs can be executed in two primary ways:

1. **AI Web Interface**: Programs can be written and executed directly through conversational AI interfaces, where users provide AILang code as part of their interaction

2. **API Integration**: AILang programs can be submitted via API calls to AI systems, enabling programmatic execution and integration into larger software systems


### The RAG-Powered Solution

A pivotal challenge with AI systems is their inherent randomness—they cannot be responsibly deployed in production environments because their outputs are unpredictable, making it impossible to guarantee they will act within expected boundaries. AILang solves this fundamental problem through its RAG (Retrieval-Augmented Generation) architecture.

The complete AILang specification is attached to the AI system as a knowledge base. When executing programs, the AI retrieves the exact behavioral definitions from this specification, ensuring consistent interpretation of instructions. This transforms AI from an unpredictable creative system into a reliable computational processor that follows precise rules while retaining intelligent adaptability where explicitly permitted.

### Advantages Over Traditional Approaches

AILang represents a significant advance over existing approaches:

* **Versus Pseudocode**: While pseudocode describes algorithms in natural language, it is not designed to be executed and requires manual translation to working code. AILang executes directly, eliminating translation errors and enabling immediate testing and iteration.

* **Versus Traditional Programming**: Conventional languages require learning artificial syntax and compilation steps. AILang uses natural language constructs that anyone can understand and write.

* **Versus Unstructured AI Prompts**: Raw AI prompts produce unpredictable outputs. AILang provides structured frameworks that ensure consistent behavior while preserving AI intelligence where appropriate.

### Three Execution Modes

AILang programs operate across three distinct execution modes, each with different guarantees and appropriate use cases:

**1. INTELLIGENT Operations**
- Executed by AI reasoning and interpretation
- Contextual, adaptive, creative decision-making
- Non-deterministic by design
- v0.8 enhancement: Operations are now typed by reasoning type (WEIGH, DEDUCE, TRACE, COMPARE, SYNTHESIZE, RETRIEVE) enabling targeted neural activation
- Appropriate for: ambiguous situations, creative tasks, strategic decisions, natural language processing

**2. DETERMINISTIC Operations** (Pseudo-Deterministic)
- Interpreted by AI following strict structural rules
- High consistency but not absolute determinism due to natural language interpretation
- Appropriate for: control flow, state management, I/O operations, structured logic
- Note: These operations are more accurately "highly structured AI interpretations" rather than truly guaranteed computation

**3. CODE Blocks**
- Executed as actual programming language code via interpreter
- Genuinely deterministic (same code + inputs = same outputs)
- Appropriate for: mathematical operations, algorithmic computation, data processing, performance-critical operations

The power of AILang lies in seamlessly combining these three modes, using each where it provides maximum value.

---

## Core Language Constructs

### 1. Data Types and Type System

AILang uses dynamic typing with intelligent type coercion for compatible types. The AI automatically handles conversions between compatible types (TEXT, NUMBER, BOOLEAN) when context makes intent clear. QUALITATIVE types maintain semantic meaning and do not coerce to numeric values.

#### Fundamental Data Types

* **TEXT**: String values (examples: `"hello"`, `"user@example.com"`)

* **NUMBER**: Numeric values (examples: `42`, `3.14`, `-17`)

* **BOOLEAN**: True/false values (examples: `true`, `false`, `yes`, `no`)

* **QUALITATIVE**: Opaque semantic labels for qualitative states (e.g., "tense_meeting", "supportive_tone", "fragile_morale").
  - **Interpretation:** Engines interpret QUALITATIVE values within INTELLIGENT operations and/or an active REALITY_CONTEXT. They are not numeric and carry no inherent scalar.
  - **Coercion:** No implicit coercion to NUMBER or BOOLEAN. Engines MAY stringify a QUALITATIVE value when a TEXT is explicitly required (e.g., logging, messages).
  - **Operations:** Equality/inequality comparisons are defined; ordering comparisons are undefined. Rich interpretation occurs via INTELLIGENT logic and the Qualitative Spectrum.
  - **Serialization:** Represent as TEXT with optional metadata tag `@qual` in environments that support typed metadata.

* **LIST**: Ordered collections (example: `[item1, item2, item3]`)

* **OBJECT**: Structured containers with properties and methods

* **NULL**: Empty or undefined values

The AI may intelligently convert between compatible types when context suggests it's appropriate, such as converting `"true"` to boolean `true` or `"42"` to numeric `42`.

#### Type Constraint Grammar

AILang supports lightweight type constraints in structured schemas (e.g., OUTPUT_FORMAT) and declarations:

**Enum (set) constraint**
`<Type> IN ["lit1","lit2", ...]`
Example: `QUALITATIVE IN ["supportive","neutral","hostile"]`

**Parametric list**
`LIST OF <Type>`
Example: `LIST OF QUALITATIVE`, `LIST OF TEXT`

**Typed object fields**
`OBJECT { field1: <Type>, field2: <Constraint>, ... }`

**Validation:** Engines SHOULD validate these constraints deterministically when constructing or emitting such structures (e.g., populating `OUTPUT_FORMAT`).

**Examples:**

```ailang
# Constrained qualitative enum
OUTPUT_FORMAT: {
  mood: QUALITATIVE IN ["tense","neutral","relaxed"],
  confidence: TEXT IN ["high","moderate","low"]
}

# Typed list
OUTPUT_FORMAT: {
  tags: LIST OF QUALITATIVE,
  scores: LIST OF NUMBER
}

# Typed object structure
OUTPUT_FORMAT: OBJECT {
  state: QUALITATIVE IN ["stable","strained","critical"],
  metrics: OBJECT {
    count: NUMBER,
    notes: LIST OF TEXT
  }
}
```

### 2. Variable Operations

Variables store and manipulate data throughout program execution. They maintain their values across the program scope unless explicitly reassigned.

#### Assignment Syntax

Variables can be assigned using natural language patterns or traditional programming syntax:

```ailang
SET [variable] TO [value]
LET [variable] BE [value]

[variable] = [value]
```

All three forms are equivalent and can be used interchangeably based on preference or context. The `=` operator provides familiarity for those coming from traditional programming backgrounds.

**Examples:**

```ailang
SET customer_count TO 0
LET total_amount BE 1500.00
username = "Alice"
is_active = true

calculation_result = (price * quantity) + tax
```

#### Property Access

Object properties and nested values use dot notation:

```ailang
SET user_profile.name TO "Alice Smith"
user_profile.email = "alice@example.com"
SET customer_count TO 0
LET total_amount BE 1500.00

config.settings.timeout = 30
```

#### Complex State Management

AILang supports complex state operations with nested structures:

```ailang
# Nested property access
SET user.preferences.notifications.email TO true
GET value FROM deeply.nested.object.property

# Dynamic property access
SET property_name TO "status"
SET object.[property_name] TO "active"  # Dynamic key access

# State accumulation
ADD item TO collection
INCREMENT counter BY 1

APPEND log_entry TO audit_trail
```

**Specification**: Variables are dynamically typed and maintain their values throughout program scope. Property access follows standard dot notation rules for nested structures. The assignment operator `=` can be used with all variable types and in all contexts where `SET` or `LET` would be valid. Complex state operations maintain deterministic behavior while supporting nested and dynamic access patterns.

### 3. Operators and Expressions

All operators follow deterministic evaluation rules and return predictable results.

#### Arithmetic Operators

Mathematical operations on numeric values:

* **Addition:** `[value1] + [value2]` or `[value1] PLUS [value2]`
* **Subtraction:** `[value1] - [value2]` or `[value1] MINUS [value2]`
* **Multiplication:** `[value1] * [value2]` or `[value1] TIMES [value2]`
* **Division:** `[value1] / [value2]` or `[value1] DIVIDED BY [value2]`
* **Remainder:** `[value1] % [value2]` or `[value1] MODULO [value2]`
* **Exponentiation:** `[value1] ^ [power]` or `[value1] TO THE POWER OF [power]`

#### Comparison Operators

All comparisons return boolean values (true/false):

**Equality Testing:**

* `[value1] EQUALS [value2]` or `[value1] == [value2]`
* `[value1] NOT EQUALS [value2]` or `[value1] != [value2]`

**Numeric Comparisons:**

* `[value1] GREATER THAN [value2]` or `[value1] > [value2]`
* `[value1] LESS THAN [value2]` or `[value1] < [value2]`
* `[value1] GREATER THAN OR EQUAL TO [value2]` or `[value1] >= [value2]`
* `[value1] LESS THAN OR EQUAL TO [value2]` or `[value1] <= [value2]`

#### QUALITATIVE Type Operations

**Equality Operations:**
`[q1] EQUALS [q2]` and `[q1] != [q2]` are defined for QUALITATIVE values (label-based equality).

**Ordering Operations:**
Ordering operators (`>`, `<`, `>=`, `<=`) are **undefined** for QUALITATIVE values. To establish ordering, define an explicit mapping function.

**String Conversion:**
QUALITATIVE values MAY be converted to TEXT for display or logging purposes, but retain their semantic type for operations.

**Examples:**

```ailang
SET mood1 TO "tense"
SET mood2 TO "tense"
SET mood3 TO "relaxed"

IF mood1 EQUALS mood2 THEN:  # Valid - true
  LOG "Moods match"
END_IF

IF mood1 != mood3 THEN:  # Valid - true
  LOG "Different moods"
END_IF

# INVALID - will produce error:
# IF mood1 > mood3 THEN:  # Error: ordering not defined
```

#### Logical Operators

Boolean logic operations for combining conditions:

* `[condition1] AND [condition2]` - Both conditions must be true
* `[condition1] OR [condition2]` - At least one condition must be true
* `NOT [condition]` - Inverts the boolean value

#### Text Operators

String manipulation and testing:

* `CONTAINS` - Checks if text contains a substring
* `STARTS WITH` - Checks if text begins with a substring
* `ENDS WITH` - Checks if text concludes with a substring
* `CONCATENATE` or `[text1] + [text2]` - Joins text strings
* `LENGTH OF [text]` - Returns the number of characters
* `SUBSTRING OF [text] FROM [start] TO [end]` - Extracts portion of text

### 4. Input/Output Operations

I/O operations provide deterministic data flow between the program and external systems.

#### Input Operations

**Purpose**: Acquire data from specified sources. **Syntax Options**:

```ailang
GET [variable] FROM [source]
[variable] << [source]    # stream operator syntax
```

The AI must retrieve data from the specified source and assign it to the variable. If the source is inaccessible, an input error is thrown.

**Examples:**

```ailang
GET user_name FROM user_input
GET weather_data FROM "weather_api.com/current"
GET file_contents FROM "document.txt"
GET current_time FROM system_clock

# Equivalent using stream operators:
user_name << user_input
weather_data << "weather_api.com/current"
file_contents << "document.txt"
current_time << system_clock
```

#### Output Operations

**Purpose**: Send data to specified destinations. **Syntax Options**:

```ailang
SEND [data] TO [destination]
[data] >> [destination]   # stream operator syntax
```

The AI must transmit the data to the specified destination. If transmission fails, an output error is thrown.

**Examples:**

```ailang
SEND greeting_message TO user_display
SEND analysis_results TO "report.txt"
SEND notification TO email_system

# Equivalent using stream operators:
greeting_message >> user_display
analysis_results >> "report.txt"
notification >> email_system
```

#### Stream Operator Chaining

The stream operators can be chained for sequential operations:

```ailang
# Input chaining: process data as it flows
raw_data << "input.csv"
processed_data << PROCESS(raw_data)

# Output chaining: send to multiple destinations
report >> "local_file.txt"
report >> email_system
report >> backup_storage
```

### 5. Control Flow Structures

Control flow determines the execution path through the program. All control structures follow deterministic branching rules.

#### Conditional Execution (`IF` Statements)

Conditionals evaluate boolean expressions and execute corresponding code blocks:

```ailang
IF [condition] THEN:
    [instructions]
ELSE IF [condition] THEN:
    [instructions]
ELSE:
    [instructions]
END_IF
```

**Specification**: Conditions are evaluated sequentially. The first branch with a true condition executes. If no conditions are true, the `ELSE` branch executes if present.

#### Loop Structures

##### `WHILE` Loops

Execute instructions repeatedly while a condition remains true:

```ailang
WHILE [condition] DO:
    [instructions]
END_WHILE
```

**Specification**: The condition is checked before each iteration. The loop continues while the condition evaluates to `true`.

##### `FOR` Loops

Iterate through collections, binding each element to a variable:

```ailang
FOR EACH [item] IN [collection] DO:
    [instructions]
END_FOR
```

**Specification**: Each element in the collection is processed sequentially, with the current element bound to the `item` variable.

##### `REPEAT` Loops

Execute instructions a specific number of times:

```ailang
REPEAT [number] TIMES:
    [instructions]
END_REPEAT
```

#### Pattern Matching

Match values against multiple patterns with structured case handling:

```ailang
MATCH [value] WITH:
    CASE [pattern1]:
        [instructions]
    CASE [pattern2]:
        [instructions]
    DEFAULT:
        [instructions]
END_MATCH
```

**Pattern Matching with QUALITATIVE:**

QUALITATIVE values can be matched using label equality:

```ailang
SET customer_mood TO "frustrated"

MATCH customer_mood WITH:
  CASE "angry":
    SET response_urgency TO "immediate"
  CASE "frustrated":
    SET response_urgency TO "high"
  CASE "neutral":
    SET response_urgency TO "standard"
  CASE "satisfied":
    SET response_urgency TO "low"
  DEFAULT:
    SET response_urgency TO "standard"
END_MATCH
```

For families of labels, use set membership:

```ailang
SET mood TO "frustrated"
SET negative_moods TO ["angry", "frustrated", "disappointed"]

IF mood IN negative_moods THEN:
  ESCALATE support_request
END_IF
```

### 6. Procedures and Functions

Procedures encapsulate reusable logic with parameters and return values.

#### Basic Operation Blocks

Simple operation blocks for organizing code:

```ailang
DO [operation_name]:
    [instructions]
END
```

Operations with parameters and return values:

```ailang
DO [operation_name] WITH [parameters]:
    [instructions]
    RETURN [value]
END
```

#### Function Definition and Calling

Define reusable procedures with formal parameters:

```ailang
DEFINE PROCEDURE [name] WITH PARAMETERS [param1, param2]:
    [instructions]
    RETURN [value]
END_PROCEDURE
```

```ailang
CALL [procedure_name] WITH [arguments]
```

#### Procedures with QUALITATIVE Parameters and Returns

Procedures MAY accept and return QUALITATIVE values. See (QUALITATIVE type) and (interface patterns) for correct handling and bridging to CODE.

```ailang
DEFINE PROCEDURE assess_response_strategy WITH PARAMETERS [mood: QUALITATIVE]:
  MATCH mood WITH:
    CASE "tense":
      RETURN "de-escalate_and_validate"
    CASE "neutral":
      RETURN "proceed_normally"
    CASE "relaxed":
      RETURN "compress_timeline"
    DEFAULT:
      RETURN "seek_clarification"
  END_MATCH
END_PROCEDURE

# Usage
SET customer_state TO "tense"
SET strategy TO assess_response_strategy(customer_state)
```

### 7. Object Management

Objects provide structured data containers with properties and methods.

#### Object Creation

Define objects with properties and methods:

```ailang
CREATE OBJECT [name]:
    [property]: [value]
    [property]: [value]

    METHOD [method_name]:
        [instructions]
    END_METHOD
END_OBJECT
```

#### Object Instantiation and Access

Create instances and access properties:

```ailang
SET [variable] TO NEW [object_name]
```

Property and method access uses dot notation:

* `[object].[property]` - Access property value
* `[object].[method]([parameters])` - Call object method

**Specification**: Objects follow deterministic structure rules for property access and method invocation, while property values may be intelligently determined based on context.

---

### 8. Reasoning Operations

AILang v0.8 introduces typed reasoning operations as first-class language constructs. This section replaces undifferentiated INTELLIGENTLY as the primary axis for intelligent operations.

#### 8.1 Neuroscientific Basis

Research from the LLM Reasoning Router project demonstrates that different reasoning types activate fundamentally different neuron populations within large language models:

- Different reasoning types activate 25-75% different neuron populations in LLM feed-forward network layers
- **RETRIEVE** uses approximately 865 consistently activated neurons; **WEIGH** uses approximately 1,531
- Jaccard similarity between WEIGH and RETRIEVE neuron populations is only 52.8%
- Most divergent pairs: SYNTHESIZE vs DEDUCE (approximately 25% overlap), TRACE vs RETRIEVE (approximately 25% overlap)
- This means typed operations can skip 25-47% of FFN compute by routing to the appropriate neuron subpopulation
- Conservative performance estimate: 25-47% reduction per intelligent operation when routing is applied

This finding invalidates the v0.7.1 approach of treating all intelligent operations as a single capability with stylistic differences. The reasoning types defined below correspond to genuinely distinct computational pathways in the AI engine. Specifying the correct type allows the engine to activate the relevant neuron populations directly rather than inferring the reasoning type from context.

#### 8.2 The Six Reasoning Operations

Each reasoning operation verb maps to a distinct pattern of neural activation. All six accept the same bounded intelligence constraints (MUST_INCLUDE, CANNOT_INCLUDE, OUTPUT_FORMAT, MAX_SCOPE) that INTELLIGENTLY used in v0.7.1.

##### `WEIGH`

**Purpose:** Evaluate competing claims by source credibility, authority, and evidence quality.

**Maps to:** Authority-evaluation neurons (approximately 1,531 consistent neurons).

**When to use:** When multiple sources provide conflicting information and the program must determine which source to trust, or when evidence must be evaluated for reliability.

**Syntax:**

```ailang
WEIGH [subject] ON [dimension] WITH:
    SOURCES: [list_of_sources]
    MUST_INCLUDE: [required_elements]
    CANNOT_INCLUDE: [forbidden_elements]
    OUTPUT_FORMAT: [structured_requirement]
    MAX_SCOPE: [boundary_definition]
END
```

**Example:**

```ailang
WEIGH expert_opinions ON treatment_efficacy WITH:
    SOURCES: [clinical_trial_data, physician_recommendation, patient_anecdote]
    MUST_INCLUDE: [credibility_assessment, conflict_of_interest_check]
    OUTPUT_FORMAT: {
        recommendation: TEXT,
        dominant_source: TEXT,
        confidence_level: QUALITATIVE IN ["high", "moderate", "low"]
    }
END
```

**Example — authority evaluation:**

```ailang
WEIGH contradictory_claims ON vaccine_safety WITH:
    SOURCES: [peer_reviewed_meta_analysis, social_media_influencer, WHO_guidance]
    MUST_INCLUDE: [source_credibility_ranking, evidence_hierarchy_position]
    CANNOT_INCLUDE: [ad_hominem_dismissals]
    OUTPUT_FORMAT: {
        strongest_claim: TEXT,
        credibility_ranking: LIST OF OBJECT { source: TEXT, credibility: QUALITATIVE },
        consensus_direction: TEXT,
        confidence_level: TEXT IN ["high", "moderate", "low"]
    }
    MAX_SCOPE: published_evidence_only
END
```

##### `DEDUCE`

**Purpose:** Derive conclusions from premises via logical rules (deductive, inductive, or abductive reasoning).

**Maps to:** Logical-inference neurons.

**When to use:** When the program has explicit premises and needs to determine what logically follows, when evaluating the validity of an argument, or when applying rules to specific cases.

**Syntax:**

```ailang
DEDUCE [conclusion] FROM [premises] WITH:
    MUST_INCLUDE: [required_elements]
    CANNOT_INCLUDE: [forbidden_elements]
    OUTPUT_FORMAT: [structured_requirement]
    MAX_SCOPE: [boundary_definition]
END
```

**Example:**

```ailang
DEDUCE contract_breach FROM contract_terms AND observed_behavior WITH:
    MUST_INCLUDE: [violated_clauses, logical_chain]
    CANNOT_INCLUDE: [speculation_beyond_evidence]
    OUTPUT_FORMAT: {
        breach_found: BOOLEAN,
        violated_clauses: LIST OF TEXT,
        logical_chain: LIST OF TEXT,
        strength_of_conclusion: TEXT IN ["certain", "probable", "possible", "unlikely"]
    }
END
```

**Example — syllogistic reasoning:**

```ailang
DEDUCE classification FROM biological_facts WITH:
    MUST_INCLUDE: [premises_used, inference_steps]
    OUTPUT_FORMAT: {
        conclusion: TEXT,
        premises: LIST OF TEXT,
        inference_type: TEXT IN ["deductive", "inductive", "abductive"],
        validity: BOOLEAN
    }
    MAX_SCOPE: provided_premises_only
END
```

##### `TRACE`

**Purpose:** Follow cause-effect chains forward (cause to effect) or backward (effect to cause).

**Maps to:** Causal-reasoning neurons.

**When to use:** When the program needs to understand what caused something (root cause analysis), predict consequences of an action, or map a chain of events.

**Supports:** `DIRECTION: FORWARD|BACKWARD` parameter to specify causal direction.

**Syntax:**

```ailang
TRACE [target] FROM [starting_point] WITH:
    DIRECTION: FORWARD|BACKWARD
    MUST_INCLUDE: [required_elements]
    CANNOT_INCLUDE: [forbidden_elements]
    OUTPUT_FORMAT: [structured_requirement]
    MAX_SCOPE: [boundary_definition]
END
```

**Example — backward (root cause):**

```ailang
TRACE root_cause FROM incident_timeline WITH:
    DIRECTION: BACKWARD
    MAX_SCOPE: "last_72_hours"
    MUST_INCLUDE: [evidence_at_each_step, alternative_explanations_considered]
    OUTPUT_FORMAT: {
        causal_chain: LIST OF OBJECT { event: TEXT, caused_by: TEXT, evidence: TEXT },
        root_cause: TEXT,
        contributing_factors: LIST OF TEXT,
        confidence_level: TEXT IN ["high", "moderate", "low"]
    }
END
```

**Example — forward (consequence prediction):**

```ailang
TRACE market_impact FROM interest_rate_change WITH:
    DIRECTION: FORWARD
    MUST_INCLUDE: [transmission_mechanism, time_horizons]
    CANNOT_INCLUDE: [speculative_second_order_effects_beyond_6_months]
    OUTPUT_FORMAT: {
        primary_effects: LIST OF TEXT,
        secondary_effects: LIST OF TEXT,
        estimated_timeline: TEXT,
        causal_chain: LIST OF TEXT
    }
    MAX_SCOPE: domestic_economy
END
```

##### `COMPARE`

**Purpose:** Establish relative ordering, ranking, or trade-off analysis across specified dimensions.

**Maps to:** Ordering neurons.

**When to use:** When the program needs to rank options, compare alternatives on multiple dimensions, or identify trade-offs between choices.

**Syntax:**

```ailang
COMPARE [subjects] AGAINST [criteria] WITH:
    DIMENSIONS: [list_of_dimensions]
    MUST_INCLUDE: [required_elements]
    CANNOT_INCLUDE: [forbidden_elements]
    OUTPUT_FORMAT: [structured_requirement]
    MAX_SCOPE: [boundary_definition]
END
```

**Example:**

```ailang
COMPARE vendor_proposals AGAINST evaluation_criteria WITH:
    DIMENSIONS: [cost, capability, risk, timeline]
    MUST_INCLUDE: [dimension_by_dimension_analysis, trade_off_identification]
    CANNOT_INCLUDE: [vendor_favoritism, undisclosed_weighting]
    OUTPUT_FORMAT: {
        ranking: LIST OF OBJECT { vendor: TEXT, rank: NUMBER, rationale: TEXT },
        trade_off_analysis: TEXT,
        recommended_choice: TEXT,
        confidence_level: TEXT IN ["high", "moderate", "low"]
    }
END
```

**Example — multi-attribute decision:**

```ailang
COMPARE programming_languages AGAINST project_requirements WITH:
    DIMENSIONS: [performance, ecosystem_maturity, team_familiarity, hiring_pool, maintenance_cost]
    MUST_INCLUDE: [scoring_rationale_per_dimension]
    OUTPUT_FORMAT: {
        comparison_matrix: LIST OF OBJECT {
            language: TEXT,
            scores: OBJECT { performance: QUALITATIVE, ecosystem: QUALITATIVE,
                             familiarity: QUALITATIVE, hiring: QUALITATIVE, maintenance: QUALITATIVE }
        },
        overall_ranking: LIST OF TEXT,
        key_trade_offs: LIST OF TEXT
    }
    MAX_SCOPE: shortlisted_languages_only
END
```

##### `SYNTHESIZE`

**Purpose:** Aggregate multiple perspectives, sources, or data streams into a unified view, identifying areas of consensus and tension.

**Maps to:** Consensus-building neurons.

**When to use:** When the program must integrate multiple viewpoints into a coherent summary, find common ground among stakeholders, or produce a balanced analysis from diverse inputs.

**Note:** Named SYNTHESIZE rather than CONSENSUS because the operation is broader than vote-counting — it includes identifying tensions, finding common themes, and producing integrated views.

**Syntax:**

```ailang
SYNTHESIZE [sources] INTO [output] WITH:
    SOURCES: [list_of_source_perspectives]
    MUST_INCLUDE: [required_elements]
    CANNOT_INCLUDE: [forbidden_elements]
    OUTPUT_FORMAT: [structured_requirement]
    MAX_SCOPE: [boundary_definition]
END
```

**Example:**

```ailang
SYNTHESIZE stakeholder_positions INTO recommendation WITH:
    SOURCES: [engineering_team, product_team, executive_sponsor]
    MUST_INCLUDE: [areas_of_agreement, unresolved_tensions, minority_views]
    CANNOT_INCLUDE: [fabricated_consensus, suppressed_disagreements]
    OUTPUT_FORMAT: {
        unified_view: TEXT,
        consensus_points: LIST OF TEXT,
        tension_points: LIST OF OBJECT { issue: TEXT, positions: LIST OF TEXT },
        recommended_path: TEXT
    }
END
```

**Example — literature review:**

```ailang
SYNTHESIZE research_findings INTO state_of_knowledge WITH:
    SOURCES: [study_group_A, study_group_B, meta_analysis_C, dissenting_paper_D]
    MUST_INCLUDE: [methodological_comparison, effect_size_consistency, publication_bias_assessment]
    OUTPUT_FORMAT: {
        consensus_findings: LIST OF TEXT,
        contested_findings: LIST OF OBJECT { finding: TEXT, for_evidence: TEXT, against_evidence: TEXT },
        gaps_in_knowledge: LIST OF TEXT,
        overall_confidence: TEXT IN ["strong", "moderate", "weak", "insufficient"]
    }
    MAX_SCOPE: peer_reviewed_literature_post_2015
END
```

##### `RETRIEVE`

**Purpose:** Direct knowledge lookup with minimal reasoning transformation.

**Maps to:** Minimal neuron activation (approximately 865 consistent neurons — the lowest activation footprint of all reasoning types).

**When to use:** When the program needs factual recall, definition lookup, or straightforward data retrieval that does not require deep inference or evaluation.

**Note:** Named RETRIEVE rather than LOOKUP because it fits AILang's natural language style better while conveying the same semantics.

**Syntax:**

```ailang
RETRIEVE [information] FOR [context] WITH:
    DOMAIN: [knowledge_domain]
    MUST_INCLUDE: [required_elements]
    CANNOT_INCLUDE: [forbidden_elements]
    OUTPUT_FORMAT: [structured_requirement]
    MAX_SCOPE: [boundary_definition]
END
```

**Example:**

```ailang
RETRIEVE compliance_requirements FOR jurisdiction WITH:
    DOMAIN: "GDPR"
    MUST_INCLUDE: [specific_articles, applicability_conditions]
    OUTPUT_FORMAT: {
        requirements: LIST OF TEXT,
        applicable_articles: LIST OF TEXT,
        key_definitions: LIST OF OBJECT { term: TEXT, definition: TEXT }
    }
END
```

**Example — factual lookup:**

```ailang
RETRIEVE capital_cities FOR european_union_members WITH:
    DOMAIN: "geography"
    OUTPUT_FORMAT: {
        results: LIST OF OBJECT { country: TEXT, capital: TEXT },
        total_count: NUMBER
    }
END
```

#### 8.3 INTELLIGENTLY as Fallback

`INTELLIGENTLY` is retained as a **fallback/shorthand** for situations where the programmer does not know or does not care which specific reasoning type to use. When INTELLIGENTLY is encountered, the engine auto-classifies the appropriate reasoning type using the rules described in Section 8.5 (Auto-Classification).

**Syntax:**

```ailang
INTELLIGENTLY [operation] WITH:
    MUST_INCLUDE: [required_elements]
    CANNOT_INCLUDE: [forbidden_elements]
    OUTPUT_FORMAT: [structured_requirement]
    MAX_SCOPE: [boundary_definition]
END
```

All v0.7.1 programs that use INTELLIGENTLY remain valid under v0.8. The engine applies auto-classification transparently, routing to the appropriate reasoning type. However, explicit reasoning type selection is recommended for production programs because:

1. It communicates programmer intent more clearly
2. It enables more efficient neural activation (skipping irrelevant neuron populations)
3. It produces more predictable and auditable results
4. It eliminates the classification step, reducing latency

#### 8.4 Style Modifiers (Secondary Axis)

CREATIVELY, ADAPTIVELY, and CONTEXTUALLY survive from v0.7.1 as **adverbial modifiers** that can be applied to any reasoning operation. Style and operation type are orthogonal dimensions — you can deduce creatively, weigh adaptively, or trace contextually.

When no style modifier is given, the default is standard analytical processing. INTELLIGENTLY as a style modifier means "use general AI judgment" — it is the default style when none is specified.

##### `CREATIVELY`

Generate novel approaches while performing the specified reasoning type:

```ailang
CREATIVELY TRACE market_shift FROM economic_indicators WITH:
    DIRECTION: FORWARD
    MUST_INCLUDE: [unconventional_causal_paths, emerging_pattern_identification]
    OUTPUT_FORMAT: { novel_causes: LIST, creative_predictions: LIST }
END
```

##### `ADAPTIVELY`

Adjust the reasoning approach based on computed conditions or varying input quality:

```ailang
ADAPTIVELY WEIGH data_sources WHEN reliability_varies WITH:
    SOURCES: [sensor_data, manual_reports, satellite_imagery]
    MUST_INCLUDE: [reliability_assessment_per_source, dynamic_weight_adjustment]
    OUTPUT_FORMAT: { weighted_conclusion: TEXT, source_reliability_map: LIST }
END
```

##### `CONTEXTUALLY`

Make the reasoning operation explicitly context-dependent, grounding it in the current program state, active REALITY_CONTEXT, and accumulated variables:

**Specification:** `CONTEXTUALLY` is equivalent to the reasoning operation with a requirement to use the **current program state** (variables, prior results, and any active `REALITY_CONTEXT`); it introduces no new boundary keys.

```ailang
CONTEXTUALLY DEDUCE next_steps FROM meeting_notes WITH:
    MUST_INCLUDE: [action_items_grounded_in_discussion, responsible_parties]
    OUTPUT_FORMAT: { action_items: LIST OF OBJECT { action: TEXT, owner: TEXT, deadline: TEXT } }
END
```

##### Combining Style Modifiers with Reasoning Operations

Style modifiers precede the reasoning operation verb:

```ailang
# Standard (no modifier) — analytical COMPARE
COMPARE strategies AGAINST KPIs WITH: ...

# Creative COMPARE — look for unconventional trade-offs
CREATIVELY COMPARE strategies AGAINST KPIs WITH: ...

# Adaptive TRACE — adjust depth based on evidence quality
ADAPTIVELY TRACE failure_chain FROM incident_report WITH: ...

# Contextual SYNTHESIZE — heavily ground in program state
CONTEXTUALLY SYNTHESIZE team_feedback INTO action_plan WITH: ...
```

#### 8.5 Auto-Classification

When `INTELLIGENTLY` is used without a specific reasoning type, the engine performs automatic classification using linguistic pattern matching. Research demonstrates 93.8% accuracy for this classification approach.

**Classification Rules:**

| Linguistic Pattern | Detected Reasoning Type |
|---|---|
| Authority markers: *expert*, *Dr.*, *Nobel*, *professor*, *study says*, *according to* | WEIGH |
| Logical connectives: *if*, *then*, *all*, *every*, *therefore*, *it follows that*, *necessarily* | DEDUCE |
| Causal verbs: *causes*, *leads to*, *because*, *results in*, *due to*, *consequence of* | TRACE |
| Comparatives: *taller*, *faster*, *than*, *better*, *worse*, *rank*, *prefer*, *versus* | COMPARE |
| Quantity/agreement words: *most*, *majority*, *consensus*, *agree*, *overall*, *integrate*, *combine* | SYNTHESIZE |
| Simple fact requests: *what is*, *who wrote*, *when did*, *define*, *list*, *name* | RETRIEVE |

**Classification Confidence:**

The engine assigns a classification confidence score that affects routing aggressiveness:

- **High confidence** (clear pattern match): Route directly to detected type
- **Moderate confidence** (ambiguous patterns): Route to detected type but widen neuron activation window by 15%
- **Low confidence** (no clear pattern): Activate broad neuron population (equivalent to untyped INTELLIGENTLY in v0.7.1)

**Example of auto-classification in action:**

```ailang
# The engine detects "leads to" (causal verb) and auto-classifies as TRACE
INTELLIGENTLY determine what_the_supply_chain_disruption_leads_to WITH:
    OUTPUT_FORMAT: { effects: LIST OF TEXT }
END
# Internally routed to: TRACE effects FROM supply_chain_disruption WITH DIRECTION: FORWARD

# The engine detects "what is" (fact request) and auto-classifies as RETRIEVE
INTELLIGENTLY determine what_is_the_capital_of_France WITH:
    OUTPUT_FORMAT: { answer: TEXT }
END
# Internally routed to: RETRIEVE capital FOR France

# The engine detects "expert" and "Dr." (authority markers) and auto-classifies as WEIGH
INTELLIGENTLY evaluate whether_Dr_Smith_or_the_WHO_is_more_credible WITH:
    OUTPUT_FORMAT: { assessment: TEXT }
END
# Internally routed to: WEIGH claims ON credibility WITH SOURCES: [Dr_Smith, WHO]
```

**Specification:** Engines MUST implement auto-classification when INTELLIGENTLY is used. Engines SHOULD log the detected reasoning type and classification confidence for debugging and auditing purposes.

#### 8.6 Reasoning Routing Architecture

This section explains the computational architecture that makes typed reasoning operations more efficient than undifferentiated INTELLIGENTLY.

##### Neural Activation Profiles

Each reasoning type activates a characteristic subset of feed-forward network (FFN) neurons. These subsets are partially overlapping but substantially distinct:

| Reasoning Type | Approximate Consistent Neurons | Primary Activation Pattern |
|---|---|---|
| RETRIEVE | ~865 | Minimal activation; direct knowledge recall pathways |
| DEDUCE | ~1,200 | Logical-inference circuits; rule-application networks |
| TRACE | ~1,100 | Causal-chain networks; temporal-sequence processors |
| COMPARE | ~1,050 | Ordering circuits; multi-attribute evaluation networks |
| SYNTHESIZE | ~1,400 | Integration networks; perspective-aggregation circuits |
| WEIGH | ~1,531 | Authority-evaluation circuits; credibility-assessment networks |

##### Cross-Type Overlap (Jaccard Similarity)

The following table shows pairwise neuron overlap between reasoning types:

| Pair | Jaccard Similarity | Interpretation |
|---|---|---|
| WEIGH vs RETRIEVE | 52.8% | Moderate overlap — WEIGH subsumes RETRIEVE's knowledge recall plus adds evaluation |
| SYNTHESIZE vs DEDUCE | ~25% | Low overlap — fundamentally different computational strategies |
| TRACE vs RETRIEVE | ~25% | Low overlap — causal chains require very different circuits than direct recall |
| WEIGH vs SYNTHESIZE | ~45% | Moderate overlap — both evaluate multiple sources but with different goals |
| DEDUCE vs TRACE | ~40% | Moderate overlap — both follow chains, but logical vs causal |
| COMPARE vs WEIGH | ~42% | Moderate overlap — both evaluate, but ordering vs authority |

##### Performance Implications

When the reasoning type is specified explicitly, the engine can:

1. **Skip irrelevant neuron populations**: 25-47% of FFN compute can be bypassed
2. **Prime relevant circuits**: Pre-activate the characteristic neuron subset before processing begins
3. **Reduce routing overhead**: Eliminate the auto-classification step
4. **Improve consistency**: Same reasoning type always activates similar neuron populations, improving output predictability

**Conservative performance estimate**: 25-47% compute reduction per intelligent operation when typed reasoning is used instead of undifferentiated INTELLIGENTLY.

##### Implications for Engine Implementers

Engines implementing AILang v0.8 SHOULD:

1. Maintain neuron activation profiles for each reasoning type
2. Route typed operations to the appropriate neuron subpopulation
3. Fall back to broad activation when INTELLIGENTLY auto-classification confidence is low
4. Log routing decisions for performance analysis and debugging
5. Track classification accuracy to improve auto-classification over time

---

### 9. Enhanced Intelligent Programming Constructs

AILang provides constructs that explicitly delegate to AI intelligence while maintaining structured frameworks. In v0.8, these constructs integrate with the typed reasoning operations defined in Section 8.

#### Contextual Intelligence Framework

When transitioning from deterministic to intelligent operations, the AI has access to:

1. **Current Variable State**: All deterministic calculations and data assignments
2. **Execution History**: Previous operations and their outcomes
3. **Program Context**: The overall objective and constraints of the program
4. **Domain Knowledge**: AI's understanding of the relevant problem domain
5. **Reasoning Type Context**: The specified reasoning type determines which neural pathways are activated (v0.8)

This ensures intelligent operations are grounded in concrete program state rather than arbitrary reasoning.

#### Intelligent Operation Blocks

Structured blocks that combine deterministic framework with typed intelligent execution:

```ailang
DO [REASONING_TYPE] [operation_description]:
    [instructions with gaps]
END
```

```ailang
DO CREATIVELY [REASONING_TYPE] [problem_description]:
    GIVEN [constraints]
    [instructions]
END
```

**Examples:**

```ailang
DO WEIGH vendor_selection:
    GIVEN [budget_constraint, timeline_requirement]
    SOURCES: [vendor_A_proposal, vendor_B_proposal, vendor_C_proposal]
    MUST_INCLUDE: [cost_comparison, risk_assessment]
END

DO CREATIVELY TRACE innovation_opportunities:
    GIVEN [current_product_line, market_trends]
    DIRECTION: FORWARD
    MUST_INCLUDE: [unconventional_connections]
END
```

For backward compatibility, INTELLIGENTLY blocks remain valid:

```ailang
DO INTELLIGENTLY [operation_description]:
    [instructions with gaps]
END
```

#### Bounded Intelligence Constraints

All intelligent operations — whether typed or using INTELLIGENTLY — must specify explicit boundaries:

```ailang
[REASONING_TYPE] operation WITH:
    MUST_INCLUDE: [required_elements]
    CANNOT_INCLUDE: [forbidden_elements]
    OUTPUT_FORMAT: [structured_requirement]
    MAX_SCOPE: [boundary_definition]
END
```

**Example with typed reasoning:**

```ailang
DEDUCE regulatory_compliance FROM product_specifications AND regulatory_framework WITH:
    MUST_INCLUDE: [applicable_regulations, compliance_gaps, remediation_steps]
    CANNOT_INCLUDE: [legal_advice, liability_assessment]
    OUTPUT_FORMAT: {
        compliant: BOOLEAN,
        gaps: LIST OF OBJECT { regulation: TEXT, gap: TEXT, severity: QUALITATIVE },
        remediation: LIST OF TEXT
    }
    MAX_SCOPE: current_product_version_only
END
```

#### QUALITATIVE Value Interpretation

When inputs contain QUALITATIVE values, INTELLIGENT operations (whether typed or untyped) MUST ground interpretation in the active REALITY_CONTEXT and report confidence via categorical levels where requested.

Engines MUST NOT invent numeric codings for QUALITATIVE values unless explicitly performing parameter exploration.

**Example with typed reasoning:**

```ailang
SET stakeholder_sentiment TO "cautiously optimistic"

WITH REALITY_CONTEXT project_planning:
  WEIGH stakeholder_input ON timeline_risk WITH:
    SOURCES: [stakeholder_sentiment, historical_project_data, team_capacity_assessment]
    MUST_INCLUDE: [risk_level, factors]
    OUTPUT_FORMAT: {
      risk: QUALITATIVE IN ["low","moderate","high","critical"],
      factors: LIST OF TEXT,
      confidence_level: TEXT IN ["high","moderate","low"]
    }
    MAX_SCOPE: timeline_risk_assessment
  END
END_WITH
```

#### Gap-Filling Syntax

##### Ellipsis Operator (`...`)

Indicates where AI should apply intelligence:

```ailang
GET user_data FROM ...appropriate_data_source
PROCESS information USING ...suitable_analysis_method
RESPOND TO user WITH ...contextually_relevant_message
```

##### Smart Defaults

Variables that adapt to context:

```ailang
SET response_time TO reasonable_duration FOR current_context
SET message_style TO appropriate_for user_preference
SET processing_method TO optimal_for data_size
```

#### Context-Aware Conditions

Conditions that combine deterministic evaluation with intelligent interpretation:

```ailang
IF situation_warrants_escalation THEN:
    # AI determines what constitutes "warranting escalation"
END_IF
```

```ailang
WHILE progress_is_being_made DO:
    # AI evaluates both quantitative and qualitative progress
END_WHILE
```

#### Intelligent Iteration

Loops where AI determines relevance or selection criteria:

```ailang
FOR EACH ...relevant_record IN large_dataset DO:
    # AI determines relevance based on context and objectives
END_FOR
```

```ailang
WHILE ...customer_is_not_happy DO:
    # Escalate to higher management level
END_WHILE
```

---

### 10. Workflow Patterns: ASSESS, EXPLORE, DECIDE

The ASSESS/EXPLORE/DECIDE pattern from v0.7.1 is retained as a **workflow pattern** that composes with typed reasoning operations. These three phases represent a natural decision-making workflow: frame the situation, explore options, then decide.

#### 10.1 ASSESS Phase (Frame the Situation)

In v0.7.1, `INTELLIGENTLY ASSESS` was the primary framing construct. In v0.8, the ASSESS phase uses typed reasoning operations to frame the situation with precision:

```ailang
# v0.7.1 style (still valid as fallback):
INTELLIGENTLY ASSESS situation AS revenue_decline_analysis

# v0.8 style — explicit reasoning type:
TRACE situation_drivers FROM revenue_data AND market_conditions WITH:
    DIRECTION: BACKWARD
    MUST_INCLUDE: [root_causes, contributing_factors, timeline]
    OUTPUT_FORMAT: {
        primary_drivers: LIST OF TEXT,
        causal_chain: LIST OF TEXT,
        severity: QUALITATIVE IN ["minor", "moderate", "severe", "critical"]
    }
END
```

The ASSESS phase can use any reasoning type depending on the nature of the framing needed:

- **TRACE** when understanding what caused the current situation
- **RETRIEVE** when gathering baseline facts
- **COMPARE** when benchmarking against standards
- **WEIGH** when evaluating conflicting assessments of the situation

#### 10.2 EXPLORE Phase (Explore Options)

`INTELLIGENTLY EXPLORE` stays as-is but internal ANALYZE steps can now use typed operations:

```ailang
INTELLIGENTLY EXPLORE workforce_scenarios:
    PARAMETERS:
        reduction_percent: [5, 10, 15, 20]
        method: ["across_board", "performance_based", "voluntary"]

    EXECUTE_CODE python:
        scenarios = []
        for pct in [5, 10, 15, 20]:
            for m in ["across_board", "performance_based", "voluntary"]:
                result = simulate_reduction(pct, m, workforce_data)
                scenarios.append(result)
        df_scenarios = pd.DataFrame(scenarios)
    END_EXECUTE

    ANALYZE:
        # The ANALYZE block can now compose typed operations:
        COMPARE results ACROSS [cost_savings, capability_retention, morale_impact] WITH:
            DIMENSIONS: [cost_savings, capability_retention, morale_impact]
            OUTPUT_FORMAT: { ranking: LIST, trade_offs: TEXT }
        END

        TRACE morale_consequences FROM each_scenario WITH:
            DIRECTION: FORWARD
            OUTPUT_FORMAT: { scenario_consequences: LIST }
        END
END_EXPLORE
```

#### 10.3 DECIDE Phase (Make the Decision)

In v0.7.1, `INTELLIGENTLY DECIDE` was untyped. In v0.8, the decision step can specify which reasoning type best fits the decision:

```ailang
# v0.7.1 style (still valid):
INTELLIGENTLY DECIDE final_plan BASED_ON:
    EXPLORATION: workforce_scenarios_results
    CONSTRAINTS: legal_risk_tolerance, timeline
END_DECIDE

# v0.8 style — WEIGH is often the right choice for decisions:
WEIGH scenario_outcomes AGAINST strategic_priorities WITH:
    SOURCES: [exploration_results, executive_guidance, legal_counsel]
    MUST_INCLUDE: [risk_assessment, implementation_feasibility, stakeholder_impact]
    OUTPUT_FORMAT: {
        selected_scenario: TEXT,
        rationale: TEXT,
        risk_level: QUALITATIVE IN ["low", "moderate", "high"],
        implementation_requirements: LIST OF TEXT
    }
END
```

#### 10.4 Complete Workflow Example

```ailang
# ========================================
# Step 1: ASSESS — Frame the situation
# ========================================
TRACE revenue_decline_causes FROM quarterly_financial_data WITH:
    DIRECTION: BACKWARD
    MUST_INCLUDE: [revenue_streams_affected, market_factors, internal_factors]
    MAX_SCOPE: "last_4_quarters"
    OUTPUT_FORMAT: {
        causal_chain: LIST OF TEXT,
        primary_cause: TEXT,
        contributing_factors: LIST OF TEXT,
        severity: QUALITATIVE IN ["minor", "moderate", "severe", "critical"]
    }
END

# ========================================
# Step 2: EXPLORE — Explore response options
# ========================================
INTELLIGENTLY EXPLORE cost_reduction_scenarios:
    PARAMETERS:
        budget_reduction_percent: [5, 10, 15, 20, 25]
        reduction_method: ["across_board", "performance_based", "voluntary"]
        retention_bonus_budget: [0, 100000, 250000, 500000]
    RESOLUTION: medium

    EXECUTE_CODE python:
        import pandas as pd
        scenarios = []
        for cut_pct in [0.05, 0.10, 0.15, 0.20, 0.25]:
            for method in ['across_board', 'performance_based', 'voluntary']:
                for retention_budget in [0, 100000, 250000, 500000]:
                    result = simulate_layoff_impact(
                        budget_reduction=cut_pct,
                        method=method,
                        retention_budget=retention_budget,
                        employee_database=current_workforce
                    )
                    scenarios.append(result)
        df_scenarios = pd.DataFrame(scenarios)
    END_EXECUTE

    ANALYZE:
        COMPARE scenarios ACROSS [cost_savings, talent_retention, morale_impact, legal_risk] WITH:
            DIMENSIONS: [cost_savings, talent_retention, morale_impact, legal_risk]
            OUTPUT_FORMAT: { sweet_spot: TEXT, danger_zones: LIST, trade_offs: TEXT }
        END
END_EXPLORE

# ========================================
# Step 3: DECIDE — Choose the path forward
# ========================================
WEIGH scenario_outcomes AGAINST strategic_priorities WITH:
    SOURCES: [exploration_results, executive_guidance, legal_counsel, hr_assessment]
    MUST_INCLUDE: [risk_assessment, implementation_timeline, talent_preservation_plan]
    CANNOT_INCLUDE: [promises_to_specific_employees, premature_announcements]
    OUTPUT_FORMAT: {
        selected_plan: TEXT,
        rationale: TEXT,
        implementation_steps: LIST OF TEXT,
        risk_mitigation: LIST OF TEXT,
        monitoring_plan: TEXT
    }
END

# ========================================
# Step 4: EXECUTE — Implement with safeguards
# ========================================
EXECUTE selected_plan WITH:
    SAFEGUARDS: [legal_review, hr_oversight, manager_training]
    MONITORING: [weekly_morale_surveys, talent_retention_tracking, productivity_metrics]
    ADJUSTMENT_TRIGGERS: [key_talent_departure_threshold, morale_critical_low]
END_EXECUTE
```

---

### 11. Reality Context

Reality contexts provide a framework for defining qualitative domains where specific patterns of understanding, interpretation, and meaning-making apply. Unlike quantitative constraints that enforce numerical boundaries, reality contexts shape how intelligent operations interpret situations and generate responses within bounded worldviews.

In v0.8, reality contexts gain a REASONING_PROFILE that specifies which reasoning types are primary, secondary, and suppressed within that context.

#### 11.1 Defining Reality Contexts

##### Basic Syntax

```ailang
DEFINE REALITY_CONTEXT [context_name]:
    WORLDVIEW: [qualitative_description]
    ASSUMPTIONS: [list_of_implicit_beliefs]
    INTERPRETIVE_FRAMEWORK: [meaning_making_patterns]
    BEHAVIORAL_NORMS: [expected_patterns]
    DISCOURSE_RULES: [communication_patterns]
    VALUE_SYSTEM: [what_matters]
    CAUSAL_MODELS: [how_change_happens]
    REASONING_PROFILE:
        PRIMARY: [reasoning_type]
        SECONDARY: [reasoning_type]
        SUPPRESS: [list_of_reasoning_types]
    END_PROFILE
END_CONTEXT
```

##### REASONING_PROFILE

The REASONING_PROFILE block (new in v0.8) specifies how reasoning operations behave within this context:

- **PRIMARY**: The default reasoning type used when INTELLIGENTLY is invoked within this context. Overrides auto-classification.
- **SECONDARY**: The second-priority reasoning type, used when the primary type cannot resolve the operation.
- **SUPPRESS**: Reasoning types that are never activated within this context, even if explicitly requested. Attempting to use a suppressed reasoning type within the context raises a context_violation error.

When inside a `WITH REALITY_CONTEXT` block, `INTELLIGENTLY` operations inherit the context's PRIMARY reasoning type rather than performing auto-classification.

##### Example: Legal Proceeding Context

```ailang
DEFINE REALITY_CONTEXT legal_proceeding:
    WORLDVIEW: "Adversarial system where truth emerges from structured argument"
    ASSUMPTIONS: [presumption_of_innocence, burden_of_proof, rules_of_evidence]
    INTERPRETIVE_FRAMEWORK: [
        "Evidence must meet admissibility standards",
        "Arguments follow logical precedent chains",
        "Authority of law supersedes personal opinion"
    ]
    BEHAVIORAL_NORMS: [
        "Formal language and procedure",
        "Respect for court hierarchy",
        "Due process at every stage"
    ]
    DISCOURSE_RULES: [
        "Citations to authority required",
        "Arguments must be logically structured",
        "Precedent guides interpretation"
    ]
    VALUE_SYSTEM: [due_process, precedent, proportionality, justice]
    CAUSAL_MODELS: [
        "Liability follows from breach of duty",
        "Precedent constrains future decisions",
        "Procedure protects substantive rights"
    ]
    REASONING_PROFILE:
        PRIMARY: DEDUCE
        SECONDARY: WEIGH
        SUPPRESS: [SYNTHESIZE]
    END_PROFILE
END_CONTEXT
```

In this context:
- `INTELLIGENTLY assess_case` routes to DEDUCE (the PRIMARY type)
- WEIGH is available as a secondary type (for evaluating witness credibility, for example)
- SYNTHESIZE is suppressed because legal proceedings require adversarial argument, not consensus-building
- TRACE, COMPARE, and RETRIEVE remain available normally

##### Example: Scientific Research Context

```ailang
DEFINE REALITY_CONTEXT scientific_research:
    WORLDVIEW: "Empirical evidence reveals natural mechanisms through systematic investigation"
    ASSUMPTIONS: [
        "Reproducible results establish facts",
        "Peer review validates methodology",
        "Statistical significance indicates real effects"
    ]
    REASONING_PROFILE:
        PRIMARY: DEDUCE
        SECONDARY: TRACE
        SUPPRESS: []
    END_PROFILE
    VALUE_SYSTEM: [reproducibility, parsimony, falsifiability, intellectual_honesty]
END_CONTEXT
```

##### Example: Therapeutic Context

```ailang
DEFINE REALITY_CONTEXT psychodynamic_therapy:
    WORLDVIEW: "Unconscious processes drive behavior"
    ASSUMPTIONS: [
        "Current problems stem from childhood experiences",
        "Defense mechanisms protect from psychological pain",
        "Transference reveals relationship patterns",
        "Dreams carry symbolic meaning"
    ]
    INTERPRETIVE_FRAMEWORK: [
        "Surface behavior conceals deeper motivations",
        "Resistance indicates proximity to truth",
        "Symptoms are compromises between desires and defenses"
    ]
    BEHAVIORAL_NORMS: [
        "Free association without censorship",
        "Emotional expression is therapeutic",
        "Insight precedes change"
    ]
    DISCOURSE_RULES: [
        "Everything said has meaning",
        "Slips reveal unconscious content",
        "Silence is communication"
    ]
    VALUE_SYSTEM: [
        "Self-awareness over comfort",
        "Authenticity over adaptation",
        "Integration over splitting"
    ]
    CAUSAL_MODELS: [
        "Repressed emotions create symptoms",
        "Naming transforms experiencing",
        "Relationship patterns repeat until resolved"
    ]
    REASONING_PROFILE:
        PRIMARY: TRACE
        SECONDARY: WEIGH
        SUPPRESS: []
    END_PROFILE
END_CONTEXT
```

#### 11.2 Applying Reality Contexts

##### Reality Context Activation

```ailang
WITH REALITY_CONTEXT [context_name]:
    [operations that occur within this reality]
END_WITH

# Or for single operations:
WITHIN [context_name] DO [operation]
```
**Syntax:** `WITHIN <context> DO <stmt>` is a single-statement form.
`WITHIN <context>:` introduces a block terminated by `END`. Parsers **MUST** accept both forms.

##### Context Resolution Precedence

When multiple reality contexts could potentially apply to an operation, engines MUST resolve precedence as follows (highest to lowest priority):

1. **Block context** - Explicit `WITH REALITY_CONTEXT ... END_WITH` block enclosing the operation
2. **Single-operation context** - `WITHIN context DO operation` applied to the specific operation
3. **Person default context** - `default_reality_context` property of a Person entity performing the operation
4. **Global program default** - Program-level default context if specified

**Example demonstrating precedence:**

```ailang
# Program default (lowest priority)
SET PROGRAM_DEFAULT_CONTEXT TO general_professional

# Person with default context
CREATE Person analyst WITH:
    default_reality_context: financial_analysis
END_CREATE

# Person's default context applies here (priority 3)
# INTELLIGENTLY routes to financial_analysis context's PRIMARY reasoning type
analyst.INTELLIGENTLY evaluate_investment

# Block context overrides person default (priority 1)
WITH REALITY_CONTEXT legal_compliance:
    # Uses legal_compliance context — INTELLIGENTLY routes to DEDUCE
    analyst.INTELLIGENTLY evaluate_investment
END_WITH

# Single-operation context (priority 2)
WITHIN risk_management DO:
    analyst.INTELLIGENTLY evaluate_investment
END
# Uses risk_management context
```

**Specification**: Engines MUST apply the highest-priority context that is active for the operation. Lower-priority contexts are ignored when a higher-priority context is present.

##### Example: Multiple Reality Contexts with Typed Reasoning

```ailang
# Same situation interpreted through different realities

SET customer_complaint TO "This product doesn't work as advertised"

WITH REALITY_CONTEXT legal_reality:
    # Legal framework — DEDUCE is primary
    DEDUCE liability_exposure FROM customer_complaint AND product_warranty WITH:
        MUST_INCLUDE: [breach_of_warranty_analysis, documentation_requirements]
        OUTPUT_FORMAT: {assessment: TEXT, risk_level: QUALITATIVE}
        MAX_SCOPE: legal_implications
    END
END_WITH

WITH REALITY_CONTEXT customer_service_reality:
    # Service framework — TRACE is primary (understanding what led to dissatisfaction)
    TRACE customer_journey FROM complaint_to_root_cause WITH:
        DIRECTION: BACKWARD
        OUTPUT_FORMAT: {assessment: TEXT, root_cause: TEXT}
        MAX_SCOPE: customer_relationship
    END
END_WITH

WITH REALITY_CONTEXT engineering_reality:
    # Engineering framework — COMPARE product behavior against specification
    COMPARE actual_behavior AGAINST design_specification WITH:
        DIMENSIONS: [functionality, performance, user_experience]
        OUTPUT_FORMAT: {assessment: TEXT, gaps: LIST}
        MAX_SCOPE: product_specifications
    END
END_WITH
```

#### 11.3 Reality Context Inheritance and Composition

##### Extending Reality Contexts

```ailang
DEFINE REALITY_CONTEXT academic_humanities EXTENDS academic_reality:
    ADD ASSUMPTIONS: [
        "Texts have multiple valid interpretations",
        "Power structures shape knowledge production",
        "Subjective experience is valid data"
    ]
    MODIFY DISCOURSE_RULES: [
        "Citation creates authority",
        "Theory frames observation",
        "Critique is contribution"
    ]
    # Inherits parent's REASONING_PROFILE unless overridden
    REASONING_PROFILE:
        PRIMARY: SYNTHESIZE
        SECONDARY: WEIGH
        SUPPRESS: []
    END_PROFILE
END_CONTEXT
```

##### Blending Reality Contexts

```ailang
DEFINE REALITY_CONTEXT design_thinking BLENDS [engineering_reality, artistic_reality]:
    RECONCILE CONFLICTS WITH:
        "Function and form are equally important"
        "Constraints inspire creativity"
        "User experience trumps pure efficiency"
    END
    # Blended contexts must explicitly specify REASONING_PROFILE
    REASONING_PROFILE:
        PRIMARY: SYNTHESIZE
        SECONDARY: COMPARE
        SUPPRESS: []
    END_PROFILE
END_CONTEXT
```

#### 11.4 Reality Context-Aware Reasoning Operations

When operating within a reality context, reasoning operations automatically adopt that context's interpretive framework. The REASONING_PROFILE determines default routing:

```ailang
WITH REALITY_CONTEXT corporate_reality:
    # INTELLIGENTLY auto-routes to corporate_reality's PRIMARY type
    INTELLIGENTLY evaluate_proposal
    # Will consider: ROI, stakeholder buy-in, political implications, precedent
END_WITH

WITH REALITY_CONTEXT academic_reality:
    # INTELLIGENTLY auto-routes to academic_reality's PRIMARY type
    INTELLIGENTLY evaluate_proposal
    # Will consider: theoretical rigor, methodology, literature positioning, novelty
END_WITH
```

Explicit reasoning types override the context's PRIMARY but still operate within the context's worldview and constraints:

```ailang
WITH REALITY_CONTEXT legal_proceeding:
    # Explicit COMPARE is allowed (not suppressed) — uses legal_proceeding's worldview
    COMPARE defense_strategies AGAINST prosecution_strength WITH:
        DIMENSIONS: [evidentiary_support, precedent_alignment, jury_impact]
        OUTPUT_FORMAT: { ranking: LIST, recommended_strategy: TEXT }
    END

    # SYNTHESIZE would raise a context_violation error (suppressed in legal_proceeding)
    # SYNTHESIZE witness_testimonies INTO unified_narrative  # ERROR
END_WITH
```

#### 11.5 Person Entities and Reality Contexts

Person entities can have inherent reality contexts that shape their worldview:

```ailang
CREATE Person therapist WITH:
    default_reality_context: psychodynamic_therapy
    context_flexibility: "low"  # How easily they shift contexts
    # Options: "rigid", "low", "moderate", "high", "fluid"
END_CREATE

CREATE Person engineer WITH:
    default_reality_context: engineering_reality
    context_flexibility: "high"  # More adaptable to other contexts
END_CREATE

# When they interact, context negotiation occurs
SET conversation TO therapist.interact_with_person(engineer, neutral_context)
# Each interprets through their reality lens, creating rich misunderstandings
# or opportunities for perspective expansion
```

**Context Flexibility Descriptors:**
* **"rigid"**: Extremely difficulty shifting contexts; interprets everything through default lens
* **"low"**: Can shift with effort but strongly prefers default context
* **"moderate"**: Can adapt to different contexts when needed
* **"high"**: Easily shifts between contexts; comfortable with multiple perspectives
* **"fluid"**: Seamlessly moves between contexts; no strong default

The context flexibility affects how persons negotiate reality differences during interaction:

```ailang
# Example: Context negotiation between different flexibility levels
CREATE Person academic WITH:
    default_reality_context: academic_humanities
    context_flexibility: "moderate"
END_CREATE

CREATE Person entrepreneur WITH:
    default_reality_context: startup_reality
    context_flexibility: "fluid"
END_CREATE

SET collaboration TO academic.interact_with_person(entrepreneur, project_context)

# Entrepreneur's high flexibility allows easy adaptation
# Academic's moderate flexibility requires conscious effort to shift
# The interaction quality depends on both parties' context flexibility
```

#### 11.6 Nested and Overlapping Reality Contexts

##### Nested Reality Contexts

```ailang
WITH REALITY_CONTEXT organizational_culture:
    # Outer context: company culture

    WITH REALITY_CONTEXT team_dynamics:
        # Inner context: specific team norms
        # Inner REASONING_PROFILE takes precedence

        INTELLIGENTLY resolve_conflict
        # Uses team_dynamics' PRIMARY reasoning type
    END_WITH
END_WITH
```

##### Reality Context Switching

```ailang
DEFINE PROCEDURE context_aware_interaction:
    SET initial_context TO professional_reality

    START conversation WITH initial_context

    IF detect_personal_disclosure THEN:
        TRANSITION TO personal_reality
    END_IF

    IF detect_conflict_escalation THEN:
        TRANSITION TO mediation_reality
    END_IF

    RETURN conversation_outcome
END_PROCEDURE
```

#### 11.7 Cultural and Social Reality Contexts

##### Cultural Reality Contexts

```ailang
DEFINE REALITY_CONTEXT collectivist_culture:
    WORLDVIEW: "Individual identity emerges from group belonging"
    ASSUMPTIONS: [
        "Harmony is more important than truth",
        "Indirect communication preserves face",
        "Decisions require consensus",
        "Family needs supersede individual desires"
    ]
    BEHAVIORAL_NORMS: [
        "Defer to elders and authority",
        "Avoid direct confrontation",
        "Share resources within in-group",
        "Maintain group reputation"
    ]
    REASONING_PROFILE:
        PRIMARY: SYNTHESIZE
        SECONDARY: WEIGH
        SUPPRESS: []
    END_PROFILE
END_CONTEXT

DEFINE REALITY_CONTEXT individualist_culture:
    WORLDVIEW: "Individual autonomy and achievement define identity"
    ASSUMPTIONS: [
        "Direct communication is honest",
        "Personal responsibility for outcomes",
        "Competition drives excellence",
        "Self-reliance is virtuous"
    ]
    BEHAVIORAL_NORMS: [
        "Assert personal opinions",
        "Pursue individual goals",
        "Maintain personal boundaries",
        "Celebrate individual achievement"
    ]
    REASONING_PROFILE:
        PRIMARY: COMPARE
        SECONDARY: DEDUCE
        SUPPRESS: []
    END_PROFILE
END_CONTEXT
```

#### 11.8 Domain-Specific Reality Contexts

##### Medical Reality Context

```ailang
DEFINE REALITY_CONTEXT biomedical_reality:
    WORLDVIEW: "Disease has biological causes with biological solutions"
    INTERPRETIVE_FRAMEWORK: [
        "Symptoms indicate underlying pathology",
        "Diagnosis requires objective testing",
        "Treatment targets biological mechanisms",
        "Evidence hierarchy prioritizes RCTs"
    ]
    REASONING_PROFILE:
        PRIMARY: DEDUCE
        SECONDARY: TRACE
        SUPPRESS: []
    END_PROFILE
END_CONTEXT

DEFINE REALITY_CONTEXT holistic_health_reality:
    WORLDVIEW: "Health emerges from balance of mind, body, spirit"
    INTERPRETIVE_FRAMEWORK: [
        "Symptoms express whole-system imbalance",
        "Healing capacity is innate",
        "Prevention through lifestyle harmony",
        "Individual constitution determines treatment"
    ]
    REASONING_PROFILE:
        PRIMARY: SYNTHESIZE
        SECONDARY: TRACE
        SUPPRESS: []
    END_PROFILE
END_CONTEXT
```

#### 11.9 Reality Context Validation

##### Consistency Checking

```ailang
VALIDATE REALITY_CONTEXT [context_name]:
    CHECK internal_consistency OF assumptions
    CHECK compatibility OF worldview WITH causal_models
    CHECK completeness OF interpretive_framework
    CHECK reasoning_profile_coherence  # v0.8: verify SUPPRESS doesn't conflict with PRIMARY/SECONDARY
    IDENTIFY potential_contradictions
    SUGGEST refinements
END_VALIDATE
```

##### Reality Context Conflict Resolution

```ailang
WHEN context_conflict_detected:
    IDENTIFY conflicting_assumptions
    DETERMINE conflict_severity

    IF severity > threshold THEN:
        REQUEST explicit_context_selection FROM user
    ELSE:
        APPLY context_priority_rules
        DOCUMENT context_compromise
    END_IF
END_WHEN
```

#### 11.10 Reality Context Implementation Notes

##### For AI Systems

1. **Context Loading**: Reality contexts should be loaded into the AI's interpretive framework before processing operations within that context

2. **Assumption Tracking**: The AI must track which assumptions from the reality context influenced each decision or interpretation

3. **Context Boundaries**: When transitioning between contexts, the AI should acknowledge the shift in interpretive framework

4. **Context Conflicts**: When multiple contexts apply, the AI should either blend them coherently or make context selection explicit

5. **REASONING_PROFILE Enforcement** (v0.8): Engines MUST enforce SUPPRESS lists — attempting to use a suppressed reasoning type within a context raises a context_violation error. Engines MUST route untyped INTELLIGENTLY operations through the context's PRIMARY reasoning type.

##### Quality Assurance

1. **Interpretive Consistency**: Operations within a reality context should consistently reflect that context's worldview

2. **Context Leakage**: Prevent assumptions from one reality context from inappropriately influencing operations in another context

3. **Context Documentation**: Clear documentation of which reality context was active for each intelligent operation

4. **User Awareness**: Users should be able to query which reality context is currently active and why

5. **Reasoning Type Audit** (v0.8): Log which reasoning type was activated for each operation, including whether it was explicitly specified, inherited from REASONING_PROFILE, or auto-classified

#### 11.11 Examples of Reality Context Applications

##### Negotiation Across Realities

```ailang
DEFINE PROCEDURE multi_context_negotiation:
    SET party_a TO Person WITH default_reality_context: legal_reality
    SET party_b TO Person WITH default_reality_context: relationship_reality

    # Each party interprets the same situation differently
    SET dispute TO "Verbal agreement about shared property"

    party_a.interpretation:  # "No written contract means no agreement" (DEDUCE from legal_reality)
    party_b.interpretation:  # "Our trust relationship is the agreement" (TRACE from relationship_reality)

    # Mediator operates in bridging context
    WITH REALITY_CONTEXT mediation_reality:
        SYNTHESIZE party_positions INTO common_ground WITH:
            SOURCES: [party_a.interpretation, party_b.interpretation]
            MUST_INCLUDE: [shared_values, bridgeable_gaps]
        END

        TRACE path_to_resolution FROM common_ground WITH:
            DIRECTION: FORWARD
            MUST_INCLUDE: [actionable_steps, fairness_assessment]
        END

        WEIGH proposed_solutions ON fairness WITH:
            SOURCES: [party_a.needs, party_b.needs, legal_standards]
        END
    END_WITH
END_PROCEDURE
```

##### Educational Context Adaptation

```ailang
DEFINE PROCEDURE adaptive_teaching:
    ASSESS student.reality_context

    IF student.context MATCHES scientific_materialism THEN:
        PRESENT concepts WITH empirical_evidence
        USE causal_mechanical_explanations
    ELSE IF student.context MATCHES narrative_thinking THEN:
        PRESENT concepts THROUGH stories
        USE character_journey_explanations
    ELSE IF student.context MATCHES visual_spatial THEN:
        PRESENT concepts AS diagrams
        USE geometric_relationship_explanations
    END_IF
END_PROCEDURE
```

##### Therapeutic Reality Navigation

```ailang
DEFINE PROCEDURE therapeutic_intervention:
    # Therapist can shift between reality contexts strategically

    START WITH REALITY_CONTEXT cognitive_behavioral:
        # cognitive_behavioral PRIMARY: DEDUCE
        DEDUCE thought_distortions FROM patient_statements WITH:
            MUST_INCLUDE: [cognitive_distortion_type, evidence_for_and_against]
        END
    END_WITH

    IF resistance_encountered THEN:
        SHIFT TO REALITY_CONTEXT psychodynamic:
            # psychodynamic PRIMARY: TRACE
            TRACE resistance_origins FROM patient_history WITH:
                DIRECTION: BACKWARD
                MUST_INCLUDE: [defense_mechanism_type, underlying_conflict]
            END
        END_WITH
    END_IF

    IF somatic_symptoms_present THEN:
        SHIFT TO REALITY_CONTEXT somatic_experiencing:
            TRACE body_sensation_patterns FROM reported_symptoms WITH:
                DIRECTION: BACKWARD
                MUST_INCLUDE: [nervous_system_state, regulation_opportunities]
            END
        END_WITH
    END_IF

    SYNTHESIZE insights ACROSS contexts INTO treatment_plan WITH:
        SOURCES: [cognitive_findings, psychodynamic_findings, somatic_findings]
        MUST_INCLUDE: [integrated_formulation, treatment_priorities]
    END
END_PROCEDURE
```

#### 11.12 Advanced Reality Context Features

##### Probabilistic Context Mixing

```ailang
DEFINE REALITY_CONTEXT_MIX market_analysis:
    COMPONENTS: [
        {context: fundamental_analysis, weight: 0.4},
        {context: technical_analysis, weight: 0.3},
        {context: behavioral_finance, weight: 0.3}
    ]
    RECONCILIATION: weighted_integration
    # REASONING_PROFILE is derived from weighted mix of component profiles
END_CONTEXT_MIX
```

##### Dynamic Context Evolution

```ailang
DEFINE EVOLVING_CONTEXT startup_growth:
    STAGE early_startup WHEN company_size < 10:
        REALITY_CONTEXT: garage_startup_reality
    STAGE growth WHEN company_size BETWEEN 10 AND 50:
        REALITY_CONTEXT: scaling_startup_reality
    STAGE established WHEN company_size > 50:
        REALITY_CONTEXT: corporate_reality

    TRANSITION_RULES: [
        "Gradual culture shift over 6 months",
        "Preserve founding principles as constraints",
        "Document reality changes explicitly"
    ]
END_EVOLVING_CONTEXT
```

##### Meta-Context Awareness

```ailang
DEFINE META_CONTEXT reality_awareness:
    RECOGNIZE current_operating_context
    UNDERSTAND context_limitations
    IDENTIFY when_context_shift_needed
    FACILITATE meta_cognitive_reflection

    METHOD examine_context_assumptions:
        LIST active_assumptions
        EVALUATE assumption_validity
        IDENTIFY assumption_alternatives
        CONSIDER context_switching_costs
    END_METHOD
END_META_CONTEXT
```

#### Implementation Requirements

Reality contexts fundamentally change how intelligent operations interpret and respond to situations. They provide the qualitative boundaries that make AI behavior coherent within specific domains of meaning while maintaining the flexibility to shift perspectives when appropriate. The REASONING_PROFILE (v0.8) adds a neuroscientific foundation to this: by specifying which reasoning types are primary, secondary, and suppressed, reality contexts shape not just the interpretive lens but the computational pathways activated within the AI engine.

---

### 12. Confidence Levels and Action Authority

AILang supports explicit confidence levels for intelligent operations that inform action authority. Confidence is reported through the output structure rather than declared as a separate control parameter.

#### Confidence Declaration

Confidence is requested as part of the OUTPUT_FORMAT structure:

```ailang
WEIGH situation_assessment ON risk_level WITH:
    SOURCES: [field_reports, sensor_data, expert_analysis]
    MUST_INCLUDE: [key_factors, assessment_basis]
    OUTPUT_FORMAT: {
        assessment: TEXT,
        confidence_level: TEXT IN ["high", "moderate", "low"],
        alternative_interpretations: LIST,
        reasoning: TEXT
    }
    MAX_SCOPE: situation_assessment
END
```

**Specification**: Engines MUST populate the `confidence_level` field when requested in OUTPUT_FORMAT. The field accepts three categorical values:
- `"high"` - Assessment grounded in observable phenomena or clear evidence
- `"moderate"` - Assessment based on reasonable inference with some uncertainty
- `"low"` - Assessment involving significant interpretation or limited evidence

The AI determines the appropriate confidence level based on the observable-interpretive spectrum (see Section 13).

#### Confidence-Based Branching

Programs can branch on the categorical confidence level returned in the output:

```ailang
WEIGH situation ON severity WITH:
    SOURCES: [reports, data, observations]
    OUTPUT_FORMAT: {
        interpretation: TEXT,
        confidence_level: TEXT IN ["high", "moderate", "low"]
    }
    MAX_SCOPE: current_situation
END

IF assessment.confidence_level EQUALS "low" THEN:
    CONFIRM WITH user: "I understand [assessment.interpretation]. Is this correct?"
    WAIT for_confirmation BEFORE proceeding
ELSE IF assessment.confidence_level EQUALS "moderate" THEN:
    LOG "Proceeding with moderate confidence"
    PROCEED WITH assessment.interpretation
ELSE IF assessment.confidence_level EQUALS "high" THEN:
    PROCEED WITH assessment.interpretation
END_IF
```

**Specification**: Lower confidence assessments typically require tighter boundaries and often user confirmation before significant actions. Programs should branch on categorical confidence levels (`"high"`, `"moderate"`, `"low"`) rather than numeric thresholds.

#### Confidence and Action Authority

The confidence level informs what actions are appropriate:

```ailang
TRACE emotional_indicators FROM observable_behavior WITH:
    DIRECTION: BACKWARD
    OUTPUT_FORMAT: {
        state: TEXT,
        confidence_level: TEXT IN ["high", "moderate", "low"],
        indicators: LIST
    }
    MAX_SCOPE: observable_behavior
END

# High confidence (observable phenomena) - direct action may be appropriate
IF emotional_assessment.state EQUALS "distressed" AND emotional_assessment.confidence_level EQUALS "high" THEN:
    OFFER support_resources
    SAY "I can see you're upset. Would you like to talk?"
END_IF

# Low confidence (interpretive) - constrained action authority
IF emotional_assessment.state EQUALS "depressed" AND emotional_assessment.confidence_level EQUALS "low" THEN:
    ONLY SUGGEST: "Is everything okay? I'm here if you want to talk."
    CANNOT:
        - diagnose_condition
        - prescribe_treatment
        - assume_underlying_causes
END_IF
```

**Specification**: Observable assessments (typically yielding high confidence) can authorize more direct actions. Interpretive assessments (typically yielding moderate or low confidence) should restrict to suggestions and require tighter boundaries.

---

### 13. The Qualitative Spectrum

Within qualitative processing, AILang recognizes a spectrum from observable to interpretive assessments that determines execution confidence and boundary placement.

#### Observable Qualitative Phenomena

Qualitative assessments grounded in verifiable, sensory data where multiple observers would largely agree:

* Physical states: "person is walking", "room is cluttered", "door is open"
* Emotional expressions: "voice sounds angry", "person is crying"
* Environmental conditions: "room is dark", "music is playing"

These assessments, while qualitative, have high confidence due to observable anchors.

**Reasoning type mapping:** Observable assessments naturally map to **RETRIEVE** (high confidence, minimal inference required, low neuron activation). The engine uses direct knowledge recall pathways to match observations to known categories.

#### Interpretive Qualitative Assessments

Assessments requiring inference chains and subjective judgment:

* Internal states: "person feels lonely", "customer is considering switching"
* Social interpretations: "meeting has tension", "joke might offend"
* Value judgments: "behavior is inappropriate", "request seems unreasonable"

These assessments require lower confidence and tighter action boundaries.

**Reasoning type mapping:** Interpretive assessments map to **TRACE** (following causal/inference chains) or **WEIGH** (evaluating evidence for competing interpretations). These reasoning types activate deeper neuron populations, reflecting the greater computational work required for interpretation.

#### Confidence-Based Execution

AILang adjusts execution based on assessment type:

```ailang
# High confidence - observable (RETRIEVE-class reasoning)
IF person_is_crying THEN:
    OFFER tissue  # Direct action authorized
END_IF

# Low confidence - interpretive (TRACE/WEIGH-class reasoning)
IF mood_seems_depressed THEN:
    ONLY SUGGEST: "Would you like to talk?"  # Minimal action
    CANNOT: diagnose, prescribe, assume_causes
END_IF
```

**Specification**: The AI must recognize where assessments fall on the observable-interpretive spectrum and adjust confidence levels and action boundaries accordingly. Observable assessments activate RETRIEVE-class pathways (minimal neurons); interpretive assessments activate TRACE or WEIGH-class pathways (deeper activation).

Engines **SHOULD** map *observable* assessments to `"high"` confidence by default, and *interpretive* assessments to `"moderate"` or `"low"` depending on inference depth.

---

### 14. Code Execution Blocks

#### Basic Syntax

```ailang
EXECUTE_CODE [language]:
    [native code in specified language]
END_EXECUTE
```

#### Supported Languages:
* python (primary support)
* Additional languages may be added based on execution environment capabilities

#### Specification

1. **Execution Guarantee**: Code blocks MUST be executed as actual code in the specified language interpreter, not interpreted as natural language by the AI

2. **Variable Scope:**
    * AILang variables are accessible within code blocks
    * Variables created/modified in code blocks become available to subsequent AILang operations
    * Type conversion occurs automatically where possible

3. **Error Handling**: Exceptions in code blocks throw AILang catchable errors

4. **Isolation**: Code blocks execute in sandboxed environments with appropriate security constraints

#### Simple Example

```ailang
# AILang variable
SET dataset TO load_csv("customer_data.csv")

# Deterministic computation in code
EXECUTE_CODE python:
    import pandas as pd

    # AILang variable 'dataset' is accessible
    df = pd.DataFrame(dataset)

    # Statistical computation
    women_over_65 = len(df[(df['gender'] == 'female') & (df['age'] > 65)])
    total_records = len(df)
    percentage = (women_over_65 / total_records) * 100

    # Results available to AILang
    analysis_results = {
        'count': women_over_65,
        'total': total_records,
        'percentage': percentage
    }
END_EXECUTE

# Continue in AILang with guaranteed-correct results
SEND "Analysis found " + analysis_results.count + " women over 65" TO user_display

IF analysis_results.percentage > 30 THEN:
    # v0.8: Use typed reasoning for the recommendation
    COMPARE marketing_strategies AGAINST demographic_profile WITH:
        DIMENSIONS: [reach, cost_effectiveness, engagement_potential]
        OUTPUT_FORMAT: { recommended_strategy: TEXT, rationale: TEXT }
    END
END_IF
```

##### Implementation Notes
###### For AI Execution Engines:

1. **Code Block Parsing**: Detect EXECUTE_CODE blocks and extract for direct execution
2. **Language Runtime**: Maintain interpreter instances for supported languages
3. **Variable Bridging**: Implement marshalling layer for AILang to code variable access
4. **Sandbox Security**: Execute code in isolated environments with appropriate constraints
5. **Result Integration**: Capture code block outputs and make available to subsequent AILang operations

###### For Parameter Exploration:

1. **Grid Generation**: Smart parameter grid construction based on resolution setting
2. **Result Structuring**: Format exploration results for effective AI pattern analysis
3. **Visualization Support**: Enable graphical representation of parameter landscapes where helpful

###### Type Conversion Guidelines:

* Simple types (numbers, strings, booleans): automatic conversion
* Collections (lists, dictionaries): structure-preserving conversion
* Complex objects: serialize with schema preservation
* Ambiguous cases: AI provides reasonable defaults with explicit documentation

---

#### Serialization of QUALITATIVE Values

When passing values across execution boundaries (e.g., from DETERMINISTIC to CODE blocks, or in API responses), QUALITATIVE values are serialized as TEXT with optional metadata `@qual` to preserve type information.

##### In CODE Blocks

QUALITATIVE values are accessible as string representations:

```ailang
SET mood TO "frustrated_but_polite"

EXECUTE_CODE python:
  # mood is received as a string
  mood_text = mood  # "frustrated_but_polite"
  has_frustration = "frustrated" in mood_text
  word_count = len(mood_text.split('_'))

  # String operations are valid
  words = mood_text.split('_')
  first_word = words[0]  # "frustrated"

  # But don't assign semantic meaning in CODE
  # WRONG: mood_score = 0.3  # arbitrary mapping
END_EXECUTE
```

##### Metadata Preservation

In environments that support typed metadata, QUALITATIVE values include a `@qual` tag:

```
# Serialization format (conceptual)
{
  "value": "frustrated_but_polite",
  "@type": "qualitative",
  "@qual": true
}
```

**Consumers lacking type metadata** MUST treat QUALITATIVE values as TEXT with no numeric assumptions. They should not attempt to:
- Convert to numeric scales
- Apply ordering comparisons
- Perform arithmetic operations
- Assume any inherent quantitative meaning

##### Semantic Interpretation

For semantic interpretation of QUALITATIVE values, use typed reasoning operations:

```ailang
SET mood TO "frustrated_but_polite"

# WRONG - Don't try semantic analysis in CODE
EXECUTE_CODE python:
  # This loses the semantic richness:
  if "frustrated" in mood:
    emotion_level = 0.3
END_EXECUTE

# CORRECT - Use typed reasoning for semantics
TRACE emotional_dimensions FROM mood WITH:
    DIRECTION: BACKWARD
    OUTPUT_FORMAT: {
        primary_emotion: TEXT,
        intensity: TEXT IN ["low","moderate","high"],
        secondary_traits: LIST OF TEXT,
        confidence_level: TEXT IN ["high","moderate","low"]
    }
    MAX_SCOPE: emotional_assessment
END

# Now you can use the structured interpretation
IF emotion_analysis.intensity EQUALS "high" THEN:
  SET priority TO "urgent"
END_IF
```

##### Cross-Boundary Pattern

```ailang
# QUALITATIVE reasoning in INTELLIGENT mode
SET customer_state TO "at_risk_but_engaged"

# Qualitative interpretation using typed reasoning
WEIGH retention_approaches ON effectiveness WITH:
    SOURCES: [customer_state, account_history, industry_benchmarks]
    OUTPUT_FORMAT: {
        approach: TEXT,
        urgency: TEXT IN ["low","medium","high","critical"],
        recommended_actions: LIST OF TEXT
    }
END

# String handling in CODE (where appropriate)
EXECUTE_CODE python:
  # Simple string operations are fine
  state_words = customer_state.split('_')
  log_entry = f"Customer state: {customer_state}"

  # But don't invent meanings:
  # WRONG: risk_score = 0.7 if "at_risk" in customer_state else 0.3
END_EXECUTE

# Back to qualitative reasoning for decisions
IF retention_strategy.urgency IN ["high","critical"] THEN:
  ASSIGN account_manager
  SCHEDULE immediate_outreach
END_IF
```

**Specification:** Engines MUST preserve the semantic type boundary when serializing QUALITATIVE values. While the value may be represented as a string for technical reasons, its QUALITATIVE nature should be preserved through metadata where possible, and engines should not provide implicit numeric conversions at serialization boundaries.

---

### 15. The Qualitative-Quantitative Interface

Managing data flow across the qualitative-quantitative boundary **is the fundamental challenge in hybrid AI-code systems.** This is because:

- **Humans reason qualitatively**: We assess situations using concepts like "high risk," "urgent priority," "moderate confidence," "strong relationship"
- **Code operates quantitatively**: Algorithms require numbers — `risk_level = 0.7`, `priority = 3`, `confidence = 0.85`
- **The translation is non-obvious**: There is no natural, universal mapping between "high risk" and a specific numeric value

Thus, managing data flow across the qualitative-quantitative boundary is the core architectural challenge of human-AI-code integration.

#### Information Flow Architecture

Information flows bidirectionally between execution modes, with each transition requiring explicit handling:

**CODE to INTELLIGENT: Quantitative to Qualitative**

Code produces numbers; AI interprets meaning using typed reasoning:

```ailang
EXECUTE_CODE python:
    portfolio_results = {
        'sharpe_ratio': 1.23,
        'max_drawdown': -0.15,
        'volatility': 0.18,
        'var_95': -0.087
    }
END_EXECUTE

# v0.8: Use SYNTHESIZE to integrate quantitative results into qualitative interpretation
SYNTHESIZE portfolio_results INTO investment_assessment WITH:
    SOURCES: [portfolio_results, client_risk_profile, market_conditions]
    MUST_INCLUDE: [risk_adjusted_performance, suitability_for_client]
    OUTPUT_FORMAT: {
        interpretation: TEXT,
        suitability: QUALITATIVE IN ["unsuitable", "marginal", "suitable", "excellent"],
        confidence_level: TEXT IN ["high", "moderate", "low"]
    }
END
```

**DETERMINISTIC to CODE and CODE to DETERMINISTIC**

Standard variable passing with type conversion:

```ailang
SET customer_records TO load_database("customers")

EXECUTE_CODE python:
    import pandas as pd
    df = pd.DataFrame(customer_records)
    high_value_customers = df[df['lifetime_value'] > 10000]
    count = len(high_value_customers)
END_EXECUTE

FOR EACH customer IN high_value_customers DO:
    # v0.8: Use typed reasoning for personalization
    SYNTHESIZE customer_profile INTO offer WITH:
        SOURCES: [customer.purchase_history, customer.preferences, current_promotions]
        MUST_INCLUDE: [personalization_rationale]
        OUTPUT_FORMAT: { offer_text: TEXT, discount_tier: TEXT }
    END
END_FOR
```

**INTELLIGENT to DETERMINISTIC and DETERMINISTIC to INTELLIGENT**

Natural language interpretation handles this boundary:

```ailang
TRACE situation_evolution FROM current_data WITH:
    DIRECTION: FORWARD
    OUTPUT_FORMAT: { assessment: TEXT, priority_indicators: LIST }
END

IF situation_assessment.assessment CONTAINS "critical" OR situation_assessment.assessment CONTAINS "urgent" THEN:
    SET priority TO "high"
END_IF

WEIGH response_options ON appropriateness WITH:
    SOURCES: [available_actions, priority_level, resource_constraints]
    OUTPUT_FORMAT: { recommended_action: TEXT }
END
```

**INTELLIGENT to CODE: Qualitative to Quantitative**

Using parameter-range exploration:

```ailang
INTELLIGENTLY EXPLORE market_strategy:
    PARAMETERS:
        volatility_assumption: [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

    EXECUTE_CODE python:
        results = {v: calculate_returns(volatility=v) for v in volatility_range}
    END_EXECUTE

    ANALYZE:
        # v0.8: Use typed reasoning within ANALYZE
        COMPARE results ACROSS volatility_range WITH:
            DIMENSIONS: [returns, risk, stability]
            OUTPUT_FORMAT: { robust_range: TEXT, threshold_points: LIST }
        END
END_EXPLORE
```

#### The Qualitative-Quantitative Interface Problem

##### When Simple Computation Works

For well-defined problems with clear quantitative parameters, direct code execution is straightforward:

```ailang
EXECUTE_CODE python:
    # Clear, computable questions
    record_count = len(database.records)
    women_over_65 = sum(1 for r in records if r.gender == 'F' and r.age > 65)
    average_transaction = sum(t.amount for t in transactions) / len(transactions)
END_EXECUTE
```

These computations are deterministic and unambiguous because:

* The question is well-defined ("how many records?")
* The data has clear structure
* The operation has established meaning
* No qualitative judgment is required

##### When the Interface Becomes Problematic

Many real-world problems involve poorly-defined parameters where qualitative assessment must somehow inform quantitative computation. For example, consider a CEO evaluating a strategic decision:

**Human reasoning (qualitative):**
- "The market feels volatile right now"
- "This acquisition seems risky but potentially transformative"
- "The team's morale is fragile after recent changes"
- "We need to move decisively but carefully"

**Code requirements (quantitative):**
- `market_volatility = ?` (what number?)
- `acquisition_risk = ?` (on what scale?)
- `team_morale = ?` (measured how?)
- `decision_urgency = ?` (relative to what?)

###### Problematic Approach: Point Estimation

```ailang
# AI pulls a number from nowhere
INTELLIGENTLY SET risk_tolerance TO 0.7  # What does 0.7 mean?

EXECUTE_CODE python:
    allocation = optimize_portfolio(risk_tolerance=0.7)
END_EXECUTE
# Result is meaningless because input was arbitrary
```

The fundamental issue here is that **a single point value (0.7) has no inherent meaning.** The AI has no principled way to choose 0.7 vs 0.65 vs 0.75, and the code operates on this arbitrary value as if it were meaningful.

In other words, the challenge is that **code requires numbers, and there's no principled way to assign them**:

* **No natural scale**: Unlike "3 meters" or "5 seconds," there's no inherent unit for "risk tolerance"
* **Context-dependent**: 0.7 might mean different things in different domains or situations
* **False precision**: The single number implies certainty that doesn't exist
* **Loses information**: The qualitative assessment contains nuance lost in conversion


###### Parameter Space Exploration

In order to address this issue, rather than forcing artificial qualitative-to-quantitative conversion, AILang is designed to explore parameter ranges and let the AI interpret patterns across the landscape. This allows AI to identify patterns and leverage what LLMs are good at: recognizing trends, thresholds, and regimes. It also allows AI to generate meaningful interpretations by assessing the material changes along a spectrum of data.

**Range-Based Approach:**

```ailang
INTELLIGENTLY EXPLORE portfolio_strategy:
    PARAMETERS:
        risk_tolerance: [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
        rebalancing_frequency: ["monthly", "quarterly", "annually"]

    EXECUTE_CODE python:
        results = []

        for risk in [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
            for rebalance in ['monthly', 'quarterly', 'annually']:
                outcome = monte_carlo_simulation(
                    risk_tolerance=risk,
                    rebalancing=rebalance,
                    scenarios=10000
                )
                results.append({
                    'risk': risk,
                    'rebalancing': rebalance,
                    'expected_return': outcome['mean'],
                    'volatility': outcome['std'],
                    'worst_case_5th_percentile': outcome['p05']
                })
    END_EXECUTE

    ANALYZE:
        # v0.8: Use typed reasoning within ANALYZE
        COMPARE results ACROSS [risk_tolerance, rebalancing_frequency] WITH:
            DIMENSIONS: [expected_return, volatility, worst_case]
            OUTPUT_FORMAT: {
                sweet_spot: TEXT,
                sensitivity_analysis: TEXT,
                regime_transitions: LIST OF TEXT
            }
        END
END_EXPLORE

WEIGH final_parameters AGAINST client_constraints WITH:
    SOURCES: [exploration_results, client_risk_profile, regulatory_requirements, market_conditions]
    OUTPUT_FORMAT: {
        recommended_parameters: OBJECT { risk: NUMBER, rebalancing: TEXT },
        rationale: TEXT,
        confidence_level: TEXT IN ["high", "moderate", "low"]
    }
END
```

###### Why Range Exploration Works

1. **Trends Are Meaningful**: "Risk 0.5-0.7 produces stable returns" is interpretable; "risk = 0.7" is not
2. **Sensitivity Analysis Is Natural**: The AI sees how outputs change with inputs, which aligns with human reasoning about parameters
3. **Phase Transitions Become Visible**: "Below 0.4, strategy A dominates; above 0.6, strategy B dominates" provides actionable intelligence
4. **Robustness Checking**: Similar results across parameter ranges indicate robust regions; wild swings indicate fragility
5. **Eliminates Arbitrary Choices**: The AI doesn't guess a single "right" value; it maps the landscape and identifies operational regimes
6. **Aligns With AI Strengths**: LLMs are good at pattern recognition and comparative analysis; poor at generating meaningful isolated numeric values
7. **Preserves Qualitative Richness**: The interpretation captures nuance that would be lost in point conversion
8. **Reveals Structure**: Discontinuities, thresholds, and interaction effects become visible

###### Parameter Space Exploration Syntax

```ailang
INTELLIGENTLY EXPLORE [exploration_name]:
    PARAMETERS:
        [parameter1]: [range_or_list_of_values]
        [parameter2]: [range_or_list_of_values]
        ...
    RESOLUTION: [coarse|medium|fine]  # Optional: controls granularity

    EXECUTE_CODE [language]:
        [code that explores parameter combinations]
    END_EXECUTE

    ANALYZE:
        [AI interpretation of patterns, trends, regimes]
        [Identification of: sensitivities, plateaus, thresholds, optima]
        [v0.8: May contain typed reasoning operations (COMPARE, TRACE, etc.)]
END_EXPLORE
```

###### Interpretation Patterns

The AI can interpret parameter space results by identifying:

* **Sensitivity**: "Small changes in X cause large changes in outcome" — critical parameter requiring careful setting
* **Plateaus**: "Wide range of X produces similar outcomes" — robust region, exact value not critical
* **Thresholds**: "Below X: regime A; above X: regime B" — phase transition, operational boundary
* **Interactions**: "Effect of X depends on value of Y" — parameters are coupled, must consider together
* **Optima**: "Maximum/minimum at X" — sweet spot or danger zone
* **Infeasibility**: "No parameter combination satisfies constraints" — problem requires reformulation

###### Complex Example: Strategic Decision-Making

```ailang
# CEO scenario: workforce reduction planning

# Step 1: ASSESS with typed reasoning
TRACE revenue_situation FROM financial_data WITH:
    DIRECTION: BACKWARD
    MUST_INCLUDE: [root_causes, timeline, severity]
    OUTPUT_FORMAT: { situation_summary: TEXT, severity: QUALITATIVE }
END

# Step 2: EXPLORE parameter space
INTELLIGENTLY EXPLORE workforce_reduction_scenarios:
    PARAMETERS:
        budget_reduction_percent: [5, 10, 15, 20, 25]
        reduction_method: ["across_board", "performance_based", "last_hired", "voluntary"]
        retention_bonus_budget: [0, 100000, 250000, 500000]
    RESOLUTION: medium

    EXECUTE_CODE python:
        import pandas as pd
        import numpy as np

        scenarios = []

        for cut_pct in [0.05, 0.10, 0.15, 0.20, 0.25]:
            for method in ['across_board', 'performance_based', 'last_hired', 'voluntary']:
                for retention_budget in [0, 100000, 250000, 500000]:
                    result = simulate_layoff_impact(
                        budget_reduction=cut_pct,
                        method=method,
                        retention_budget=retention_budget,
                        employee_database=current_workforce,
                        performance_data=performance_reviews
                    )
                    scenarios.append({
                        'budget_cut': cut_pct,
                        'method': method,
                        'retention_budget': retention_budget,
                        'employees_affected': result['headcount_reduction'],
                        'cost_savings': result['annual_savings'],
                        'key_talent_retained': result['high_performers_remaining'],
                        'morale_impact_score': result['predicted_morale'],
                        'productivity_impact': result['productivity_change'],
                        'legal_risk_score': result['legal_exposure'],
                        'time_to_implement': result['implementation_weeks']
                    })

        df_scenarios = pd.DataFrame(scenarios)
    END_EXECUTE

    ANALYZE:
        COMPARE scenarios ACROSS [cost_savings, talent_retention, morale_impact, legal_risk] WITH:
            DIMENSIONS: [cost_savings, key_talent_retained, morale_impact_score, legal_risk_score]
            OUTPUT_FORMAT: {
                viable_range: TEXT,
                optimal_configuration: TEXT,
                danger_zones: LIST OF TEXT,
                threshold_behaviors: LIST OF TEXT
            }
        END
END_EXPLORE

# Step 3: DECIDE with typed reasoning
WEIGH scenario_outcomes AGAINST strategic_priorities WITH:
    SOURCES: [exploration_results, executive_guidance, legal_counsel, hr_assessment]
    MUST_INCLUDE: [risk_assessment, implementation_feasibility, talent_preservation_plan]
    CANNOT_INCLUDE: [promises_to_specific_employees]
    OUTPUT_FORMAT: {
        selected_plan: TEXT,
        rationale: TEXT,
        implementation_steps: LIST OF TEXT,
        risk_mitigation: LIST OF TEXT
    }
END

# Implement decision with monitoring
EXECUTE selected_plan WITH:
    SAFEGUARDS: [legal_review, hr_oversight, manager_training]
    MONITORING: [weekly_morale_surveys, talent_retention_tracking, productivity_metrics]
    ADJUSTMENT_TRIGGERS: [key_talent_departure_threshold, morale_critical_low]
END_EXECUTE
```

#### Best Practices

**Use CODE blocks for:**

* Mathematical computations requiring precision
* Algorithm implementations
* Data processing and transformation
* Statistical analysis
* Optimization problems
* Any operation where deterministic behavior is essential

**Use DETERMINISTIC operations for:**

* Program control flow
* State management
* Input/output operations
* Structured logic that benefits from readability

**Use INTELLIGENT operations for:**

* Ambiguous decisions
* Creative problem-solving
* Natural language processing
* Strategic reasoning
* Contextual interpretation
* Pattern recognition in exploration results

**Choose reasoning type based on the cognitive task:**

| Task | Recommended Type |
|---|---|
| Evaluating source credibility | WEIGH |
| Applying rules to reach conclusions | DEDUCE |
| Root cause analysis or consequence prediction | TRACE |
| Ranking options or trade-off analysis | COMPARE |
| Integrating multiple perspectives | SYNTHESIZE |
| Factual recall or definition lookup | RETRIEVE |
| Unknown or mixed reasoning needs | INTELLIGENTLY (auto-classifies) |

**Use Parameter Exploration when:**

* Converting qualitative assessments to quantitative parameters
* Parameters lack inherent natural units or scales
* Understanding sensitivity and robustness is important
* Identifying operational regimes and phase transitions
* Multiple parameters interact in complex ways
* The "right" value depends on trade-offs rather than calculation

#### QUALITATIVE to CODE Bridge

When CODE blocks require numeric values but the program works with QUALITATIVE labels, programs SHOULD use one of two principled approaches:

##### Option 1: Parameter Exploration (Recommended)

Scan plausible numeric ranges and let AI interpret regimes across the parameter space:

```ailang
SET stakeholder_trust TO "high_trust"  # QUALITATIVE

INTELLIGENTLY EXPLORE trust_scenarios:
  PARAMETERS:
    assumed_trust_scalar: [0.55, 0.65, 0.75, 0.85]  # candidate mappings

  EXECUTE_CODE python:
    outcomes = {t: simulate_project(success_factor=t)
                for t in assumed_trust_scalar}
  END_EXECUTE

  ANALYZE:
    COMPARE outcomes ACROSS assumed_trust_scalar WITH:
        DIMENSIONS: [project_success, team_velocity, risk_level]
        OUTPUT_FORMAT: {
            robust_range: TEXT,
            recommended_proxy: NUMBER,
            sensitivity: TEXT
        }
    END
END_EXPLORE

# Use the AI-validated mapping
SET trust_proxy TO 0.70
EXECUTE_CODE python:
  final_result = simulate_project(success_factor=trust_proxy)
END_EXECUTE
```

##### Option 2: Explicit Domain Mapping

When domain knowledge or empirical data establishes a validated mapping, provide an explicit conversion function:

```ailang
DEFINE PROCEDURE map_trust_to_scalar WITH PARAMETERS [trust_label: QUALITATIVE]:
  # Mapping based on empirical study (Smith et al., 2024):
  # Survey of 500 projects correlated trust assessments with success factors

  MATCH trust_label WITH:
    CASE "no_trust":       RETURN 0.15  # Based on failed collaboration data
    CASE "low_trust":      RETURN 0.30  # Limited information sharing observed
    CASE "medium_trust":   RETURN 0.60  # Standard project execution baseline
    CASE "high_trust":     RETURN 0.80  # Enhanced collaboration metrics
    CASE "complete_trust": RETURN 0.95  # Rare, exceptional partnership data
    DEFAULT:               RETURN 0.50  # Conservative fallback
  END_MATCH
END_PROCEDURE

# Usage with explicit documentation
SET trust_state TO "high_trust"
SET trust_scalar TO map_trust_to_scalar(trust_state)

LOG "Mapping qualitative trust '" + trust_state + "' to scalar " + trust_scalar

EXECUTE_CODE python:
  result = simulate_project(success_factor=trust_scalar)
END_EXECUTE
```

##### Prohibited Pattern: Silent Coercion

**NEVER do this:**

```ailang
SET mood TO "tense"  # QUALITATIVE

# WRONG - Implicit, undocumented numeric conversion
EXECUTE_CODE python:
  # This mapping is invisible to the program reader:
  mood_map = {"relaxed": 1, "neutral": 0.5, "tense": 0}
  score = mood_map.get(mood, 0.5)
  result = calculate_something(score)
END_EXECUTE
```

**Why this is prohibited:**
- The mapping is hidden from anyone reading the program
- No rationale for the numeric values (why is "relaxed" = 1?)
- Loses all semantic richness of the QUALITATIVE type
- Makes debugging and auditing impossible
- Violates the purpose of having QUALITATIVE as a distinct type
- Creates maintenance burden (hidden magic numbers)

**Specification Requirement:**

Silent, ad hoc scalarization of QUALITATIVE values by the engine or in CODE blocks is **not permitted**. Programs MUST explicitly handle the conversion using either:
1. Parameter Exploration (INTELLIGENTLY EXPLORE), or
2. An explicit, documented mapping function (DEFINE PROCEDURE)

Engines MUST NOT provide implicit numeric coercion for QUALITATIVE values, even when CODE blocks require numeric inputs.

---

### 16. Mathematical Operations

Complex mathematical operations should generally be implemented in executable code rather than as natural language constructs. This provides:

- **Guaranteed precision** for numerical computations
- **Access to mature libraries** (NumPy, SciPy, SymPy, etc.)
- **Performance** for intensive calculations
- **Reliability** for mission-critical computations

#### When to Use Code for Mathematics

**Use EXECUTE_CODE blocks for:**
- Symbolic mathematics (using SymPy)
- Numerical analysis and scientific computing
- Linear algebra operations
- Calculus (differentiation, integration)
- Differential equations
- Optimization problems
- Statistical analysis
- Signal processing
- Any computation requiring guaranteed precision

**Example:**

```ailang
EXECUTE_CODE python:
    import numpy as np
    from scipy import integrate, optimize
    from sympy import symbols, diff, integrate as sym_integrate

    # Symbolic differentiation
    x = symbols('x')
    f = x**3 + 2*x
    derivative = diff(f, x)  # 3*x^2 + 2

    # Numerical integration
    def integrand(x):
        return x**2
    result, error = integrate.quad(integrand, 0, 1)  # 1/3

    # Optimization
    def objective(x):
        return x**2 + x + 1
    minimum = optimize.minimize(objective, x0=0)
END_EXECUTE
```

#### Simple Mathematical Expressions in AILang

For basic arithmetic that doesn't require code execution overhead, AILang supports standard mathematical notation:

```ailang
# Basic arithmetic
SET result TO (a + b) * (c - d) / e
SET power TO x^2
SET root TO sqrt(x^2 + y^2)

# These are interpreted by the AI for simple calculations
SET total TO 5 + 3 * 2  # = 11
SET percentage TO (achieved / target) * 100
```

**Use these simple expressions when:**
* The calculation is straightforward and unambiguous
* Precision requirements are modest
* Performance is not critical
* The expression serves primarily as program logic rather than scientific computation

#### Mathematical Context for Complex Domains

When working with complex numbers, quaternions, or specialized mathematical domains, use CODE blocks with appropriate libraries:

```ailang
EXECUTE_CODE python:
    import numpy as np

    # Complex number operations
    z1 = 3 + 4j
    z2 = 1 - 2j

    product = z1 * z2  # Complex multiplication
    magnitude = abs(z1)  # |z1| = 5
    phase = np.angle(z1)  # arg(z1)

    # Quaternions (using specialized library)
    from pyquaternion import Quaternion
    q1 = Quaternion(axis=[0, 0, 1], angle=np.pi/4)
    q2 = Quaternion(axis=[1, 0, 0], angle=np.pi/2)
    rotation = q1 * q2
END_EXECUTE
```

#### Domain-Specific Mathematical Operations

For specialized mathematical operations, leverage domain-specific Python libraries within CODE blocks:

##### Physics and Engineering:

```ailang
EXECUTE_CODE python:
    from scipy import constants
    from scipy.integrate import odeint

    # Physical constants
    c = constants.speed_of_light
    h = constants.Planck

    # Solve differential equations
    def model(y, t):
        dydt = -0.5 * y
        return dydt

    y0 = 5
    t = np.linspace(0, 10, 100)
    solution = odeint(model, y0, t)
END_EXECUTE
```

##### Signal Processing:

```ailang
EXECUTE_CODE python:
    from scipy import signal
    from scipy.fft import fft, fftfreq

    # Fourier transform
    N = 1000
    T = 1.0 / 800.0
    x = np.linspace(0.0, N*T, N)
    y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)

    yf = fft(y)
    xf = fftfreq(N, T)

    # Filter design
    b, a = signal.butter(4, 100, 'low', fs=1000)
    filtered = signal.filtfilt(b, a, y)
END_EXECUTE
```

##### Optimization and Numerical Methods:

```ailang
EXECUTE_CODE python:
    from scipy.optimize import minimize, differential_evolution
    from scipy.linalg import solve, eig

    # Linear algebra
    A = np.array([[4, 2, 3], [3, 5, 7], [8, 2, 6]])
    eigenvalues, eigenvectors = eig(A)

    # Constrained optimization
    def objective(x):
        return x[0]**2 + x[1]**2

    def constraint(x):
        return x[0] + x[1] - 1

    constraints = {'type': 'eq', 'fun': constraint}
    result = minimize(objective, x0=[0.5, 0.5], constraints=constraints)
END_EXECUTE
```

##### Best Practices for Mathematical Operations

1. Default to CODE blocks for any mathematical operation beyond basic arithmetic
2. Use established libraries rather than implementing numerical methods from scratch
3. Document units and assumptions in comments within code blocks
4. Validate results when precision is critical
5. Consider numerical stability for ill-conditioned problems
6. Use symbolic computation (SymPy) when exact results are needed

##### Integration with AILang Workflow

Mathematics typically fits into the broader AILang workflow like this:

```ailang
# Step 1: AI assesses the problem qualitatively using typed reasoning
TRACE simulation_requirements FROM problem_description WITH:
    DIRECTION: FORWARD
    OUTPUT_FORMAT: { parameters_needed: LIST, constraints: LIST, physics_model: TEXT }
END

# Step 2: Explore parameter space to understand behavior
INTELLIGENTLY EXPLORE simulation_parameters:
    PARAMETERS:
        time_step: [0.001, 0.01, 0.1]
        damping_coefficient: [0.1, 0.5, 1.0, 2.0]

    EXECUTE_CODE python:
        import numpy as np
        from scipy.integrate import odeint

        results = []
        for dt in [0.001, 0.01, 0.1]:
            for damping in [0.1, 0.5, 1.0, 2.0]:
                # Simulate damped oscillator
                def model(y, t, d):
                    dydt = [y[1], -y[0] - d*y[1]]
                    return dydt

                t = np.arange(0, 10, dt)
                y0 = [1, 0]
                solution = odeint(model, y0, t, args=(damping,))

                results.append({
                    'dt': dt,
                    'damping': damping,
                    'final_amplitude': abs(solution[-1, 0]),
                    'stability': is_stable(solution)
                })
    END_EXECUTE

    ANALYZE:
        COMPARE results ACROSS [time_step, damping_coefficient] WITH:
            DIMENSIONS: [stability, final_amplitude, computational_cost]
            OUTPUT_FORMAT: {
                optimal_configuration: TEXT,
                stability_boundaries: LIST OF TEXT,
                trade_offs: TEXT
            }
        END
END_EXPLORE

# Step 3: AI makes decision based on mathematical exploration
WEIGH simulation_configurations AGAINST requirements WITH:
    SOURCES: [exploration_results, accuracy_requirements, performance_constraints]
    OUTPUT_FORMAT: {
        selected_configuration: OBJECT { time_step: NUMBER, damping: NUMBER },
        rationale: TEXT
    }
END
```

In summary: let code handle computation, let typed reasoning operations handle interpretation and decision-making.

---

### 17. Execution Boundaries

Clear delineation between deterministic and intelligent execution ensures program reliability.

#### What AI Must Execute Deterministically

These operations must behave consistently every time:

1. **Variable Assignment:** `SET` / `LET` operations must behave consistently
2. **Control Flow Logic:** `IF` / `WHILE` / `FOR` must follow exact branching rules
3. **Input/Output Operations:** `GET` / `SEND` must attempt specified operations
4. **Comparison Results:** Same inputs must yield same boolean outputs
5. **Object Structure:** Property and method access must follow defined patterns

#### What AI May Handle Intelligently

These aspects allow for contextual adaptation:

1. **Underspecified Parameters:** Choosing appropriate defaults when values aren't explicit
2. **Error Recovery:** Deciding how to handle unexpected situations gracefully
3. **Optimization Decisions:** Improving performance without changing logical behavior
4. **Contextual Interpretation:** Understanding intent when natural language is ambiguous
5. **Creative Problem-Solving:** Generating solutions within specified constraints
6. **Reasoning Type Selection:** When INTELLIGENTLY is used, the engine selects the appropriate reasoning type via auto-classification (v0.8)

### 18. State-Aware Dynamic Boundaries

AILang maintains state that creates dynamic execution boundaries:

#### State-Dependent Limits

```ailang
SET daily_limit TO 1000
SET current_usage TO 0

FOR EACH request IN queue DO:
    IF current_usage + request.amount > daily_limit THEN:
        DEFER request TO next_day
    ELSE:
        PROCESS request
        INCREMENT current_usage BY request.amount
    END_IF
END_FOR
```

#### Progressive Authorization

```ailang
IF success_rate > 0.95 FOR last_100_operations THEN:
    EXPAND authority TO level_2_operations
ELSE IF error_rate > 0.10 THEN:
    RESTRICT authority TO read_only_mode
END_IF
```

#### Cascade Prevention

```ailang
# Prevent action cascades
IF actions_taken_for(entity) > threshold TODAY THEN:
    ESCALATE TO human_supervisor
    STOP_PROCESSING_FOR entity
END_IF
```

#### Compositional Limits

```ailang
WITHIN time_period(1_hour) ALLOW:
    MAXIMUM 10 external_api_calls
    MAXIMUM 100 database_updates
    MAXIMUM 50 customer_contacts
END_WITHIN
```

**Specification**: Boundaries can dynamically adjust based on program state, but must always remain within maximum defined limits. State-aware boundaries prevent cascade failures and resource exhaustion while allowing adaptive behavior within safe parameters.

---

### 19. Person Entities: Framework Overview

This section provides the conceptual framework and usage patterns needed to understand and work with Person entities at a high level.

**IMPORTANT: Person entities represent one of AILang's most sophisticated domain modeling capabilities. Due to the comprehensive nature of human behavioral modeling — encompassing cognitive systems, personality dynamics, social interactions, and group memberships — the detailed specifications for all Person subsystems are provided in the [Person Extension Document](https://github.com/pcoz/ailang/blob/main/AILang_Specification_Person_Extension.md).**

#### 19.1 Person Class Architecture

Person entities model humans across multiple dimensions:

- **Cognitive Systems**: Thought processes, speech patterns, and physical actions
- **Sensory Experience**: Multi-modal perception (vision, hearing, touch, smell, taste, proprioception, interoception)
- **Memory Systems**: Working memory, episodic memories, semantic knowledge, procedural skills, emotional associations
- **Personality Framework**: Three-dimensional model (Logos, Energiae, Ethos) that shapes behavior and responses
- **Social Interaction**: Relationship management, personality exchange mechanisms, group dynamics
- **Economic Awareness**: Financial understanding, possession management, purchase evaluation
- **Knowledge & Learning**: Domain expertise, learning strategies, skill acquisition
- **Goal-Directed Behavior**: Intelligent planning, adaptive navigation, circumstance-responsive decision-making
- **Identity & Contact**: Legal identifiers, contact information, digital identities, location tracking
- **Group Memberships**: Family, organizational, and social group affiliations with role-based behavior
- **Reasoning Profile** (v0.8): Primary and secondary reasoning types that shape how the person's think() and decide() methods process information

Use Person entities when you need to:
- Model individual human behavior with psychological depth
- Simulate social interactions with personality dynamics
- Track character development over time
- Represent agents with realistic cognitive/emotional constraints
- Model organizational hierarchies with human decision-makers
- Simulate group dynamics and social influence

**Core Architecture**

```ailang
CLASS Person:
    PROPERTIES:
        # Identity and Demographics
        id: unique_identifier
        name: text
        age: number
        gender: text

        # Cognitive and Behavioral Systems
        thought_system: ThoughtSystem
        speech_system: SpeechSystem
        action_system: ActionSystem

        # Experiential Systems
        experience_system: ExperienceSystem
        memory_system: MemorySystem

        # Personality and Social Systems
        personality: PersonalitySystem  # Logos, Energiae, Ethos
        interaction_system: InteractionSystem

        # Contextual Systems
        economic_system: EconomicSystem
        knowledge_system: KnowledgeSystem
        planning_system: PlanningSystem

        # Identity and Membership
        background: PersonBackground
        identity_contact: IdentityAndContactSystem
        group_membership_system: GroupMembershipSystem

        # Reasoning Profile (v0.8)
        reasoning_profile: ReasoningProfile

        current_state: PersonState
```

#### 19.2 Reasoning Profile for Person Entities (v0.8)

Person entities can specify PRIMARY_REASONING and SECONDARY_REASONING types that determine how their `think()` and `decide()` methods route through the reasoning operations defined in Section 8.

```ailang
CLASS ReasoningProfile:
    PROPERTIES:
        primary_reasoning: TEXT  # One of: WEIGH, DEDUCE, TRACE, COMPARE, SYNTHESIZE, RETRIEVE
        secondary_reasoning: TEXT
        reasoning_flexibility: TEXT IN ["rigid", "low", "moderate", "high", "fluid"]
        # How easily the person shifts between reasoning types
```

**Example:**

```ailang
CREATE Person attorney WITH:
    name: "Sarah Chen"
    reasoning_profile: {
        primary_reasoning: "DEDUCE",
        secondary_reasoning: "WEIGH",
        reasoning_flexibility: "low"
    }
    default_reality_context: legal_proceeding
END_CREATE

# When this person thinks or decides, operations route through DEDUCE
attorney.think(case_evidence)
# Internally: DEDUCE conclusions FROM case_evidence WITH attorney's worldview

attorney.decide(settlement_offer)
# Internally: DEDUCE optimal_response FROM settlement_offer AND legal_precedent
# Falls back to WEIGH when evaluating witness credibility
```

```ailang
CREATE Person diplomat WITH:
    name: "Ambassador Liu"
    reasoning_profile: {
        primary_reasoning: "SYNTHESIZE",
        secondary_reasoning: "WEIGH",
        reasoning_flexibility: "high"
    }
END_CREATE

# Diplomat naturally synthesizes competing positions
diplomat.think(treaty_negotiations)
# Internally: SYNTHESIZE positions INTO framework WITH diplomat's worldview

# High flexibility means the diplomat can shift reasoning types easily
diplomat.decide(crisis_response)
# May shift to TRACE for understanding causal chains in a crisis
```

#### 19.3 Core Systems Summary

**Cognitive Systems**

* ThoughtSystem: Conscious and subconscious thought processes, reflection, decision-making
* SpeechSystem: Verbal communication with tone, vocabulary, and linguistic patterns
* ActionSystem: Physical capabilities, skill learning, and action execution

**Experiential Systems**

* ExperienceSystem: Multi-sensory perception (vision, hearing, touch, smell, taste, proprioception, interoception)
* MemorySystem: Working memory, episodic memory, semantic memory, procedural memory, emotional memory

**Personality Framework (Logos-Energiae-Ethos)**

The personality system models three fundamental dimensions of human character:

* Logos: Rational principle, reasoning styles, logical consistency, intellectual curiosity
* Energiae: Active forces, drives, motivations, life force, creative energy
* Ethos: Moral character, values, principles, virtues, integrity

These three components interact dynamically, generating graded responses to events and shaping behavior through their integration.

**Social and Contextual Systems**

* InteractionSystem: Social skills, relationships, personality exchange mechanisms
* EconomicSystem: Financial awareness, possessions, budgeting, purchase evaluation
* KnowledgeSystem: Domain expertise, learning strategies, knowledge synthesis
* PlanningSystem: Goal management, intelligent navigation, adaptive execution

**Identity Systems**

* PersonBackground: Demographics, family history, life events, cultural background
* IdentityAndContactSystem: Legal identifiers, contact information, digital identities, privacy
* GroupMembershipSystem: Family, work, social group memberships and their influence

#### 19.4 Usage Patterns

**Basic Person Creation**

```ailang
CREATE Person alice WITH:
    name: "Alice Chen"
    age: 28
    gender: "female"
    background: {
        birth_place: "San Francisco",
        education: ["BS Computer Science", "MA Psychology"],
        languages: {english: 1.0, mandarin: 0.9}
    }
    reasoning_profile: {
        primary_reasoning: "SYNTHESIZE",
        secondary_reasoning: "COMPARE",
        reasoning_flexibility: "high"
    }
END_CREATE

# Initialize personality traits
SET alice.personality.logos.reasoning_style TO "analytical"
SET alice.personality.energiae.drives TO {achievement: 0.8, connection: 0.7}
SET alice.personality.ethos.core_values TO ["integrity", "growth", "compassion"]
```

**Person-to-Person Interaction**

```ailang
# Two persons interact with full personality exchange
SET conversation TO alice.interact_with_person(bob, meeting_context)

# The interaction includes:
# - Logos exchange (intellectual/reasoning styles)
# - Energiae exchange (energetic compatibility/resonance)
# - Ethos exchange (moral alignment/values)
# - Reasoning type negotiation (v0.8): whose reasoning profile dominates?
```

**Intelligent Goal Pursuit**

```ailang
# Person navigates toward goal with adaptive intelligence
alice.planning_system.decide_and_navigate(
    goal_description: "Learn advanced machine learning",
    constraints: {time: "3 months", budget: 1000}
)

# The system:
# - Assesses circumstances continuously (using alice's primary reasoning type)
# - Makes intelligent decisions at junctures
# - Adapts path based on outcomes
# - Learns from experience
```

**Group Context Activation**

```ailang
# Activate family context - behavior adjusts accordingly
SET family_context TO alice.group_membership_system.activate_group_context("family")

# Alice's speech, behavior, and cognition now reflect family role
alice.interact_with_family(family_context)
```

**Multi-Person Simulation**

```ailang
DEFINE PROCEDURE social_gathering WITH PARAMETERS [attendees, location]:
    FOR EACH person IN attendees DO:
        person.experience_system.perceive(environment)
    END_FOR

    WHILE gathering.active DO:
        # Persons interact, relationships evolve
        # Memories form, personalities influence each other
        # Each person's reasoning profile shapes their contributions (v0.8)
    END_WHILE
END_PROCEDURE
```

#### 19.5 Integration with AILang Constructs

Person entities seamlessly integrate with core language features:

**Deterministic Operations: Person state changes follow exact rules**

```ailang
INCREMENT alice.age BY 1
DECREMENT alice.action_system.energy_level BY 0.3
```

**Typed Reasoning Operations (v0.8): Decisions use the person's reasoning profile**

```ailang
# Uses alice's primary reasoning type (SYNTHESIZE)
alice.knowledge_system.SYNTHESIZE knowledge FROM ["psychology", "AI"] INTO integrated_understanding

# Explicit override: use COMPARE even though it's not alice's primary type
alice.knowledge_system.COMPARE frameworks AGAINST research_goals WITH:
    DIMENSIONS: [theoretical_depth, practical_applicability]
END
```

**Reality Contexts: Persons can have default reality contexts**

```ailang
CREATE Person therapist WITH:
    default_reality_context: psychodynamic_therapy
    reasoning_profile: {
        primary_reasoning: "TRACE",
        secondary_reasoning: "WEIGH",
        reasoning_flexibility: "moderate"
    }
END_CREATE
```

**Error Handling: Person operations can fail gracefully**

```ailang
TRY:
    alice.action_system.perform_action(complex_task, environment)
CATCH insufficient_skill:
    alice.knowledge_system.acquire_knowledge(required_skill, urgency: "high")
END_TRY
```

**Implementation Notes**

* State Persistence: Person state can be serialized and restored across sessions
* Scalability: Multiple persons can coexist and interact within programs
* Extensibility: New subsystems can be added through inheritance
* Deterministic Core: All state changes follow deterministic rules
* Intelligent Overlay: Decision-making uses bounded intelligence where specified
* Reasoning Profile: Person's reasoning type affects all intelligent operations performed by that person (v0.8)

For complete specifications of all Person subsystems, see the [Person Extension Document](https://github.com/pcoz/ailang/blob/main/AILang_Specification_Person_Extension.md).

---

### 20. Universal Space and Accomplishment Systems

AILang provides a unified framework for modeling navigation through structured domains — whether physical terrain, manufacturing processes, or institutional hierarchies. This section introduces **spaces** as formal structures that define what accomplishments are possible, and **journeys** as the actualization of these possibilities through intelligent navigation.

The framework is grounded in a transcendental perspective: spaces are not mere containers but the formal conditions that make accomplishment intelligible. By recognizing that diverse domains share the same underlying structure — staged progression toward objectives within possibility spaces — AILang enables consistent modeling across radically different content areas.

#### 20.0 Philosophical Foundation

This framework is grounded in a transcendental perspective: space is not merely a container but the formal structure that makes experience and accomplishment possible. AILang generalizes this — different domains have their own formal structures (spaces) that are the conditions of possibility for action and accomplishment within those domains.

**A Priori / A Posteriori / Synthesis.** The space structure (locations, pathways, prerequisites, rules) exists prior to any journey (a priori). The actual journey is empirical and contingent (a posteriori). Navigation requires synthesis: applying formal understanding of the space to the situation at hand to make intelligent decisions.

**Why one framework works across domains.** Physical journeying, manufacturing processes, and institutional advancement share the same formal pattern: staged progression within a possibility space toward objectives. The content differs; the form is identical.

#### 20.1 Conceptual Foundation

**Space as condition of possibility.** A space in AILang is a formal structure that makes certain kinds of accomplishment possible. It defines:
- **Locations/Stages** (positions that can be occupied/achieved)
- **Pathways** (permitted transitions)
- **Prerequisites** (what must be true to access a stage)
- **Rules** (constraints governing movement)

**Journey as actualization within space.** A journey is the empirical actualization of possibilities within that structure, involving a **navigator**, **circumstances**, **decisions**, and resulting **accomplishments**.

**Types of spaces (same form, different content).**
- **Physical Space:** Geographic locations; accomplishment = arrival.
- **Process Space:** Production/service stages; accomplishment = stage completion.
- **Organizational Space:** Institutional positions; accomplishment = attained authorization/role.
- **Abstract Spaces:** States in conceptual domains; accomplishment = target state achieved.

#### 20.2 Core Space Framework

The following classes define the foundational machinery for all space types. The `Space` class captures the formal structure (locations, pathways, rules), while `Location` represents positions that can be accomplished. `SpaceCharacteristics` describes structural properties, and `NavigationRules` governs what transitions are possible.

Core classes define the **formal structure (a priori)**, **empirical assessment (a posteriori)**, and **navigation rules (synthesis)**.

```ailang
CLASS Space:
    PROPERTIES:
        space_id: text
        space_type: text  # "physical", "process", "organizational", "abstract"
        space_name: text

        # A priori structure
        locations: MAP[location_id -> Location]
        pathways: GRAPH[location_id -> LIST[location_id]]
        entry_points: LIST[location_id]
        objectives: LIST[location_id]  # Target accomplishments

        space_characteristics: SpaceCharacteristics
        navigation_rules: NavigationRules

    CLASS Location:
        # A position/stage/state in the formal structure
        PROPERTIES:
            location_id: text
            location_type: text  # "stage", "position", "state", "waypoint"
            name: text
            description: text

            # Formal significance within space structure
            is_objective: boolean
            is_milestone: boolean
            accomplishment_value: text  # "critical","major","significant","minor"

            # A priori accessibility relations
            prerequisites: LIST
            enables: LIST

            properties: MAP[property -> value]

        METHOD describe_accomplishment():
            # v0.8: Use SYNTHESIZE for rich accomplishment description
            RETURN SYNTHESIZE accomplishment_description FROM:
                SOURCES: [this, this.accomplishment_value, space_context, this.enables]
                OUTPUT_FORMAT: { description: TEXT, significance: TEXT, unlocks: LIST }
            END
        END_METHOD
    END_CLASS

    CLASS SpaceCharacteristics:
        PROPERTIES:
            dimensionality: text  # "linear","branching","networked","multidimensional"
            connectivity: text    # "fully_connected","sparse","hierarchical","sequential"
            reversibility: text   # "fully_reversible","partially_reversible","irreversible"
            progress_measurability: text  # "precise","approximate","qualitative"
            completion_criteria: text
            static_or_dynamic: text  # "static","evolving","reactive","adaptive"
            time_dependency: text    # "timeless","time_sensitive","deadline_driven"
    END_CLASS

    CLASS NavigationRules:
        PROPERTIES:
            movement_constraints: LIST
            transition_requirements: MAP[pathway -> requirements]
            authorization_model: text  # "open","restricted","role_based","achievement_gated"

        METHOD can_transition(from_location, to_location, navigator):
            SET pathway TO find_pathway(from_location, to_location)
            IF pathway NOT_EXISTS THEN:
                RETURN {allowed: false, reason: "no_pathway_in_space_structure"}
            END_IF

            SET requirements TO this.transition_requirements[pathway]
            SET requirements_met TO evaluate_requirements(requirements, navigator)

            RETURN {
                allowed: requirements_met.all_satisfied,
                reason: requirements_met.explanation,
                missing_prerequisites: requirements_met.unsatisfied
            }
        END_METHOD
    END_CLASS

    METHOD get_accomplishment_status(navigator):
        RETURN {
            locations_achieved: navigator.achieved_locations,
            current_location: navigator.current_location,
            objectives_completed: count_completed_objectives(navigator),
            objectives_remaining: count_remaining_objectives(navigator),
            progress_assessment: assess_overall_progress(navigator),
            next_significant_accomplishments: identify_next_milestones(navigator)
        }
    END_METHOD
END_CLASS
```

#### 20.3 Physical Space Specification

Physical space extends the core framework to model geographic locations and movement through terrain.

```ailang
CLASS PhysicalSpace EXTENDS Space:
    PROPERTIES:
        coordinate_system: text  # "lat_long","cartesian","address","landmark_based"
        terrain_data: TerrainData
        infrastructure: InfrastructureMap

    CLASS PhysicalLocation EXTENDS Location:
        PROPERTIES:
            coordinates: GeographicCoordinates OR Address
            altitude: number
            accessibility: text
            terrain_type: text
            climate_zone: text
            local_amenities: LIST

        METHOD get_distance_to(other_location):
            IF both_have_coordinates THEN:
                RETURN calculate_haversine_distance(this.coordinates, other_location.coordinates)
            ELSE:
                RETURN estimate_distance_from_infrastructure()
            END_IF
        END_METHOD
    END_CLASS

    CLASS GeographicCoordinates:
        PROPERTIES:
            latitude: number
            longitude: number
            altitude: number
            coordinate_system: text
    END_CLASS

    CLASS TerrainData:
        PROPERTIES:
            terrain_difficulty: MAP[region -> difficulty_descriptor]
            natural_barriers: LIST
            traversable_routes: LIST
    END_CLASS

    METHOD calculate_physical_journey(origin, destination, constraints):
        SET available_routes TO find_physical_routes(origin, destination, this.infrastructure)
        # v0.8: Use COMPARE for route selection
        SET optimal_route TO COMPARE available_routes AGAINST constraints WITH:
            DIMENSIONS: [distance, terrain_difficulty, travel_time, cost]
            OUTPUT_FORMAT: { selected_route: OBJECT, rationale: TEXT }
        END

        RETURN {
            route: optimal_route,
            estimated_duration: calculate_travel_time(optimal_route),
            distance: calculate_total_distance(optimal_route),
            waypoints: optimal_route.significant_locations,
            accomplishments_along_route: identify_milestone_locations(optimal_route)
        }
    END_METHOD
END_CLASS
```

#### 20.4 Process Space Specification

Process space models production, service delivery, and project execution as formal stage structures.

```ailang
CLASS ProcessSpace EXTENDS Space:
    PROPERTIES:
        process_type: text  # "manufacturing","service_delivery","project","approval"
        process_owner: text
        quality_gates: LIST[QualityGate]

    CLASS ProcessStage EXTENDS Location:
        PROPERTIES:
            stage_number: number
            stage_type: text  # "input","transformation","inspection","output","decision"

            # Formal requirements (a priori)
            required_inputs: LIST
            transformation: text
            expected_outputs: LIST
            duration_estimate: duration
            resource_requirements: LIST

            # Quality criteria
            completion_criteria: LIST
            quality_standards: LIST
            inspection_required: boolean

            # Dependencies (a priori)
            depends_on_stages: LIST[stage_id]
            enables_stages: LIST[stage_id]
            parallel_allowed: boolean

        METHOD accomplish_stage(inputs, resources):
            IF NOT all_prerequisites_met() THEN:
                RETURN {success: false, reason: "prerequisites_not_met"}
            END_IF

            SET input_validation TO validate_inputs(inputs, this.required_inputs)
            IF NOT input_validation.valid THEN:
                RETURN {success: false, reason: "invalid_inputs", details: input_validation}
            END_IF

            SET transformation_result TO EXECUTE this.transformation WITH inputs, resources
            SET output_validation TO validate_outputs(transformation_result, this.expected_outputs)
            IF NOT output_validation.valid THEN:
                RETURN {success: false, reason: "outputs_failed_quality", details: output_validation}
            END_IF

            RETURN {
                success: true,
                outputs: transformation_result
            }
        END_METHOD
    END_CLASS

    METHOD execute_process(objective, starting_inputs, available_resources):
        SET current_stage TO entry_points[0]
        SET accomplished_stages TO []
        SET process_state TO {
            current_stage: current_stage,
            intermediate_outputs: starting_inputs,
            resources_consumed: [],
            quality_assessments: []
        }

        WHILE NOT process_objective_achieved(process_state) DO:
            # v0.8: Use COMPARE for stage selection
            SET next_stage TO COMPARE available_next_stages AGAINST process_objectives WITH:
                DIMENSIONS: [alignment_with_objective, resource_availability, dependency_satisfaction]
                OUTPUT_FORMAT: { selected_stage: OBJECT, rationale: TEXT }
            END

            SET stage_result TO next_stage.accomplish_stage(
                process_state.intermediate_outputs,
                allocated_resources
            )

            IF stage_result.success THEN:
                APPEND next_stage.location_id TO accomplished_stages
                UPDATE process_state WITH stage_result.outputs

                IF quality_gate_at(next_stage) THEN:
                    SET gate_passage TO evaluate_quality_gate(process_state, next_stage)
                    IF NOT gate_passage.approved THEN:
                        RETURN {
                            status: "blocked_at_quality_gate",
                            gate: gate_passage.gate_id,
                            deficiencies: gate_passage.deficiencies,
                            accomplished_so_far: accomplished_stages
                        }
                    END_IF
                END_IF
            ELSE:
                IF stage_result.rework_required THEN:
                    EXECUTE rework_procedure(stage_result.deficiencies)
                ELSE:
                    RETURN {
                        status: "process_failed",
                        failed_stage: next_stage.location_id,
                        reason: stage_result.reason,
                        accomplished_so_far: accomplished_stages
                    }
                END_IF
            END_IF
        END_WHILE

        RETURN {
            status: "objective_accomplished",
            final_outputs: process_state.intermediate_outputs,
            stages_accomplished: accomplished_stages,
            total_duration: calculate_elapsed_time(),
            resources_consumed: process_state.resources_consumed,
            quality_record: process_state.quality_assessments
        }
    END_METHOD
END_CLASS
```

#### 20.5 Organizational Space Specification

Organizational space captures institutional hierarchies, positions, and authority relationships.

```ailang
CLASS OrganizationalSpace EXTENDS Space:
    PROPERTIES:
        organization_type: text
        hierarchy: OrganizationalHierarchy
        authorization_structure: AuthorizationStructure
        institutional_culture: InstitutionalCulture

    CLASS OrganizationalPosition EXTENDS Location:
        PROPERTIES:
            position_title: text
            position_code: text
            department: text
            division: text
            hierarchy_level: number

            # Formal relationships (a priori)
            reporting_to: position_id
            reporting_from: LIST[position_id]
            lateral_peers: LIST[position_id]
            authority_scope: LIST

            # Access and capability granted by the position
            can_authorize: LIST
            access_privileges: LIST
            budget_authority: number
            hiring_authority: boolean
            policy_setting_authority: LIST

            # Requirements to attain the position (a priori)
            qualifications_required: LIST
            experience_required: duration
            clearance_level: text
            certifications_required: LIST

        METHOD can_authorize_action(action, ctx):
            # v0.8: Use DEDUCE for authorization determination
            DEDUCE authorization_result FROM action AND this.authority_scope WITH:
                MUST_INCLUDE: [authority_type_check, scope_check, budget_check]
                OUTPUT_FORMAT: {
                    can_authorize: BOOLEAN,
                    reason: TEXT,
                    escalation_required: BOOLEAN,
                    escalate_to: TEXT
                }
            END
        END_METHOD

        METHOD assess_accomplishment_difficulty(candidate, current_position):
            # v0.8: Use COMPARE for assessment
            RETURN COMPARE candidate_qualifications AGAINST position_requirements WITH:
                DIMENSIONS: [qualifications, experience, certifications, cultural_fit]
                OUTPUT_FORMAT: {
                    assessment: TEXT,
                    gaps: LIST,
                    estimated_timeline: TEXT,
                    feasibility: QUALITATIVE IN ["impossible","highly_unlikely","challenging","achievable","straightforward"]
                }
            END
        END_METHOD
    END_CLASS

    CLASS OrganizationalHierarchy:
        PROPERTIES:
            levels: number
            structure_type: text  # "flat","tall","matrix","networked"
            reporting_chains: GRAPH[position_id -> LIST[position_id]]
            span_of_control: MAP[position_id -> number]
            typical_advancement_paths: MAP[position_id -> LIST[position_id]]
            lateral_movement_allowed: boolean
            cross_functional_paths: LIST

        METHOD find_common_authority(p1, p2):
            RETURN compute_lca_in_reporting_graph(p1, p2)
        END_METHOD

        METHOD identify_advancement_path(current_position, target_position):
            IF target_position IN typical_advancement_paths[current_position] THEN:
                RETURN {path_type: "direct_promotion", intermediate_positions: []}
            END_IF
            # v0.8: Use TRACE for career path construction
            RETURN TRACE career_path FROM current_position TO target_position WITH:
                DIRECTION: FORWARD
                MUST_INCLUDE: [intermediate_positions, skill_requirements_at_each_step]
                OUTPUT_FORMAT: {
                    path: LIST OF TEXT,
                    estimated_duration: TEXT,
                    critical_transitions: LIST OF TEXT
                }
            END
        END_METHOD
    END_CLASS

    CLASS AuthorizationStructure:
        PROPERTIES:
            authorization_types: LIST[AuthorizationType]
            delegation_rules: DelegationRules
            signature_authority: MAP[position_id -> signature_limits]

        CLASS AuthorizationType:
            PROPERTIES:
                type_name: text
                authorization_levels: MAP[level -> threshold]
                required_clearance: text
                delegation_allowed: boolean

            METHOD get_required_level_for(action):
                RETURN determine_level_from_thresholds(action.magnitude, authorization_levels)
            END_METHOD
        END_CLASS

        CLASS DelegationRules:
            PROPERTIES:
                delegation_depth: number
                requires_written_delegation: boolean
                delegation_time_limits: duration
                revocable: boolean

            METHOD can_delegate(delegating_position, receiving_position, authority):
                IF NOT authority.delegation_allowed THEN
                    RETURN {can_delegate: false, reason: "authority_not_delegable"}
                END_IF
                IF hierarchy_distance(delegating_position, receiving_position) > delegation_depth THEN
                    RETURN {can_delegate: false, reason: "exceeds_delegation_depth"}
                END_IF
                RETURN {can_delegate: true,
                        requires_written: this.requires_written_delegation,
                        time_limit: this.delegation_time_limits}
            END_METHOD
        END_CLASS

        METHOD construct_approval_chain(action, requester_position):
            SET req_level TO determine_required_level(action)
            RETURN build_chain_via_hierarchy(req_level, requester_position)
        END_METHOD
    END_CLASS

    CLASS InstitutionalCulture:
        PROPERTIES:
            formality_level: text
            advancement_philosophy: text
            networking_importance: text
            sponsor_requirement: text
            visibility_importance: text
            politics: MAP[text -> value]
    END_CLASS

    METHOD navigate_institutional_advancement(person, target_position):
        SET feasibility TO target_position.assess_accomplishment_difficulty(person, person.current_organizational_position)
        IF feasibility.assessment IN ["impossible","highly_unlikely"] THEN:
            RETURN {advancement_viable: false, reason: feasibility.explanation,
                    missing: feasibility.deficiencies}
        END_IF
        SET path TO hierarchy.identify_advancement_path(person.current_organizational_position, target_position)
        IF path.intermediate_positions.EMPTY THEN:
            RETURN plan_direct_promotion(person, target_position)
        ELSE:
            RETURN plan_multi_step_advancement(person, path.intermediate_positions, target_position)
        END_IF
    END_METHOD

    METHOD navigate_organizational_approval(request, requester_position):
        SET chain TO authorization_structure.construct_approval_chain(request, requester_position)
        RETURN execute_approval_chain(chain, request)
    END_METHOD
END_CLASS
```

---

#### 20.6 Journey and Navigation Framework

The Journey framework unifies navigation across all space types by implementing the synthesis of formal structure with empirical circumstances.

```ailang
CLASS Journey:
    PROPERTIES:
        journey_id: text
        space: Space
        navigator: Navigator
        origin: location_id
        destination: location_id OR objective_description
        route: Route
        current_location: location_id
        accomplished_locations: LIST[location_id]
        progress: JourneyProgress
        journey_type: text    # "planned","exploratory","adaptive","forced"
        journey_status: text  # "not_started","in_progress","paused","completed","abandoned"

    CLASS Navigator:
        PROPERTIES:
            navigator_id: text
            navigator_type: text  # "person","entity","system","process"
            capabilities: LIST
            resources: LIST
            constraints: LIST
            navigation_preference: text   # "efficient","scenic","risk_averse","exploratory"
            decision_making_style: text   # "analytical","intuitive","adaptive"

        METHOD can_accomplish(location, state):
            # v0.8: Use COMPARE for capability assessment
            RETURN COMPARE navigator_capabilities AGAINST location_requirements WITH:
                DIMENSIONS: [skills, resources, prerequisites]
                OUTPUT_FORMAT: {
                    capable: BOOLEAN,
                    reason: TEXT,
                    missing: LIST
                }
            END
        END_METHOD
    END_CLASS

    CLASS Route:
        PROPERTIES:
            route_type: text  # "direct","mandatory_waypoints","flexible"
            waypoints: LIST[location_id]
            alternatives: LIST[AlternativeRoute]
            estimated_duration: duration
            estimated_cost: number OR "variable"
            difficulty_assessment: text

        METHOD adapt(current_location, circumstances):
            SET remaining TO waypoints_after(current_location)
            # v0.8: Use WEIGH for route evaluation
            SET should_change TO WEIGH route_options ON suitability WITH:
                SOURCES: [remaining, circumstances, this.alternatives]
                OUTPUT_FORMAT: { should_change: BOOLEAN, rationale: TEXT }
            END
            IF should_change THEN
                RETURN TRACE optimal_path FROM current_location TO journey.destination WITH:
                    DIRECTION: FORWARD
                    MUST_INCLUDE: [circumstance_adaptation, preference_alignment]
                    OUTPUT_FORMAT: { new_route: OBJECT }
                END
            END_IF
            RETURN this
        END_METHOD
    END_CLASS

    CLASS JourneyProgress:
        PROPERTIES:
            locations_accomplished: number
            total_locations: number
            progress_percentage: number
            on_schedule: boolean
            within_budget: boolean
            quality_maintained: boolean
            obstacles: LIST
            deviations: LIST

        METHOD assess():
            # v0.8: Use SYNTHESIZE for progress assessment
            RETURN SYNTHESIZE progress_indicators INTO assessment WITH:
                SOURCES: [this.progress_percentage, this.on_schedule, this.within_budget,
                          this.quality_maintained, this.obstacles, this.deviations]
                OUTPUT_FORMAT: {
                    overall_status: QUALITATIVE IN ["on_track","at_risk","behind","critical"],
                    key_findings: LIST OF TEXT,
                    recommended_actions: LIST OF TEXT
                }
            END
        END_METHOD
    END_CLASS

    METHOD begin():
        SET current_location TO origin
        APPEND origin TO accomplished_locations
        SET journey_status TO "in_progress"
        RETURN {started: true, start: origin, route: this.route}
    END_METHOD

    METHOD advance():
        SET next_loc TO route.next_waypoint_after(current_location)
        SET capable TO navigator.can_accomplish(space.locations[next_loc], {progress: this.progress})
        IF NOT capable.capable THEN
            RETURN {failed: true, reason: capable.reason, missing: capable.missing}
        END_IF

        SET allowed TO space.navigation_rules.can_transition(current_location, next_loc, navigator)
        IF NOT allowed.allowed THEN
            RETURN {blocked: true, reason: allowed.reason, missing_prereqs: allowed.missing_prerequisites}
        END_IF

        SET result TO accomplish_location(space.locations[next_loc], navigator, {progress: this.progress})
        IF NOT result.success THEN
            RETURN {accomplishment_failed: true, reason: result.reason, retry_possible: result.can_retry}
        END_IF

        SET current_location TO next_loc
        APPEND next_loc TO accomplished_locations
        UPDATE progress
        RETURN {advanced: true, location: next_loc, assessment: progress.assess()}
    END_METHOD

    METHOD navigate_intelligently_to_destination():
        WHILE current_location != destination AND journey_status == "in_progress" DO:
            SET circumstances TO assess_current_circumstances()
            SET route TO route.adapt(current_location, circumstances)
            SET step TO advance()
            IF step.failed OR step.blocked OR step.accomplishment_failed THEN:
                CALL handle_advancement_issue(step, circumstances)
            END_IF
        END_WHILE
        IF current_location == destination THEN:
            SET journey_status TO "completed"
            RETURN {completed: true, path: accomplished_locations, summary: progress.assess()}
        ELSE:
            RETURN {completed: false, status: journey_status, progress: progress.assess()}
        END_IF
    END_METHOD
END_CLASS
```

---

#### 20.7 Synthesis in Action: Complete Examples

##### Example A: Physical Journey

```ailang
CREATE PhysicalSpace road_net WITH:
    coordinate_system: "lat_long"
    locations: { sf:{}, slc:{}, denver:{}, chicago:{} }
    pathways: { sf->slc:[], slc->denver:[], denver->chicago:[] }
END_CREATE

CREATE Person driver WITH:
    capabilities:["driving"], resources:["vehicle","budget:1000","time:7d"],
    navigation_preference:"efficient"
END_CREATE

CREATE Journey xcountry WITH:
    space: road_net, navigator: driver, origin: sf, destination: chicago
END_CREATE

xcountry.begin()
SET circumstances TO {weather:"heavy_snow_denver", road_status:"I-76_closed"}
SET route2 TO xcountry.route.adapt(xcountry.current_location, circumstances)
xcountry.navigate_intelligently_to_destination()
```

##### Example B: Process Journey

```ailang
CREATE ProcessSpace widget WITH:
    stages: { raw: {}, fab: {depends_on:[raw]}, asm: {depends_on:[fab]}, qc:{depends_on:[asm]} }
END_CREATE

CREATE Journey build WITH:
    space: widget, navigator: production_team, origin: raw, destination: qc
END_CREATE

SET dev TO {tolerance_out:0.15}

# v0.8: Use WEIGH for rework vs proceed decision
WEIGH rework_decision ON quality_outcome WITH:
    SOURCES: [{formal_tolerance: "0.1mm", actual_deviation: dev}, quality_standards]
    OUTPUT_FORMAT: { decision: TEXT IN ["rework", "proceed"], rationale: TEXT }
END

APPLY decision; build.navigate_intelligently_to_destination()
```

##### Example C: Organizational Journey

```ailang
CREATE OrganizationalSpace tech_co WITH:
    hierarchy:{typical_advancement_paths:{junior->[senior]}}
END_CREATE

CREATE Person sarah WITH:
    current_position: junior, qualifications:["BS_CS"], years_experience:1
    reasoning_profile: { primary_reasoning: "DEDUCE", secondary_reasoning: "COMPARE" }
END_CREATE

SET plan TO tech_co.navigate_institutional_advancement(sarah, director)
# plan likely multi-step: junior -> senior -> manager -> director
```

---

#### 20.8 The Kantian Pattern Across All Spaces

1) **A Priori Structure (Formal Conditions)**
- Physical: locations and spatial relations
- Process: stages and dependencies
- Organizational: positions and authority relations
- Abstract: states and transformation rules

2) **A Posteriori Content (Empirical Actualization)**
- Physical: terrain, weather, fatigue, breakdowns
- Process: real inputs, machine performance, quality outcomes
- Organizational: qualifications, performance evidence, politics, culture
- Abstract: actual states, observed constraints

3) **Synthesis (Intelligent Navigation)**
- Apply formal understanding to empirical reality to choose routes, execute stages, gain approvals, or transform states.
- v0.8: Synthesis uses typed reasoning operations — COMPARE for route selection, TRACE for path construction, WEIGH for decisions under uncertainty, DEDUCE for rule application.

4) **Accomplishment (Actualization)**
- Arrival at destination; completion of stage; attainment of position/authorization; achievement of target state.

#### 20.9 Implementation Principles

When implementing space and journey systems, respect the Kantian structure.

##### 1) Define Formal Structure First (A Priori)
- What locations/stages/positions exist?
- What are their relationships and pathways?
- What are the formal requirements, constraints, and completion criteria?
- What authorization rules and limits apply (if any)?
- How is progress assessed in principle?

##### 2) Model Empirical Content (A Posteriori)
- What circumstances can actually occur in this domain?
- What capabilities and resources does the navigator have right now?
- What obstacles, risks, or environmental conditions appear?
- What measurements and evidence can be observed?

##### 3) Implement Synthesis (Intelligent Navigation)
- How do structural constraints limit what is possible?
- How do empirical circumstances shape which option is prudent?
- How are adaptations triggered and carried out without violating structure?
- What are the re-synthesis triggers after a failure or change?
- v0.8: Which reasoning types are most appropriate at each synthesis point?

##### 4) Track Accomplishment (Actualization)
- What has been formally accomplished so far?
- What remains formally possible but not yet actualized?
- How does empirical progress compare to formal expectations?
- What lessons were learned from deviations and failures?

#### 20.10 Advanced Synthesis Patterns

##### Pattern 1: Formal Impossibility vs Empirical Infeasibility

```ailang
METHOD evaluate_accomplishment_possibility(space, target_location, navigator):
    # Step 1 -- Formal possibility (a priori)
    SET formal_check TO space.navigation_rules.can_transition(
        navigator.current_location, target_location, navigator
    )
    IF NOT formal_check.allowed THEN:
        RETURN {
            possible: false,
            type: "formal_impossibility",
            reason: formal_check.reason,
            remedy: "requires_change_to_space_structure"
        }
    END_IF

    # Step 2 -- Empirical feasibility (a posteriori)
    SET empirical_check TO navigator.can_accomplish(
        space.locations[target_location], {progress: navigator.progress}
    )
    IF NOT empirical_check.capable THEN:
        RETURN {
            possible: true, feasible: false, type: "empirical_infeasibility",
            reason: empirical_check.reason,
            required_changes: empirical_check.missing,
            may_become_feasible: true
        }
    END_IF

    RETURN { possible: true, feasible: true, type: "accomplishable" }
END_METHOD
```

##### Pattern 2: Multiple Valid Syntheses

```ailang
METHOD generate_valid_syntheses(space, navigator, objective, circumstances):
    SET routes TO space.find_all_formal_routes(navigator.current_location, objective)
    SET viable TO []
    FOR EACH r IN routes DO:
        # v0.8: Use COMPARE for multi-dimensional route evaluation
        SET s TO COMPARE route_attributes AGAINST navigator_priorities WITH:
            DIMENSIONS: [time, cost, risk, quality]
            OUTPUT_FORMAT: { viable: BOOLEAN, scores: OBJECT, rationale: TEXT }
        END
        IF s.viable THEN: APPEND s TO viable END_IF
    END_FOR
    RETURN {
        valid: viable,
        fastest: select_by(viable, "time"),
        cheapest: select_by(viable, "cost"),
        safest: select_by(viable, "risk"),
        best_quality: select_by(viable, "quality"),
        recommended: WEIGH viable_options ON overall_suitability WITH:
            SOURCES: viable
            OUTPUT_FORMAT: { selected: OBJECT, rationale: TEXT }
        END
    }
END_METHOD
```

##### Pattern 3: Synthesis Failure and Recovery

```ailang
METHOD handle_synthesis_failure(space, initial_synthesis, failure_point, failure_reason):
    SET learned TO extract_constraints_from_failure(failure_reason)
    SET updated TO update_empirical_model(initial_synthesis.empirical_assumptions, learned)

    # v0.8: Use TRACE to understand failure and COMPARE for recovery options
    SET failure_analysis TO TRACE failure_chain FROM failure_point WITH:
        DIRECTION: BACKWARD
        OUTPUT_FORMAT: { root_cause: TEXT, contributing_factors: LIST }
    END

    SET recovery_options TO COMPARE recovery_strategies AGAINST constraints WITH:
        DIMENSIONS: [feasibility, cost, time, objective_preservation]
        OUTPUT_FORMAT: { strategies: LIST OF OBJECT { strategy: TEXT, feasibility: QUALITATIVE } }
    END

    MATCH best_recovery.strategy WITH:
        CASE "alternative_route": RETURN {strategy: "route_change", route: recovery.route}
        CASE "modify_objective": RETURN {strategy: "objective_modification", new_objective: recovery.objective}
        CASE "acquire_capabilities": RETURN {strategy: "capability_acquisition", plan: recovery.plan}
        CASE "wait": RETURN {strategy: "temporal_delay", until: recovery.until}
        CASE "abandon": RETURN {strategy: "abandon_or_transform", lessons: recovery.lessons}
    END_MATCH
END_METHOD
```

##### Pattern 4: Formal Structure Evolution

```ailang
METHOD handle_space_structure_change(space, structural_change):
    MATCH structural_change.type WITH:
        CASE "new_location": ADD structural_change.location TO space.locations
                              UPDATE space.pathways WITH structural_change.connections
                              NOTIFY active_journeys OF "new_formal_possibility"
        CASE "remove_location": REMOVE structural_change.location FROM space.locations
                                PRUNE space.pathways OF structural_change.location
                                FORCE_RESYNTHESIZE journeys_using(structural_change.location)
        CASE "prerequisites_changed": UPDATE space.locations[structural_change.location].prerequisites
                                      REEVALUATE feasibility FOR all_active_journeys
        CASE "new_pathway": ADD structural_change.pathway TO space.pathways
                            NOTIFY active_journeys OF "new_route_available"
    END_MATCH
END_METHOD
```

##### Pattern 5: Cross-Space Synthesis

```ailang
METHOD synthesize_multi_space_journey(spaces, navigator, compound_objective):
    SET components TO decompose_into_space_components(compound_objective)

    # v0.8: Use SYNTHESIZE for cross-space coordination
    SET coordination TO SYNTHESIZE space_requirements INTO unified_plan WITH:
        SOURCES: [find_cross_space_dependencies(components),
                  align_deadlines(components),
                  identify_shared_resources(components)]
        OUTPUT_FORMAT: {
            coordination_plan: TEXT,
            dependencies: LIST,
            critical_path: LIST
        }
    END

    RETURN TRACE execution_path FROM current_state TO compound_objective WITH:
        DIRECTION: FORWARD
        MUST_INCLUDE: [space_transitions, resource_allocation, timing_constraints]
        OUTPUT_FORMAT: { plan: OBJECT, estimated_duration: TEXT }
    END
END_METHOD
```

#### 20.11 Philosophical Implications for AI Systems

##### 1) Understanding Requires Both Structure and Content

```ailang
METHOD navigate_purely_formally(space, current, destination):
    RETURN shortest_path_in_graph(space.pathways, current, destination)
END_METHOD  # Ignores empirical reality.

METHOD navigate_purely_empirically(circumstances):
    RETURN respond_to_current_conditions(circumstances)
END_METHOD  # Lacks structural understanding.

METHOD navigate_with_synthesis(space, navigator, circumstances, objective):
    # v0.8: Synthesis uses typed reasoning appropriate to the situation
    RETURN WEIGH navigation_options ON suitability WITH:
        SOURCES: [space.formal_structure, circumstances, navigator.capabilities, objective]
        OUTPUT_FORMAT: { plan: OBJECT, rationale: TEXT }
    END
END_METHOD  # Adequate.
```

##### 2) Intelligence Operates at the Synthesis Layer

```ailang
CLASS StructureKnowledge: PROPERTIES: space_definitions, formal_rules, relations END_CLASS
CLASS EmpiricalPerception: PROPERTIES: observations, measurements, conditions END_CLASS
CLASS SyntheticIntelligence:
    PROPERTIES: structure: StructureKnowledge, perception: EmpiricalPerception, engine: SynthesisEngine
    METHOD navigate_intelligently():
        # v0.8: Synthesis composes multiple reasoning types
        RETURN SYNTHESIZE navigation_decision FROM:
            SOURCES: [structure, perception]
            OUTPUT_FORMAT: { decision: OBJECT, reasoning_chain: LIST }
        END
    END_METHOD
END_CLASS
```

##### 3) Learning Occurs Through Failed Synthesis

```ailang
METHOD learn_from_synthesis_failure(attempt, outcome):
    SET gap TO diff(attempt.assumptions, outcome.revealed_reality)
    UPDATE empirical_model WITH gap
    RETURN {new_knowledge: gap, source: "failed_actualization"}
END_METHOD
```

##### 4) Deterministic vs Intelligent Operations (Kantian Mapping)
- **Deterministic (analytic / a priori):** assignment, arithmetic, pure graph traversal, static validation.
- **Intelligent (synthetic / a posteriori):** route selection, adaptation, evaluation, decisions under uncertainty.
- **v0.8 addition:** Each intelligent synthesis operation is typed — COMPARE for multi-attribute evaluation, TRACE for causal analysis, WEIGH for authority-based decisions, DEDUCE for rule application, SYNTHESIZE for perspective integration, RETRIEVE for fact lookup.


#### 20.12 Implementation Checklist

**A Priori Structure**
- Locations/stages/positions defined; relationships/pathways explicit.
- Prerequisites, constraints, completion criteria documented.
- Authorization rules and limits mapped; space characteristics categorized.

**A Posteriori Content**
- Circumstances observable; capabilities/resources assessable.
- Environmental conditions monitored; progress empirically measurable.
- Failure reasons diagnosable with evidence capture.

**Synthesis**
- Decision points identified; integration logic specified.
- Adaptation and re-synthesis mechanisms defined.
- Learning from failure enabled; multiple valid syntheses considered.
- v0.8: Reasoning types specified at each synthesis point.

**Accomplishment**
- Formal accomplishment recognized; empirical progress measured.
- Deviations tracked; lessons learned captured; success criteria evaluated.
- Journey summaries produced for auditability and learning loops.


#### 20.13 Conclusion: Space as Transcendental Structure

AILang's Space and Journey framework is more than a modeling convenience — it encodes the **transcendental conditions of purposive action**.
- *A Priori:* domain structure (what is formally possible).
- *A Posteriori:* empirical content (what is actually encountered).
- *Synthesis:* intelligent navigation (how structure is applied to reality).
- *Accomplishment:* realized outcomes (formal possibilities actualized).

By honoring this structure, AI systems can model physical logistics, operational processes, and institutional navigation with **one coherent machinery**, cleanly distinguishing **formal impossibility** from **empirical infeasibility**, enabling **adaptation and learning**, and producing **auditably intelligent** decisions. With v0.8's typed reasoning operations, the synthesis layer gains explicit computational structure — each decision point activates the appropriate neural pathways for the specific type of reasoning required.

---

### 21. Matter Entities: Framework Overview

This section provides the conceptual framework and usage patterns needed to understand and work with Matter entities at a high level.

**IMPORTANT: Matter entities represent one of AILang's most sophisticated domain modeling capabilities for representing human concerns and their multi-level abstraction structure. Due to the comprehensive nature of categorical cognition, abstraction level dynamics, actor positioning, lifecycle management, and conceptual mediation — the detailed specifications for all Matter subsystems are provided in the [Matter Extension Document](https://github.com/pcoz/ailang/blob/main/AILang_Specification_Matter_Extension.md).**

#### 21.1 Matter Class Architecture

Matter entities model units of human concern that exist at the intersection of objective reality and subjective experience. Matters are how humans structure their engagement with reality through categorical constructs that organize attention, action, and understanding.

**Critical Insight: A matter cannot be fully defined or understood at its own level of abstraction.** Definition and verification require vertical movement through abstraction levels — moving downward to concrete grounding and upward to categorical frameworks.

Use Matter entities when you need to:
- Model projects, initiatives, or organizational efforts with proper abstraction structure
- Represent concerns that evolve through lifecycle stages (recognition, becoming, completion, memorial)
- Track how actors positioned at different levels (IN-system vs ON-system) engage with the same matter
- Manage the translation from abstract intentions to concrete artifacts (corporealisation)
- Preserve patterns after matter cessation through multi-level perpetuation
- Validate claims about matters through adjacent-level checking
- Understand how conceptual frameworks mediate actor engagement across abstraction levels

**Core Architecture**

```ailang
CLASS Matter:
    PROPERTIES:
        # Identity and Classification
        matter_id: unique_identifier
        matter_name: text
        matter_type: text  # "project", "initiative", "organization", "democracy", etc.

        # Abstraction Hierarchy Structure
        abstraction_hierarchy: AbstractionHierarchy
        primary_level: abstraction_level  # The level where this matter "lives"

        # Lifecycle Management
        lifecycle_stage: text  # "recognition", "becoming", "completion", "cessation", "memorial"
        lifecycle_tracker: LifecycleTracker

        # Actor Configuration
        actor_configuration: ActorConfiguration

        # Conceptual Framework
        conceptual_framework: ConceptualFramework

        # State Dimensions
        objective_state: ObjectiveState
        subjective_state: SubjectiveState

        # Corporealisation Process
        corporealisation_state: CorporealisationState

        # Memorial Persistence
        memorial_state: MemorialState

        current_status: MatterStatus
```

#### 21.2 The Five-Layer Abstraction Hierarchy and Reasoning Routing

Every matter exists within a predefined abstraction hierarchy for its domain. In v0.8, each abstraction level carries implicit reasoning routing preferences:

**PHILOSOPHICAL FOUNDATION**
- Deepest abstractions about the nature of concern itself
- Theories and fundamental principles
- Example: "What makes something matter-worthy?", theories about why humans organize
- **Implicit reasoning routing: DEDUCE, WEIGH** (deriving conclusions from first principles, evaluating philosophical positions)

**CATEGORICAL FRAMEWORK**
- Patterns, types, and organizing structures that define kinds of matters
- Methodologies, design patterns, matter classifications
- Example: "Legacy modernization project", "distributed organization", "participatory democracy"
- **Implicit reasoning routing: WEIGH, SYNTHESIZE** (evaluating which patterns apply, integrating multiple categorical perspectives)

**INSTANCE**
- The specific matter itself as experienced and recognized
- The matter as a recognizable entity
- Example: "Our Q4 platform migration", "Acme Corporation", "The Athenian polis"
- **Implicit reasoning routing: TRACE** (understanding how this specific instance developed and where it's headed)

**COMPONENTS**
- Concrete parts, mechanisms, and observable properties
- Specific modules, teams, processes, artifacts
- Example: "The authentication module", "The finance team", "The weekly assembly meetings"
- **Implicit reasoning routing: COMPARE, DEDUCE** (comparing component qualities, deducing component behavior from specifications)

**PRIMITIVES**
- Atomic facts, singular events, individual data points
- Individual actions, discrete observations
- Example: "The 2pm standup on Tuesday", "Sarah's commit at 3:47pm", "327 votes cast"
- **Implicit reasoning routing: RETRIEVE** (direct factual lookup with minimal reasoning transformation)

When intelligent operations are performed at a specific abstraction level within a matter, the engine SHOULD prefer the level's implicit reasoning types unless overridden by an explicit reasoning operation or a REALITY_CONTEXT REASONING_PROFILE.

#### 21.3 Core Principles Summary

**The Impossibility of Self-Definition**

At its own level of abstraction, a thing can only be itself. Attempts to define at the same level produce:
1. **Tautology**: "A project is a project" (useless)
2. **Level-characterization**: "Projects have goals and timelines" (defines the category, not the instance)
3. **Instance-comparison**: "This project is larger" (assumes understanding, provides only relative positioning)

Genuine definition requires vertical movement between abstraction levels.

**The Adjacency Principle**

To understand or verify anything at a given level, examine the **immediately adjacent levels**:
- **One level more concrete**: Provides grounding in verifiable specifics
- **One level more abstract**: Provides categorical framework that makes sense of specifics
- **Validation power decreases with distance**: Adjacent levels optimal, distant levels degrade

**Categorical Cognition**

Human engagement with matters operates through categorical assembly:
- Categories exist at the Categorical Framework level
- Specific matters exist at the Instance level
- Categorization is inherently an Instance to Categorical Framework operation
- Conceptual frameworks span multiple levels, mediating how actors recognize and engage with matters

**Actor Position Determines Abstraction Access**

- **IN-system actors**: Strong access to Primitives/Components, weak to Categorical Framework/Philosophical
- **ON-system actors**: Strong access to Categorical Framework/Philosophical, weak to Primitives/Components
- Neither position alone provides complete understanding
- Both perspectives required for full validation

**Corporealisation as Level Translation**

The process of materializing abstract intentions as concrete fragments involves:
- Translating Categorical/Philosophical intentions to Instance design to Component fragments
- Learning to "see" Categorical Framework patterns in Component artifacts
- Reducing intention-dependency as actors internalize level bridging
- Tracking fragment assembly progress and coherence

#### 21.4 Usage Patterns

**Creating a Software Project Matter**

```ailang
METHOD create_software_project_matter():
    SET project TO CREATE Matter WITH:
        matter_name: "Q4 Platform Migration"
        matter_type: "software_project"
        primary_level: "instance"

        abstraction_hierarchy: CREATE AbstractionHierarchy WITH:
            philosophical_foundation: {
                principles: ["modular_design", "separation_of_concerns"],
                theories: ["software_evolution_theory"]
            }

            categorical_framework: {
                project_type: "legacy_modernization",
                methodology: "iterative_migration",
                patterns: ["strangler_fig_pattern", "anti_corruption_layer"]
            }

            instance: {
                specific_project: "Q4 Platform Migration",
                start_date: "2024-10-01",
                target_completion: "2024-12-31",
                team_size: 8
            }

            components: {
                modules: ["authentication", "data_layer", "api_gateway"],
                teams: ["backend_team", "frontend_team"],
                processes: ["daily_standup", "weekly_review", "sprint_planning"]
            }

            primitives: {
                events: [],
                commits: [],
                meetings: []
            }
        END

        actor_configuration: CREATE ActorConfiguration WITH:
            actors: [
                {id: "dev_team", position: "in_system"},
                {id: "architect", position: "on_system"},
                {id: "product_owner", position: "on_system"}
            ]
        END

        lifecycle_stage: "recognition"
    END

    RETURN project
END_METHOD
```

**Validating Matter Claims with Typed Reasoning (v0.8)**

```ailang
METHOD validate_project_success_claim(project, claim):
    # Claim: "The Q4 migration project is well-architected"
    # Must validate at adjacent levels using typed reasoning

    # Check Components level (one level down) — use COMPARE
    SET component_validation TO COMPARE component_qualities AGAINST architecture_standards WITH:
        DIMENSIONS: [modularity, coupling, cohesion, testability]
        OUTPUT_FORMAT: {
            assessment: QUALITATIVE IN ["poor", "acceptable", "good", "excellent"],
            issues: LIST OF TEXT
        }
    END

    IF component_validation.assessment EQUALS "poor" THEN:
        RETURN {
            valid: false,
            reason: "Components do not support 'well-architected' claim",
            evidence: component_validation.issues
        }
    END_IF

    # Check Categorical Framework level (one level up) — use DEDUCE
    SET framework_validation TO DEDUCE pattern_alignment FROM:
        project.categorical_framework.patterns AND project.components WITH:
        MUST_INCLUDE: [pattern_by_pattern_analysis]
        OUTPUT_FORMAT: {
            alignment: TEXT IN ["aligned", "partially_aligned", "misaligned"],
            misalignments: LIST OF TEXT
        }
    END

    IF framework_validation.alignment EQUALS "misaligned" THEN:
        RETURN {
            valid: false,
            reason: "Implementation does not align with Categorical Framework patterns",
            evidence: framework_validation.misalignments
        }
    END_IF

    RETURN {
        valid: true,
        confidence: "high",
        grounding: "Components demonstrate good architecture",
        framework: "Implementation follows stated architectural patterns"
    }
END_METHOD
```

#### 21.5 Key Takeaways

**Critical Understanding Requirements:**

1. **Multi-Level Structure is Essential**: Matters cannot be represented at a single abstraction level. Full representation requires explicit multi-level architecture.

2. **Validation Requires Adjacent Levels**: To verify any claim about a matter, check both one level more concrete (for grounding) and one level more abstract (for categorical framework).

3. **Actor Position Determines Perspective**: IN-system actors have strong access to Primitives/Components; ON-system actors to Categorical Framework/Philosophical. Both required.

4. **Corporealisation is Level Translation**: Creating a matter involves translating abstract intentions through Instance design into concrete Components.

5. **Memorial Robustness Through Multi-Level Perpetuation**: Patterns persist most robustly when perpetuated across multiple abstraction levels.

6. **Abstraction Levels Carry Reasoning Preferences (v0.8)**: Each level in the hierarchy has natural affinity for specific reasoning types — RETRIEVE at Primitives, COMPARE/DEDUCE at Components, TRACE at Instance, WEIGH/SYNTHESIZE at Categorical Framework, DEDUCE/WEIGH at Philosophical Foundation.

**For complete details on all Matter subsystems, implementation patterns, and philosophical foundations, refer to the [Matter Extension Document](https://github.com/pcoz/ailang/blob/main/AILang_Specification_Matter_Extension.md).**

---

### 22. Error Handling

AILang provides both deterministic error handling patterns and intelligent error recovery mechanisms.

#### Deterministic Error Patterns

Structured try-catch blocks with explicit error handling:

```ailang
TRY:
    [instructions that might fail]
CATCH [error_type]:
    [specific error handling]
CATCH ANY:
    [general error handling]
FINALLY:
    [cleanup instructions]
END_TRY
```

#### Intelligent Error Recovery

Adaptive error handling that leverages AI intelligence within defined boundaries:

```ailang
TRY:
    [instructions]
INTELLIGENTLY_HANDLE any_errors WITH:
    CONSTRAINTS: [safety_requirements]
    OBJECTIVES: [desired_outcomes]
    FALLBACKS: [alternative_approaches]
    CONTEXT: [relevant_state]
END_TRY
```

The AI uses specified constraints and objectives to determine recovery strategies while maintaining safety requirements. Error handling remains bounded by explicit constraints even when using intelligence.

**Example with typed reasoning (v0.8):**

```ailang
TRY:
    CONNECT TO external_service
CATCH connection_error:
    # Use TRACE to understand what went wrong
    TRACE failure_cause FROM connection_error WITH:
        DIRECTION: BACKWARD
        OUTPUT_FORMAT: { root_cause: TEXT, recoverable: BOOLEAN }
    END

    IF failure_analysis.recoverable THEN:
        # Use COMPARE to select best recovery strategy
        COMPARE recovery_strategies AGAINST constraints WITH:
            DIMENSIONS: [success_likelihood, time_cost, data_risk]
            OUTPUT_FORMAT: { selected_strategy: TEXT }
        END
        EXECUTE selected_strategy
    ELSE:
        ESCALATE TO human_operator WITH failure_analysis
    END_IF
FINALLY:
    LOG connection_attempt_details
END_TRY
```

#### Context Violation Errors (v0.8)

When a suppressed reasoning type is invoked within a REALITY_CONTEXT that suppresses it, the engine raises a `context_violation` error:

```ailang
DEFINE REALITY_CONTEXT adversarial_proceeding:
    REASONING_PROFILE:
        PRIMARY: DEDUCE
        SUPPRESS: [SYNTHESIZE]
    END_PROFILE
END_CONTEXT

WITH REALITY_CONTEXT adversarial_proceeding:
    TRY:
        # This will raise context_violation because SYNTHESIZE is suppressed
        SYNTHESIZE positions INTO agreement WITH:
            SOURCES: [prosecution, defense]
        END
    CATCH context_violation:
        LOG "Cannot SYNTHESIZE within adversarial_proceeding context"
        # Fall back to the context's PRIMARY reasoning type
        DEDUCE judgment FROM evidence AND legal_standards WITH:
            OUTPUT_FORMAT: { conclusion: TEXT, basis: LIST OF TEXT }
        END
    END_TRY
END_WITH
```

---

### Appendix A: Complete Syntax Reference

#### Reasoning Operation Syntax

```
# Full form
[REASONING_TYPE] [subject] [preposition] [object] WITH:
    [constraints]
END

# With style modifier
[STYLE_MODIFIER] [REASONING_TYPE] [subject] [preposition] [object] WITH:
    [constraints]
END

# Fallback (auto-classified)
INTELLIGENTLY [operation] WITH:
    [constraints]
END
```

**Reasoning types:** WEIGH, DEDUCE, TRACE, COMPARE, SYNTHESIZE, RETRIEVE

**Style modifiers:** CREATIVELY, ADAPTIVELY, CONTEXTUALLY

**Constraint keys:** MUST_INCLUDE, CANNOT_INCLUDE, OUTPUT_FORMAT, MAX_SCOPE

**TRACE-specific:** DIRECTION: FORWARD|BACKWARD

**WEIGH-specific:** SOURCES: [list], ON [dimension]

**COMPARE-specific:** AGAINST [criteria], DIMENSIONS: [list]

**SYNTHESIZE-specific:** INTO [output], SOURCES: [list]

**RETRIEVE-specific:** FOR [context], DOMAIN: [domain]

#### Reality Context with REASONING_PROFILE

```
DEFINE REALITY_CONTEXT [name]:
    WORLDVIEW: [description]
    ASSUMPTIONS: [list]
    INTERPRETIVE_FRAMEWORK: [list]
    BEHAVIORAL_NORMS: [list]
    DISCOURSE_RULES: [list]
    VALUE_SYSTEM: [list]
    CAUSAL_MODELS: [list]
    REASONING_PROFILE:
        PRIMARY: [reasoning_type]
        SECONDARY: [reasoning_type]
        SUPPRESS: [list_of_reasoning_types]
    END_PROFILE
END_CONTEXT
```

#### Person Reasoning Profile

```
CREATE Person [name] WITH:
    reasoning_profile: {
        primary_reasoning: [reasoning_type],
        secondary_reasoning: [reasoning_type],
        reasoning_flexibility: [flexibility_descriptor]
    }
END_CREATE
```

---

### Appendix B: Migration Guide from v0.7.1

#### Backward Compatibility

All v0.7.1 programs are valid v0.8 programs. The following constructs work without modification:

- `INTELLIGENTLY [operation]` — auto-classified to the appropriate reasoning type
- `CREATIVELY [operation]` — treated as style modifier with auto-classified reasoning type
- `ADAPTIVELY [operation]` — treated as style modifier with auto-classified reasoning type
- `CONTEXTUALLY [operation]` — treated as style modifier with auto-classified reasoning type
- `INTELLIGENTLY ASSESS` — auto-classified (typically TRACE or RETRIEVE)
- `INTELLIGENTLY EXPLORE` — unchanged
- `INTELLIGENTLY DECIDE` — auto-classified (typically WEIGH)
- All bounded intelligence constraints (MUST_INCLUDE, etc.) — work identically
- All REALITY_CONTEXT definitions — work without REASONING_PROFILE (no reasoning routing applied)

#### Recommended Upgrades

For production programs, the following upgrades improve performance and clarity:

| v0.7.1 Pattern | v0.8 Recommended |
|---|---|
| `INTELLIGENTLY assess_credibility` | `WEIGH sources ON credibility` |
| `INTELLIGENTLY determine_cause` | `TRACE cause FROM effect WITH DIRECTION: BACKWARD` |
| `INTELLIGENTLY predict_outcome` | `TRACE outcome FROM action WITH DIRECTION: FORWARD` |
| `INTELLIGENTLY rank_options` | `COMPARE options AGAINST criteria` |
| `INTELLIGENTLY integrate_views` | `SYNTHESIZE views INTO summary` |
| `INTELLIGENTLY look_up_fact` | `RETRIEVE fact FOR context` |
| `INTELLIGENTLY draw_conclusion` | `DEDUCE conclusion FROM premises` |
| `INTELLIGENTLY DECIDE plan` | `WEIGH options AGAINST priorities` |
| `INTELLIGENTLY ASSESS situation` | `TRACE drivers FROM data` or `RETRIEVE facts FOR situation` |

#### Adding REASONING_PROFILE to Existing Contexts

Existing REALITY_CONTEXT definitions can optionally add a REASONING_PROFILE block. Without it, INTELLIGENTLY within the context uses standard auto-classification (no PRIMARY override, no SUPPRESS restrictions).

```ailang
# v0.7.1 (still valid)
DEFINE REALITY_CONTEXT my_context:
    WORLDVIEW: "..."
    ASSUMPTIONS: [...]
END_CONTEXT

# v0.8 enhanced
DEFINE REALITY_CONTEXT my_context:
    WORLDVIEW: "..."
    ASSUMPTIONS: [...]
    REASONING_PROFILE:
        PRIMARY: DEDUCE
        SECONDARY: WEIGH
        SUPPRESS: []
    END_PROFILE
END_CONTEXT
```

---

### Appendix C: Reasoning Type Selection Guide

#### Decision Tree

```
Is the task about evaluating who/what to trust?
  YES -> WEIGH

Is the task about deriving conclusions from rules/premises?
  YES -> DEDUCE

Is the task about understanding causes or predicting effects?
  YES -> TRACE (BACKWARD for causes, FORWARD for effects)

Is the task about ranking, ordering, or comparing options?
  YES -> COMPARE

Is the task about integrating multiple viewpoints into a unified view?
  YES -> SYNTHESIZE

Is the task about looking up a fact or definition?
  YES -> RETRIEVE

Not sure / mixed reasoning needs?
  -> INTELLIGENTLY (auto-classification)
```

#### Common Patterns by Domain

**Legal:** DEDUCE (primary), WEIGH (witness/evidence credibility), RETRIEVE (statute lookup)

**Medical:** DEDUCE (diagnosis from symptoms), TRACE (disease progression), WEIGH (treatment evidence), RETRIEVE (drug interactions)

**Business Strategy:** WEIGH (strategic decisions), COMPARE (vendor/option selection), SYNTHESIZE (stakeholder alignment), TRACE (market dynamics)

**Engineering:** TRACE (root cause analysis), COMPARE (architecture decisions), DEDUCE (specification compliance), RETRIEVE (standards lookup)

**Research:** SYNTHESIZE (literature review), DEDUCE (hypothesis testing), WEIGH (source credibility), COMPARE (methodology selection)

**Education:** RETRIEVE (knowledge recall), DEDUCE (logical exercises), SYNTHESIZE (interdisciplinary connections), COMPARE (framework comparison)
