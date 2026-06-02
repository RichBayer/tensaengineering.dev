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
    knowledge-base/
    glossary/
    knowledge-base/ai-operations/
    knowledge-base/persistent-ai-memory/
    knowledge-base/controlled-ai-systems/
    knowledge-base/local-first-ai/
    knowledge-base/safe-tool-interaction/
    knowledge-base/linux-diagnostics/
    knowledge-base/troubleshooting-training/
    knowledge-base/neurocore-architecture/
    story/

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
- public explanation-layer framing
- future public artifact direction

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
    Argus Lab = early real-Linux troubleshooting, training, and validation environment

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

The NeuroCore page is a public platform explainer.

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

The page should remain public-facing.

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

    Live

Current role:

The Argus ACLI page explains Argus as the first practical product / distribution built on NeuroCore.

It explains:

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

Use these before rewriting or significantly expanding the Argus ACLI page:

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

    Live

Current role:

The Argus Lab page explains Argus Lab as an early real-Linux troubleshooting, training, and validation environment.

It explains:

- original personal Linux troubleshooting practice goal
- portfolio origin
- real Linux failure scenarios
- controlled fault injection
- resettable lab sessions
- realistic support-ticket-style scenarios
- mentor-style AI guidance
- validation role for NeuroCore and Argus ACLI
- current early implementation status
- what Argus Lab is not

Important:

Argus Lab is in early implementation.

Do not imply it is publicly available, downloadable, or a finished training product.

---

### Source Docs Used For Current Full Page

Current full page was written from:

    Argus Lab README.md
    Argus Lab docs/vision/argus_lab_vision.md

If expanding deeper implementation details later, also use:

    Argus Lab architecture docs
    Argus Lab scenario planning docs
    Argus Lab validation strategy docs
    Argus Lab training flow docs
    Argus Lab mentor-mode behavior docs

---

### Special Notes

Argus Lab is early implementation.

Do not describe it as publicly available or finished.

Do not make it sound like a simple quiz platform.

Do not make it sound like a fake terminal simulator.

Core idea:

    Real skill comes from solving real problems.

---

## Knowledge Base Index

Path:

    knowledge-base/index.html

Current status:

    Live

Current role:

The Knowledge Base is the public teaching layer for concepts that appear across the ecosystem.

It currently introduces and routes readers through the first recommended eight-article path:

    AI Operations
    Persistent AI Memory
    Controlled AI Systems
    Local-First AI
    Safe Tool Interaction
    Linux Diagnostics
    Troubleshooting Training
    NeuroCore Architecture

---

### Required Source Docs Before Major Knowledge Base Index Rewrite

Use:

    docs/planning/website_information_architecture.md
    docs/website_state.md
    docs/ai-operations/tensa_website_resume_prompt.md
    docs/infrastructure/tensa_repository_map.txt
    docs/planning/internal_linking_strategy.md
    docs/planning/page_inventory.md
    docs/planning/content_style_guide.md

Use source docs from the relevant project whenever the Knowledge Base index makes specific factual claims beyond routing and summary language.


---

## Glossary Page

Path:

    glossary/index.html

Current status:

    Live

Current role:

The Glossary page is the public reference page for important TENSA ecosystem terms.

It explains compact definitions for:

- TENSA Engineering
- NeuroCore
- Argus ACLI
- Argus Lab
- AI Operations
- Linux diagnostics
- control-plane language
- evidence and telemetry language
- memory and continuity language
- tool-boundary language

The Glossary page supports readers without bloating every public page.

It also serves as the target for inline glossary tooltip links from Knowledge Base articles.

---

### Required Source Docs Before Major Glossary Rewrite

Use:

    docs/planning/glossary_strategy.md
    docs/planning/content_style_guide.md
    docs/planning/internal_linking_strategy.md
    docs/planning/page_inventory.md
    docs/website_state.md
    current public project pages
    current Knowledge Base articles

Use relevant project source docs if adding or changing definitions that make factual project claims.

---

### Special Notes

Glossary definitions should be short, plain-English, and helpful.

Do not turn the Glossary into a full Knowledge Base replacement.

Do not add terms just because they are interesting.

Add terms when they help readers understand current public pages.

Inline glossary tooltip behavior is governed by:

    docs/planning/glossary_strategy.md
    docs/planning/internal_linking_strategy.md
    assets/js/glossary-tooltips.js

---

## Knowledge Base Article Source Requirements

These are factual public teaching articles.

Do not rewrite or significantly expand them from memory.

Use the article-specific requirements below, plus:

    docs/planning/content_style_guide.md
    docs/planning/internal_linking_strategy.md
    docs/planning/page_inventory.md
    docs/website_state.md
    current public project pages when changing ecosystem relationship language

---

### AI Operations Article

Path:

    knowledge-base/ai-operations/index.html

Current status:

    Live

Current role:

