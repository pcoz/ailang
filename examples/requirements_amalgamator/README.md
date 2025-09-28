# AILang Example — **Requirements Amalgamator (Scattered → Normalized Register)**

This example shows how to use AILang to **ingest scattered requirements** from multiple real-world sources (JIRA tickets, Confluence pages, emails, Slack, and meeting notes) and synthesize a single **normalized Requirements Register** (Excel). It demonstrates how AILang’s “intelligent” constructs can merge, de-duplicate, and reconcile inconsistencies while preserving provenance/traceability.

---

## What this example is

A runnable AILang script, `reqs.ail`, that:

* **Reads heterogeneous inputs**:

  * JIRA auth epic (PTA-101) with registration/login/reset/session details. 
  * Confluence high-level app requirements: Projects, Tasks (fields & statuses), Roles.   
  * Email thread on **task assignment** (members only, searchable dropdown), **history of reassignments**, and **email notifications** (SendGrid, opt-out).  
  * Slack brainstorm on **due-date reminders**, **in-app notifications**, **user-configurable channels**, and **overdue highlighting**. 
  * JIRA dashboard/reporting ticket (PTA-205): **task list by due date**, **filters** (incl. new **priority** field), **overdue highlighting**, **quick actions**, **perf & mobile**, **links to notifications**, **depends on authentication**.   
  * Sprint-planning notes: finalize **Task CRUD** incl. change assignee/due/status, **delete only by creator/admin**, **notifications scope** (email for assignments & due dates only), **auto-add assignee to project**, **priority field → Confluence update**, **QA tests for dashboard filters**.  

* **Emits**: `/requirements_register.xlsx` — a single, filterable register that consolidates and cross-references all the above.

> Why it matters: in real teams, requirements live in ten places at once; this example shows how AILang can **pull the threads together into one coherent artifact** without losing context.

---

## Repository layout

```
/examples/requirements_amalgamator/
├─ reqs.ail                     # The AILang program (ingest + normalize + output)
├─ inputs/
│  ├─ reqs - 1.txt              # JIRA PTA-101 (Authentication)
│  ├─ reqs - 2.txt              # Confluence High-Level Requirements
│  ├─ reqs - 3.txt              # Email: Task Assignment & Notifications
│  ├─ reqs - 4.txt              # Slack: Notifications Brainstorm
│  ├─ reqs - 5.txt              # JIRA PTA-205 (Dashboard & Reporting)
│  └─ reqs - 6.txt              # Sprint Planning Notes
└─ output/
   └─ requirements_register.xlsx # Normalized register (generated)
```

---

## How it works (conceptual flow)

1. **Ingest & Parse**
   The script reads each source, preserving metadata (source type, ID, date, author) for traceability. Items are parsed into a **common interim schema** (Feature / Capability / Rule / Constraint / Acceptance Criterion / Decision / Open Question).

2. **Normalization & De-duplication**
   Overlapping fragments are **merged**:

* “Task statuses To Do / In Progress / Done” consolidated from Confluence into the canonical “Task” entity. 
* Dashboard’s new **priority** field and overdue highlighting are folded into the Task model and dashboard view. 
* Assignment rules (members only, searchable dropdown, reassignment history) captured as **Task.Assignment** constraints. 

3. **Policy Reconciliation**
   Where sources differ, the script applies hierarchy + recency:

* **Notifications** scope becomes: email on assignment and due dates (no SMS for now), configurable per user; in-app notifications for status changes; due-date reminders; overdue in red.  
* **Auth dependency** recorded: Dashboard requires login. 

4. **Acceptance & Non-functional capture**

* Auth ACs and session token expiry recorded under **Security**. 
* Dashboard performance (<2s) and mobile responsiveness saved as **NFRs**. 

5. **Governance & Traceability**
   Each register row includes **Source(s)** with pointers back to JIRA/Confluence/Email/Slack/Notes (you’ll see these as concatenated references in the Excel “Provenance” column). Example linkages:

* Task Priority: Confluence + JIRA PTA-205 + Sprint notes.   
* Assignment Emails: Email thread + Sprint notes (scope).  

---

**What you’ll see in the Excel:**

* Columns like: `REQ-ID`, `Title`, `Type` (Feature/Rule/AC/NFR/Decision), `Description`, `Status`, `Priority`, `Owner`, `Provenance (Source→Location)`, `Depends On`, `Acceptance`, `Notes`.
* Ready-to-filter facets for **Area** (Auth / Projects / Tasks / Dashboard / Notifications).
* Cross-references (e.g., Dashboard → depends on Authentication). 

---

## Why this is powerful

* **Reality-proof**: Teams rarely keep a single source of truth. This example shows how AILang can **converge messy threads** into one register without losing nuance.
* **Traceable by design**: Every line remains **explainable back to its source** (JIRA/Confluence/Email/Slack/Notes), so reviewers can audit and sign off with confidence.
* **Balanced “intelligence”**: The script uses AILang’s intelligent blocks to reconcile scopes (e.g., notifications) while **respecting explicit constraints** like NFRs and ACs.
* **Ops-ready**: The Excel output can feed your PMO dashboards, test-case generation, API design, and backlog grooming—immediately.

---

## Extend it

* Add more sources (contracts, API specs); the script will classify and merge.
* Flip on **conflict flags** to surface contradictions for human review (e.g., if two sources disagree on notification channels).
* Emit additional artifacts (Markdown spec, Mermaid diagrams) from the same normalized model.

---

**TL;DR**: This example turns **distributed, inconsistent requirements** into a **single authoritative register**—with provenance—showcasing AILang as a practical glue between human conversations and executable, auditable specification.
