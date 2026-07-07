# TENSA Engineering Blog Engagement Strategy

---

## Purpose

This document defines the planning strategy for reader contact, blog-post calls to action, contributor outreach, guest posting, attribution, and cross-site collaboration for the future TENSA Engineering Blog.

This is an internal planning document.

It is not a public website page.

No public blog pages, contact forms, guest posts, or collaboration programs are created by this document.

---

## Core Principle

The blog should invite useful technical conversation without turning the site into a low-quality comment system, backlink exchange, or content farm.

The goal is to create legitimate paths for:

- reader questions
- topic suggestions
- corrections
- collaboration inquiries
- guest article discussions
- cross-site educational references
- future expert contributions

The goal is not to manufacture links for ranking purposes.

---

## Blog Contact CTA

Each future blog post should include a small, consistent contact call-to-action near the end of the article.

The CTA should encourage useful reader interaction without implying live support, consulting availability, or an open comment thread.

Suggested public copy direction:

    Have a question, correction, or topic idea?
    Contact TENSA Engineering.

Possible button text:

    Contact TENSA Engineering
    Suggest a topic
    Send a question

Preferred destination:

    /contact.html

The current site already has email forwarding and a public contact page. Blog posts should reuse that route instead of introducing a new form or comment system during the first blog phase.

---

## Reader Question Workflow

Reader questions may become future blog topics, but should not be treated as a public Q&A system at launch.

Good reader-question uses:

- identify common confusion
- collect repeated pain points
- find new article ideas
- clarify explanations that missed the mark
- discover homelab, AI coding, local AI, or tooling problems readers actually face

Avoid promising:

- personal technical support
- guaranteed replies
- free troubleshooting
- emergency help
- custom architecture reviews
- code review through the contact page

The public contact page or blog CTA may eventually explain that selected questions may inspire future articles, with identifying details removed unless explicit permission is granted.

---

## Comment System Boundary

Do not add a public comment system in the first blog phase.

Reasons:

- moderation burden
- spam risk
- link spam risk
- privacy concerns
- static-site simplicity
- low early traffic does not justify the maintenance

Use the contact page first.

Future options, if real need appears:

- email-based topic suggestions
- moderated GitHub Discussions if appropriate
- newsletter replies
- curated reader-question posts
- private submission form with clear expectations

Any future user-generated public link area should handle user-generated links cautiously and should not allow unreviewed promotional links.

---

## Guest Posts and Contributor Articles

Guest posts can help visibility and credibility when they are based on real expertise, complementary audiences, and useful technical content.

Good guest-post fits:

- a Linux admin writing about real troubleshooting lessons
- a homelab builder explaining a purposeful setup and what it actually runs
- an AI-assisted developer explaining a workflow failure and what fixed it
- a local AI builder sharing practical constraints and lessons learned
- a tools reviewer with hands-on evidence and clear limits

Poor guest-post fits:

- generic AI news summaries
- thin tool roundups
- affiliate-first product posts
- posts written mainly to get a backlink
- paid guest posts that pass ranking credit
- unrelated content from agencies or link builders
- keyword-stuffed anchor text

Guest content should meet the same trust standard as TENSA-authored content.

---

## Cross-Site Collaboration

Cross-site collaboration can be useful when it is editorially natural.

Examples:

- TENSA writes an original article for another technical blog with clear attribution.
- Another technical blogger writes a relevant article for TENSA with clear attribution.
- Two related posts cite each other because each adds real value.
- A homelab article links to a builder's detailed rack documentation because it is genuinely useful.
- A TENSA article cites another site's tutorial, benchmark, review, or example when it improves the reader's understanding.

Avoid treating collaboration as a simple link swap.

Do not use language like:

    Link to me and I will link to you.

Do not build partner pages solely for cross-linking.

Do not use optimized anchor text just to target search rankings.

---

## SEO and Link Safety

