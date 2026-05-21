# TENSA Engineering Search Indexing Strategy

---

## Purpose

This document defines the search indexing strategy for the TENSA Engineering website.

It tracks how the site should be prepared for discovery by search engines such as Google and Bing.

It exists to prevent:

- missing sitemap updates
- stale sitemap URLs
- planned pages appearing in the sitemap before they exist
- search engine registration being forgotten
- robots.txt becoming outdated
- page additions not being reflected in indexing files
- SEO planning being mixed into unrelated website docs
- accidental overstatement of search readiness
- copy/paste replacement mistakes going undetected during indexing closeout

This is an internal planning document.

It is not a public website page.

---

## Current Site

Primary public domain:

    https://tensaengineering.dev

Deployment:

    GitHub Pages

DNS / domain provider:

    Cloudflare

Current public pages:

    /
    /projects/
    /projects/neurocore.html
    /projects/argus-acli.html
    /projects/argus-lab.html
    /knowledge-base/
    /story/

Current search-indexing status:

    sitemap.xml created locally
    robots.txt created locally
    canonical URLs added to all current public HTML pages
    Open Graph metadata added to all current public HTML pages
    Twitter large-image card metadata added to all current public HTML pages
    dedicated 1200 x 630 social preview image created
    JSON-LD structured data added to all current public HTML pages
    Google Search Console verified
    sitemap submitted successfully to Google
    Bing Webmaster Tools imported from Google Search Console
    sitemap submitted to Bing and processing
    /story/ added to sitemap locally during Story page closeout

---

## Core Principle

Search engines should be given a clean, accurate map of the real public website.

Only real public pages should appear in the sitemap.

Do not include planned pages, placeholder directories, future URLs, internal docs, assets, or private planning files.

The sitemap should reflect what exists now, not what is intended later.

---

## Files Owned By This Strategy

This strategy governs the creation and maintenance of:

    sitemap.xml
    robots.txt
    docs/planning/search_indexing_strategy.md

Future related files may include:

    scripts/generate_sitemap.py
    scripts/check_internal_links.py

The sitemap and robots files belong at the repository root:

    /sitemap.xml
    /robots.txt

For the live site, these should resolve as:

    https://tensaengineering.dev/sitemap.xml
    https://tensaengineering.dev/robots.txt

---

## Current Sitemap Plan

The root-level sitemap file is:

    sitemap.xml

The current sitemap should include only the current real public pages:

    https://tensaengineering.dev/
    https://tensaengineering.dev/projects/
    https://tensaengineering.dev/projects/neurocore.html
    https://tensaengineering.dev/projects/argus-acli.html
    https://tensaengineering.dev/projects/argus-lab.html
    https://tensaengineering.dev/knowledge-base/
    https://tensaengineering.dev/story/

Do not include:

    /resources/
    /build-notes/
    /about.html
    /knowledge-base/controlled-ai-systems/
    /knowledge-base/ai-operations/
    /knowledge-base/persistent-ai-memory/
    /knowledge-base/local-first-ai/
    /knowledge-base/safe-tool-interaction/
    /knowledge-base/linux-diagnostics/
    /knowledge-base/troubleshooting-training/
    /knowledge-base/neurocore-architecture/

until those pages or directories actually exist.

---

## Sitemap URL Rules

Use canonical public URLs.

Preferred canonical format:

    https://tensaengineering.dev/

Directory index pages should use clean directory URLs when appropriate:

    https://tensaengineering.dev/projects/
    https://tensaengineering.dev/knowledge-base/
    https://tensaengineering.dev/story/

Standalone HTML pages should use their actual paths:

    https://tensaengineering.dev/projects/neurocore.html
    https://tensaengineering.dev/projects/argus-acli.html
    https://tensaengineering.dev/projects/argus-lab.html

Avoid duplicate sitemap entries such as:

    https://tensaengineering.dev/index.html
    https://tensaengineering.dev/projects/index.html
    https://tensaengineering.dev/knowledge-base/index.html
    https://tensaengineering.dev/story/index.html

