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
    /knowledge-base/ai-operations/index.html
    /knowledge-base/persistent-ai-memory/index.html
    /knowledge-base/controlled-ai-systems/index.html
    /knowledge-base/local-first-ai/index.html
    /knowledge-base/safe-tool-interaction/index.html
    /knowledge-base/linux-diagnostics/index.html
    /knowledge-base/troubleshooting-training/index.html
    /knowledge-base/neurocore-architecture/index.html
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
| NeuroCore Architecture | `/knowledge-base/neurocore-architecture/` | Same, plus deeper future subtopics if needed | Public architecture article explains the governed platform behind TENSA's AI systems. |
| Argus ACLI | `/projects/argus-acli.html` | Same | Full public product page for local-first read-only Linux diagnostics. |
| Argus Lab | `/projects/argus-lab.html` | Same | Full public landing page for the planned real-Linux troubleshooting, training, and validation environment. |
| Knowledge Base | `/knowledge-base/` | Same | Main teaching layer index. |
| Origin story | `/story/` | Same, or future deeper story article if needed | Story index now owns the full public origin narrative. |
| Public technical artifacts | No public link yet | `/resources/` | Future Resources page may organize selected documentation, examples, release materials, downloads, videos, and any future public repository or open-component links. |
| AI Operations | `/knowledge-base/ai-operations/` | Same, plus deeper future subtopics if needed | Article 1 in the current recommended Knowledge Base path. |
| Persistent AI memory | `/knowledge-base/persistent-ai-memory/` | Same, plus deeper future subtopics if needed | Article 2 in the current recommended Knowledge Base path. |
| Continuity | `/knowledge-base/persistent-ai-memory/` or `/story/` | Same, or future deeper continuity article if needed | Use Story for origin/philosophy; use Persistent AI Memory for concept explanation. |
| Context | `/knowledge-base/persistent-ai-memory/` | Future deeper context-and-continuity article if needed | Current article explains memory vs continuity and source-grounded context. |
| RAG / retrieval augmented generation | `/projects/neurocore.html` | Future deeper RAG/local knowledge article if needed | NeuroCore page currently explains the local retrieval/RAG foundation at the project level. |
| Structured knowledge base | `/knowledge-base/persistent-ai-memory/` | Future structured-knowledge-base article if needed | Current persistent memory article is the best public conceptual destination. |
| CAG-style context assembly | `/projects/neurocore.html` | Future context-aware memory article if needed | NeuroCore page currently covers future context-aware memory direction. |
| Controlled AI systems | `/knowledge-base/controlled-ai-systems/` | Same, plus deeper future subtopics if needed | Article 3 in the current recommended Knowledge Base path. |
| Intelligence vs authority | `/knowledge-base/controlled-ai-systems/` | Future focused article if needed | Current article owns the “AI can reason, but authority must be governed” concept. |
| Control plane | `/knowledge-base/neurocore-architecture/` | Future deeper control-plane article if needed | NeuroCore Architecture is the current public architecture destination. |
| Safe tool interaction | `/knowledge-base/safe-tool-interaction/` | Same, plus deeper future subtopics if needed | Article 5 in the current recommended Knowledge Base path. |
| Tool execution | `/knowledge-base/safe-tool-interaction/` | Future controlled-tool-execution article if needed | Current article owns the public tool-boundary explanation. |
| Observability | `/knowledge-base/neurocore-architecture/` | Future observability article if needed | Current NeuroCore Architecture article explains evidence, tool layers, and system awareness at a public level. |
| Local-first AI | `/knowledge-base/local-first-ai/` | Same, plus deeper future subtopics if needed | Article 4 in the current recommended Knowledge Base path. |
| Documentation as memory | `/knowledge-base/ai-operations/` or `/story/` | Future documentation-as-operational-memory article if needed | Use AI Operations for workflow discipline; use Story for origin narrative. |
| Linux diagnostics | `/knowledge-base/linux-diagnostics/` | Same, plus deeper future subtopics if needed | Article 6 in the current recommended Knowledge Base path. |
| Raw evidence | `/knowledge-base/linux-diagnostics/` | Future raw-evidence article if needed | Current Linux Diagnostics article owns evidence-first diagnostic framing. |
| Severity / findings / recommendations | `/knowledge-base/linux-diagnostics/` or `/projects/argus-acli.html` | Future structured-diagnostics article if needed | Use Argus ACLI for product behavior; use Linux Diagnostics for concept explanation. |
| Kernel-Up / Service Intelligence | `/projects/neurocore.html` | Future Linux diagnostics / service intelligence article if needed | NeuroCore architecture showcase currently mentions this near-term expansion. |
| Troubleshooting training | `/knowledge-base/troubleshooting-training/` | Same, plus deeper future subtopics if needed | Article 7 in the current recommended Knowledge Base path. |
| Real Linux failure scenarios | `/knowledge-base/troubleshooting-training/` or `/projects/argus-lab.html` | Future real-failure-scenarios article if needed | Use Argus Lab for platform/lab role; use Troubleshooting Training for skill-development concept. |
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
    → Knowledge Base
    → AI Operations
    → Persistent AI Memory
    → Controlled AI Systems
    → Local-First AI
    → Safe Tool Interaction
    → NeuroCore Architecture
    → NeuroCore