Explains AI Operations as the discipline of making AI-assisted work repeatable, grounded, reviewable, and continuous.

Required source material before major rewrite:

    TENSA AI-operations workflow docs
    TENSA website resume prompt
    TENSA documentation closeout protocol
    Claude website polish workflow prompt if discussing multi-model writing workflow
    AI Operations methodology source material
    current Story page if changing origin/workflow bridge language

Special notes:

- Keep this article focused on disciplined AI-assisted work.
- Do not turn it into a generic prompting tips article.
- Preserve the distinction between AI productivity and governed AI operations.

---

### Persistent AI Memory Article

Path:

    knowledge-base/persistent-ai-memory/index.html

Current status:

    Live

Current role:

Explains why AI memory is useful but not the same as continuity, and why source-grounded context matters.

Required source material before major rewrite:

    NeuroCore origin story source material
    The Day The AI Forgot Everything source material
    NeuroCore memory/context planning docs when available
    NeuroCore RAG / retrieval docs if changing retrieval claims
    NeuroCore architecture docs if changing platform continuity claims
    current NeuroCore project page
    current Story page

Special notes:

- Keep memory, continuity, and source-grounded context clearly separated.
- Do not imply the future memory system is fully implemented unless source docs prove it.
- Preserve current-vs-future distinction around advanced memory, context-aware generation, and Karpathy-style wiki ideas.

---

### Controlled AI Systems Article

Path:

    knowledge-base/controlled-ai-systems/index.html

Current status:

    Live

Current role:

Explains the TENSA principle that AI can reason, but authority must be governed.

Required source material before major rewrite:

    NeuroCore control plane docs
    NeuroCore tool execution docs
    NeuroCore security / policy docs
    NeuroCore observability docs
    NeuroCore architecture docs
    current NeuroCore project page
    current Safe Tool Interaction article if changing tool-boundary language
    current public incident references if changing external incident examples

Special notes:

- Keep incident examples cautious, sourced, and limited.
- Do not overclaim causality from public reports.
- Preserve the distinction between reasoning, authority, approval, and execution.

---

### Local-First AI Article

Path:

    knowledge-base/local-first-ai/index.html

Current status:

    Live

Current role:

Explains why the default trust boundary should start close to the user, the system, and the evidence.

Required source material before major rewrite:

    NeuroCore local-first architecture/source docs
    Argus ACLI local-first diagnostic source docs
    NeuroCore project page
    Argus ACLI project page
    privacy / security positioning docs if available
    current Controlled AI Systems and Safe Tool Interaction articles if changing trust-boundary language

Special notes:

- Keep local-first framed as a trust-boundary and system-awareness design choice.
- Do not pretend local-first eliminates all risks.
- Do not imply cloud models are never useful.
- Preserve practical tradeoffs.

---

### Safe Tool Interaction Article

Path:

    knowledge-base/safe-tool-interaction/index.html

Current status:

    Live

Current role:

Explains how AI can work near tools and systems without becoming an uncontrolled operator.

Required source material before major rewrite:

    NeuroCore control plane docs
    NeuroCore tool registry docs
    NeuroCore BaseTool / tool contract docs
    NeuroCore command runner docs
    NeuroCore execution engine docs
    NeuroCore security / policy docs
    current Controlled AI Systems article
    current NeuroCore Architecture article

Special notes:

- Preserve the model-authority boundary.
- Do not describe the model as directly executing commands.
- Do not recommend destructive or state-changing behavior outside governed tool paths.
- Keep public examples clear but not implementation-leaky.

---

### Linux Diagnostics Article

Path:

    knowledge-base/linux-diagnostics/index.html

Current status:

    Live

Current role:

Explains evidence-first troubleshooting and why diagnostic systems must start from real system signals rather than guesses.

Required source material before major rewrite:

    Argus ACLI source docs
    Argus output/tool contract docs
    Argus tool layer docs
    Argus system summary / analysis docs
    NeuroCore tool execution docs
    relevant service diagnostics / Kernel-Up planning docs if changing service intelligence language
    current Argus ACLI project page
    current Safe Tool Interaction article
    current NeuroCore Architecture article

Special notes:

- Keep diagnostics grounded in raw evidence, telemetry, logs, findings, severity, and recommendations.
- Do not imply Argus diagnoses everything.
- Preserve current-vs-future distinction around service intelligence, Kernel-Up, and broader diagnostic coverage.

---

### Troubleshooting Training Article

Path:

    knowledge-base/troubleshooting-training/index.html

Current status:

    Live

Current role:

Explains why diagnostic tools and AI guidance still need human judgment, practice, and structured troubleshooting skill.

Required source material before major rewrite:

    Argus Lab README.md
    Argus Lab docs/vision/argus_lab_vision.md
    Argus Lab validation / scenario docs if changing implementation details
    Argus Lab training flow / mentor-mode docs if changing guidance behavior
    current Argus Lab project page
    current Linux Diagnostics article
    current Argus ACLI project page

