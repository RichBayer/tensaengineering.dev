# TENSA Engineering Internal Linking Strategy

---

## Purpose

This document defines how TENSA Engineering pages should link to each other as the website grows.

It exists to prevent link drift, duplicate explanations, orphaned pages, and confusing visitor paths.

The goal is to make the site feel like a structured ecosystem knowledge platform, not a pile of disconnected pages.

Use this document to answer:

- When a page mentions a topic, where should it link?
- Which page is the preferred destination for each concept?
- Which links are active now?
- Which links are planned but not created yet?
- How should readers move from concept to project to proof?
- How should public pages avoid duplicating the same explanation over and over?

This document works alongside:

- `docs/planning/page_inventory.md`
- `docs/planning/content_source_map.md`
- `docs/planning/website_information_architecture.md`
- `docs/website_state.md`
- `docs/infrastructure/tensa_repository_map.txt`

---

## Core Rule

Every important topic should eventually have one preferred destination.

When a topic is mentioned across the site, link to the best existing page for that topic.

If no proper destination exists yet, do not force a bad link.

Instead, mark the destination as planned in this document and update links after the page exists.

---

## Current Active Public Pages

Current active public pages:

    /index.html
    /projects/index.html
    /projects/neurocore.html
    /projects/argus-acli.html
    /projects/argus-lab.html
    /knowledge-base/index.html
    /story/index.html

Current active public sections:

    None currently tracked as primary public section anchors.

---

## Current Primary Navigation Targets

Current header navigation should use:

| Label | Target | Status | Notes |
|---|---|---|---|
| Home | `/index.html` | Active | Use relative path appropriate to page depth. |
| Projects | `/projects/` | Active | Main ecosystem project index. |
| Knowledge Base | `/knowledge-base/` | Active | Main teaching layer index. |
| Story | `/story/` | Active | Full public origin story page. |

---

## Link Destination Map

Use these preferred destinations when topics appear in public pages.