when the clean directory URL is the preferred public route.

---

## Current sitemap.xml Content

Current root-level `sitemap.xml` should use this structure:

    <?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
      <url>
        <loc>https://tensaengineering.dev/</loc>
      </url>
      <url>
        <loc>https://tensaengineering.dev/projects/</loc>
      </url>
      <url>
        <loc>https://tensaengineering.dev/projects/neurocore.html</loc>
      </url>
      <url>
        <loc>https://tensaengineering.dev/projects/argus-acli.html</loc>
      </url>
      <url>
        <loc>https://tensaengineering.dev/projects/argus-lab.html</loc>
      </url>
      <url>
        <loc>https://tensaengineering.dev/knowledge-base/</loc>
      </url>
      <url>
        <loc>https://tensaengineering.dev/story/</loc>
      </url>
    </urlset>

Do not add `lastmod` until there is a reliable maintenance process.

Incorrect or stale `lastmod` values are worse than omitting them.

---

## Current robots.txt Plan

The root-level robots file is:

    robots.txt

Current purpose:

- allow normal crawling
- point crawlers to the sitemap
- avoid accidentally blocking public pages
- establish a standard root-level crawler guidance file

Current root-level `robots.txt` should contain:

    User-agent: *
    Allow: /

    Sitemap: https://tensaengineering.dev/sitemap.xml

Do not use robots.txt to hide private information.

Private or sensitive material should not be deployed publicly in the first place.

---

## Google Search Console Plan

Google Search Console should be configured after:

    sitemap.xml exists
    robots.txt exists
    the files are pushed to GitHub
    GitHub Pages has deployed them
    both files are reachable at the live domain

Google Search Console setup steps:

1. Open Google Search Console.
2. Add the TENSA Engineering domain property or URL-prefix property.
3. Verify ownership.
4. Confirm Google can access:

       https://tensaengineering.dev/
       https://tensaengineering.dev/sitemap.xml
       https://tensaengineering.dev/robots.txt

5. Submit the sitemap:

       https://tensaengineering.dev/sitemap.xml

6. Inspect the homepage URL.
7. Request indexing for the homepage if appropriate.
8. Monitor indexing status and sitemap processing errors.
9. After new public pages are added and deployed, confirm the updated sitemap is processed and inspect important new URLs such as:

       https://tensaengineering.dev/story/

Preferred verification method:

    Domain verification through DNS if practical.

Reason:

    Domain verification covers the whole domain more cleanly than a single URL-prefix property.

Because DNS is managed through Cloudflare, DNS verification should be straightforward if Google provides a TXT record.

---

## Bing Webmaster Tools Plan

Bing Webmaster Tools should be configured after:

    sitemap.xml exists
    robots.txt exists
    the files are pushed to GitHub
    GitHub Pages has deployed them
    both files are reachable at the live domain

Bing setup steps:

1. Open Bing Webmaster Tools.
2. Add the TENSA Engineering site.
3. Verify ownership.
4. Submit the sitemap:

       https://tensaengineering.dev/sitemap.xml

5. Confirm Bing can fetch the sitemap.
6. Monitor sitemap processing status.
7. Monitor crawl/indexing issues.
8. After new public pages are added and deployed, confirm Bing can see the updated sitemap.

Possible verification methods:

- DNS TXT record through Cloudflare
- meta tag in the homepage
- import from Google Search Console if already configured

Preferred method:

    DNS verification through Cloudflare if practical.

---

## Search Engine Registration Order

Recommended order for initial setup:

1. Create `sitemap.xml`.
2. Create `robots.txt`.
3. Commit and push both files.
4. Wait for GitHub Pages deployment to complete.
5. Confirm these URLs load in the browser:

       https://tensaengineering.dev/sitemap.xml
       https://tensaengineering.dev/robots.txt

