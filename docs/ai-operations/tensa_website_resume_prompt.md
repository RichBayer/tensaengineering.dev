# TENSA Website: Now

Updated: 2026-10-10

Two lanes. Ask Rich which one before reading anything else.

## Website lane

- Active: none.
- Next up, not started: AI Operations category / article index conversion. Move the long-form content on `/knowledge-base/ai-operations/` into its own article page and leave the category page as an index.
- Branch: `feature/kb-ai-operations-index`, cut from `main`. Not created yet.
- Read for it, all in `docs/planning/`: `page_inventory.md`, `content_source_map.md`, `knowledge_base_article_template.md`, `internal_linking_strategy.md`.

## Blog lane

- Branch: `feature/blog-public-foundation`. Do not start another Blog implementation branch.
- Active: none.
- Next step: build the article-specific source packet for the leading candidate, "Why does AI coding burn through my usage limit so fast?" Runner-up: "Why does my coding AI forget or repeat work?"
- The candidate is a research question, not a locked title or slug. Those are decided after the source packet.
- Do not restart the research from zero. It is recorded in `docs/planning/blog_strategy.md`.
- Do not draft public HTML first. Order: source packet, then reader question, title, slug and Quick Answer, then outline, one proof article, validation, category page, Blog home.
- The Blog stays on its branch until the proof article validates. No Blog navigation or sitemap entries until real pages exist and validate.
- Read for it, from the Blog branch and not from `main`, whose copies are older: `blog_strategy.md`, `blog_reader_experience.md`, `blog_engagement_strategy.md`, `seo_topic_map.md`, all in `docs/planning/`.

## Parked

- Protected local stash: `stash@{0}: On content/knowledge-base-reading-experience: WIP knowledge-base-reading-experience before ai-ops guardrail update`. No stash action of any kind without Rich approving that exact action. It is local only; GitHub cannot see it.

## To resume

Read this note and ask which lane. Then read `docs/ai-operations/operating_rules.md` and only the docs that lane names above. Then ask Rich for `git status --short`, the current branch and `git stash list`. What the repo is: `README.md`.
