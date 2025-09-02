# Mind Game – User Manual

Welcome to **Mind Game: Argument Battle** – a fast-paced rhetorical duel where you face an AI opponent in structured debate rounds. Win by crafting better arguments using strategic tactics.

**Play here:** [Mind Game](https://chatgpt.com/g/g-68b57a7405bc8191bd6377d87bf88ba7-mind-game)

---

## Quick Start

1. Open the game link above
2. Choose a debate topic or type `random`
3. Select a tactic number (1-10) and write your argument
4. Read the AI's counter-argument and the judge's scoring
5. Continue through rounds to see who wins

---

## How to Play

### Starting a Match

When the game starts, you'll see:
```
Enter a debate topic (or "random"):
```

Type any debatable topic like:
- `Should schools require uniforms?`
- `Is social media harmful to society?`
- `random` (lets the AI choose)

### Making Your Move

Each round presents you with 10 tactical options:

```
Your argument tactics:
1. Logical Reasoning (systematic logic)
2. Emotional Appeal (pathos)
3. Factual Evidence (concrete data)
4. Rhetorical Question (thought-provoking)
5. Reductio ad Absurdum (show absurdity)
6. Analogy (comparative reasoning)
7. Counterexample (disprove by example)
8. Appeal to Authority (expert opinion)
9. Humor Deflection (wit and charm)
10. Moral High Ground (ethical superiority)

Choose your tactic (1-10):
Make your argument:
```

**Step 1:** Type a number from 1-10 to select your tactic  
**Step 2:** Type your argument using that tactic

### Input Format

The game expects two separate inputs:
1. First prompt: Enter just the tactic number (e.g., `3`)
2. Second prompt: Enter your complete argument

**Example Turn:**
```
Choose your tactic (1-10): 5
Make your argument: If we allow AI to make all our decisions, we might as well let toasters run for president.
```

### Reading the Results

After your argument, you'll see:
1. **AI's Response:** The tactic it chose and its counter-argument
2. **Judge's Verdict:** Round winner and scores (0-10 scale)
3. **Commentary:** Why one argument won
4. **Current Score:** Running tally

### Continuing or Stopping

After each round (except the last), you'll be asked:
```
Continue to next round? (yes/no):
```
- Type `yes` or `y` to continue
- Type `no` or `n` to end early

---

## Tactics Guide

### 1. Logical Reasoning
Build structured arguments with clear premises leading to conclusions.
- **Example:** "If A leads to B, and B leads to C, then A must lead to C."

### 2. Emotional Appeal
Connect with values, fears, or aspirations.
- **Example:** "Think of the children who will suffer if we don't act now."

### 3. Factual Evidence
Use data, statistics, or concrete examples.
- **Example:** "Studies show 73% of participants improved after this intervention."

### 4. Rhetorical Question
Ask questions that make your point without needing answers.
- **Example:** "Do we really want to live in a world where...?"

### 5. Reductio ad Absurdum
Push opponent's logic to absurd conclusions.
- **Example:** "By that logic, we should ban cars because they could be dangerous."

### 6. Analogy
Compare to familiar situations.
- **Example:** "This is like trying to bail out the Titanic with a teaspoon."

### 7. Counterexample
Provide one case that disproves a general claim.
- **Example:** "You say all X are Y, but here's an X that isn't Y."

### 8. Appeal to Authority
Cite experts or institutions.
- **Example:** "The World Health Organization states..."

### 9. Humor Deflection
Use wit to reframe or deflate tension.
- **Example:** "That argument has more holes than Swiss cheese at a shooting range."

### 10. Moral High Ground
Appeal to ethics and principles.
- **Example:** "This is fundamentally about human dignity and rights."

---

## Scoring System

### Round Scoring

Each argument receives 0-10 points based on:
- **Relevance:** Stays on topic and addresses opponent's points
- **Support:** Provides reasoning and evidence
- **Coherence:** Clear, logical structure
- **Tactic Execution:** How well you used your chosen tactic
- **Counter Effectiveness:** How well you refuted the opponent

### Tactic Bonuses

Some tactics naturally counter others:
- Factual Evidence beats Emotional Appeal (+2 bonus)
- Counterexample beats Logical Reasoning (+2 bonus)
- Humor Deflection beats Moral High Ground (+1 bonus)

### Winning

- **Round Winner:** Higher score that round
- **Match Winner:** Most rounds won after 5 rounds
- **Tiebreakers:** Average margin of victory, final round performance

---

## Strategy Tips

### Opening Moves
- Start strong with Logical Reasoning or Factual Evidence to establish your position
- Save Reductio ad Absurdum for when opponent makes sweeping claims

### Mid-Game
- Vary your tactics to keep opponent off-balance
- Use Counterexample when opponent overgeneralizes
- Deploy Humor Deflection when debate gets too heated

### Closing
- Return to your strongest points with Moral High Ground
- Use Factual Evidence to cement your position
- Rhetorical Questions can leave lasting impressions

### General Advice
- **Be specific:** Name exactly what you're refuting
- **Stay focused:** Don't introduce new topics
- **Adapt:** Choose tactics that counter opponent's approach
- **Be concise:** Clear, punchy arguments score better than rambling

---

## FAQ

**Q: Can I type the tactic name instead of number?**  
A: Use the number (1-10) for reliable recognition.

**Q: Do I have to use all tactics?**  
A: No, but variety usually scores better than repetition.

**Q: Can I use real sources?**  
A: Yes, brief citations strengthen Factual Evidence and Appeal to Authority tactics.

**Q: What if I enter an invalid tactic number?**  
A: The game defaults to Logical Reasoning.

**Q: Can I change my argument after typing it?**  
A: No, once submitted, your argument is final for that round.

---

## Example Game Session

```
=== ARGUMENT BATTLE: MIND GAME ===

Enter a debate topic (or "random"): Should AI have rights?

DEBATE TOPIC: Should AI have rights?

=== ROUND 1 ===

Your argument tactics:
[1-10 list shown]

Choose your tactic (1-10): 5
Make your argument: If we give rights to AI, should we also give rights to calculators and thermostats?

AI uses: logical_reasoning
AI argues: Rights aren't based on computation but on capacity for interests and agency...

--- Round Judgment ---
AI wins this round! (7 vs 5)
Explanation: The reductio was clever but oversimplified the criteria for rights...

SCORE - You: 0 | AI: 1

Continue to next round? (yes/no): yes

=== ROUND 2 ===
[continues...]
```

---

## Technical Note

Mind Game is implemented in AILang, a natural language programming system where AI executes structured English instructions. The specification combines deterministic game rules (scoring, rounds, tactics) with intelligent operations (argument generation, quality evaluation, contextual responses). This hybrid approach ensures consistent gameplay while enabling dynamic, context-aware debates.

For more about AILang, see the specification at `github.com/pcoz/ailang`