6. Set up Google Search Console.
7. Submit sitemap to Google.
8. Set up Bing Webmaster Tools.
9. Submit sitemap to Bing.
10. Record completion status in this document and `docs/website_state.md`.

Do not submit the sitemap before it is live and reachable.

For later public page additions:

1. Add the real public page.
2. Add the new public route to `sitemap.xml`.
3. Verify the sitemap locally.
4. Commit and push.
5. Wait for GitHub Pages deployment.
6. Confirm the live sitemap includes the new URL.
7. Inspect the new page in Google Search Console if appropriate.
8. Monitor Bing after its next sitemap fetch.

---

## Indexing Expectations

Submitting a sitemap does not guarantee indexing.

Search engines decide what to crawl, index, and rank.

The sitemap helps discovery.

It does not replace:

- useful public content
- clean internal links
- accurate titles and descriptions
- readable page structure
- meaningful page text
- consistent canonical URLs
- good public documentation
- useful project pages
- helpful Knowledge Base content

Early indexing may be limited because the site currently has only a small number of pages.

That is acceptable.

The first goal is clean discoverability.

The second goal is useful content expansion.

---

## What Should Not Be Indexed

The following should not appear in the sitemap:

    docs/
    assets/
    README.md
    CNAME
    styles.css
    internal planning docs
    source maps
    resume prompts
    repository maps
    documentation closeout docs
    image files
    future planned URLs
    placeholder directories that do not exist

Important:

The `docs/` directory exists in the public GitHub Pages repository, but it is internal planning content.

Do not intentionally surface it through public navigation or the sitemap.

If internal docs being publicly reachable becomes a concern later, revisit repository structure or GitHub Pages deployment strategy.

For now:

    Do not link public pages to internal docs.
    Do not include internal docs in sitemap.xml.

---

## Sitemap Update Triggers

Update `sitemap.xml` when:

- a public page is created
- a public page is removed
- a public page is renamed
- a public route changes
- a section index is created
- a Knowledge Base category page is created
- a Story, Resources, About, or Build Notes page is created
- old public URLs are retired or redirected

Do not update the sitemap for:

- CSS changes
- branding image changes
- internal documentation changes
- README changes
- planning doc updates
- source map updates
- pages that are planned but not created

---

## Documentation Update Triggers

When `sitemap.xml` or `robots.txt` is created, update:

    docs/infrastructure/tensa_repository_map.txt
    docs/planning/page_inventory.md
    docs/website_state.md
    docs/ai-operations/tensa_website_resume_prompt.md

When search indexing setup is completed, update:

    docs/website_state.md
    docs/planning/search_indexing_strategy.md
    docs/ai-operations/tensa_website_resume_prompt.md if it affects future startup context

When new public pages are added, update:

    sitemap.xml
    docs/planning/page_inventory.md
    docs/planning/internal_linking_strategy.md
    docs/website_state.md
    docs/infrastructure/tensa_repository_map.txt
    docs/planning/content_source_map.md if source requirements changed or a factual page type was added
    docs/planning/search_indexing_strategy.md if sitemap/indexing state changed

Also update this document if the indexing workflow changes.

---

## Relationship To Other Docs

### website_state.md

Owns:

    current live status of sitemap, robots.txt, Google Search Console, and Bing Webmaster Tools.

Does not own:

    detailed indexing workflow.

---

### tensa_repository_map.txt

Owns:

    file existence and repository location for sitemap.xml, robots.txt, and this strategy doc.

Does not own:

    search submission strategy.

---

### page_inventory.md

Owns:

    public page existence and status.

Does not own:

    search engine submission details.

---

### internal_linking_strategy.md

Owns:

    internal page-to-page linking and reader flow.

Does not own:

    sitemap submission or webmaster tool setup.

---

### documentation_strategy.md

Owns:

    documentation responsibility boundaries.

Does not own:

    specific search indexing workflow.

---

### content_source_map.md

Owns:

    source-doc requirements before writing factual pages.

Does not own:

    sitemap or robots.txt policy.