| Topic / Mention | Preferred Destination Now | Future Preferred Destination | Notes |
|---|---|---|---|
| TENSA Engineering | `/index.html` | `/about.html` may supplement | Homepage remains public front door. |
| Ecosystem | `/projects/` | `/projects/` | Projects page explains platform/product/lab structure. |
| NeuroCore | `/projects/neurocore.html` | Same | Main public NeuroCore platform explainer. |
| Argus ACLI | `/projects/argus-acli.html` | Same | Full public product page for local-first read-only Linux diagnostics. |
| Argus Lab | `/projects/argus-lab.html` | Same | Full public landing page for the planned real-Linux troubleshooting, training, and validation environment. |
| Knowledge Base | `/knowledge-base/` | Same | Main teaching layer index. |
| Origin story | `/story/` | Same, or future deeper story article if needed | Story index now owns the full public origin narrative. |
| Public technical artifacts | No public link yet | `/resources/` | Future Resources page may organize selected documentation, examples, release materials, downloads, videos, and any future public repository or open-component links. |
| Persistent AI memory | `/projects/neurocore.html` | `/knowledge-base/persistent-ai-memory/` | NeuroCore currently explains continuity/memory direction best. |
| Continuity | `/story/` or `/projects/neurocore.html` | `/knowledge-base/persistent-ai-memory/` or story article | Story explains the human origin; NeuroCore explains the platform direction. |
| Context | `/projects/neurocore.html` | `/knowledge-base/persistent-ai-memory/context-and-continuity.html` | Future article likely needed. |
| RAG / retrieval augmented generation | `/projects/neurocore.html` | `/knowledge-base/persistent-ai-memory/rag-and-local-knowledge.html` | NeuroCore page currently explains the local retrieval/RAG foundation. |
| Structured knowledge base | `/projects/neurocore.html` | `/knowledge-base/persistent-ai-memory/structured-knowledge-base.html` | Future Knowledge Base explainer. |
| CAG-style context assembly | `/projects/neurocore.html` | `/knowledge-base/persistent-ai-memory/context-aware-memory.html` | Future Knowledge Base explainer. |
| Controlled AI systems | `/knowledge-base/` | `/knowledge-base/controlled-ai-systems/` | Category not created yet. |
| Intelligence vs authority | `/projects/neurocore.html` | `/knowledge-base/controlled-ai-systems/ai-can-reason-but-authority-must-be-governed.html` | Strong future article candidate. |
| Control plane | `/projects/neurocore.html` | `/knowledge-base/neurocore-architecture/control-plane.html` | Current explanation lives in NeuroCore page. |
| Safe tool interaction | `/knowledge-base/` | `/knowledge-base/safe-tool-interaction/` | Category not created yet. |
| Tool execution | `/projects/neurocore.html` | `/knowledge-base/safe-tool-interaction/controlled-tool-execution.html` | Future public explainer. |
| Observability | `/projects/neurocore.html` | `/knowledge-base/neurocore-architecture/observability.html` | Future public explainer. |
| Local-first AI | `/projects/neurocore.html` | `/knowledge-base/local-first-ai/` | NeuroCore and Argus ACLI currently explain the concept practically. |
| AI Operations | `/story/` or `/knowledge-base/` | `/knowledge-base/ai-operations/` | Story explains the origin; Knowledge Base category not created yet. |
| Documentation as memory | `/story/` | `/knowledge-base/ai-operations/documentation-as-operational-memory.html` | Future story/knowledge bridge article. |
| Linux diagnostics | `/projects/argus-acli.html` | `/knowledge-base/linux-diagnostics/` | Argus ACLI page is current practical destination. |
| Raw evidence | `/projects/argus-acli.html` | `/knowledge-base/linux-diagnostics/raw-evidence.html` | Future explainer. |
| Severity / findings / recommendations | `/projects/argus-acli.html` | `/knowledge-base/linux-diagnostics/structured-diagnostics.html` | Future explainer. |
| Kernel-Up / Service Intelligence | `/projects/neurocore.html` | `/knowledge-base/linux-diagnostics/kernel-up-service-intelligence.html` | NeuroCore architecture showcase currently mentions this near-term expansion. |
| Troubleshooting training | `/projects/argus-lab.html` | `/knowledge-base/troubleshooting-training/` | Argus Lab page is current practical destination. |
| Real Linux failure scenarios | `/projects/argus-lab.html` | `/knowledge-base/troubleshooting-training/real-failure-scenarios.html` | Future explainer. |
| Build history | No public link yet | `/build-notes/` | Build Notes not created yet. Public build summaries should avoid exposing private implementation details. |
| Downloads / install guidance | No public link yet | `/resources/downloads.html` or Argus ACLI page | Do not create until product readiness supports it. |

---

## Reader Flow Strategy

The website should guide readers through logical paths.

### Path 1: General Visitor

    Home
    → Projects
    → NeuroCore / Argus ACLI / Argus Lab
    → Knowledge Base

Purpose:

Help a new visitor understand what TENSA Engineering is, how the ecosystem fits together, and where to go next.

---

### Path 2: AI Architecture Reader

    Home
    → NeuroCore
    → Knowledge Base
    → Controlled AI Systems
    → Safe Tool Interaction

Purpose:

Help technical readers understand the architectural philosophy without requiring immediate access to implementation repositories.

---

### Path 3: AI Operations Reader

    Home
    → Story
    → NeuroCore
    → Persistent AI Memory
    → AI Operations
    → Build Notes after created

Purpose:

Connect the origin story to continuity engineering, documentation discipline, and system design.

---

### Path 4: Linux Diagnostics Reader

    Home
    → Projects
    → Argus ACLI
    → NeuroCore
    → Linux Diagnostics
    → Raw Evidence / Structured Diagnostics

Purpose:

Show how Argus uses NeuroCore to turn real Linux system data into grounded diagnostic understanding.

---

