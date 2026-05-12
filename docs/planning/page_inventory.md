# TENSA Engineering Page Inventory

---

## Purpose

This document tracks the public and internal pages in the TENSA Engineering website repository.

It exists to prevent website drift as the site grows from a small static website into a modular ecosystem knowledge platform.

Use this document to answer:

- What pages exist?
- What is each page for?
- What state is each page in?
- What source docs are required before expanding it?
- What navigation links point to it?
- What still needs to happen next?

This is an operational tracking document.

It does not replace:

- `docs/website_state.md`
- `docs/planning/content_source_map.md`
- `docs/planning/website_information_architecture.md`
- `docs/infrastructure/tensa_repository_map.txt`

---

## Status Key

Use these status labels consistently:

    Live
    Placeholder
    Structure-only
    Planned
    Needs source docs
    Needs rewrite
    Needs review

Definitions:

- **Live**: Page exists and is usable publicly.
- **Placeholder**: Page exists mainly to prevent dead links and reserve structure.
- **Structure-only**: Page exists as a public section/index, but deeper content is not built yet.
- **Planned**: Page does not exist yet.
- **Needs source docs**: Page should not be expanded until required source docs are loaded.
- **Needs rewrite**: Page exists but needs major content or structural work.
- **Needs review**: Page has changed and should be checked before closeout.

---

## Public Page Inventory

| Path | Page Title | Type | Status | Purpose | Source Docs Required | Navigation Status | Next Action |
|---|---|---|---|---|---|---|---|
| `/index.html` | TENSA Engineering | Homepage | Live | Introduces TENSA Engineering, the ecosystem, core philosophy, project cards, knowledge-base direction, origin story preview, and GitHub proof. | Website state, website information architecture, resume prompt, repository map. Project source docs only if factual project claims change. | Linked as Home from all current public pages. Header links to `/projects/`, `/knowledge-base/`, `#story`, and `#proof`. | Keep concise as front door. Do not turn into full knowledge base. |
| `/projects/index.html` | Projects | Public index page | Live | Explains the ecosystem structure and routes visitors to NeuroCore, Argus ACLI, and Argus Lab. | Website state, website information architecture, resume prompt, repository map. Project source docs if descriptions are expanded. | Linked from homepage and all current public headers. | Keep as ecosystem router. Expand only if needed for clarity. |
| `/projects/neurocore.html` | NeuroCore | Project detail page | Live | Story-first public explanation of NeuroCore’s origin, continuity problem, local-first direction, knowledge layer, daemon, control plane, tool execution, observability, Argus ACLI, and Argus Lab relationship. | NeuroCore README, NeuroCore vision, architecture docs, relevant build logs, Argus Lab context if Argus Lab section changes. | Linked from homepage project card, Projects page, Argus ACLI page, Argus Lab page, and footer calls to action. | Preserve story-first style. Move deeper architecture detail into Knowledge Base or Build Notes later. |
| `/projects/argus-acli.html` | Argus ACLI | Project detail page | Placeholder | Public destination for Argus ACLI as the first product/distribution built on NeuroCore. Currently a branded placeholder. | Required before full page: Argus ACLI vision, How Argus Works, Argus output/tool contract, ACLI spec, Argus deployment docs, Argus V1 blueprint, UX layer docs, tool layer docs, Phase 5J/6 docs, relevant build logs. | Linked from homepage project card, Projects page, NeuroCore page, and Argus Lab page. | Build full Argus ACLI page from source docs. Do not overstate product maturity. |
| `/projects/argus-lab.html` | Argus Lab | Project detail page | Placeholder | Public destination for Argus Lab as planned real-Linux troubleshooting, training, and validation environment. Currently a branded placeholder. | Required before full page: Argus Lab README and Argus Lab vision doc. Later: architecture, scenario planning, validation strategy, training flow, mentor-mode docs. | Linked from homepage project card, Projects page, NeuroCore page, and Argus ACLI page. | Build full Argus Lab page from source docs. Keep future-phase status clear. |
| `/knowledge-base/index.html` | Knowledge Base | Public index page | Structure-only | Establishes the Knowledge Base as the public teaching layer for controlled AI systems, AI operations, persistent AI memory, local-first AI, safe tool interaction, Linux diagnostics, troubleshooting training, and NeuroCore architecture. | Website information architecture, website state, resume prompt, repository map. Specific article source docs required when factual articles are created. | Linked from all current public headers. | Create first topic/category pages after internal linking strategy is defined. |

---

## Internal Planning / Continuity Docs

