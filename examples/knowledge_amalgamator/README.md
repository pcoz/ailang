# Knowledge Amalgamator Example

## Overview

This example demonstrates AILang's approach to knowledge ingestion and conversational retrieval from heterogeneous document sources. The implementation uses a **lightweight Person entity** as an organizational framework for processing information according to document structure characteristics, with strict provenance tracking throughout.

## What This Example Does

The system consists of two AILang programs:

* **`knowledge_amalgamator.ail`** - Ingests documents and builds structured memory files
* **`knowledge_responder.ail`** - Provides conversational access to the ingested knowledge with strict source attribution

## Example Use Case: Software Project Documentation

Given these inputs:
- Project management docs (meetings, timelines)
- Functional specifications (30-page PDF)
- Jira epics and user stories
- Email communications (escalations, decisions)
- Slack conversations (technical discussions)

### Processing Results

The amalgamator produces exactly six files (no more, no less):

1. `episodic_memory.jsonl` - Processing history
2. `semantic_memory.graph.json` - Extracted facts, decisions, risks
3. `procedural_memory.json` - Runbooks and step-by-step procedures
4. `outline_index.json` - Document structure backbone
5. `citation_index.csv` - Global provenance mapping
6. `manifest.json` - Integrity verification

### Query Examples

```
User: "How's this project going generally?"

Archivist: Yellow—generally on track, but with real risks you're 
actively managing.

[Provides evidence-based snapshot with precise citations:]
- Overall status: marked "🟡 Yellow" (Meetings.pdf → p.1)
- Current sprint health: burndown on track, 0 blocked stories 
  (Meetings.pdf → p.5)
- Key risks: Legacy DB credentials delayed (Meetings.pdf → p.5), 
  Incomplete historical data migration (Meetings.pdf → p.7)
```

```
User: "Should we remove any gold plating from the initial release?"

Archivist: Yes—trim the "gold plating" from R1. You already have 
clear markers for what can move to Phase 2.

What to defer (with receipts):
- Redis caching for tariff lookup (Slack.pdf → p.8: "nice to have, 
  P2")
- Denormalized customer data view (Slack.pdf → p.8: grouped with 
  P2 items)
[Provides exact Jira keys and one-liner for status deck]
```
### Design Choices

#### Provenance Strictness

The responder operates in two modes:

- **Default**: Returns sourced facts + clearly-marked general guidance
- **Strict**: Returns ONLY sourced facts, suppresses all guidance

This prevents the system from inventing claims or mixing speculation with evidence.

#### Fact vs. Guidance Separation

Every response clearly separates:

```
# SOURCE-DERIVED FACTS & QUOTES
[SOURCE] Project status marked "🟡 Yellow" — Meetings.pdf (p.1)
[SOURCE] Redis caching classified as P2 — Slack.pdf (p.8)

# GENERAL ADVICE (clearly marked as guidance)
[GUIDANCE] Consider moving optimization tasks to Phase 2 if 
timeline pressure increases
```

### Running This Example

See the PDF transcripts in this directory showing the actual execution:
- `knowledge_amalgamator - load data.pdf` - Ingestion execution
- `knowledge_amalgamator - chat.pdf` - Query session

The system processes 116 pages of heterogeneous documentation and enables precise, cited question-answering without inventing facts or losing source attribution.

## Key Advantages Over Traditional Knowledge Graphs

### 1. Structure-Aware Processing

Rather than forcing all documents through a uniform extraction pipeline, the system classifies sources qualitatively:

- **Well-structured** (Confluence, formal specs) → Store outlines + anchors only
- **Semi-structured** (Reports with sections) → Limited synthesis 
- **Loosely-structured** (Slack, email) → Heavy internalization into semantic/procedural memory

This mirrors how humans actually read: we skim structured docs but carefully distill messy conversations.

### 2. Provenance-First Architecture

Every piece of internalized knowledge maintains traceable provenance:

```json
{
  "id": "concept_node_id",
  "label": "Late fee assessment rule",
  "provenance": {
    "artifact_id": "Jira-Epics.pdf",
    "uri": "path/to/source",
    "anchors": ["page 16, line 143"]
  }
}
```

The responder **never generates claims without citations** - it either returns sourced facts or clearly-marked guidance.

### 3. Person-Entity Framework (Lightweight Implementation)

The responder creates a minimal Person entity with basic profile attributes:

```ailang
CREATE Person respondent WITH:
  name: "Archivist"
  temperament: "calm, evidence-driven, collaborative"
  style: "clear, structured, cites sources"
END_CREATE
```

This serves as an organizational framework that:
- Provides a coherent interaction model
- Establishes consistent response patterns
- Enables natural conversational flow
- Maintains behavioral consistency across queries

**Note**: The current implementation uses a lightweight Person entity primarily for organizational purposes. The full Person subsystems (Personality/Logos-Energiae-Ethos, multi-layered Memory Systems, Planning & Navigation) are **not** actively implemented in this version. The memory files are loaded and accessed through custom objects (`MemIO`, `Provenance`) rather than through Person.memory_system.

### 4. Multi-Layered Memory Architecture

The amalgamator produces distinct memory types:

- **Episodic memory** → "What did I process and when?"
- **Semantic memory** → Facts, decisions, risks extracted from loose sources
- **Procedural memory** → Runbooks and step-by-step processes
- **Outline index** → Navigation backbone for structured docs

This creates natural boundaries between different kinds of knowledge.

### 5. Intelligent Synthesis Only Where Appropriate

The system **doesn't** attempt to:
- Paraphrase well-structured content (just link to it)
- Generate summaries of complete documents
- Create redundant semantic nodes for content already in clean outlines

It **does** intelligently extract:
- Decisions buried in email threads
- Risks mentioned in Slack conversations

## What This Demonstrates About AILang

1. **Person entities provide organizational coherence** for knowledge management systems
2. **Qualitative classification** (structure_classes) allows intelligent processing adaptation
3. **Provenance tracking** is first-class, not an afterthought
4. **Bounded intelligence** - AI synthesis only where document structure is insufficient
5. **Deterministic outputs** - strict contracts prevent hallucinated file creation
6. **Clear fact/guidance boundaries** - AILang script controls the interpretation layer