### Path 5: Training / Lab Reader

    Home
    → Projects
    → Argus Lab
    → Argus ACLI
    → Troubleshooting Training
    → Linux Diagnostics

Purpose:

Explain Argus Lab as both a future human training platform and a validation environment for Argus ACLI.

---

## Current Navigation To Fix Later

These are intentional temporary or future targets.

| Current Link | Temporary Target | Final Target |
|---|---|---|
| Homepage Knowledge Base preview | `/knowledge-base/` | `/knowledge-base/` |
| Homepage origin story preview | `/story/` | `/story/` |
| Public technical artifacts | No public link yet | Possibly `/resources/` after enough useful public material exists |
| Argus Lab project page | `/projects/argus-lab.html` | Full public landing page now active |

---

## Link Creation Rules

Before adding links to a public page:

1. Check whether the destination page exists.
2. Check `docs/planning/page_inventory.md`.
3. Check this internal linking strategy.
4. If the destination exists, link to the preferred destination.
5. If the destination does not exist, either:
   - link to the best current parent/index page, or
   - leave plain text and record the future link here.
6. Avoid creating dead links.
7. Avoid linking every repeated term on a page.
8. Prefer the first meaningful mention of a topic.
9. Prefer links that help the reader move forward logically.
10. Do not link to internal planning docs from public pages.

---

## Public Page Link Rules

### Homepage

The homepage should link to:

- `/projects/`
- `/knowledge-base/`
- `/story/`
- `/projects/neurocore.html`
- `/projects/argus-acli.html`
- `/projects/argus-lab.html`

The homepage should not become a link dump.

---

### Projects Page

The Projects page should link to:

- `/projects/neurocore.html`
- `/projects/argus-acli.html`
- `/projects/argus-lab.html`
- `/knowledge-base/` where helpful
- `/story/` through header navigation
- future related knowledge-base articles after they exist

The Projects page should remain an ecosystem router.

---

### NeuroCore Page

The NeuroCore page should link to:

- `/story/` through header navigation
- `/projects/argus-acli.html`
- `/projects/argus-lab.html`
- `/knowledge-base/`
- future Persistent AI Memory pages
- future Controlled AI Systems pages
- future Safe Tool Interaction pages
- future NeuroCore Architecture pages
- future public technical artifacts after a Resources page or public artifact strategy exists

The NeuroCore page should remain public-facing and business-readable.

It should not become the full architecture manual.

---

### Argus ACLI Page

The Argus ACLI page should link to:

- `/story/` through header navigation
- `/projects/neurocore.html`
- `/projects/argus-lab.html`
- `/knowledge-base/linux-diagnostics/` after created
- `/knowledge-base/safe-tool-interaction/` after created
- future public technical artifacts after a Resources page or public artifact strategy exists

The Argus ACLI page should clearly distinguish current product state from future product direction.

---

### Argus Lab Page

The Argus Lab page should link to:

- `/story/` through header navigation
- `/projects/neurocore.html`
- `/projects/argus-acli.html`
- `/knowledge-base/troubleshooting-training/` after created
- `/knowledge-base/linux-diagnostics/` after created
- future public technical artifacts after a Resources page or public artifact strategy exists

The Argus Lab page should clearly remain future-phase until implementation status changes.

The page is now a full public landing page. Keep future-phase status clear until implementation status changes.

---

### Knowledge Base Index

The Knowledge Base index should link to:

- `/story/` through header navigation
- category pages once they exist
- `/projects/neurocore.html`
- `/projects/argus-acli.html`
- `/projects/argus-lab.html`
- future Story pages where relevant

Until category pages exist, topic cards should not be fake links.

---

### Story Page

The Story page should link to:

- `/projects/`
- `/projects/neurocore.html`
- `/projects/argus-acli.html`
- `/projects/argus-lab.html`
- `/knowledge-base/` through header navigation

The Story page should remain the origin and philosophy page.

It should not become:

