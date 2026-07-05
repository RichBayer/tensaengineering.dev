# Knowledge Base Article Template

## Purpose

This document defines the reusable structure for future long-form TENSA Engineering Knowledge Base articles.

Use it when creating or rewriting focused Knowledge Base articles that should read like polished technical articles or short engineering book chapters.

The reference implementation is:

    knowledge-base/ai-operations/how-to-keep-ai-from-losing-project-context.html

That page is the current proof page for the prose-first Knowledge Base article reading standard.

This document is a template and creation guide. It does not replace:

- `docs/planning/content_style_guide.md`
- `docs/planning/content_source_map.md`
- `docs/planning/page_inventory.md`
- `docs/planning/internal_linking_strategy.md`
- `docs/website_state.md`

---

## When to Use This Template

Use this template for focused Knowledge Base articles that explain one reader question in depth.

Good fits:

- conceptual explainers
- AI Operations guides
- architecture explainers
- troubleshooting methodology articles
- controlled-AI design articles
- local-first / memory / tool-boundary articles

Do not use this template unchanged for:

- category landing pages
- glossary entries
- project pages
- homepage sections
- short announcements
- internal planning docs
- repository maps
- build logs

Category pages and article pages have different jobs.

A category page should orient readers, group related articles, and provide recommended reading paths.

A focused article should answer one reader question clearly and deeply.

---

## Reference Implementation

Current reference article:

    /knowledge-base/ai-operations/how-to-keep-ai-from-losing-project-context.html

Role of the reference article:

- demonstrates the preferred long-form Knowledge Base reading experience
- shows prose-first section flow
- uses three styled explanatory diagrams
- keeps FAQ useful but secondary
- uses a plain article metadata sentence
- avoids dashboard-card walls, heavy numbered lists, and raw code-looking diagrams

Do not blindly copy the article content.

Use its structure, pacing, and visual rhythm as the production example.

---

## Standard Article Structure

A long-form Knowledge Base article should generally follow this order:

1. HTML document shell
2. SEO and social metadata
3. JSON-LD structured data when appropriate
4. shared site header
5. article header
6. article summary
7. article context line
8. prose-first article body
9. two or three useful diagrams or figures
10. restrained callouts
11. FAQ section when useful
12. where-this-fits / related concept section
13. article navigation
14. related reading links
15. shared site footer

The article should not feel like a checklist. The structure is a scaffold, not a visible outline.

---

## Article Header Pattern

The article header should include:

- category eyebrow
- clear article title
- short summary paragraph
- plain article-context sentence

Example visible pattern:

    AI Operations, a practical continuity guide for long-running projects

The category text may link to the category page. The rest should read as plain text, not as fake buttons or disconnected tags.

Avoid pill-style metadata chips unless they are intentionally functioning as tags or filters.

---

## Prose Standard

The article body should be prose-first.

Prefer:

- full paragraphs with natural transitions
- clear section headings
- short-to-medium paragraphs that develop an idea
- occasional short sentences for emphasis
- practical examples where they help
- reader-facing explanations before jargon

Avoid:

- long chains of one- or two-sentence fragments
- turning every idea into a list
- numbered lists unless sequence is genuinely important
- default documentation rhythm
- dashboard-card walls
- internal planning language
- over-compressed technical summaries

A good article should feel like a polished technical explanation, not a converted project checklist.

---

## List and Bullet Rules

Bullets are allowed, but they should be deliberate.

Use bullets when:

- the reader needs to scan a set of options
- the article is comparing several items
- the content is genuinely checklist-like
- the list would be harder to read as a paragraph

Avoid bullets when:

- the list is replacing explanation
- every section becomes a list
- the same point would read better as prose
- the list interrupts the reading rhythm

Use numbered lists only when order matters.

---

## Diagram Standard

Use diagrams sparingly.

Most long-form articles should have two or three strong diagrams, not seven or eight weak ones.

Diagrams should:

- clarify an idea quickly
- add visual rhythm without taking over the article
- look like polished explanatory article graphics
- use readable labels
- support the surrounding prose
- include useful captions
- work on mobile layouts

Avoid diagrams that look like:

- terminal output
- file trees
- raw code blocks
- internal planning diagrams
- repository maps
- oversized card walls

Exception:

If the article is specifically teaching code, configuration, CLI output, or repository structure, code-like diagrams may be appropriate. Even then, they should be styled intentionally and explained clearly.

