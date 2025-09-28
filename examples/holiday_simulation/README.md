# AILang Example — **Person-Centric Group Holiday Synthesizer (Gateshead → Madrid)**

This example shows how to use AILang’s **person function** and **intelligent blocks** to synthesize five named, locally-plausible people from Gateshead-upon-Tyne and have them co-create a complete summer holiday to Madrid—planning, travel, daily choices, conversations, frictions, repairs, and post-trip reflections. It demonstrates **structured emergence**: you specify constraints and intent; the runtime generates lifelike behavior and dialogue without hard-coding outcomes.

---

## What this example is

A self-contained, runnable scenario that:

* **Creates five people** with backgrounds, personalities, and interaction systems using `INTELLIGENTLY create_person … WITH HINTS/BOUNDS`.
* **Plans a trip** (dates, flights, lodging, budget) under explicit constraints (heat safety, walkability, A/C, quiet hours).
* **Simulates days** with weather, siestas, activities, food, nightlife, and **explicit social intercourse** (conversations, micro-conflict and repair).
* **Emits two artifacts**:

  1. a structured **holiday report** (JSON) suitable for downstream analysis/visualization, and
  2. a **readable memoir** generated from the report.

You can see both in the bundled outputs:

* `holidays_output.json` – the synthesized report with dates, area, routes, dialogues, costs, and reflections 
* `holidays_memoir.md` – a narrative write-up of the same trip, preserving all details as story prose 

---

## Why it’s powerful

* **People first, plans second.** Trips aren’t just itineraries—they’re interactions. The example shows how **person models** drive **emergent choices** (e.g., runner’s dawn routines vs. late-night music; vegetarian preferences shaping tapas routes).
* **Bounded realism without brittleness.** You guide generation with **HINTS** (names, age ranges, job hints) and **BOUNDS** (“fictional but locally plausible”), avoiding brittle hard-coding while keeping outputs coherent.
* **Constraint-aware synthesis.** Heat/siesta cadence, walkability, and quiet hours are respected automatically—e.g., **siesta windows**, **hydration cues**, and **A/C usage** all surface organically in the day logs and memoir (see the JSON’s daily advisories and siesta blocks, and the memoir’s repeated “blinds down, A/C on eco” cadence).  
* **Social dynamics & repair.** Minor frictions (late-night vs. early runs; venue volume) appear naturally and are **repaired** via apology/compromise/splitting then rejoining—modeled explicitly in both artifacts. 
* **Dual artifacts: data ↔ story.** The same run produces a machine-readable report and a human-readable memoir, keeping analysis and communication in sync.  

---

## Files in this example

```
/examples/people_holiday_madrid/
├─ holiday.ail               # The AILang program (person-centric generator)
├─ holidays_output.json      # Example run output (structured report)
└─ holidays_memoir.md        # Example memoir produced from the report
```

* The JSON shows: **dates** (Fri→Wed in August), **origin NCL → MAD** with BCN connection, **Malasaña** apartment with A/C and walkability, **daily diaries** (weather, activities, spend), **conversations**, **return journey**, **settlement**, and **reflections**. 
* The memoir retells those exact details (Prado mornings, Retiro dawn run, flamenco, tapas, rooftop, minor delay on return, fair split of costs) in fluent prose. 

---

## How it works (spec constructs)

### 1) People (the **person function**)

The program invokes:

```ailang
INTELLIGENTLY create_person FROM "Gateshead-upon-Tyne" WITH:
  OUTPUT: lee
  MUST_INCLUDE: [name, background, personality, interaction_system]
  BOUNDS: "fictional but locally plausible"
  HINTS: {name: "Lee Robson", age_range: [28, 35], job_hint: "joiner", football: "Newcastle sympathies"}
END
```

* **HINTS** guide synthesis; **MUST_INCLUDE** ensures each person has a profile + interaction system.
* Similar blocks create Ayesha, Callum, Sophie, and Gavin. These people then **speak**, **negotiate**, and **influence** choices throughout the itinerary (see JSON `conversations` and memoir dialogue).  

### 2) Planning (constraints + intelligent choice)

Blocks like `plan_basics` synthesize **dates**, **flights**, and **stay** options, then pick balanced choices under constraints (budget cap, A/C, quiet hours, walkability). The outputs match what you see in the JSON: Fri→Wed in August; NCL→BCN→MAD; **Malasaña** top-floor flat with A/C; **walk score ≈ 97**; supermarket and Metro proximity. 

### 3) Day simulation (weather, siesta, social)

Each day is generated with:

* **Weather advisories** (e.g., “siesta strongly advised 14:00–18:00”).
* **Activity blocks** (Prado, Retiro, Bernabéu, Lavapiés tour, Reina Sofía).
* **Conversations** and **minor frictions** + **repair** steps.
  All of this is visible in `diary` and `conversations`, and then rendered narratively in the memoir (e.g., loud venue → quieter bar; split for sleep vs. music).  

### 4) Post-processing (dual artifacts)

* The program **emits JSON** (for analytics/pipelines/dashboards).
* A second pass renders a **memoir** from that JSON, preserving every fact but changing the medium. Compare the tapas items, flamenco scene, Retiro dawn run, and closing circle across both files.  

---

## What to look for in the outputs

* **People drive the plot.** Note how Sophie’s running and Ayesha’s veg preferences shape mornings and menus, while Lee/Callum’s football interest shapes Day 3. 
* **Heat-aware cadence.** Siesta and hydration are structural, not afterthoughts. 
* **Conflict-repair pattern.** Volume too high? Group splits and reconvenes. Late night vs. early run? Pre-agreed micro-split, then breakfast together. 
* **Dual artifacts stay in sync.** Cross-check the memoir’s scenes with the JSON’s facts (e.g., **Malasaña flat**, **Tribunal station**, **Prado → Retiro → Gran Vía** flow, **minor delay** on return).  

---

## Extending the example

* **Swap the origin/city** while keeping the person seeds; watch how choices adapt to a different climate/culture.
* **Add accessibility constraints** (e.g., lift/elevator requirements, step-free routes).
* **Introduce roles** (e.g., trip “treasurer,” “navigator,” “restaurant-scout”) and see how conversations change.
* **Instrument costs** with stricter budget envelopes; feed the JSON to a dashboard for spend vs. plan.

---

## FAQ

**Is anything hard-coded?**
No outcomes are hard-coded. Names and **HINTS/BOUNDS** guide synthesis; all events, scenes, and dialogue are generated under constraints and person dynamics. The artifacts capture those emergent results (see outputs).  

**Why model people explicitly?**
Because **intent lives in people**. When personas carry traits and preferences, itineraries become the *consequence* of who’s traveling—not a brittle list of to-dos.

**What if I rerun it?**
You’ll get **variant but consistent** trips—same scaffolding and constraints, new micro-events and lines—unless you fix a deterministic seed (if your runner supports it).

---

### Credits

* Example program: `holiday.ail`
* Example outputs: `holidays_output.json`, `holidays_memoir.md` (generated from a single AILang run and then rendered by AI as prose).  