- a technical architecture manual
- a Knowledge Base article
- a roadmap dump
- an internal planning document
- a replacement for the project pages

Deeper definitions should branch into the Knowledge Base later.

---

## Planned Link Upgrades

When these pages are created, update links across the site.

| New Page Created | Update These Existing Pages |
|---|---|
| Full `/projects/argus-lab.html` page | Completed. Keep related links current if homepage, Projects page, NeuroCore page, or Argus ACLI page copy changes later. |
| `/story/index.html` | Completed. Header navigation now points to `/story/`. Keep story-related links current if deeper Story articles are added later. |
| `/knowledge-base/controlled-ai-systems/` | Homepage Knowledge Base section, Knowledge Base index, NeuroCore page |
| `/knowledge-base/persistent-ai-memory/` | Homepage Knowledge Base section, Knowledge Base index, NeuroCore page, Story page |
| `/knowledge-base/ai-operations/` | Homepage Knowledge Base section, Knowledge Base index, Story page |
| `/knowledge-base/linux-diagnostics/` | Knowledge Base index, Argus ACLI page, Argus Lab page |
| `/knowledge-base/troubleshooting-training/` | Knowledge Base index, Argus Lab page |
| `/resources/index.html` | Header nav if Resources becomes primary, footer/artifacts sections, Knowledge Base index, project pages where useful |
| `/build-notes/index.html` | Knowledge Base index, NeuroCore page, Story page where useful |

---

## Dead Link Prevention

Before closeout, run a link-oriented check manually or with a future script.

Current manual checks:

    grep -R "href=" -n index.html projects/*.html knowledge-base/*.html story/*.html
    find . -maxdepth 3 -name "*.html" -print

Future recommended script:

    scripts/check_internal_links.py

The script should eventually:

- scan public HTML files
- extract internal href targets
- confirm local files exist
- ignore external links
- ignore page anchors only after confirming base file exists
- report broken links clearly

Do not rely on manual clicking forever.

---

## Replacement Verification Rule

After each full-file replacement during closeout or live website editing, run a targeted verification check before moving to the next file.

The verification should confirm the intended change actually landed and that the old/stale text or link was removed when applicable.

Examples:

    grep -n 'href="../story/"\|href="../index.html#story"' projects/argus-acli.html
    grep -n "17 directories, 51 files\|story/index.html" docs/infrastructure/tensa_repository_map.txt

This rule exists to catch:

- paste mistakes
- missed saves
- wrong-file edits
- stale snippets
- unintended partial replacements

---

## Current Verified Link Snapshot

Last verified command:

    grep -R "href=" -n index.html projects/*.html knowledge-base/*.html story/*.html

Current verified public HTML files:

    ./index.html
    ./knowledge-base/index.html
    ./projects/argus-acli.html
    ./projects/argus-lab.html
    ./projects/index.html
    ./projects/neurocore.html
    ./story/index.html

Current notable link state:

- Home, Projects, Knowledge Base, and Story navigation exists across current public pages.
- Public GitHub navigation has been removed from current public pages.
- Direct public links to private implementation repositories have been removed from current public pages.
- Knowledge Base links point to the real `/knowledge-base/` page.
- Story links point to the real `/story/` page.
- Argus ACLI links to NeuroCore and Argus Lab.
- NeuroCore links to Argus ACLI and Argus Lab.
- Argus Lab links to Argus ACLI, NeuroCore, and the Projects page.
- Story links to NeuroCore, Argus ACLI, Argus Lab, Projects, and Knowledge Base.

---

## Anti-Drift Rules

If a new public page is created, add it to `page_inventory.md`.

If a new major topic is introduced, add it to this internal linking strategy.

If a temporary link is replaced by a real page, update this document.

If a page is renamed, update:

- all affected HTML files
- `page_inventory.md`
- this file
- `content_source_map.md` if source requirements changed
- `website_state.md`
- `tensa_repository_map.txt`

Do not allow the public site to grow faster than its link strategy.