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
| `/index.html` | TENSA Engineering | Homepage | Live | Introduces TENSA Engineering, the ecosystem, core philosophy, project cards, knowledge-base direction, origin story preview, and public explanation-layer / future-artifacts framing. | Website state, website information architecture, resume prompt, repository map. Project source docs only if factual project claims change. | Linked as Home from all current public pages. Header links to `/projects/`, `/knowledge-base/`, and `/story/`. | Keep concise as front door. Do not turn into full knowledge base. |
| `/projects/index.html` | Projects | Public index page | Live | Explains the ecosystem structure and routes visitors to NeuroCore, Argus ACLI, and Argus Lab. It also states the current public website / private implementation repository boundary. | Website state, website information architecture, resume prompt, repository map. Project source docs if descriptions are expanded. | Linked from homepage and all current public headers. Header links to `/story/`. | Keep as ecosystem router. Expand only if needed for clarity. |
| `/projects/neurocore.html` | NeuroCore | Project detail page | Live | Public NeuroCore platform page explaining local-first governed AI runtime, continuity, current RAG/retrieval foundation, future memory direction, control plane architecture, Argus diagnostics flow, model explanation, and near-term Kernel-Up / Service Intelligence expansion. | NeuroCore vision, platform ecosystem, system architecture, system state, control plane, tool execution, security/policy docs, memory/context docs, service intelligence docs, and relevant build logs if factual claims change. | Linked from homepage project card, Projects page, Argus ACLI page, Argus Lab page, Story page, and footer / CTA links. Header links to `/story/`. | Preserve public-facing platform explanation. Move deeper architecture details into Knowledge Base or Build Notes later. |
| `/projects/argus-acli.html` | Argus ACLI | Project detail page | Live | Full public product page for Argus ACLI as the first product built on NeuroCore. Explains local-first read-only Linux diagnostics, structured findings, severity, recommendations, raw evidence, and AI explanation grounded in system evidence. | Argus ACLI vision, How Argus Works, Argus output/tool contract, ACLI spec, Argus deployment docs, Argus V1 blueprint, UX layer docs, tool layer docs, Phase 5J/6 docs, relevant build logs. | Linked from homepage project card, Projects page, NeuroCore page, Argus Lab page, and Story page. Header links to `/story/`. | Keep product maturity honest. Add install/download guidance only when packaging exists. |
| `/projects/argus-lab.html` | Argus Lab | Project detail page | Live | Full public landing page for Argus Lab as a planned real-Linux troubleshooting, training, and validation environment. Explains controlled failures, resettable lab sessions, mentor-style AI guidance, validation role, future-phase status, and relationship to NeuroCore and Argus ACLI. | Argus Lab README and Argus Lab vision doc used for current full page. Later architecture, scenario planning, validation strategy, training flow, and mentor-mode docs required if those details are expanded. | Linked from homepage project card, Projects page, NeuroCore page, Argus ACLI page, and Story page. Header links to `/story/`. | Keep future-phase status clear. Do not imply availability until implementation begins. |
| `/knowledge-base/index.html` | Knowledge Base | Public index page | Structure-only | Establishes the Knowledge Base as the public teaching layer for controlled AI systems, AI operations, persistent AI memory, local-first AI, safe tool interaction, Linux diagnostics, troubleshooting training, and NeuroCore architecture. It also frames future public artifacts without implying public implementation repositories are currently available. | Website information architecture, website state, resume prompt, repository map. Specific article source docs required when factual articles are created. | Linked from all current public headers. Header links to `/story/`. | Create first topic/category pages after internal linking strategy is defined. |
| `/story/index.html` | The Day the AI Forgot Everything | Story page / public origin page | Live | Tells the origin story behind NeuroCore and TENSA Engineering: the AI continuity failure, documentation becoming project memory, local AI changing the direction, real systems requiring control, and the bridge to Argus ACLI, Argus Lab, and AI Operations. | NeuroCore origin story source material, AI Operations methodology split source material, current project pages, content style guide, and website information architecture. | Linked from all current public headers. Homepage story preview links to `/story/`. Story page links to NeuroCore, Argus ACLI, Argus Lab, Projects, and Knowledge Base. | Keep human and readable. Do not turn into a technical architecture manual; move definitions into Knowledge Base later. |

