# AILang: Natural Language Programming for the AI Era

**Version 0.4** | [fleetingswallow.com](https://fleetingswallow.com/)

## What is AILang?

AILang is a natural language programming system that lets you write programs in structured English that AI can reliably interpret and execute. It uses RAG (Retrieval-Augmented Generation) architecture to constrain AI operations to known boundaries, enabling production deployment.

Instead of forcing human logic through the bottleneck of artificial syntax, AILang allows you to express computational intent in the same structured natural language you use to think through problems.

## Why AILang Exists

Real-world software virtually always requires three interwoven types of thinking:
- **Logical flow** (if-then decisions, loops, data management)
- **Mathematical computation** (calculations, optimizations, physical constraints)
- **Domain expertise** (business rules, industry knowledge, contextual judgment)

### The Problem with Traditional Programming

Traditional programming forces developers to fragment these naturally unified thought processes:

**The Fragmentation Problem:**
- Logic gets expressed in control structures (if/else, for loops)
- Math gets relegated to libraries or external tools
- Domain expertise gets buried in comments or external documentation
- Business rules become hard-coded magic numbers and brittle conditionals

**How This Is "Solved" Today:**
- **Multi-language stacks**: Python for logic, R for statistics, SQL for data, JavaScript for UI
- **Framework proliferation**: Different tools for different aspects of the same problem
- **Abstraction layers**: ORMs, middleware, API layers that add complexity while trying to hide it
- **Documentation overhead**: Extensive wikis explaining what the code actually means

**The Persistent Problems:**
- **Cognitive context switching**: Constantly translating between different syntaxes and paradigms
- **Lost intent**: The "why" disappears in the "how" of implementation
- **Expertise bottleneck**: Domain experts can't directly contribute without learning to code
- **Maintenance nightmare**: Changes require understanding multiple layers and their interactions
- **Testing complexity**: Unit tests for logic, integration tests for systems, but nothing tests whether the business intent is preserved

## The AILang Solution: Three-Layer Architecture

AILang recognizes that logical flow, mathematical computation, and domain expertise aren't separate—they're different aspects of the same thought process. Our architecture mirrors how humans naturally approach complex problems:

### 1. The Deterministic Layer: Your Logical Foundation

Just as humans rely on consistent rules for basic reasoning, AILang's deterministic layer provides predictable operations you can count on.

```ailang
# Clear, deterministic logic - like following a recipe
SET total_cost TO 0
FOR EACH item IN shopping_cart DO:
    SET total_cost TO total_cost + item.price
    IF item.category EQUALS "electronics" THEN:
        APPLY warranty_option
    END_IF
END_FOR
```

### 2. The Intelligent Layer: Your Creative Problem-Solver

When humans face ambiguous situations, we apply judgment, experience, and creativity. AILang's intelligent layer does the same.

```ailang
# Intelligent operations - like asking an expert colleague
INTELLIGENTLY assess_customer_sentiment FROM feedback WITH:
    MUST_INCLUDE: [emotion_indicators, satisfaction_level]
    OUTPUT_FORMAT: detailed_analysis
END
```

### 3. The Mathematical Layer: Reality's Governing Laws

The universe operates on mathematical principles that we cannot ignore. AILang acknowledges these fundamental constraints.

```ailang
MATHEMATICAL_CONTEXT:
    DOMAIN: real
    PRECISION: high
END_CONTEXT

# Physics constraints must be satisfied
ASSERT energy_in EQUALS energy_out + losses
ASSERT ALL(probabilities >= 0 AND probabilities <= 1)
```

## Core Language Constructs

Build from simple to complex with these fundamental building blocks:

### Variables & Arithmetic

```ailang
DO subtotal_example:
    SET prices TO [12.99, 4.50, 7.25]
    SET subtotal TO SUM(prices)
    SEND "Subtotal is {subtotal}" TO console
END
```

### Conditions (IF / ELSE)

```ailang
DEFINE PROCEDURE apply_discount WITH PARAMETERS [amount]:
    IF amount >= 100 THEN:
        RETURN amount * 0.9
    ELSE:
        RETURN amount
    END_IF
END_PROCEDURE
```

### Loops (FOR EACH)

```ailang
DO count_electronics:
    SET count TO 0
    FOR EACH item IN shopping_cart DO:
        IF item.category EQUALS "electronics" THEN:
            SET count TO count + 1
        END_IF
    END_FOR
    SEND "Electronics items: {count}" TO console
END
```

### Pattern Matching (MATCH / CASE)

```ailang
DEFINE PROCEDURE shipping_cost WITH PARAMETERS [region]:
    MATCH region WITH:
        CASE "US": RETURN 5
        CASE "EU": RETURN 8
        CASE "APAC": RETURN 10
        DEFAULT: RETURN 12
    END_MATCH
END_PROCEDURE
```

### Data I/O (GET / SEND)

```ailang
DO pipeline:
    GET orders FROM "orders.csv"
    SET avg TO MEAN(orders.total)
    SEND {average_order: avg} TO "reports/daily.json"
END
```

### Mathematical Context & Assertions

```ailang
DO finance_math:
    MATHEMATICAL_CONTEXT:
        DOMAIN: real
        PRECISION: high
    END_CONTEXT

    SET rates TO [0.01, 0.02, 0.03]
    SET expected TO MEAN(rates)
    ASSERT expected >= 0 AND expected <= 1
    SEND "Expected rate {expected}" TO console
END
```

### Deterministic Helpers (Reusable Procedures)

```ailang
DEFINE PROCEDURE normalize WITH PARAMETERS [xs]:
    SET s TO SUM(xs)
    IF s == 0 THEN RETURN xs END_IF
    RETURN [ x / s FOR x IN xs ]
END_PROCEDURE
```

### Intelligent Operations

```ailang
DO summarize_feedback:
    GET feedback FROM "feedback.csv"
    INTELLIGENTLY assess_customer_sentiment FROM feedback WITH:
        MUST_INCLUDE: [emotion_indicators, satisfaction_level]
        OUTPUT_FORMAT: summary
    END
    SEND summary TO stakeholders
END
```

### Creative Operations

```ailang
DO campaign_ideas:
    CREATIVELY generate_marketing_message BASED_ON:
        audience_demographics AND recent_sentiment
        CONSTRAINTS: [brand_guidelines, regulatory_requirements]
    END
    SEND marketing_message TO "marketing@company.com"
END
```

## Combining Layers: Real Solutions

The true power of AILang emerges when all three layers work together:

```ailang
# Insurance pricing combines all three layers naturally
DEFINE PROCEDURE price_insurance_policy WITH PARAMETERS [applicant]:
    # Logic and domain knowledge interweave naturally
    IF applicant.age > 65 AND applicant.has_pre_existing_conditions THEN:
        # Mathematical constraints from actuarial science
        SET base_risk TO CALCULATE_ACTUARIAL_RISK(mortality_tables, applicant)
        
        # Domain expertise expressed directly
        INTELLIGENTLY adjust_for_lifestyle_factors:
            CONSIDER exercise_habits, occupation_risks, family_history
            APPLY industry_best_practices
            ENSURE regulatory_compliance
        END
        
        # Price from risk
        SET premium TO PRICE_PREMIUM(base_risk, loadings, target_margin)

        # Mathematical reality enforces boundaries
        ASSERT premium * expected_policies > expected_payouts + operational_costs
    END_IF
END_PROCEDURE
```

## Advanced Feature: Person Entities

As of version 0.4, AILang includes Person entities - computational models of human agents with cognition, personality, and social dynamics. This enables sophisticated multi-agent simulations where behavior emerges from character interactions rather than being scripted.

### Creating People

```ailang
# Create a person with background and personality
INTELLIGENTLY create_person FROM "London" WITH:
    OUTPUT: alice
    MUST_INCLUDE: [name, background, personality, interaction_system]
    BOUNDS: "fictional but locally plausible"
    HINTS: {name: "Alice Chen", age_range: [25,35], profession: "data analyst"}
END

# Set personality traits (Logos/Energiae/Ethos model)
SET alice.personality.logos.reasoning_style TO "analytical"
SET alice.personality.energiae.drives TO {achievement: 0.8, connection: 0.7}
SET alice.personality.ethos.core_values TO ["integrity", "growth"]
```

### Person Architecture

Each Person has interconnected systems:
- **Cognitive**: Thought processing, memory (episodic/semantic/procedural), knowledge acquisition
- **Personality**: Three-component model (Logos=reasoning, Energiae=drives, Ethos=values)
- **Social**: Interaction systems, group memberships, relationship dynamics
- **Planning**: Goal pursuit with adaptive navigation
- **Practical**: Economic awareness, identity management

### Multi-Person Simulations

```ailang
# Example: Team collaboration with emergent dynamics
DO simulate_project_meeting:
    # Create team with different personalities
    INTELLIGENTLY create_person WITH:
        OUTPUT: sophie
        HINTS: {traits: ["detail-oriented", "morning-person"]}
    END
    
    INTELLIGENTLY create_person WITH:
        OUTPUT: james
        HINTS: {traits: ["creative", "night-owl"]}
    END
    
    # Their interactions emerge from personality differences
    SET discussion TO sophie.interact_with_person(james, work_context)
    
    # Natural conflicts arise and resolve
    IF sophie.wants_morning_meeting AND james.prefers_afternoon THEN:
        # Resolution emerges from their interaction systems
        ADAPTIVELY find_compromise BASED_ON:
            sophie.personality.ethos  # Values efficiency
            james.personality.energiae # Peak creativity afternoon
        END
        # Result: Agree on late morning with coffee
    END_IF
END
```

### Why Person Entities Matter

1. **Emergent Behavior**: Actions arise from personality and context, not scripts
2. **Consistency**: People remain themselves while adapting to situations
3. **Social Realism**: Group dynamics emerge from individual interactions
4. **Explainability**: Can trace why someone made a particular choice

## Real-World Application Examples

### 1. Applying Science in Everyday Scenarios

Diagnose why bread isn't rising by testing hypotheses with actual physics:

```ailang
DEFINE PROCEDURE diagnose_bread_problem WITH PARAMETERS [user_observation]:
    GET description FROM "My bread's been coming out flat and dense lately."
    GET environmental_data FROM kitchen_sensors
    
    # Build testable hypotheses
    SET potential_factors TO []
    
    # Temperature hypothesis
    IF kitchen_sensors.temperature != previous_location.temperature THEN:
        # Arrhenius equation for yeast activity
        SET k1 TO A * e^(-Ea/(R*T1))  # Rate at old temperature
        SET k2 TO A * e^(-Ea/(R*T2))  # Rate at new temperature
        SET activity_ratio TO k2/k1
        
        IF activity_ratio < 0.5 THEN:
            RECOMMEND: "Your yeast is working at {activity_ratio*100}% speed. 
                       Try proofing {1/activity_ratio} times longer."
        END_IF
    END_IF
END_PROCEDURE
```

### 2. Mathematical Pattern Discovery

Automatically detect patterns in data without knowing the math beforehand:

```ailang
DEFINE PROCEDURE analyze_unknown_pattern WITH PARAMETERS [data]:
    MATHEMATICAL_CONTEXT:
        DOMAIN: real
        PRECISION: high
    END_CONTEXT
    
    # Test data characteristics
    SET autocorrelation TO [ CORRELATE(data, SHIFT(data, lag)) FOR lag IN [1..n/4] ]
    SET has_periodicity TO MAX(autocorrelation[2:]) > 0.7
    
    # Branch based on discovered characteristics
    IF has_periodicity THEN:
        # Apply frequency analysis
        SET spectrum TO FOURIER_TRANSFORM(data)
        SET frequencies TO FIND_PEAKS(|spectrum|)
        SET period TO 1 / frequencies[0]
    ELSE IF is_exponential THEN:
        # Exponential growth/decay detected
        SET growth_rate TO (LOG(data[-1]) - LOG(data[0])) / n
        SET doubling_time TO ln(2) / growth_rate IF growth_rate > 0
    END_IF
    
    RETURN findings_in_natural_language
END_PROCEDURE
```

### 3. Group Holiday Simulation with Person Entities

Simulate five friends planning and experiencing a trip:

```ailang
# Five friends from Newcastle plan Madrid trip
CREATE group WITH [lee, ayesha, callum, sophie, gavin]

# Each person's traits influence the trip
# Sophie (runner) → dawn runs in Retiro
# Lee (social) → late-night bars
# Ayesha (vegetarian) → restaurant choices

# Natural friction emerges and resolves
IF venue_too_loud FOR sophie THEN:
    GROUP splits_temporarily
    lee.continues_night
    sophie.returns_for_sleep
    AGREEMENT: "Meet for breakfast"
END_IF

# Outputs both structured data and narrative
SEND holiday_report TO "trip_data.json"
SEND holiday_memoir TO "trip_story.md"
```

## Why AILang Transforms Development

1. **Rapid Prototyping**: Move from idea to working solution without translation overhead
2. **Living Documentation**: Code explains itself; business stakeholders can read and verify logic directly
3. **Adaptive Systems**: Build systems that intelligently handle unexpected situations while maintaining reliability
4. **Domain Expert Accessibility**: Subject matter experts express complex domain logic without learning syntax
5. **Reduced Cognitive Load**: Focus on solving problems, not remembering syntax
6. **No Syntax Translation**: Express all types of thinking in natural language
7. **No Context Loss**: Domain expertise remains visible and executable
8. **No Artificial Separation**: Math, logic, and business rules coexist naturally

## Getting Started

### Prerequisites

- An AI system with RAG (Retrieval-Augmented Generation) capabilities
- The complete AILang specification (`AILang_Specification.md`)

### Basic Setup

1. Load the specification into your AI system's knowledge base
2. Write your program using natural language constructs
3. Execute through AI interpretation

### Complete Starter Program

```ailang
# A complete program combining all three layers
DO analyze_customer_behavior:
    # Deterministic: Load data
    GET transactions FROM "customer_transactions.csv"
    
    # Mathematical: Calculate metrics
    SET average_order TO MEAN(transactions.amount)
    SET trend TO LINEAR_REGRESSION(transactions.amount OVER time)
    
    # Intelligent: Understand behavior
    INTELLIGENTLY segment_customers BASED_ON:
        transaction_patterns, timing, product_preferences
        OUTPUT: customer_segments WITH characteristics
    END
    
    # Creative: Generate strategies
    FOR EACH segment IN customer_segments DO:
        CREATIVELY design_retention_strategy CONSIDERING:
            segment.characteristics, market_conditions, company_resources
        END
    END_FOR
    
    # Deterministic: Output results
    SEND analysis_report TO stakeholders
END
```

## The Paradigm Shift

AILang isn't just another programming language—it's a fundamental rethinking of how humans should interact with computational systems. By aligning with natural human thought patterns and leveraging AI's understanding capabilities, AILang makes programming accessible to anyone who can think logically and express ideas clearly.

With Person entities, it now also models how computational agents interact with each other, creating simulations where complex behaviors emerge from simple personality rules.

The future of programming isn't about learning computer languages. It's about computers learning human language and human nature. AILang is that future, available today.

## License

MIT License - See LICENSE file for details

---

*AILang: Write programs in structured English that AI can reliably interpret and execute. Uses RAG architecture to constrain AI operations to known boundaries, enabling production deployment.*