---

## Image and Stock-Visual Guidance

Editorial or stock-style imagery may be useful later, but it should not be added randomly.

Use images when they:

- help the article feel more polished
- support the topic visually
- break up a long article naturally
- match TENSA's technical visual identity

Avoid images that:

- look generic or unrelated
- imply a product feature that does not exist
- distract from the explanation
- make the site feel like a stock marketing template

Image assets should be added deliberately and tracked in the repository map and closeout docs when new files are created.

---

## Callout Standard

Callouts should be restrained.

Use a callout for:

- a central rule
- a caution
- a short principle worth emphasizing
- a reader takeaway

Do not use callouts as a replacement for article structure.

A long article usually needs only one to three callouts.

---

## FAQ Standard

FAQ sections are optional.

Use FAQ when the article naturally raises common reader questions.

A good FAQ should:

- answer real questions
- stay short
- reinforce the article
- avoid becoming the main content
- align with JSON-LD FAQPage schema if structured data is included

Do not add FAQ just because the template has one.

---

## SEO and Metadata Requirements

Each public article should include:

- useful `<title>` text
- clear meta description
- canonical URL
- Open Graph metadata where current site patterns use it
- Twitter card metadata where current site patterns use it
- JSON-LD Article schema when appropriate
- FAQPage schema only when visible FAQ content exists and matches the schema

Metadata should reflect the real article and current public site state.

Do not use metadata to claim product maturity, public availability, deployment status, indexing status, or features that are not verified.

---

## Internal Link Requirements

Before creating or changing article links, check:

    docs/planning/internal_linking_strategy.md
    docs/planning/page_inventory.md

A focused article should usually link to:

- its category page
- the Knowledge Base index
- the next related concept where appropriate
- relevant project pages when useful
- glossary anchors for selected terms

Do not add links to pages that do not exist.

Do not add public links to private implementation repositories.

Run local internal-link validation when public links, routes, or anchors change.

---

## Source Requirements

Before writing or significantly rewriting factual article content, check:

    docs/planning/content_source_map.md

Use source docs before making factual claims about:

- NeuroCore
- Argus ACLI
- Argus Lab
- current implementation status
- architecture details
- future roadmap
- availability
- security boundaries
- deployment behavior

If source context is missing, stop and ask for it.

---

## HTML / CSS Pattern

The current production implementation uses shared Knowledge Base article classes in `styles.css`.

Important current classes include:

- `kb-article-shell`
- `kb-article-header`
- `kb-article-summary`
- `kb-article-meta`
- `kb-article-body`
- `kb-section`
- `kb-callout`
- `kb-visual-diagram`
- `kb-faq-list`
- `kb-reading-nav`
- `kb-related-card`

Future articles should reuse shared classes where possible.

Avoid creating one-off CSS unless the article needs a specific visual treatment that can become reusable.

---

## Creation Workflow

Recommended workflow for a new focused article:

1. Confirm the article belongs in the Knowledge Base.
2. Confirm the category and URL slug.
3. Check `page_inventory.md` and `internal_linking_strategy.md`.
4. Check `content_source_map.md` for required source docs.
5. Draft the article in prose-first form.
6. Add only the diagrams that genuinely help.
7. Add FAQ only if useful.
8. Add SEO/social metadata and schema.
9. Link the article from its category or relevant discovery path.
10. Run browser review.
11. Run internal-link validation.
12. Update closeout/planning docs.

---

## Things to Avoid

Avoid:

- creating articles without a category plan
- adding articles that are really project pages
- making category pages read like full articles
- overusing bullets and numbered lists
- overusing diagrams
- making diagrams look like raw terminal or code output by default
- adding stock images without a clear purpose
- letting FAQ dominate the article
- claiming unverified deployment, indexing, availability, or product maturity
- using private implementation repositories as public proof links
- publishing public pages faster than the planning docs can track them

---

## Current Next Application

The next planned use of this template is likely the AI Operations category/index cleanup:

    /knowledge-base/ai-operations/
        should become a category / article index page

    /knowledge-base/ai-operations/what-is-ai-operations.html
        likely future dedicated article for current long-form AI Operations content

    /knowledge-base/ai-operations/how-to-keep-ai-from-losing-project-context.html
        remains the focused continuity guide and reference implementation

Final slug and structure should be approved before implementation.