---

## Internal Planning / Continuity Docs

| Path | Type | Status | Purpose | Update Trigger |
|---|---|---|---|
| `docs/ai-operations/claude/claude_website_polish_resume_prompt.md` | AI operations / Claude polish prompt | Live | Defines the reusable Claude handoff workflow for polishing TENSA public website copy while preserving factual boundaries, page type, HTML structure, metadata, links, and current-vs-future status. | Update when Claude workflow, tone/cadence rules, page-type modifiers, or factual-boundary rules change. |
| `docs/ai-operations/documentation_closeout_protocol.md` | AI operations / closeout protocol | Live | Defines the required documentation closeout workflow for serious website build sessions. | Update when closeout workflow rules change. |
| `docs/ai-operations/tensa_website_resume_prompt.md` | AI operations / resume prompt | Live | Fresh-thread startup context for website build sessions. | Update after major site structure, page, workflow, or direction changes. |
| `docs/website_state.md` | State record | Live | Current live-state record for pages, completed work, incomplete work, and next steps. | Update at closeout after major build sessions. |
| `docs/infrastructure/tensa_repository_map.txt` | Repository map | Live | Maps current repository structure and file roles. | Update after directories, assets, pages, or major files are added/removed/moved. |
| `docs/planning/website_information_architecture.md` | Planning / information architecture | Live | Defines long-term website structure, pillars, navigation, page strategy, and expansion plan. | Update only when the long-term architecture changes. |
| `docs/planning/content_source_map.md` | Source-doc map | Live | Defines required source docs before writing factual pages. | Update when new page types are added or source requirements change. |
| `docs/planning/content_style_guide.md` | Planning / content style | Live | Defines public writing voice, tone, formatting, copy standards, and style direction for website content. | Update when public writing standards or page-copy conventions change. |
| `docs/planning/documentation_strategy.md` | Documentation strategy | Live | Defines ownership boundaries, scaling rules, update triggers, and overlap prevention for internal website documentation. | Update when internal documentation responsibilities change or new planning docs become part of the core workflow. |
| `docs/planning/page_inventory.md` | Page inventory | Live | Tracks what pages exist, what state they are in, and what needs to happen next. | Update whenever pages are created, renamed, retired, or change status. |
| `docs/planning/internal_linking_strategy.md` | Internal link strategy | Live | Tracks logical page-to-page relationships and preferred link destinations. | Update whenever major topic pages, project pages, story pages, or knowledge-base pages are added. |
| `docs/planning/search_indexing_strategy.md` | Search indexing strategy | Live | Tracks sitemap, robots.txt, canonical URL rules, Google Search Console, Bing Webmaster Tools, and search-discovery workflow. | Update when sitemap, robots.txt, indexing setup, or search-discovery workflow changes. |
| `docs/planning/seo_topic_map.md` | Planning / SEO topic map | Live | Tracks future SEO topic strategy and Knowledge Base topic planning. | Update when SEO content strategy, search targets, or planned Knowledge Base topics change. |

---

## Root Search / Indexing Support Files

| Path | Type | Status | Purpose | Update Trigger |
|---|---|---|---|
| `/sitemap.xml` | Search indexing support | Live | Lists the current real public website URLs for search engine discovery and sitemap submission. | Update whenever public pages are created, removed, renamed, or public routes change. |
| `/robots.txt` | Search indexing support | Live | Allows normal crawling and points search engines to the root sitemap. | Update when sitemap location, crawl guidance, or search indexing policy changes. |

Current public HTML pages include canonical URLs.

Open Graph metadata, Twitter large-image card metadata, and JSON-LD structured data are present where currently implemented.

