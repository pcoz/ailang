# AILang Example: Requirements → Workflows → Use Cases → Persona‑on‑the‑fly User Stories

This worked example shows how to take a real‑world **requirements specification** and automatically derive:
1) end‑to‑end **Workflows** and reusable **Sub‑Workflows**, then  
2) canonical **Use Cases**, and finally  
3) **User Stories** that generate the **right persona on the fly** (no global persona cache).

It demonstrates AILang + AI performing: **Extract → Discover Workflows → Synthesize Use Cases → Generate Persona‑on‑the‑fly Stories** — all in one pass.

---

## Inputs

- A requirements document/documents describing system capabilities, actors/users, goals, constraints, events, and dependencies.  
  In this worked example we used “Technical Specifications_Mobile Surveillance System_Item 3.pdf” specification as the source.

- **`use_cases_and_user_stories.ail`**: the AILang program that performs the transformation. It expects the requirements as `requirements_spec.txt` by default (you can point it to the PDF‑to‑text output you prefer).

---

## Outputs

- **`outputs/workflows-usecases-userstories.md`**  
  A single, human‑readable Markdown doc with:
  - **Workflows**: end‑to‑end processes discovered from the spec
  - **Sub‑Workflows**: reusable sequences (e.g., setup, safety interlocks, evidence handling)
  - **Use Cases**: preconditions, triggers, main/alternate flows, postconditions, business rules
  - **User Stories (Persona‑on‑the‑fly)**: persona is synthesized **per story** from the use case context, constraints, and domain — not reused globally — plus Acceptance Criteria and Definition of Done hints

- **`outputs/personas.json`** (optional)  
  If enabled in the script, you can also output the ephemeral persona snapshots that were used when generating each story. These are constructed on demand and are **not** intended as master personas.

---

## How it works (methodology)

The example uses a single AILang program that runs four stages in sequence:

1) **Extract** structured signals from the requirements  
   - actors, domains, goals, features, constraints, business rules, **events**, **dependencies**, and artifacts.

2) **Discover Workflows** and **Sub‑Workflows** **first**  
   - Group features and goals into top‑level **workflows** (ordered stages).  
   - Detect recurring stage sequences and promote them to **sub‑workflows** for reuse (e.g., elevation/park interlocks, DVR evidence handling).

3) **Synthesize Use Cases** from workflow stages  
   - Each stage becomes one or more use cases with canonical fields: primary actor, stakeholders, preconditions, triggers, main & alternate flows, postconditions, business rules.  
   - Global **constraints** are attached as guardrails. **Events** and **dependencies** inform sequencing and triggers.

4) **Generate Persona‑on‑the‑fly User Stories**  
   - For each use case, a **fresh Person** is synthesized based on the UC’s role, domain, and constraint posture (e.g., privacy/security/performance).  
   - No global persona cache is used: the persona is **tailored to the story**.  
   - Produce a story title, **Acceptance Criteria** (including NFR‑aware checks), and a brief **Definition of Done** checklist.

This design ensures the user stories reflect **true context** (actor + domain + constraints) and avoids generic personas that don’t match the scenario.

---

## The AILang script (use_cases_and_user_stories.ail)

The core sections of the program are:

- `extract_requirements(text)` — deterministic extraction with bounded intelligence.  
- `discover_workflows(...)` — builds ordered workflows and reusable sub‑workflows.  
- `synthesize_use_cases(...)` — converts workflow stages to canonical use cases.  
- `synthesize_person_for_uc(uc, domains, constraints)` — **persona‑on‑the‑fly** builder.  
- `use_case_to_user_stories(...)` — generates contextual user stories with AC/DoD.  
- Output composer that collates all sections into `outputs/workflows-usecases-userstories.md`.

> The script is self‑contained and does not require external taxonomies; it strictly works off your provided requirements document(s).

---

## Customization tips

- **Enforce your templates**: replace the Use Case / Story composition section with your organization’s headings (e.g., RUP‑style UCs, Jira story format, full Gherkin).  
- **Tune persona synthesis**: adjust the mapping from constraints/domains to persona values (e.g., add accessibility, safety‑criticality).  
- **Emit traceability**: add a section that lists which requirement clauses influenced each workflow/UC/story.  
- **Language/locale**: the output is Markdown; feel free to switch headings or phrasing to your target language.

---

## Validation checklist (quick QA)

- Workflows cover all major goals and features; sub‑workflows capture repeats.  
- Each use case has clear preconditions, triggers, and postconditions.  
- Acceptance Criteria include constraint‑sensitive checks (security/privacy/performance, as applicable).  
- Stories read naturally and the persona feels appropriate to the scenario.  
- Cross‑check a sample of outputs back to the requirements text (spot‑verify traceability).

---

## License & attribution

- Replace the example input with your own requirements document(s).  
- The AILang program in `use_cases_and_user_stories.ail` is provided as an example; adapt freely to your processes and templates.
