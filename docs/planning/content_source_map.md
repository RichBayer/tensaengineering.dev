# TENSA Engineering Content Source Map

---

## Purpose

This document maps TENSA Engineering website pages to the source documents needed before writing, rewriting, or significantly expanding them.

The goal is to prevent drift.

TENSA website pages should not be written from memory, assumptions, or vague summaries when factual project details matter.

The website explains and teaches.

The repositories remain the source of truth.

---

## Core Rule

Before writing or significantly changing a factual project page, load the source docs for that page.

Do not guess.

Do not fill gaps with confident-sounding copy.

If the source docs are missing, ask for them.

---

## Current Public Pages

Current public pages:

    /
    projects/
    projects/neurocore.html
    projects/argus-acli.html
    projects/argus-lab.html

---

## Homepage

Path:

    index.html

Current status:

    Live

Current role:

The homepage is the front door for the TENSA Engineering ecosystem.

It should introduce:

- TENSA Engineering
- controlled AI systems
- NeuroCore
- Argus ACLI
- Argus Lab
- Knowledge Base direction
- origin story preview
- GitHub proof

The homepage should stay concise.

It should not become the full explanation of every project.

---

### Required Source Docs Before Major Homepage Rewrite

Use:

    docs/website_state.md
    docs/planning/website_information_architecture.md
    docs/ai-operations/tensa_website_resume_prompt.md
    docs/infrastructure/tensa_repository_map.txt

Use project source docs only if changing factual claims about a specific project.

---

## Projects Overview Page

Path:

    projects/index.html

Current status:

    Live

Current role:

The Projects page explains the ecosystem model:

    NeuroCore = platform
    Argus ACLI = first product / distribution
    Argus Lab = future training and validation environment

It should route visitors to individual project pages.

---

### Required Source Docs Before Major Projects Page Rewrite

Use:

    docs/website_state.md
    docs/planning/website_information_architecture.md
    docs/ai-operations/tensa_website_resume_prompt.md
    docs/infrastructure/tensa_repository_map.txt

For deeper factual project descriptions, also use the relevant source docs listed under each project below.

---

## NeuroCore Page

Path:

    projects/neurocore.html

Current status:

    Live

Current role:

The NeuroCore page is a story-first public explainer.

It explains:

- the personal Linux learning origin
- the AI forgetting problem
- context
- continuity
- why local AI mattered
- why local knowledge mattered
- why RAG mattered
- why a persistent daemon mattered
- why the control plane became necessary
- why controlled tools matter
- why observability matters
- what NeuroCore became
- how Argus ACLI and Argus Lab fit

The page should remain story-first.

Do not turn it into a dry architecture manual.

Deeper architecture detail should eventually move into Knowledge Base or Build Notes pages.

---

### Required Source Docs

Use these before rewriting or significantly expanding the NeuroCore page:

    NeuroCore README.md
    NeuroCore docs/architecture/neurocore_vision.md
    NeuroCore docs/architecture/system_state.md
    NeuroCore docs/architecture/system_architecture.md
    NeuroCore docs/architecture/control_plane.md
    NeuroCore docs/architecture/tool_execution.md
    NeuroCore docs/architecture/security_policy.md
    NeuroCore docs/architecture/observability.md
    NeuroCore docs/architecture/neurocore_master_blueprint.md

Use these build logs for origin and evolution:

    NeuroCore build-logs/000_foundation.md
    NeuroCore build-logs/001_runtime_stack.md
    NeuroCore build-logs/002_interface_layer.md
    NeuroCore build-logs/003_knowledge_layer.md
    NeuroCore build-logs/004_knowledge_retrieval.md
    NeuroCore build-logs/005_logic_layer_router.md
    NeuroCore build-logs/006_rag_reasoning_integration.md
    NeuroCore build-logs/009_neurocore_daemon_foundation.md
    NeuroCore build-logs/016_runtime_control_plane_enforcement.md
    NeuroCore build-logs/017_execution_layer_and_control_integration.md
    NeuroCore build-logs/018_observability_and_tracing.md

Use Argus Lab context if changing the Argus Lab section:

    Argus Lab README.md
    Argus Lab docs/vision/argus_lab_vision.md

---

### Special Notes

Old NeuroCore build logs may still reference the former project name:

    Jarvis

Public TENSA copy should use:

    NeuroCore

Do not mention the old name unless the page is specifically discussing the rename or early historical development.

---

## Argus ACLI Page

Path:

    projects/argus-acli.html

Current status:

    Placeholder

Current role:

The Argus ACLI page should eventually explain Argus as the first practical product / distribution built on NeuroCore.

It should explain:

- what Argus ACLI is
- why read-only diagnostics matter
- how Argus uses NeuroCore
- how system tools and Argus tools differ
- how real telemetry becomes structured findings
- severity classification
- recommendations
- raw evidence
- output controls
- current Linux / Ubuntu focus
- current V1 status
- future install/download direction when ready

---

### Required Source Docs

Use these before writing the full Argus ACLI page:

    NeuroCore docs/vision/argus_acli_vision.md
    NeuroCore docs/how_argus_works.md
    NeuroCore docs/architecture/argus_output_and_tool_contract.md
    NeuroCore docs/distributions/argus/acli_spec.md
    NeuroCore docs/distributions/argus/argus_distribution_and_deployment.md
    NeuroCore docs/distributions/argus_v1_blueprint.md
    NeuroCore docs/design/argus_acli_user_experience_layer.md
    NeuroCore docs/design/argus_tool_layer.md
    NeuroCore docs/design/argus_system_summary_v1.md
    NeuroCore docs/design/phase_5j_argus_core_tool_expansion.md
    NeuroCore docs/design/phase_6_argus_acli_output_control.md

