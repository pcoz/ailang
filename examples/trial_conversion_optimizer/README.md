# Trial → Paid Optimizer

## What This Does

Imagine you run a software company with a 14-day free trial. Every day during that trial, you face three key decisions:

1. **What price should we charge** for the paid subscription?
2. **How much should we nudge users** with emails and in-app messages?
3. **Should we offer a discount today** and if so, how much?

This AILang program solves all three questions simultaneously by building a mathematical model of user behavior, then finding the optimal strategy that maximizes revenue while respecting your business rules and budget constraints.

**The key insight**: Instead of guessing or running endless A/B tests, you can use math to find the best strategy directly, then let AI explain the reasoning behind each day's decisions in plain English.

---

## Why This Approach Works

Traditional methods require you to:
- Run separate experiments for pricing, messaging, and discounting
- Wait weeks or months for statistically significant results  
- Manually coordinate between different teams (pricing, marketing, product)
- Make decisions based on incomplete information

This AILang approach lets you:
- **Model user behavior mathematically** using concepts from survival analysis (originally developed for medical research)
- **Optimize everything together** rather than in isolation
- **Encode business rules as hard constraints** (like "no discounts after day 10" or "messaging budget can't exceed $X")
- **Get human-readable explanations** for every decision the system makes

---

## The Business Problem We're Solving

### The Challenge: Balancing Competing Objectives

During a free trial, you want to:
- **Convert as many users as possible** to paid plans
- **Avoid being too pushy** (which damages brand reputation)
- **Stay within budget constraints** for marketing spend
- **Respect company policies** (e.g., legal requirements, brand guidelines)
- **Maximize revenue per converted user** through optimal pricing

These objectives often conflict. Higher prices mean more revenue per user but lower conversion rates. More aggressive messaging increases conversions but costs more and may annoy users. The mathematical approach finds the sweet spot.

### Why Mathematical Optimization Beats Intuition

**Human intuition says**: "Let's discount heavily on the last day to create urgency."

**Mathematical analysis reveals**: If users learn this pattern, they'll wait for the last-day discount, actually reducing conversions on earlier days. The optimal strategy might be steady low-level discounts early, then no discounts at the end.

**Business rules matter**: Maybe your legal team says "no discounts after day 10" to avoid creating misleading urgency. The math respects this constraint while finding the best strategy within those limits.

---

## How It Works (The Mathematical Foundation Explained Simply)

### Step 1: Model User Behavior