A future metadata pass should verify the expanded NeuroCore page after the latest content changes.

---

## Planned Public Pages

| Planned Path | Page Type | Purpose | Dependency | Status |
|---|---|---|---|---|
| `/resources/index.html` | Public section index | Collect future public technical artifacts, selected documentation, examples, release materials, downloads, videos, and public resource links when enough useful material exists. | Website IA and current public resource inventory. | Planned |
| `/about.html` | Public standalone page | Explain TENSA Engineering, the mission, and builder context professionally and concisely. | Website IA and approved public bio/mission framing. | Planned |
| `/build-notes/index.html` | Public section index | Public-friendly build milestone summaries that explain project evolution without exposing private implementation details. | Build logs and source repos. | Planned |

---

## Planned Knowledge Base Categories

| Planned Path | Category | Purpose | Status |
|---|---|---|---|
| `/knowledge-base/controlled-ai-systems/` | Controlled AI Systems | Teach intelligence vs authority, control planes, execution governance, and safe AI-system interaction. | Planned |
| `/knowledge-base/ai-operations/` | AI Operations | Teach structured AI workflows, documentation as memory, context loading, resume prompts, and anti-drift safeguards. | Planned |
| `/knowledge-base/persistent-ai-memory/` | Persistent AI Memory | Teach AI forgetting, continuity loss, engineered continuity, RAG, structured knowledge, context-aware memory, and repository-grounded restoration. | Planned |
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
    Story → /story/

Public GitHub navigation has been removed from current public pages.

Direct public links to private implementation repositories have been removed from current public pages.

When `/resources/` is created:

    Resources may become the home for public technical artifacts, selected documentation, release materials, examples, downloads, videos, and any future public repository or open-component links.

Do not leave navigation pointing to old anchors once real top-level pages exist.

Do not add public links to private implementation repositories.

---

## Current Known Navigation State

Current pages with full header navigation:

    /index.html
    /projects/index.html
    /projects/neurocore.html
    /projects/argus-acli.html
    /projects/argus-lab.html
    /knowledge-base/index.html
    /story/index.html

Current Knowledge Base nav target:

    /knowledge-base/

Current Story nav target:

    /story/

Current public artifact / repository-link state:

    Public GitHub navigation has been removed.
    Direct public links to private implementation repositories have been removed.
    Future public artifact links should be routed deliberately, likely through a future Resources page.

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

## Replacement Verification Rule

After each full-file replacement during closeout or live website editing, run a targeted verification check before moving to the next file.

The verification should confirm the intended change actually landed and that the old/stale text or link was removed when applicable.

Examples:

    grep -n '/story/index.html\|Story → /story/\|claude_website_polish_resume_prompt.md' docs/planning/page_inventory.md
    grep -n 'href="../story/"\|href="../index.html#story"' knowledge-base/index.html

This rule exists to catch:

- paste mistakes
- missed saves
- wrong-file edits
- stale snippets
- unintended partial replacements

---

## Current Next Public Page Priority

Recommended next public-page options:

    /resources/index.html
    /about.html
    first Knowledge Base category pages
    /build-notes/index.html

Reason:

NeuroCore, Argus ACLI, Argus Lab, Knowledge Base, and Story now all have public site structure. The next major website step should either organize future public technical artifacts, add concise organizational identity, or begin focused teaching articles.

Likely next direction:

- create Resources if organizing future public technical artifacts, selected documentation, videos, downloads, examples, and public links becomes the priority
- create About if a concise TENSA mission/builder page is needed
- create Knowledge Base categories if the teaching layer becomes the next focus
- create Build Notes if public development history becomes the next content lane

---

## Anti-Drift Rule

If a page exists publicly, it must be represented in this inventory.

If a public navigation link exists, its destination should be represented here or in the internal linking strategy.

If a page is placeholder, structure-only, planned, or future-phase, say so clearly.

Do not let the website grow faster than the documentation system that tracks it.