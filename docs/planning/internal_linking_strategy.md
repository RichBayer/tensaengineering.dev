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

Current active public sections:

    /index.html#story
    /index.html#proof

---

## Current Primary Navigation Targets

Current header navigation should use:

| Label | Target | Status | Notes |
|---|---|---|---|
| Home | `/index.html` | Active | Use relative path appropriate to page depth. |
| Projects | `/projects/` | Active | Main ecosystem project index. |
| Knowledge Base | `/knowledge-base/` | Active | Main teaching layer index. |
| Story | `/index.html#story` | Temporary | Should become `/story/` after story section exists. |
| GitHub | `/index.html#proof` or direct GitHub repo | Temporary / mixed | Most pages use the homepage proof anchor. NeuroCore currently links directly to the NeuroCore GitHub repo. Decide final Resources/GitHub strategy later. |

---

## Link Destination Map

Use these preferred destinations when topics appear in public pages.

| Topic / Mention | Preferred Destination Now | Future Preferred Destination | Notes |
|---|---|---|---|
| TENSA Engineering | `/index.html` | `/about.html` may supplement | Homepage remains public front door. |
| Ecosystem | `/projects/` | `/projects/` | Projects page explains platform/product/lab structure. |
| NeuroCore | `/projects/neurocore.html` | Same | Main public NeuroCore platform explainer. |
| Argus ACLI | `/projects/argus-acli.html` | Same | Full public product page for local-first read-only Linux diagnostics. |
| Argus Lab | `/projects/argus-lab.html` | Same | Placeholder now; full page is next recommended build. |
| Knowledge Base | `/knowledge-base/` | Same | Main teaching layer index. |
| Origin story | `/index.html#story` | `/story/the-day-the-ai-forgot-everything.html` | Use homepage section until Story pages exist. |
| GitHub proof | `/index.html#proof` or direct GitHub repo | `/resources/github.html` or `/resources/` | Keep mixed current behavior until Resources strategy is created. |
| Persistent AI memory | `/projects/neurocore.html` | `/knowledge-base/persistent-ai-memory/` | NeuroCore currently explains continuity/memory direction best. |
| Continuity | `/projects/neurocore.html` | `/knowledge-base/persistent-ai-memory/` or story article | NeuroCore page currently explains continuity best. |
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
| AI Operations | `/knowledge-base/` | `/knowledge-base/ai-operations/` | Category not created yet. |
| Documentation as memory | `/knowledge-base/` | `/knowledge-base/ai-operations/documentation-as-operational-memory.html` | Future story/knowledge bridge article. |
| Linux diagnostics | `/projects/argus-acli.html` | `/knowledge-base/linux-diagnostics/` | Argus ACLI page is current practical destination. |
| Raw evidence | `/projects/argus-acli.html` | `/knowledge-base/linux-diagnostics/raw-evidence.html` | Future explainer. |
| Severity / findings / recommendations | `/projects/argus-acli.html` | `/knowledge-base/linux-diagnostics/structured-diagnostics.html` | Future explainer. |
| Kernel-Up / Service Intelligence | `/projects/neurocore.html` | `/knowledge-base/linux-diagnostics/kernel-up-service-intelligence.html` | NeuroCore architecture showcase currently mentions this near-term expansion. |
| Troubleshooting training | `/projects/argus-lab.html` | `/knowledge-base/troubleshooting-training/` | Argus Lab page is current practical destination. |
| Real Linux failure scenarios | `/projects/argus-lab.html` | `/knowledge-base/troubleshooting-training/real-failure-scenarios.html` | Future explainer. |
| Build history | `/index.html#proof` | `/build-notes/` | Build Notes not created yet. |
| Downloads / install guidance | No public link yet | `/resources/downloads.html` or Argus ACLI page | Do not create until product readiness supports it. |

---

## Reader Flow Strategy

The website should guide readers through logical paths.

### Path 1: General Visitor

    Home
    → Projects
    → NeuroCore / Argus ACLI / Argus Lab
    → Knowledge Base
    → GitHub proof

Purpose:

Help a new visitor understand what TENSA Engineering is and where the real work lives.

---

### Path 2: AI Architecture Reader

    Home
    → NeuroCore
    → Knowledge Base
    → Controlled AI Systems
    → Safe Tool Interaction
    → GitHub proof

Purpose:

Help technical readers understand the architectural philosophy before diving into the repo.

---

### Path 3: AI Operations Reader

    Home
    → Story
    → NeuroCore
    → Persistent AI Memory
    → AI Operations
    → Build Notes / GitHub proof

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

These are intentional temporary or mixed targets.