We use a concept called "hazard analysis" (borrowed from medical research, where it's used to predict patient recovery rates). 

**In medical terms**: "What's the probability a patient recovers each day, given they haven't recovered yet?"

**In business terms**: "What's the probability a user converts each day, given they haven't converted yet?"

The mathematical formula looks intimidating but captures common-sense ideas:

```
Conversion probability each day = Base rate × Seasonal effects × 
    exp(Price sensitivity × (Price - Reference price) - 
        Messaging effectiveness × Messaging level - 
        Discount effectiveness × Discount level)
```

**What this means in English**:
- **Base rate**: Some people naturally convert without any nudging
- **Seasonal effects**: Weekends might be different from weekdays  
- **Price sensitivity**: Higher prices make conversion less likely
- **Messaging effectiveness**: More emails/nudges increase conversion probability
- **Discount effectiveness**: Bigger discounts increase conversion probability
- **The "exp" function**: This mathematical function ensures that changes have bigger effects when they compound (which matches real user behavior)

### Step 2: Encode Business Constraints

The system translates business rules into mathematical constraints:

**Business rule**: "Marketing budget can't exceed $8,000 for messaging across all trial days"
**Mathematical constraint**: ∫(messaging intensity) ≤ 8.0 (where the integral adds up all daily messaging costs)

**Business rule**: "No discounts after day 10 due to legal requirements"  
**Mathematical constraint**: For all days t > 10, discount(t) = 0

**Business rule**: "No single-day discount can exceed 30%"
**Mathematical constraint**: For all days t, discount(t) ≤ 0.30

### Step 3: Optimize Everything Simultaneously  

The system searches through millions of possible combinations of price, messaging intensity, and discount percentages to find the strategy that generates the most revenue. Unlike simple optimization problems that have one clear best answer, this problem has multiple competing objectives that must be balanced against each other.

The mathematical objective function balances:
- **Revenue gain**: More conversions at higher prices = more money
- **Messaging costs**: Aggressive messaging costs money and brand goodwill  
- **Discount costs**: Deep discounts reduce revenue per conversion

### Step 4: Generate Human-Readable Explanations

After the math determines the optimal strategy, AI explains each day's decisions:

Instead of: "Set m(t)=0.2, d(t)=0.05 because ∂h/∂m=-0.0491"  
You get: "Light messaging with 5% discount because messaging reduces barriers to conversion and the discount makes the decision easier without giving away too much revenue."

---

## Files and What They Do

### The Program That Does the Math
**`trial_to_paid_conversion_optimizer.ail`** - This is the AILang program that:
- Defines the mathematical model of user behavior
- Sets up the optimization problem with all constraints
- Solves for the best price and daily messaging/discount strategy  
- Generates human-friendly explanations of each decision

### The Knobs You Can Turn
**`trial_paid_inputs.jsonc`** - This file contains all the settings you can adjust:

**Business Settings**:
- `horizon_days`: How long is your trial? (14 days in this example)
- `p_min`, `p_max`: What's the reasonable price range? ($7.99 to $19.99)
- `cost_per_user_per_day`: What does it cost you per trial user per day? ($0.10)

**Marketing Budget Controls**:
- `msg_cost_weight`: How much do you penalize aggressive messaging? (Higher = quieter campaigns)
- `disc_cost_weight`: How much do you penalize deep discounts? (Higher = smaller discounts)
- `total_msg_budget`: Maximum messaging spend across all days (8.0 units)
- `avg_discount_cap`: Average discount can't exceed this (8% across all days)

**Business Rules**:
- `max_daily_discount_pct`: No single day can discount more than this (30%)
- `no_discount_after_day`: No discounts allowed after this day (day 10)
- `max_m_endgame`: Cap on messaging intensity in final days (2.0)

**User Behavior Parameters** (these would ideally come from your data):
- `lambda0`: What % of people convert naturally each day without nudging? (10%)
- `alpha`: How much do higher prices hurt conversion rates? (6% reduction per dollar)
- `beta`: How much do messages help conversion rates? (35% boost)
- `gamma`: How much do discounts help conversion rates? (60% boost)

**Seasonal Patterns**:
- `seasonality`: Are some days naturally better than others? (Array of 14 values, one per day)

### The Generated Results (using ChatGPT 5 - Thinking)

**`trial_paid_plan.json`** - The basic output:
- Chosen price: **$19.49**
- Daily schedule: Message intensity and discount % for each day  
- Performance metrics: Expected revenue, total costs, etc.

**`trial_paid_plan_annotated.json`** - Same plan with AI explanations:
- Each day includes a human-readable assessment
- "Why this decision" explanations  
- Mathematical sensitivity analysis (how much each factor matters)
- Policy notes (which business rules are affecting decisions)

**`trial_message_pack.md`** - Ready-to-use marketing copy:
- Email templates for each day
- In-app message suggestions
- Call-to-action text
- Legal disclaimers

**`trial_message_pack_plus.md`** - Same marketing copy plus the daily explanations embedded inline for easy review

---

## Reading the Results

### The Chosen Strategy

**Price Decision**: $19.49
- *Why this price?* The math found this maximizes revenue. Lower prices don't generate enough extra conversions to offset the revenue loss. Higher prices lose too many potential customers.

**Messaging Strategy**:
- *Days 0-10*: Light messaging (intensity 0.2) - consistent gentle nudges
- *Days 11-13*: Medium messaging (intensity 0.5) - more urgent as trial ends
- *Why this pattern?* Early aggressive messaging is wasteful - users need time to evaluate. Ramping up messaging as the trial ends captures procrastinators without annoying early deciders.

**Discount Strategy**:
- *Days 0-10*: 5% discount consistently 
- *Days 11-13*: No discounts (company policy)
- *Why this pattern?* Steady small discounts remove price friction without training users to expect bigger discounts. The no-discount policy after day 10 is respected absolutely.

### Understanding the AI Explanations

Each day includes an assessment like:
> **Day 9 — 💡 Targeted promo**  
> **Why this**: seasonality uplift ≈ +6%; messaging reduces hazard (∂h/∂m≈-0.0496); discount eases decision (∂h/∂d≈-0.00085/%pt)

**Translation**: 
- "seasonality uplift ≈ +6%": Day 9 is naturally 6% better for conversions than average  
- "messaging reduces hazard": Each unit of messaging makes conversion 4.96% more likely
- "discount eases decision": Each 1% of discount makes conversion 0.085% more likely  
- The math balanced these factors to choose messaging=0.2, discount=5%

### Performance Metrics Explained

**Objective: 16.7956** - This is the "score" the system maximized. Higher is better.
- **LTV component: 16.9201** - Revenue from conversions  
- **Control cost: 0.1245** - Cost of messaging and discounting
- **Net value: 16.7956** - Revenue minus costs

**Avg discount: 3.93%** - Across all 14 days, discounts averaged under 4%
**Messaging integral: 3.7** - Total messaging "volume" used 3.7 out of 8.0 budget
**Discount days ≥5%: 11** - Eleven days had discounts of 5% or more

---

## Tuning the System (How to Experiment)

### Making the Campaign More Aggressive
Want more activity? In `trial_paid_inputs.jsonc`:
- **Lower** `msg_cost_weight` from 0.10 to 0.05 (makes messaging cheaper in the optimization)
- **Lower** `disc_cost_weight` from 0.20 to 0.10 (makes discounting cheaper)  
- **Raise** `beta` from 0.35 to 0.50 (makes messaging more effective)
- **Raise** `gamma` from 0.60 to 0.80 (makes discounting more effective)

### Making the Campaign Quieter  
Want less pushy messaging? Do the opposite:
- **Raise** `msg_cost_weight` to 0.30 (makes messaging expensive)
- **Raise** `disc_cost_weight` to 0.40 (makes discounting expensive)
- **Lower** `beta` to 0.20 (makes messaging less effective)
- **Lower** `gamma` to 0.40 (makes discounting less effective)

### Changing Timing Patterns
Want different timing? Modify `seasonality`:
- `[1.0, 1.0, 1.0, ...]` - Every day is the same
- `[0.8, 0.8, 1.2, 1.2, ...]` - Weekends better than weekdays
- `[1.0, 1.0, ..., 1.5, 1.5, 1.5]` - Big push at the end

### Testing Different Business Rules
Want to allow discounts until the end? Change `no_discount_after_day` from 10 to 13
Want smaller discount budget? Lower `avg_discount_cap` from 0.08 to 0.05

---

## Why This Is Powerful (Technical Benefits)

### 1. **Holistic Optimization**
Most companies optimize pricing, messaging, and discounting separately. This creates suboptimal results because these decisions interact. Mathematical optimization finds the global optimum across all decisions simultaneously.

### 2. **Constraint Satisfaction**  
Business rules become hard mathematical constraints. The system cannot violate them, even by tiny amounts. This gives you confidence that legal, policy, and budget requirements will be met exactly.

### 3. **Sensitivity Analysis**
The system shows you exactly how sensitive your results are to each assumption. If small changes in user behavior parameters lead to big strategy changes, you know to collect better data in those areas.

### 4. **Rapid Iteration**
Instead of running 6-week A/B tests, you can test dozens of scenarios in minutes by adjusting the input parameters. This is especially valuable for seasonal businesses or new product launches where you can't wait for experimental results.

### 5. **Explainable AI**
Every decision comes with mathematical justification AND human-readable explanation. You can confidently present the strategy to executives, legal teams, and marketing teams because the reasoning is transparent.

---

## Real-World Application 

### Before This System
**Product Manager**: "Should we run a 10% discount on day 12?"  
**Marketing**: "Let's A/B test it for 6 weeks"  
**Data Science**: "We need more data to be confident"  
**Legal**: "Are we creating false urgency?"  
**Finance**: "What's the revenue impact?"

*Result: Decision paralysis, delayed launches, suboptimal strategies*

### With This System  
**Product Manager**: "Should we run a 10% discount on day 12?"  
**System**: "No. The math shows 5% discount on days 0-10 generates 12% more revenue while respecting the no-discount-after-day-10 policy. Here's the detailed explanation and sensitivity analysis."

*Result: Confident decisions backed by mathematical rigor and business logic*

### The Bigger Picture

This example demonstrates AILang's power to bridge three normally separate worlds:

1. **Mathematical Optimization**: The heavy-duty math that finds optimal solutions
2. **Business Logic**: The rules, constraints, and policies that must be respected  
3. **Human Communication**: AI-generated explanations that make complex decisions understandable

Most systems excel at one of these but fail at integration. AILang excels at all three simultaneously, making it practical for real business use.

---

## Getting Started

1. **Examine the Results**: Open `trial_message_pack_plus_v3.md` to see what the current optimal strategy looks like with explanations

2. **Try Simple Changes**: Edit `trial_paid_inputs.jsonc` to change the price range or messaging budget, then re-run to see how strategy changes

3. **Understand the Tradeoffs**: Compare the basic plan (`trial_paid_plan_v3.json`) with the annotated version to see how mathematical decisions translate to business logic

4. **Adapt to Your Business**: Replace the example parameters with your actual user behavior data, pricing constraints, and business rules

The power isn't just in getting an answer—it's in understanding WHY that answer is optimal, and being able to quickly test alternatives as conditions change.

---

## Advanced Features for Technical Users

While this README focuses on accessibility, the system includes sophisticated mathematical capabilities:

- **Continuous-time calculus**: The underlying model uses integrals and derivatives for precise optimization
- **Survival analysis**: Hazard functions model user conversion behavior over time
- **Constrained optimization**: Multiple types of constraints (linear, nonlinear, discrete) are handled simultaneously  
- **Sensitivity analysis**: Partial derivatives show how results change with parameter adjustments
- **Stochastic modeling**: The seasonality vector can incorporate randomness and uncertainty

The beauty of the AILang approach is that this mathematical sophistication is hidden behind natural language interfaces, making it accessible to non-mathematicians while preserving full technical rigor for those who need it.

---

## AILang Showcase

This example highlights AILang's unique strengths:

1. **Natural Language Math**: Complex optimization expressed in readable terms
2. **Bounded Intelligence**: AI explanations constrained by mathematical facts  
3. **Deterministic Core with Intelligent Edges**: The math is exact, the explanations are contextual
4. **Real-World Complexity**: Multiple interacting decisions with realistic constraints
5. **Practical Business Value**: Directly applicable to revenue optimization

This example solves a real problem that businesses face daily, using mathematical rigor that's typically accessible only to specialists, while producing results that non-technical stakeholders can understand and act upon.