Purpose:

Help technical readers understand the architectural philosophy without requiring immediate access to implementation repositories.

---

### Path 3: AI Operations Reader

    Home
    → Story
    → AI Operations
    → Persistent AI Memory
    → NeuroCore
    → Build Notes after created

Purpose:

Connect the origin story to continuity engineering, documentation discipline, and system design.

---

### Path 4: Linux Diagnostics Reader

    Home
    → Projects
    → Argus ACLI
    → Linux Diagnostics
    → Troubleshooting Training
    → NeuroCore Architecture

Purpose:

Show how Argus uses NeuroCore to turn real Linux system data into grounded diagnostic understanding.

---

### Path 5: Training / Lab Reader

    Home
    → Projects
    → Argus Lab
    → Troubleshooting Training
    → Linux Diagnostics
    → Argus ACLI

Purpose:

Explain Argus Lab as both a future human training platform and a validation environment for Argus ACLI.

---

### Path 6: Recommended Knowledge Base Path

    Knowledge Base
    → AI Operations
    → Persistent AI Memory
    → Controlled AI Systems
    → Local-First AI
    → Safe Tool Interaction
    → Linux Diagnostics
    → Troubleshooting Training
    → NeuroCore Architecture

Purpose:

Give readers a coherent conceptual path from disciplined AI-assisted work to the governed NeuroCore platform architecture.

---

## Current Navigation To Fix Later

These are intentional temporary or future targets.

| Current Link | Temporary Target | Final Target |
|---|---|---|
| Homepage Knowledge Base preview | `/knowledge-base/` | `/knowledge-base/` |
| Homepage origin story preview | `/story/` | `/story/` |
| Public technical artifacts | No public link yet | Possibly `/resources/` after enough useful public material exists |
| Build history | No public link yet | Possibly `/build-notes/` after public-friendly build summaries are ready |

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
- relevant Knowledge Base articles after deliberate copy/link review

The Projects page should remain an ecosystem router.

---

### NeuroCore Page

The NeuroCore page should link to:

- `/story/` through header navigation
- `/projects/argus-acli.html`
- `/projects/argus-lab.html`
- `/knowledge-base/`
- `/knowledge-base/neurocore-architecture/` where deeper architecture explanation is useful
- `/knowledge-base/persistent-ai-memory/` where continuity or memory explanation is useful
- `/knowledge-base/controlled-ai-systems/` where governed authority explanation is useful
- `/knowledge-base/safe-tool-interaction/` where tool-boundary explanation is useful
- future public technical artifacts after a Resources page or public artifact strategy exists

The NeuroCore page should remain public-facing and business-readable.

It should not become the full architecture manual.

---

### Argus ACLI Page

The Argus ACLI page should link to:

- `/story/` through header navigation
- `/projects/neurocore.html`
- `/projects/argus-lab.html`
- `/knowledge-base/linux-diagnostics/` where evidence-first diagnostics explanation is useful
- `/knowledge-base/safe-tool-interaction/` where tool-boundary explanation is useful
- `/knowledge-base/neurocore-architecture/` where platform architecture explanation is useful
- future public technical artifacts after a Resources page or public artifact strategy exists

