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
| `/index.html` | TENSA Engineering | Homepage | Live | Introduces TENSA Engineering as the umbrella engineering company and ecosystem owner, with core philosophy, project cards, knowledge-base direction, origin story preview, and future public-artifacts framing. | Website state, website information architecture, resume prompt, repository map. Project source docs only if factual project claims change. | Linked as Home from all current public pages. Header links to `/projects/`, `/knowledge-base/`, `/glossary/`, and `/story/`. | Keep concise as front door. Do not turn into full knowledge base. |
| `/projects/index.html` | Projects | Public index page | Live | Explains the ecosystem structure and routes visitors to NeuroCore, Argus ACLI, and Argus Lab. It also states the current public website / private implementation repository boundary. | Website state, website information architecture, resume prompt, repository map. Project source docs if descriptions are expanded. | Linked from homepage and all current public headers. Header links to `/knowledge-base/`, `/glossary/`, and `/story/`. | Keep as ecosystem router. Expand only if needed for clarity. |
| `/projects/neurocore.html` | NeuroCore | Project detail page | Live | Public NeuroCore platform page explaining local-first governed AI runtime, continuity, current RAG/retrieval foundation, future memory direction, control plane architecture, Argus diagnostics flow, model explanation, and near-term Kernel-Up / Service Intelligence expansion. | NeuroCore vision, platform ecosystem, system architecture, system state, control plane, tool execution, security/policy docs, memory/context docs, service intelligence docs, and relevant build logs if factual claims change. | Linked from homepage project card, Projects page, Argus ACLI page, Argus Lab page, Story page, and footer / CTA links. Header links to `/knowledge-base/`, `/glossary/`, and `/story/`. | Preserve public-facing platform explanation. Move deeper architecture details into Knowledge Base or Build Notes later. |
| `/projects/argus-acli.html` | Argus ACLI | Project detail page | Live | Full public product page for Argus ACLI as the first product built on NeuroCore. Explains local-first read-only Linux diagnostics, structured findings, severity, recommendations, raw evidence, and AI explanation grounded in system evidence. | Argus ACLI vision, How Argus Works, Argus output/tool contract, ACLI spec, Argus deployment docs, Argus V1 blueprint, UX layer docs, tool layer docs, Phase 5J/6 docs, relevant build logs. | Linked from homepage project card, Projects page, NeuroCore page, Argus Lab page, and Story page. Header links to `/knowledge-base/`, `/glossary/`, and `/story/`. | Keep product maturity honest. Add install/download guidance only when packaging exists. |
| `/projects/argus-lab.html` | Argus Lab | Project detail page | Live | Full public project page for Argus Lab as an early implementation of real-Linux troubleshooting, training, and validation. Explains the learner experience, controlled failures, resettable lab sessions, mentor-style AI guidance, validation role, current web01 baseline, and relationship to NeuroCore and Argus ACLI. | Argus Lab README, Argus Lab vision docs, current verified web01 baseline details, and current Argus Lab implementation status required if factual implementation claims change. Later scenario planning, validation strategy, training flow, and mentor-mode docs required if those details are expanded. | Linked from homepage project card, Projects page, NeuroCore page, Argus ACLI page, Story page, and Glossary page where relevant. Header links to `/knowledge-base/`, `/glossary/`, and `/story/`. | Keep implementation status honest. Public page may state early implementation and known-good web01 baseline, but must not imply public availability, downloadable product status, or completed training platform. |
| `/knowledge-base/index.html` | Knowledge Base | Public index page | Live | Knowledge Base teaching-layer index for the TENSA ecosystem. Introduces the Knowledge Base and routes readers through the current eight-article recommended path. | Website information architecture, website state, resume prompt, repository map, content style guide, current public project pages, and article-specific source docs if factual article content changes. | Linked from all current public headers. Links to all eight current Knowledge Base articles. Header links to `/projects/`, `/knowledge-base/`, `/glossary/`, and `/story/`. | Keep as article-path router. Add future topics deliberately after source requirements are defined. |
| `/glossary/index.html` | Glossary | Public reference page | Live | Plain-English glossary for TENSA, NeuroCore, Argus ACLI, Argus Lab, AI Operations, Linux diagnostics, control-plane, evidence, memory, and tool-boundary terms. Supports readers without bloating every public page. | Glossary strategy, website state, content style guide, current public project pages, and Knowledge Base articles. Source docs required if definitions expand into factual project claims. | Linked from primary navigation across current public pages, included in sitemap.xml, and targeted by inline glossary tooltip links from Knowledge Base articles. | Maintain as compact reference page. Add terms deliberately when they help readers understand public pages. Avoid turning it into a full Knowledge Base replacement. |
| `/knowledge-base/ai-operations/index.html` | AI Operations | Knowledge Base article | Live | Explains AI Operations as the discipline of making AI-assisted work repeatable, grounded, reviewable, and continuous. | AI Operations methodology source material, content style guide, website state, current project pages, and current public ecosystem positioning. | Linked from Knowledge Base index, NeuroCore Architecture restart link, and article-path navigation. Header links to `/projects/`, `/knowledge-base/`, `/glossary/`, and `/story/`. | Maintain as article 1 of 8. Update only with source-grounded AI Operations changes. |
| `/knowledge-base/persistent-ai-memory/index.html` | Persistent AI Memory | Knowledge Base article | Live | Explains why AI memory is useful but not the same as continuity, and why source-grounded context matters. | Persistent memory / continuity source material, NeuroCore origin context, content style guide, website state, and current public project pages. | Linked from Knowledge Base index, AI Operations next link, and article-path navigation. Header links to `/projects/`, `/knowledge-base/`, `/glossary/`, and `/story/`. | Maintain as article 2 of 8. Keep current-vs-future memory claims clear. |
| `/knowledge-base/controlled-ai-systems/index.html` | Controlled AI Systems | Knowledge Base article | Live | Explains the TENSA principle that AI can reason, but authority must be governed. | Controlled AI systems source material, relevant public incident references if incident examples change, content style guide, website state, and current project pages. | Linked from Knowledge Base index, Persistent AI Memory next link, and article-path navigation. Header links to `/projects/`, `/knowledge-base/`, `/glossary/`, and `/story/`. | Maintain as article 3 of 8. Keep public incident language cautious and sourced. |
| `/knowledge-base/local-first-ai/index.html` | Local-First AI | Knowledge Base article | Live | Explains why the default trust boundary should start close to the user, the system, and the evidence. | Local-first AI source material, NeuroCore public positioning, content style guide, website state, and current project pages. | Linked from Knowledge Base index, Controlled AI Systems next link, and article-path navigation. Header links to `/projects/`, `/knowledge-base/`, `/glossary/`, and `/story/`. | Maintain as article 4 of 8. Keep tradeoffs practical and avoid overstating current product availability. |
| `/knowledge-base/safe-tool-interaction/index.html` | Safe Tool Interaction | Knowledge Base article | Live | Explains how AI can work near tools and systems without becoming an uncontrolled operator. | Safe tool interaction source material, NeuroCore control/tool architecture source material, content style guide, website state, and current project pages. | Linked from Knowledge Base index, Local-First AI next link, and article-path navigation. Header links to `/projects/`, `/knowledge-base/`, `/glossary/`, and `/story/`. | Maintain as article 5 of 8. Preserve the model-authority boundary. |
| `/knowledge-base/linux-diagnostics/index.html` | Linux Diagnostics | Knowledge Base article | Live | Explains evidence-first troubleshooting and why diagnostic systems must start from real system signals rather than guesses. | Linux diagnostics source material, Argus ACLI source docs, NeuroCore/Argus diagnostic architecture docs, content style guide, website state, and current project pages. | Linked from Knowledge Base index, Safe Tool Interaction next link, and article-path navigation. Header links to `/projects/`, `/knowledge-base/`, `/glossary/`, and `/story/`. | Maintain as article 6 of 8. Keep claims tied to evidence-first diagnostics and current/future boundaries. |
| `/knowledge-base/troubleshooting-training/index.html` | Troubleshooting Training | Knowledge Base article | Live | Explains why diagnostic tools and AI guidance still need human judgment, practice, and structured troubleshooting skill. | Troubleshooting training source material, Argus Lab vision/source docs, Linux diagnostics article, content style guide, website state, and current project pages. | Linked from Knowledge Base index, Linux Diagnostics next link, and article-path navigation. Header links to `/projects/`, `/knowledge-base/`, `/glossary/`, and `/story/`. | Maintain as article 7 of 8. Keep Argus Lab availability described as planned/future where appropriate. |
| `/knowledge-base/neurocore-architecture/index.html` | NeuroCore Architecture | Knowledge Base article | Live | Explains NeuroCore as the governed platform behind TENSA's AI systems, including runtime, control path, tool boundary, context layer, evidence layer, model explanation layer, and product foundation. | NeuroCore architecture/source docs, current public project pages, website state, content style guide, and source-grounded current-vs-future implementation details. | Linked from Knowledge Base index, Troubleshooting Training next link, and article-path navigation. Header links to `/projects/`, `/knowledge-base/`, `/glossary/`, and `/story/`. | Maintain as article 8 of 8. Keep implemented, planned, and future-direction claims clearly separated. |
| `/story/index.html` | The Day the AI Forgot Everything | Story page / public origin page | Live | Tells the origin story behind NeuroCore and TENSA Engineering: the AI continuity failure, documentation becoming project memory, local AI changing the direction, real systems requiring control, and the bridge to Argus ACLI, Argus Lab, and AI Operations. | NeuroCore origin story source material, AI Operations methodology split source material, current project pages, content style guide, and website information architecture. | Linked from all current public headers. Homepage story preview links to `/story/`. Story page links to NeuroCore, Argus ACLI, Argus Lab, Projects, Knowledge Base, and Glossary. | Keep human and readable. Do not turn into a technical architecture manual; move definitions into Knowledge Base later. |

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
| `docs/planning/glossary_strategy.md` | Planning / glossary strategy | Live | Defines the public glossary purpose, term-selection rules, inline tooltip behavior, and glossary expansion guardrails. | Update when glossary page structure, term strategy, or inline glossary behavior changes. |
| `docs/planning/search_answer_optimization_template.md` | Planning / search-answer optimization | Live | Defines the future search-and-answer optimization pass template for improving page clarity, answerability, headings, and reader-intent alignment. | Use in a later focused optimization session; update when the search-answer workflow changes. |
| `docs/planning/page_inventory.md` | Page inventory | Live | Tracks what pages exist, what state they are in, and what needs to happen next. | Update whenever pages are created, renamed, retired, or change status. |
| `docs/planning/internal_linking_strategy.md` | Internal link strategy | Live | Tracks logical page-to-page relationships and preferred link destinations. | Update whenever major topic pages, project pages, story pages, or knowledge-base pages are added. |
| `docs/planning/search_indexing_strategy.md` | Search indexing strategy | Live | Tracks sitemap, robots.txt, canonical URL rules, Google Search Console, Bing Webmaster Tools, and search-discovery workflow. | Update when sitemap, robots.txt, indexing setup, or search-discovery workflow changes. |
| `docs/planning/seo_topic_map.md` | Planning / SEO topic map | Live | Tracks future SEO topic strategy and Knowledge Base topic planning. | Update when SEO content strategy, search targets, or planned Knowledge Base topics change. |