| Path | Type | Status | Purpose | Update Trigger |
|---|---|---|---|---|
| `docs/ai-operations/documentation_closeout_protocol.md` | AI operations / closeout protocol | Live | Defines the required documentation closeout workflow for serious website build sessions. | Update when closeout workflow rules change. |
| `docs/ai-operations/tensa_website_resume_prompt.md` | AI operations / resume prompt | Live | Fresh-thread startup context for website build sessions. | Update after major site structure, page, workflow, or direction changes. |
| `docs/website_state.md` | State record | Live | Current live-state record for pages, completed work, incomplete work, and next steps. | Update at closeout after major build sessions. |
| `docs/infrastructure/tensa_repository_map.txt` | Repository map | Live | Maps current repository structure and file roles. | Update after directories, assets, pages, or major files are added/removed/moved. |
| `docs/planning/website_information_architecture.md` | Planning / information architecture | Live | Defines long-term website structure, pillars, navigation, page strategy, and expansion plan. | Update only when the long-term architecture changes. |
| `docs/planning/content_source_map.md` | Source-doc map | Live | Defines required source docs before writing factual pages. | Update when new page types are added or source requirements change. |
| `docs/planning/page_inventory.md` | Page inventory | Live | Tracks what pages exist, what state they are in, and what needs to happen next. | Update whenever pages are created, renamed, retired, or change status. |
| `docs/planning/internal_linking_strategy.md` | Internal link strategy | Live | Tracks logical page-to-page relationships and preferred link destinations. | Update whenever major topic pages, project pages, story pages, or knowledge-base pages are added. |

---

## Planned Public Pages

| Planned Path | Page Type | Purpose | Dependency | Status |
|---|---|---|---|---|
| `/story/index.html` | Public section index | Introduce the story/philosophy section and route readers to origin/continuity pages. | Story source material and website IA. | Planned |
| `/story/the-day-the-ai-forgot-everything.html` | Story page | Public origin story explaining the continuity failure that led to NeuroCore. | Origin story source material. | Planned |
| `/resources/index.html` | Public section index | Collect GitHub repos, future downloads, future videos, documentation, and public resource links. | Website IA and current public resource inventory. | Planned |
| `/about.html` | Public standalone page | Explain TENSA Engineering, the mission, and builder context professionally and concisely. | Website IA and approved public bio/mission framing. | Planned |
| `/build-notes/index.html` | Public section index | Public-friendly build milestone summaries that link back to GitHub proof. | Build logs and source repos. | Planned |

---

## Planned Knowledge Base Categories

| Planned Path | Category | Purpose | Status |
|---|---|---|---|
| `/knowledge-base/controlled-ai-systems/` | Controlled AI Systems | Teach intelligence vs authority, control planes, execution governance, and safe AI-system interaction. | Planned |
| `/knowledge-base/ai-operations/` | AI Operations | Teach structured AI workflows, documentation as memory, context loading, resume prompts, and anti-drift safeguards. | Planned |
| `/knowledge-base/persistent-ai-memory/` | Persistent AI Memory | Teach AI forgetting, continuity loss, engineered continuity, and repository-grounded restoration. | Planned |
| `/knowledge-base/local-first-ai/` | Local-First AI | Teach local inference, data control, system awareness, privacy, and tradeoffs. | Planned |
| `/knowledge-base/safe-tool-interaction/` | Safe Tool Interaction | Teach tool registries, command boundaries, structured outputs, risk classification, and approval workflows. | Planned |
| `/knowledge-base/linux-diagnostics/` | Linux Diagnostics | Teach raw evidence, telemetry, logs, severity, recommendations, and diagnostic workflows. | Planned |
| `/knowledge-base/troubleshooting-training/` | Troubleshooting Training | Teach realistic failure scenarios, resettable labs, progressive guidance, and demonstrated ability. | Planned |
| `/knowledge-base/neurocore-architecture/` | NeuroCore Architecture | Teach runtime manager, control plane, tool layers, observability, and grounded system awareness in public-facing language. | Planned |

---

## Navigation Rules

Current primary navigation should point to:

    Home → /index.html
    Projects → /projects/
    Knowledge Base → /knowledge-base/
    Story → /index.html#story until /story/ exists
    GitHub → /index.html#proof until a resources/github page exists

When `/story/` is created:

    Story should point to /story/

When `/resources/` or a GitHub/resources page is created:

    GitHub may remain #proof on homepage or become Resources depending on site strategy.

Do not leave navigation pointing to old anchors once real top-level pages exist.

---

## Current Known Navigation State

Current pages with full header navigation:

    /index.html
    /projects/index.html
    /projects/neurocore.html
    /projects/argus-acli.html
    /projects/argus-lab.html
    /knowledge-base/index.html

Current Knowledge Base nav target:

    /knowledge-base/

Current Story nav target:

    /index.html#story

Current GitHub nav target:

    /index.html#proof

---

## Page Creation Rules

Before creating a new public page:

1. Check `docs/planning/website_information_architecture.md`.
2. Check `docs/planning/content_source_map.md`.
3. Check this page inventory.
4. Check `docs/planning/internal_linking_strategy.md`.
5. Confirm whether required source docs are loaded.
6. Create the page.
7. Update navigation if needed.
8. Update this page inventory.
9. Update repository map if new files/directories were added.
10. Update website state at closeout.

---

## Anti-Drift Rule

If a page exists publicly, it must be represented in this inventory.

If a public navigation link exists, its destination should be represented here or in the internal linking strategy.

If a page is placeholder, structure-only, planned, or future-phase, say so clearly.

Do not let the website grow faster than the documentation system that tracks it.