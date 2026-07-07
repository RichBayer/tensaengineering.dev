# TENSA Engineering Blog Reader Experience

---

## Purpose

This document defines the planned reader experience for future TENSA Engineering Blog articles and blog index pages.

It captures article layout features, reader-facing components, technical metadata expectations, future RSS/newsletter direction, and feature boundaries.

This is an internal planning document.

It is not a public website page.

No public blog pages, article templates, RSS feed, newsletter, navigation links, or sitemap entries are created by this document.

---

## Core Principle

TENSA blog articles should feel like they belong to the same site as the product pages and Knowledge Base, but they should read faster.

The blog should use the same brand system, typography, dark technical visual language, header/footer patterns, card language, and grounded tone.

The blog should not feel like a disconnected WordPress theme, a generic tech-news site, or an affiliate content farm.

The target feel:

    TENSA-branded technical magazine article.
    Plainspoken.
    Useful fast.
    Connected to deeper engineering ideas.

---

## Blog Article Role

A blog post should start from a reader's practical question, frustration, curiosity, or decision point.

The article should then explain:

1. what the reader is seeing
2. what they probably think is happening
3. what is actually happening
4. what to do instead
5. where the deeper TENSA concept fits
6. where to go next

Blog articles should be more flexible than Knowledge Base articles.

They may cover:

- AI coding frustrations
- homelab planning
- tool and model choices
- local AI hardware and tradeoffs
- practical build lessons
- future buying guides
- reader questions
- collaboration topics

---

## Standard Blog Article Components

Every future blog article should include these core components unless there is a clear reason not to.

### Required Launch Components

- consistent site header
- breadcrumb or clear category path
- category label
- clear article title
- short subtitle / summary
- author or site attribution
- published date
- updated date when changed
- estimated reading time
- quick answer box
- main article body
- related reading section
- contact / topic-suggestion CTA
- consistent site footer

### Strongly Recommended Components

- direct-answer introduction
- “what people usually get wrong” section
- “do this instead” section
- practical example
- one useful visual or diagram when it improves understanding
- source / freshness note for current tool, model, price, or hardware claims
- related Knowledge Base links
- related project links where appropriate

---

## Article Metadata Pattern

Future blog articles should show plain metadata near the article header.

Suggested visible pattern:

    Richard Bayer · TENSA Engineering · Published July 2026 · Updated July 2026 · 7 min read

If a guest author is involved, use a clear attribution pattern:

    Guest author: Name, role or background.
    Edited and reviewed by TENSA Engineering.

Readers should never be confused about authorship.

---

## Quick Answer Box

Each blog post should include an early quick answer box.

The quick answer box should give readers a useful answer in two to four sentences.

Purpose:

- help search visitors quickly confirm they are in the right place
- improve readability
- support answer-engine clarity
- prevent long articles from burying the main answer

Example direction for a homelab post:

    Quick answer:
    A homelab is useful when it helps you learn, test, host, troubleshoot, or validate something real. Start with the workload. If VMs solve the problem, use VMs. Buy hardware when the limitation becomes real.

Example direction for an AI coding post:

    Quick answer:
    AI-generated code often breaks after one fix because the model is working from incomplete project context, unclear boundaries, or weak verification. A better model helps, but a better workflow matters more.

The quick answer should not replace the article.

It should orient the reader.

---

## Common TENSA Blog Sections

Blog posts should not all look identical, but these reusable section patterns should appear often.

### The Problem

Describe the reader's pain or decision point plainly.

Examples:

- your AI assistant fixed one bug and broke another
- your homelab looks impressive but does not have a clear workload
- you are comparing coding models without knowing what job they need to do
- you want to run local AI but do not know whether your GPU is enough

### What People Usually Get Wrong

This should become a signature TENSA blog section.

It lets the post correct a bad assumption without insulting the reader.

Examples:

    They think the model is refusing to listen.
    Usually, it is working from incomplete context.

    They think a rack server automatically makes a better homelab.
    Usually, the better first lab is a VM, a used mini PC, or the laptop they already own.

### What Is Actually Happening

Explain the real mechanism, constraint, or tradeoff.

This section should be practical and grounded.

### Do This Instead

Every practical post should give the reader a better next step.

For AI coding:

    Give the model the repo structure, current goal, constraints, files it may touch, files it must not touch, and the verification command.

For homelab:

    Write down the workload first: learning Linux, running services, testing backups, practicing networking, or hosting local AI. Then choose the smallest setup that solves that job.

### Where This Fits in TENSA

Connect the blog lesson back to deeper TENSA concepts without forcing a sales pitch.

Possible destinations:

- AI Operations
- Persistent AI Memory
- Safe Tool Interaction
- Controlled AI Systems
- Local-First AI
- Linux Diagnostics
- Troubleshooting Training
- NeuroCore
- Argus ACLI
- Argus Lab

---

## Blog Index Page Features

The future `/blog/` page should orient readers quickly and route them by interest.

Recommended components:

- page hero
- short explanation of the blog's role
- featured article
- latest posts
- category cards
- short category descriptions
- “suggest a topic” contact CTA
- RSS link after RSS exists

The blog index should not become a giant archive dump.

It should help readers choose where to start.

---

## Category Page Features

Future category pages should include:

- category title
- short category explanation
- best starting article
- latest posts in that category
- related Knowledge Base links
- contact/topic CTA where appropriate

Example category description:

    Purposeful Homelab
    Practical notes on building labs around real workloads, not just impressive hardware.

Category pages should remain light until there are enough articles to justify deeper organization.

---

## Related Reading

Every blog post should include related reading links near the end.

Recommended groups:

- related Knowledge Base article
- related blog post
- related project page
- contact page CTA

Links should be natural and useful.

Avoid vague link text like:

- click here
- read more
- article

Prefer descriptive link text like:

- Learn how AI Operations keeps project context grounded
- Read about safe AI tool interaction
- Explore Argus Lab's troubleshooting direction
- Contact TENSA Engineering with a topic idea

Public blog posts should not link to internal planning docs.

---

## Contact CTA

Each blog post should include a small contact call-to-action near the end.

The CTA should invite useful contact without promising support.

Standard direction:

    Have a question, correction, or topic idea?
    Send a note through the TENSA Engineering contact page.

Homelab direction:

    Have a purposeful homelab setup with real lessons learned?
    Send a note. It may help shape a future article.

AI coding direction:

    Running into a repeated AI coding failure?
    Send the pattern, not private code. It may become a future explanation article.

Preferred destination:

    /contact.html

Do not add a public comment system during the first blog phase.

---

## Visual and Image Guidance

The blog should use visuals deliberately.

Good visual fits:

- simple explanatory diagrams
- article-specific social preview cards
- screenshots when they teach something
- homelab planning diagrams
- workflow diagrams
- comparison tables
- gear photos when they support the article

Avoid:

- generic glowing AI robot images
- random stock photos
- images that imply unavailable TENSA features
- gear photos that encourage buying without purpose
- huge visual blocks that interrupt the article

A future blog image structure already exists on the planning branch:

    assets/images/blog/
    assets/images/blog/ai-coding/
    assets/images/blog/homelab/
    assets/images/blog/tools-and-models/
    assets/images/blog/local-ai/
    assets/images/blog/build-lessons/
    assets/images/blog/buying-guides/

---

## Tables, Diagrams, and Code Blocks

Use tables when comparison helps.

Good table fits:

- VM vs mini PC vs rack server
- local AI vs cloud AI
- coding assistant vs coding agent
- beginner homelab workloads
- when to upgrade / when to wait

Use diagrams when they clarify a concept.

Good diagram fits:

- prompt -> incomplete context -> bad change
- workload -> VM -> mini PC -> server rack
- model -> tool boundary -> human approval
- raw logs -> evidence -> findings -> recommendation

Use code blocks only when the article genuinely teaches commands, configuration, repo structure, or examples.

Do not make blog posts look like raw internal docs.

---

## Table of Contents

A table of contents is optional.

Use it for longer posts, especially:

- homelab buying guides
- tool comparisons
- local AI hardware explainers
- multi-step tutorials
- long troubleshooting explainers

Skip it for short posts.

The first blog template should support a table of contents but not require it.

---

## Technical Metadata Expectations

Every future public blog article should eventually include:

- unique title
- meta description
- canonical URL
- Open Graph title
- Open Graph description
- Open Graph URL
- Open Graph image
- Twitter/X card metadata
- BlogPosting JSON-LD
- author
- datePublished
- dateModified
- image metadata when applicable
- breadcrumb structured data when appropriate

The existing website already uses metadata and JSON-LD patterns on public pages.

Blog pages should follow that discipline instead of becoming informal one-off pages.

---

## RSS Feed Planning

RSS is a future subscription feature.

An RSS feed is a simple public XML file that lets readers subscribe to new posts in RSS readers without checking the site manually.

Possible future path:

    /feed.xml

RSS fits the TENSA audience because technical readers, Linux users, homelab builders, and developers often appreciate direct subscription options that do not depend on social algorithms.

Do not create the RSS feed until there are enough real posts to make it useful.

Suggested order:

1. blog structure
2. first two or three posts
3. blog index and category pages
4. RSS feed
5. newsletter later if needed

Future RSS link text:

    Follow new posts by RSS

---

## Newsletter Planning

A newsletter may be useful later, but it is not a first-phase requirement.

Do not add newsletter signup before there is enough content rhythm to justify it.

Possible future uses:

- new blog post updates
- build lessons
- homelab planning notes
- AI workflow notes
- local AI experiments
- Argus / NeuroCore milestone summaries

Avoid popups or aggressive signup prompts.

If added later, the newsletter should feel optional and low-pressure.

---

## Search and Filtering

Do not add blog search or tag filtering during the first blog phase.

Possible future features:

- category filter
- tag pages
- search field
- series pages
- author pages

Add these only after enough posts exist to justify them.

A small static site with a handful of posts does not need complex filtering.

---

## Features to Avoid at Launch

Avoid adding these during the first blog phase:

- public comments
- popups
- ads
- auto-playing media
- infinite scroll
- AI chatbot widget
- login/account system
- like buttons
- overbuilt tag clouds
- affiliate blocks before trust exists
- unreviewed user-generated links

The blog should feel clean, useful, and trustworthy.

---

## First Implementation Recommendation

The first public blog implementation branch should create only enough to prove the format.

Recommended first public structure:

    /blog/index.html
    /blog/ai-coding/index.html
    /blog/ai-coding/why-ai-code-breaks-after-it-works-once.html

Recommended second category proof:

    /blog/homelab/index.html
    /blog/homelab/what-is-a-homelab-actually-for.html

The first proof article should validate the AI coding lane.

The second proof article should validate the homelab lane.

Together, they prevent the blog from becoming pigeonholed as only AI coding frustration content.

---

## Current Planning Boundary

This document records future blog reader-experience planning only.

It does not create:

- public blog pages
- public blog article templates
- public RSS feed
- public newsletter signup
- public comments
- public category pages
- navigation links
- sitemap entries
- article content

Future public implementation should happen in a separate branch or later continuation of the current branch with local review, browser preview, and internal-link validation.