---

## Root Search / Indexing Support Files

| Path | Type | Status | Purpose | Update Trigger |
|---|---|---|---|
| `/sitemap.xml` | Search indexing support | Live | Lists the current real public website URLs, including `/glossary/`, for search engine discovery and sitemap submission. | Update whenever public pages are created, removed, renamed, or public routes change. |
| `/robots.txt` | Search indexing support | Live | Allows normal crawling and points search engines to the root sitemap. | Update when sitemap location, crawl guidance, or search indexing policy changes. |

Current public HTML pages include canonical URLs.

Open Graph metadata, Twitter large-image card metadata, and JSON-LD structured data are present where currently implemented.

A future metadata pass should verify all public pages as the site continues to expand.

---

## Planned Public Pages

| Planned Path | Page Type | Purpose | Dependency | Status |
|---|---|---|---|---|
| `/resources/index.html` | Public section index | Collect future public technical artifacts, selected documentation, examples, release materials, downloads, videos, and public resource links when enough useful material exists. | Website IA and current public resource inventory. | Planned |
| `/about.html` | Public standalone page | Explain TENSA Engineering, the mission, and builder context professionally and concisely. | Website IA and approved public bio/mission framing. | Planned |
| `/build-notes/index.html` | Public section index | Public-friendly build milestone summaries that explain project evolution without exposing private implementation details. | Build logs and source repos. | Planned |