Useful build logs:

    NeuroCore build-logs/021_argus_tool_layer_initial.md
    NeuroCore build-logs/022_structured_tool_contract.md
    NeuroCore build-logs/023_system_tool_structuring_and_normalization.md
    NeuroCore build-logs/024_argus_tool_layer_foundation_and_expansion.md
    NeuroCore build-logs/025_system_analysis_multi_signal.md
    NeuroCore build-logs/026_phase_6_argus_acli_output_control.md

Also useful:

    NeuroCore distributions/argus/manifests/argus_tool_manifest.md

---

### Special Notes

Argus ACLI should be presented as:

    read-only
    Linux-focused
    local-first
    evidence-backed
    practical
    built on NeuroCore

Do not overstate product maturity.

Do not imply install/download availability until that actually exists.

---

## Argus Lab Page

Path:

    projects/argus-lab.html

Current status:

    Placeholder

Current role:

The Argus Lab page should explain Argus Lab as the future real-Linux troubleshooting, training, and validation environment.

It should explain:

- original personal Linux troubleshooting practice goal
- portfolio origin
- real Linux failure scenarios
- controlled fault injection
- resettable lab sessions
- realistic support-ticket-style scenarios
- mentor-style AI guidance
- adaptive difficulty
- validation role for NeuroCore and Argus ACLI
- tracked troubleshooting progress
- demonstrated ability / proficiency direction

---

### Required Source Docs

Use these before writing the full Argus Lab page:

    Argus Lab README.md
    Argus Lab docs/vision/argus_lab_vision.md

If available later, also use:

    Argus Lab architecture docs
    Argus Lab scenario planning docs
    Argus Lab validation strategy docs
    Argus Lab training flow docs
    Argus Lab mentor-mode behavior docs

---

### Special Notes

Argus Lab is future-phase.

Do not describe it as currently available.

Do not make it sound like a simple quiz platform.

Do not make it sound like a fake terminal simulator.

Core idea:

    Real skill comes from solving real problems.

---

## Knowledge Base Index

Future path:

    knowledge-base/index.html

Current status:

    Not created

Future role:

The Knowledge Base should become the public teaching layer for concepts that appear across the ecosystem.

It should teach the ideas behind the projects without dumping raw technical docs into public pages.

---

### Required Source Docs Before Creating

Use:

    docs/planning/website_information_architecture.md
    docs/website_state.md
    docs/ai-operations/tensa_website_resume_prompt.md
    docs/infrastructure/tensa_repository_map.txt

Use source docs from the relevant project whenever a knowledge base page makes specific claims.

---

### Initial Knowledge Base Categories

Likely categories:

    Controlled AI Systems
    AI Operations
    Persistent AI Memory
    Local-First AI
    Safe Tool Interaction
    Linux Diagnostics
    Troubleshooting Training
    NeuroCore Architecture

---

## Story Index

Future path:

    story/index.html

Current status:

    Not created

Future role:

The Story section should explain the origin and philosophy behind TENSA Engineering, NeuroCore, Argus ACLI, and Argus Lab.

It should preserve the real story without making the homepage too long.

---

### Required Source Docs Before Creating

Use:

    docs/planning/website_information_architecture.md
    docs/website_state.md
    docs/ai-operations/tensa_website_resume_prompt.md

Use origin story material:

    NeuroCore origin story notes
    The Day The AI Forgot Everything source material
    AI Operations / continuity workflow source material

---

### Potential Story Pages

    story/the-day-the-ai-forgot-everything.html
    story/intelligence-without-continuity-is-fragile.html
    story/documentation-as-operational-memory.html
    story/ai-needs-structure-not-just-better-prompts.html

---

## Build Notes

Future path:

    build-notes/index.html

Current status:

    Not created

Future role:

Build Notes should make technical progress readable to the public.

They should not replace source build logs.

They should explain:

- what changed
- why it mattered
- what architectural lesson came from it
- where the source proof lives

---

### Required Source Docs Before Creating

Use:

    NeuroCore build logs
    NeuroCore architecture docs
    docs/planning/website_information_architecture.md
    docs/website_state.md

---

## Resources Page

Future path:

    resources/index.html

Current status:

    Not created

Future role:

The Resources page should collect useful links.

Potential links:

- NeuroCore GitHub repo
- Argus Lab GitHub repo
- future Argus ACLI install/download page
- future videos
- future social channels
- future docs index
- future release notes

---

## About Page

Future path:

    about.html

Current status:

    Not created

Future role:

The About page should explain TENSA Engineering and the mission.

It should be professional and concise.

It may mention the origin story, but the deeper origin story belongs in the Story section.

---

## Future Internal Planning Docs

Recommended future docs:

    docs/planning/page_inventory.md
    docs/planning/content_style_guide.md
    docs/planning/internal_linking_strategy.md
    docs/planning/seo_topic_map.md
    docs/planning/old_site_migration_plan.md

---

## Content Style Rules

Public pages should:

- teach clearly
- use conversational prose when explaining story or philosophy
- introduce technical terms, then explain them plainly
- avoid AI hype
- avoid corporate fluff
- distinguish current reality from future vision
- avoid pretending future-phase features are available
- avoid excessive bullets in narrative sections
- keep the homepage concise
- use deeper pages for deeper explanations

---

## Anti-Drift Rules

Always check:

    docs/website_state.md
    docs/ai-operations/tensa_website_resume_prompt.md
    docs/planning/website_information_architecture.md
    docs/infrastructure/tensa_repository_map.txt
    docs/planning/content_source_map.md

Before major work.

Use full file replacements only.

No hidden changes.

No guessing.

Ask for source docs before writing factual project pages.