Google's public spam policies warn against creating links to or from a site primarily to manipulate search rankings. Their examples include buying or selling links that pass ranking credit, exchanging money/goods/services for posts that contain links, excessive link exchanges, and advertorials or guest posts with optimized anchor text meant to pass ranking credit.

Planning reference:

    https://developers.google.com/search/docs/essentials/spam-policies

Google also recommends qualifying outbound links when the relationship should be disclosed. Paid, sponsored, affiliate, or compensated links should use appropriate link attributes such as `rel="sponsored"`. User-generated links may use `rel="ugc"`. When a link should not imply endorsement or association, `rel="nofollow"` may be appropriate.

Planning reference:

    https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links

TENSA blog collaboration should be built around usefulness, attribution, and real editorial value, not ranking manipulation.

---

## Attribution Pattern

Guest posts should clearly show who wrote the article and why they are relevant.

Future guest-post metadata should include:

- author name
- author role or background
- author site or profile when appropriate
- article date
- editor / review note when appropriate
- disclosure if there is any compensation, sponsorship, affiliate relationship, or material connection

Suggested public pattern:

    Guest author: Name, role or background.
    Edited and reviewed by TENSA Engineering.

If an article is contributed by someone else, readers should not be confused about authorship.

---

## Outbound Link Policy

Outbound links in blog posts should serve the reader.

Good outbound links:

- source documentation
- vendor documentation
- model/tool release notes
- product specifications
- benchmark sources when relevant
- another blogger's genuinely useful article
- original research, diagrams, or tutorials
- GitHub repositories that prove a technical claim

Avoid outbound links that exist only for:

- ranking manipulation
- paid placement without disclosure
- irrelevant promotion
- reciprocal linking pressure
- affiliate revenue without usefulness
- keyword-rich anchor text games

Anchor text should be natural and descriptive.

Bad:

    best cheap homelab server rack affiliate deal

Better:

    Dell R730 hardware notes
    the author's homelab build write-up
    Google Search Central's outbound link guidance

---

## Affiliate and Sponsored Content Relationship

Affiliate links and sponsored relationships must remain separate from editorial judgment.

Rules:

- disclose material connections clearly
- qualify paid/sponsored/affiliate links appropriately in HTML
- do not sell links for ranking credit
- do not let affiliate potential decide whether a topic is worth writing
- do not recommend hardware or tools that do not fit the reader's actual problem
- do not put affiliate links in core Knowledge Base doctrine pages
- do not put affiliate links in core project architecture pages

Affiliate-friendly posts may exist later, especially in buying guides, homelab hardware recommendations, networking gear, local AI hardware, and tool subscription comparisons.

Trust comes first.

---

## Future Blog Article CTA Pattern

Each future article template should include one of these CTA variants near the end.

### Standard Reader CTA

    Have a question, correction, or topic idea?
    Send a note through the TENSA Engineering contact page.

### Collaboration CTA

    Build or write about this kind of work?
    TENSA Engineering is open to useful technical collaboration and guest article ideas when they help readers.

### Homelab CTA

    Have a homelab setup with a clear purpose and real lessons learned?
    Send a note. It may help shape a future article.

### AI Coding CTA

    Running into a repeated AI coding failure?
    Send the pattern, not private code. It may become a future explanation article.

These should link to:

    /contact.html

Do not expose raw email addresses in every blog post unless that becomes an intentional anti-spam decision.

---

## Future Collaboration Page

A dedicated collaboration page is not required for the first blog phase.

Possible future route:

    /contact.html#collaboration

or:

    /collaborate.html

Only create a dedicated collaboration page if:

- the blog is active
- outside contributors are a real workflow
- guest-post rules need public explanation
- the contact page becomes too crowded

---

## Current Planning Boundary

This document records future blog engagement planning only.

It does not create:

- a public comment system
- a guest-post program
- public collaboration pages
- public blog CTAs
- email workflow automation
- affiliate links
- sponsored content
- public article content

Future public implementation should happen in a separate branch with local review, browser preview, and link validation.