---

## Future Automation

When the site grows beyond a small number of pages, consider adding:

    scripts/generate_sitemap.py

Purpose:

- scan public HTML files
- exclude internal docs
- generate canonical public URLs
- write sitemap.xml automatically
- reduce stale sitemap risk

Potential future behavior:

- include `/` for root index
- include clean directory URLs for section indexes
- include standalone `.html` pages
- exclude `docs/`
- exclude `assets/`
- exclude hidden files
- optionally include `lastmod` based on Git metadata if reliable

Do not create automation until manual maintenance becomes annoying or error-prone.

For the current site size, manual sitemap maintenance is acceptable.

---

## Future SEO Relationship

This document is not the SEO topic map.

SEO topic planning lives in:

    docs/planning/seo_topic_map.md

That file should own:

- target topics
- article clusters
- search intent
- Knowledge Base content priorities
- content sequencing
- internal SEO links

This search indexing strategy owns:

- sitemap
- robots.txt
- Google Search Console
- Bing Webmaster Tools
- indexing setup
- search-discovery maintenance workflow

Do not mix the two too heavily.

Indexing is technical discoverability.

SEO topic planning is content strategy.

---

## Replacement Verification Rule

After each full-file replacement during closeout or live website editing, run a targeted verification check before moving to the next file.

The verification should confirm the intended change actually landed and that old/stale text or links were removed when applicable.

Examples:

    grep -n "https://tensaengineering.dev/story/\|/story/ added to sitemap" docs/planning/search_indexing_strategy.md
    grep -n "https://tensaengineering.dev/story/" sitemap.xml

This rule exists to catch:

- paste mistakes
- missed saves
- wrong-file edits
- stale snippets
- unintended partial replacements

---

## Current Recommended Next Steps

Immediate next steps:

1. Commit and push the Story page, navigation updates, sitemap update, Claude polish prompt, and closeout documentation updates.

2. Wait for GitHub Pages deployment to complete.

3. Confirm these URLs load in the browser:

       https://tensaengineering.dev/story/
       https://tensaengineering.dev/sitemap.xml
       https://tensaengineering.dev/robots.txt

4. Confirm the live sitemap includes:

       https://tensaengineering.dev/story/

5. Inspect the new Story URL in Google Search Console if appropriate:

       https://tensaengineering.dev/story/

6. Monitor Google and Bing sitemap processing after deployment.

Later next steps:

- create Resources if organizing GitHub, future videos, downloads, and public links becomes the priority
- create About if concise TENSA mission/builder identity becomes the priority
- create Knowledge Base categories if the teaching layer becomes the priority
- create Build Notes if public development history becomes the next content lane

---

## Completion Criteria

Search indexing foundation is complete when:

- `sitemap.xml` exists at repo root
- `robots.txt` exists at repo root
- `robots.txt` points to the sitemap
- sitemap includes only real public pages
- canonical URLs exist on all current public HTML pages
- Open Graph metadata exists on all current public HTML pages
- Twitter large-image card metadata exists on all current public HTML pages
- dedicated 1200 x 630 social preview image exists
- JSON-LD structured data exists and validates on all current public HTML pages
- sitemap is reachable at the live domain
- robots.txt is reachable at the live domain
- Google Search Console property is verified
- sitemap is submitted to Google
- Bing Webmaster Tools property is verified
- sitemap is submitted to Bing
- `docs/website_state.md` records indexing status
- repo map includes the new files
- page inventory reflects search/indexing support files where appropriate
- resume prompt includes search/indexing status if useful for future sessions

After the Story page closeout deploys, confirm:

- `https://tensaengineering.dev/story/` is reachable
- the live sitemap includes `https://tensaengineering.dev/story/`

---

## Final Rule

Search engines should see the real public website clearly.

Do not submit fantasy pages.

Do not hide broken structure behind a sitemap.

Do not treat indexing as SEO magic.

Build useful pages.

Link them clearly.

Keep the sitemap honest.