Special notes:

- Keep Argus Lab status accurate as early implementation where appropriate.
- Do not imply public availability, downloadable access, or finished platform maturity before those exist.
- Do not describe Argus Lab as a simple quiz or fake-terminal simulator.
- Preserve the training-vs-diagnostics distinction.

---

### NeuroCore Architecture Article

Path:

    knowledge-base/neurocore-architecture/index.html

Current status:

    Live

Current role:

Explains NeuroCore as the governed platform behind TENSA's AI systems, including runtime, control path, tool boundary, context layer, evidence layer, model explanation layer, and product foundation.

Required source material before major rewrite:

    NeuroCore README.md
    NeuroCore docs/architecture/neurocore_vision.md
    NeuroCore docs/architecture/system_state.md
    NeuroCore docs/architecture/system_architecture.md
    NeuroCore docs/architecture/control_plane.md
    NeuroCore docs/architecture/tool_execution.md
    NeuroCore docs/architecture/security_policy.md
    NeuroCore docs/architecture/observability.md
    NeuroCore docs/architecture/neurocore_master_blueprint.md
    NeuroCore Argus / ACLI distribution docs if changing product-foundation language
    current NeuroCore project page
    current Argus ACLI project page
    current Argus Lab project page

Special notes:

- Keep implemented, planned, and future-direction claims clearly separated.
- Do not make the article more implementation-specific than public-facing site strategy allows.
- Do not turn the public article into the private architecture manual.
- Preserve NeuroCore as the governed platform, not a chatbot wrapper.

---

## Story Page

Path:

    story/index.html

Current status:

    Live

Current role:

The Story page explains the origin and philosophy behind TENSA Engineering, NeuroCore, Argus ACLI, Argus Lab, and AI Operations.

It preserves the real origin story without making the homepage too long.

The Story page explains:

- the day the AI forgot everything
- why AI memory failed as a project continuity layer
- why documentation became project memory
- why workflow discipline started to mirror architecture discipline
- how local AI changed the direction
- why real systems required control
- how NeuroCore emerged
- how Argus ACLI became the first practical proof
- how Argus Lab became the early training and validation environment
- how AI Operations became the disciplined way of working behind the ecosystem

Important:

The Story page should remain human, readable, and grounded.

Do not turn it into:

    a technical architecture manual
    a Knowledge Base article
    a roadmap dump
    an internal planning note
    a marketing hype page

Deeper technical definitions belong in the Knowledge Base or Glossary, depending on whether the reader needs a full article or a compact reference definition.

---

### Source Docs Used For Current Story Page

Current full page was written from:

    NeuroCore origin story source material
    The Day The AI Forgot Everything source material
    AI Operations methodology split source material
    Current public NeuroCore page
    Current public Argus ACLI page
    Current public Argus Lab page
    docs/planning/content_style_guide.md
    docs/planning/website_information_architecture.md
    docs/website_state.md

---

### Required Source Docs Before Major Story Rewrite

Use:

    docs/planning/website_information_architecture.md
    docs/website_state.md
    docs/ai-operations/tensa_website_resume_prompt.md
    docs/planning/content_style_guide.md
    docs/planning/internal_linking_strategy.md

Use origin story material:

    NeuroCore origin story notes
    The Day The AI Forgot Everything source material
    AI Operations / continuity workflow source material

Use public project pages when changing ecosystem relationship language:

    projects/neurocore.html
    projects/argus-acli.html
    projects/argus-lab.html

Use specific NeuroCore / Argus / Argus Lab source docs if adding deeper technical claims.

---

### Potential Future Story / Philosophy Pages

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

- future public technical artifacts
- selected public documentation
- future Argus ACLI install/download page
- future videos
- future social channels
- future docs index
- future release notes
- future public repository or open-component links, if deliberately approved

Do not add direct public links to private implementation repositories.

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

    docs/planning/old_site_migration_plan.md

Existing core docs:

    docs/planning/page_inventory.md
    docs/planning/content_style_guide.md
    docs/planning/internal_linking_strategy.md
    docs/planning/seo_topic_map.md
    docs/ai-operations/claude/claude_website_polish_resume_prompt.md

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

## Replacement Verification Rule

After each full-file replacement during closeout or live website editing, run a targeted verification check before moving to the next file.

The verification should confirm the intended change actually landed and that old/stale text or links were removed when applicable.

Examples:

    grep -n "Glossary Page\|glossary/index.html\|glossary_strategy.md\|early implementation" docs/planning/content_source_map.md
    grep -n 'href="../story/"\|href="../index.html#story"' projects/argus-lab.html

This rule exists to catch:

- paste mistakes
- missed saves
- wrong-file edits
- stale snippets
- unintended partial replacements

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

After each full-file replacement, run a targeted verification check before moving to the next file.

No hidden changes.

No guessing.

Ask for source docs before writing factual project pages.