The Argus ACLI page should clearly distinguish current product state from future product direction.

---

### Argus Lab Page

The Argus Lab page should link to:

- `/story/` through header navigation
- `/projects/neurocore.html`
- `/projects/argus-acli.html`
- `/knowledge-base/troubleshooting-training/` where troubleshooting skill explanation is useful
- `/knowledge-base/linux-diagnostics/` where evidence-first diagnostics explanation is useful
- future public technical artifacts after a Resources page or public artifact strategy exists

The Argus Lab page should clearly remain future-phase until implementation status changes.

The page is now a full public landing page. Keep future-phase status clear until implementation status changes.

---

### Knowledge Base Index

The Knowledge Base index should link to:

- `/story/` through header navigation
- `/projects/` through header navigation and CTA links
- `/knowledge-base/ai-operations/`
- `/knowledge-base/persistent-ai-memory/`
- `/knowledge-base/controlled-ai-systems/`
- `/knowledge-base/local-first-ai/`
- `/knowledge-base/safe-tool-interaction/`
- `/knowledge-base/linux-diagnostics/`
- `/knowledge-base/troubleshooting-training/`
- `/knowledge-base/neurocore-architecture/`

The Knowledge Base index currently acts as the article-path router for the first eight public Knowledge Base articles.

Do not add fake links for planned topics before pages exist.

---

### Knowledge Base Articles

Current Knowledge Base articles should link through the recommended path:

    AI Operations
    → Persistent AI Memory
    → Controlled AI Systems
    → Local-First AI
    → Safe Tool Interaction
    → Linux Diagnostics
    → Troubleshooting Training
    → NeuroCore Architecture
    → AI Operations

Each article should:

- link back to `/knowledge-base/` through article metadata or navigation
- include header navigation to Home, Projects, Knowledge Base, and Story
- preserve previous/next navigation where appropriate
- include related links only to real public pages
- avoid links to internal planning docs or private repositories

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
| `/knowledge-base/ai-operations/` | Completed. Linked from Knowledge Base index and article-path navigation. Add contextual links from Story/project pages later only after deliberate copy review. |
| `/knowledge-base/persistent-ai-memory/` | Completed. Linked from Knowledge Base index and article-path navigation. Add contextual links from Story/project pages later only after deliberate copy review. |
| `/knowledge-base/controlled-ai-systems/` | Completed. Linked from Knowledge Base index and article-path navigation. Add contextual links from project pages later only after deliberate copy review. |
| `/knowledge-base/local-first-ai/` | Completed. Linked from Knowledge Base index and article-path navigation. Add contextual links from project pages later only after deliberate copy review. |
| `/knowledge-base/safe-tool-interaction/` | Completed. Linked from Knowledge Base index and article-path navigation. Add contextual links from project pages later only after deliberate copy review. |
| `/knowledge-base/linux-diagnostics/` | Completed. Linked from Knowledge Base index and article-path navigation. Add contextual links from Argus ACLI or Argus Lab later only after deliberate copy review. |
| `/knowledge-base/troubleshooting-training/` | Completed. Linked from Knowledge Base index and article-path navigation. Add contextual links from Argus Lab later only after deliberate copy review. |
| `/knowledge-base/neurocore-architecture/` | Completed. Linked from Knowledge Base index and article-path navigation. Add contextual links from NeuroCore or project pages later only after deliberate copy review. |
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
    grep -n "25 directories, 59 files\|knowledge-base/neurocore-architecture/index.html" docs/infrastructure/tensa_repository_map.txt

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
    ./knowledge-base/ai-operations/index.html
    ./knowledge-base/persistent-ai-memory/index.html
    ./knowledge-base/controlled-ai-systems/index.html
    ./knowledge-base/local-first-ai/index.html
    ./knowledge-base/safe-tool-interaction/index.html
    ./knowledge-base/linux-diagnostics/index.html
    ./knowledge-base/troubleshooting-training/index.html
    ./knowledge-base/neurocore-architecture/index.html
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
- The Knowledge Base index links to all eight current Knowledge Base articles.
- The current Knowledge Base article path links from AI Operations through NeuroCore Architecture, then back to AI Operations.
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
