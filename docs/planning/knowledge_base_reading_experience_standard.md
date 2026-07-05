# Knowledge Base Reading Experience Standard

## Purpose

This document records the planned TENSA Engineering Knowledge Base reading and navigation standard before public page implementation resumes.

The immediate goal is to avoid another round of ad hoc visual edits, overbuilt article cards, confusing navigation, broad CSS overrides, or branch/stash confusion.

The next implementation session should use this document as the planning source before changing public HTML or CSS.

---

## Current Decision

The approved article wording on `main` remains the source of truth for the long-form AI Operations article:

`knowledge-base/ai-operations/how-to-keep-ai-from-losing-project-context.html`

The experimental visual-refinement work should not be merged or applied as-is.

Known local experimental state:

- Branch: `content/knowledge-base-reading-experience`
- Stash: `stash@{0}`
- Stash label: `WIP knowledge-base-reading-experience before ai-ops guardrail update`

The stash may be used only as reference material. It should not be applied, popped, dropped, or merged without explicit approval.

---

## Navigation Concepts

The previous session confused two different navigation needs: whole-Knowledge-Base navigation and same-page article section navigation.

TENSA should treat them as separate patterns.

### 1. Knowledge Base front page navigation

This is the public front door for the Knowledge Base.

It belongs on:

- `knowledge-base/index.html`

The Knowledge Base front page should remain short, clean, and easy to scan.

Expected behavior:

- show the main Knowledge Base categories or topic areas
- use clickable category cards or category links
- help readers choose a topic area quickly
- avoid trying to show every article directly on the front page once the library grows
- avoid empty or awkward future-category UI

Clicking a category should take the reader to that category landing page, not force the reader directly into the first article.

Example flow:

`Knowledge Base` → `AI Operations` → `AI Operations article list and reading path`

### 2. Category landing pages

A category landing page is the article directory for one Knowledge Base topic area.

Example:

- `knowledge-base/ai-operations/index.html`

Expected behavior:

- explain what the category covers
- list all articles in that category
- show a recommended reading path
- make technical depth clear enough that experienced readers can skip introductory material
- let returning readers jump directly to a specific article
- preserve guided learning without trapping readers in a single linear path

A category landing page should serve both reader types:

- new readers who want a recommended path from introductory to more technical content
- experienced readers who want to jump directly to deeper material

### 3. Recommended reading path

This is guided learning navigation.

It belongs primarily on category landing pages and may also appear at the bottom of individual articles.

Expected behavior:

- show the suggested article order
- make the next recommended article obvious
- optionally show previous/next article links
- help readers move from concept to implementation
- support increasingly technical articles as a category matures

This is not the same as the full Knowledge Base directory.

### 4. Optional in-article section navigation

This is same-page navigation.

It should only be used on long reference-style pages where section jumping genuinely helps.

It should not be the default for every Knowledge Base article.

If used, it must be visually restrained and clearly separate from whole-Knowledge-Base navigation.

---

## Article Standard

TENSA Knowledge Base articles should feel like polished technical book chapters or high-quality engineering articles.

The default article structure should be:

1. Article title
2. Short summary
3. Plain metadata line
4. Article body
5. Occasional diagrams or figures
6. Occasional restrained callouts
7. FAQ only when useful
8. Recommended next reading
9. Link back to the relevant Knowledge Base category and full Knowledge Base directory

The article body should prioritize:

- flowing paragraphs
- clear section headings
- readable line length
- comfortable spacing
- restrained emphasis
- useful diagrams with captions
- short lists only when lists are clearer than prose

The article body should avoid:

- walls of bullets
- dashboard-style card grids
- decorative formatting that interrupts reading
- repeated definitions in both article prose and glossary tooltip text
- linking every occurrence of a glossary term
- raw terminal-looking diagrams without article figure styling
- CSS override piles that repeatedly cancel earlier rules

---

## Diagram and Figure Standard

Simple diagrams are allowed and useful, but they should feel like figures inside an article.

A diagram should generally include:

- a clear figure title or caption
- consistent spacing
- readable monospace text when ASCII diagrams are used
- restrained border/background treatment
- horizontal scrolling on narrow screens if needed
- no excessive glow or dashboard styling

Diagrams should clarify concepts such as:

- project continuity loop
- local working tree versus local repository versus remote repository versus connector
- branch isolation
- controlled AI write workflow
- source precedence
- session startup and closeout

Do not turn every process or sequence into a card grid.

---

## List Standard

Lists should be used when they improve comprehension.

Use numbered lists for:

- true sequences
- step-by-step workflows
- ordered processes

Use bullets for:

- short grouped items
- examples
- compact comparisons

Prefer paragraphs when:

- the content is explanatory
- the list becomes long
- each bullet needs multiple sentences
- the section starts to feel like notes instead of an article

---

## FAQ Standard

FAQs should be visibly interactive when implemented with expandable details blocks.

A reader should immediately understand that each question opens and closes.

The FAQ style should be restrained:

- clear question row
- plus/minus or chevron affordance
- readable answer area
- no dashboard card wall

FAQs belong near the bottom of an article unless the page has a specific reason to place them elsewhere.

---

## Glossary Link Standard

Inline glossary links should provide useful supplemental context.

Do not link a term when the surrounding sentence already defines the term.

Example to avoid:

Version control is a system that records changes to files over time.

If that sentence already defines version control, linking the term to a tooltip with the same definition is repetitive.

Preferred approach:

- link the first meaningful use only
- avoid linking every repeated occurrence
- use glossary links for supplemental explanation, not duplicated explanation
- keep article prose readable without requiring tooltips

---

## CSS Standard

Article and Knowledge Base styles should be reusable components, not one-off override piles.

Preferred direction:

- define reusable Knowledge Base article classes
- define reusable figure/diagram classes
- define reusable FAQ classes
- define reusable directory/path navigation classes
- keep article-specific CSS minimal
- avoid repeatedly appending later CSS blocks that undo earlier CSS blocks

The future implementation should promote approved patterns into shared Knowledge Base styling only after the pattern is reviewed.

---

## Implementation Recommendation

Next implementation session should start from clean `main` or a fresh branch based on `main`.

Recommended order:

1. Confirm clean local repository state.
2. Confirm the experimental stash still exists but do not apply it.
3. Review this planning document.
4. Define the reusable Knowledge Base directory/navigation pattern.
5. Define the reusable article visual standard.
6. Repair the long-form AI Operations article using the approved wording from `main`.
7. Style diagrams as article figures.
8. Review the article in the browser.
9. Review the AI Operations category page.
10. Review the Knowledge Base index.
11. Review glossary terms only after article formatting is approved.
12. Consolidate CSS.
13. Run internal link and anchor validation.
14. Update closeout/state documentation once public pages are approved.

---

## Branch and Merge Guidance

Do not merge `content/knowledge-base-reading-experience` as-is.

Do not apply or pop `stash@{0}` as-is.

Do not keep experimental formatting merely because it exists.

If useful patterns are found in the stash, extract them deliberately into a fresh implementation branch after the standard is agreed.

The public article content on `main` is the approved wording baseline.

The next implementation branch should rebuild presentation from the approved baseline instead of trying to rescue the entire experimental branch.