| Current Link | Temporary Target | Final Target |
|---|---|---|
| Story | `/index.html#story` | `/story/` |
| GitHub | `/index.html#proof` or direct NeuroCore GitHub repo | Possibly `/resources/` or `/resources/github.html` |
| Homepage Knowledge Base preview | `/knowledge-base/` | `/knowledge-base/` |
| Homepage origin story preview | `/story/` after created | `/story/` |
| Argus Lab project page | `/projects/argus-lab.html` placeholder | Full Argus Lab landing page |

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
- `/projects/neurocore.html`
- `/projects/argus-acli.html`
- `/projects/argus-lab.html`
- GitHub proof links
- future `/story/` once created

The homepage should not become a link dump.

---

### Projects Page

The Projects page should link to:

- `/projects/neurocore.html`
- `/projects/argus-acli.html`
- `/projects/argus-lab.html`
- `/knowledge-base/` where helpful
- future related knowledge-base articles after they exist

The Projects page should remain an ecosystem router.

---

### NeuroCore Page

The NeuroCore page should link to:

- `/projects/argus-acli.html`
- `/projects/argus-lab.html`
- `/knowledge-base/`
- future Persistent AI Memory pages
- future Controlled AI Systems pages
- future Safe Tool Interaction pages
- future NeuroCore Architecture pages
- GitHub repo

The NeuroCore page should remain public-facing and business-readable.

It should not become the full architecture manual.

---

### Argus ACLI Page

The Argus ACLI page should link to:

- `/projects/neurocore.html`
- `/projects/argus-lab.html`
- `/knowledge-base/linux-diagnostics/` after created
- `/knowledge-base/safe-tool-interaction/` after created
- GitHub proof when appropriate

The Argus ACLI page should clearly distinguish current product state from future product direction.

---

### Argus Lab Page

The Argus Lab page should link to:

- `/projects/neurocore.html`
- `/projects/argus-acli.html`
- `/knowledge-base/troubleshooting-training/` after created
- `/knowledge-base/linux-diagnostics/` after created
- GitHub proof when appropriate

The Argus Lab page should clearly remain future-phase until implementation status changes.

The next recommended website build is to convert this page from placeholder to a full public landing page using required source docs.

---

### Knowledge Base Index

The Knowledge Base index should link to:

- category pages once they exist
- `/projects/neurocore.html`
- `/projects/argus-acli.html`
- `/projects/argus-lab.html`
- future Story pages where relevant

Until category pages exist, topic cards should not be fake links.

---

## Planned Link Upgrades

When these pages are created, update links across the site.

| New Page Created | Update These Existing Pages |
|---|---|
| Full `/projects/argus-lab.html` page | Homepage if copy changes, Projects page if project-card description changes, NeuroCore page CTAs if needed, Argus ACLI ecosystem section if needed, this document, page inventory, website state |
| `/story/index.html` | Homepage nav, Projects nav, NeuroCore nav, Argus ACLI nav, Argus Lab nav, Knowledge Base nav |
| `/knowledge-base/controlled-ai-systems/` | Homepage Knowledge Base section, Knowledge Base index, NeuroCore page |
| `/knowledge-base/persistent-ai-memory/` | Homepage Knowledge Base section, Knowledge Base index, NeuroCore page, Story page |
| `/knowledge-base/ai-operations/` | Homepage Knowledge Base section, Knowledge Base index, Story page |
| `/knowledge-base/linux-diagnostics/` | Knowledge Base index, Argus ACLI page, Argus Lab page |
| `/knowledge-base/troubleshooting-training/` | Knowledge Base index, Argus Lab page |
| `/resources/index.html` | Header nav if Resources becomes primary, footer/proof sections |
| `/build-notes/index.html` | Homepage proof section, Knowledge Base index, NeuroCore page |

---

## Dead Link Prevention

Before closeout, run a link-oriented check manually or with a future script.

Current manual checks:

    grep -R "href=" -n index.html projects/*.html knowledge-base/*.html
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

## Current Verified Link Snapshot

Last verified command:

    grep -R "href=" -n index.html projects/*.html knowledge-base/*.html

Current verified public HTML files:

    ./index.html
    ./knowledge-base/index.html
    ./projects/argus-acli.html
    ./projects/argus-lab.html
    ./projects/index.html
    ./projects/neurocore.html

Current notable link state:

- Home, Projects, Knowledge Base, Story, and GitHub navigation exists across current public pages.
- Knowledge Base links point to the real `/knowledge-base/` page.
- Story links still point to the homepage `#story` section.
- Most GitHub navigation links point to homepage `#proof`.
- The NeuroCore page currently links directly to the NeuroCore GitHub repo in the header and CTA areas.
- Argus ACLI links to NeuroCore and Argus Lab.
- NeuroCore links to Argus ACLI and Argus Lab.
- Argus Lab still has placeholder-oriented wording in at least one CTA and should be cleaned up when the full page is built.

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