# TENSA Engineering Website

The public website for TENSA Engineering, at https://tensaengineering.dev. It is a static site: plain HTML, one stylesheet and a small script for glossary tooltips. GitHub Pages builds it from `main` at the repository root. Cloudflare handles DNS.

TENSA Engineering is the public home for NeuroCore, Argus ACLI and Argus Lab. The site explains those systems and teaches the ideas behind them, and it is the only long-term public website for the ecosystem.

## Direction

What keeps the site on course. The full version is owned by `docs/planning/website_information_architecture.md`, in its Purpose, Website Role, Core Positioning, Brand Philosophy, Voice and Tone, and Honesty Rules sections.

- **Purpose.** One clear public front door that organizes and explains the ecosystem for technical and non-technical readers. A structured knowledge base, not one giant document, and no page tries to explain the whole ecosystem.
- **Positioning.** TENSA Engineering builds controlled AI systems for real environments. "Intelligence without continuity is fragile." "AI can reason, but authority must be governed." Control was not the original vision; it is what the vision required once persistent AI began interacting with real systems.
- **Role.** Teach the ideas, explain the systems, and route readers to NeuroCore, Argus ACLI and Argus Lab, without sending visitors to GitHub to understand them.
- **Design principles.** Clear, structured, expandable, search-conscious, technical but understandable, honest about current status, grounded in real engineering work. No AI hype, no corporate fluff, no unfinished system presented as complete, no burying visitors in architecture too early.

## What is here

- Public pages: `index.html`, `about.html`, `contact.html`, `projects/`, `knowledge-base/`, `glossary/` and `story/`, with `styles.css` and `assets/`.
- `blog/`: empty placeholder folders. The Blog is not public yet.
- `docs/`: internal planning and process docs. Not published.
- `_config.yml`: keeps `docs/` and this README off the published site.
- `sitemap.xml`, `robots.txt`, `CNAME` and `favicon.ico`.

## Resume

Read `docs/ai-operations/tensa_website_resume_prompt.md`. It names the two lanes, website work and Blog work, and each lane's next step. Then read `docs/ai-operations/operating_rules.md` and only the docs that lane names. Open nothing else unless the task needs it.

## Where things are tracked

- Pages and their status: `docs/planning/page_inventory.md`
- Long-term site structure: `docs/planning/website_information_architecture.md`
- What each planning doc owns: `docs/planning/documentation_strategy.md`
- Branding, deployment facts and open decisions: `docs/website_state.md`
- What each top-level directory is for: `docs/infrastructure/tensa_repository_map.txt`
- The Claude prose-polish pass: `docs/ai-operations/claude/claude_website_polish_resume_prompt.md`, loaded only for a polish pass

## Keeping it small

- **Caps are hard.** A file over its line cap gets cut before anything is added. Caps: this README 80 lines, the resume note 40, the operating rules 150, `website_state.md` 120, the repository map 60, the closeout pointer 5.
- **One in, one out.** A new rule replaces or deletes an existing one and names the incident behind it.
- **Rules come from incidents on real work.** No workflow rules for risks nobody has hit.
- **No new planning doc** unless the topic needs ongoing tracking and no existing doc owns it.
- **Planning docs own their subject, not the workflow.** The workflow lives in the operating rules and nowhere else.
- **History lives in git.** The long process docs from before the 2026-10-10 slim-down are kept under the tag `archive/pre-slim-20261010`.

## Ecosystem registry pointer

For ecosystem-level repository ownership, repository relationships, routing, or source selection for public claims, consult:

    RichBayer/build-ops-doctrine::docs/ecosystem/README.md
    RichBayer/build-ops-doctrine::docs/ecosystem/repository_registry.yaml
    RichBayer/build-ops-doctrine::docs/ecosystem/document-index/tensaengineering_dev.yaml

Do not load these for website-local work. This repository stays the authority for its own pages, structure, state and content workflow. Build Ops Doctrine provides ecosystem routing only and gives no outside repository write authority here.