---

## Current Knowledge Base Article Path

Current recommended public article path:

| Path | Article | Position | Status |
|---|---|---|---|
| `/knowledge-base/ai-operations/` | AI Operations | 1 of 8 | Live |
| `/knowledge-base/persistent-ai-memory/` | Persistent AI Memory | 2 of 8 | Live |
| `/knowledge-base/controlled-ai-systems/` | Controlled AI Systems | 3 of 8 | Live |
| `/knowledge-base/local-first-ai/` | Local-First AI | 4 of 8 | Live |
| `/knowledge-base/safe-tool-interaction/` | Safe Tool Interaction | 5 of 8 | Live |
| `/knowledge-base/linux-diagnostics/` | Linux Diagnostics | 6 of 8 | Live |
| `/knowledge-base/troubleshooting-training/` | Troubleshooting Training | 7 of 8 | Live |
| `/knowledge-base/neurocore-architecture/` | NeuroCore Architecture | 8 of 8 | Live |

Future Knowledge Base topics should be added deliberately after source requirements are defined in the content source map and link destinations are added to the internal linking strategy.

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
    /knowledge-base/ai-operations/index.html
    /knowledge-base/persistent-ai-memory/index.html
    /knowledge-base/controlled-ai-systems/index.html
    /knowledge-base/local-first-ai/index.html
    /knowledge-base/safe-tool-interaction/index.html
    /knowledge-base/linux-diagnostics/index.html
    /knowledge-base/troubleshooting-training/index.html
    /knowledge-base/neurocore-architecture/index.html
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
    /build-notes/index.html
    additional focused Knowledge Base articles

Reason:

NeuroCore, Argus ACLI, Argus Lab, Knowledge Base, Story, and the first eight Knowledge Base articles now all have public site structure. The next major website step should either organize future public technical artifacts, add concise organizational identity, publish public-friendly build history, or expand the teaching layer with additional focused articles.

Likely next direction:

- create Resources if organizing future public technical artifacts, selected documentation, videos, downloads, examples, and public links becomes the priority
- create About if a concise TENSA mission/builder page is needed
- create Build Notes if public development history becomes the next content lane
- add additional Knowledge Base articles only after source requirements and link destinations are defined

---

## Anti-Drift Rule

If a page exists publicly, it must be represented in this inventory.

If a public navigation link exists, its destination should be represented here or in the internal linking strategy.

If a page is placeholder, structure-only, planned, or future-phase, say so clearly.

Do not let the website grow faster than the documentation system that tracks it.
