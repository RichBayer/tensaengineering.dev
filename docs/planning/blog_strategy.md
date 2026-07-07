# TENSA Engineering Blog Strategy

---

## Purpose

This document defines the planning strategy for a future TENSA Engineering Blog.

The blog should become the faster, more flexible public content layer for the TENSA Engineering website. It should help the site respond to timely questions, common frustrations, search trends, tool/model confusion, homelab hardware interest, practical builder lessons, and future buyer-intent topics without weakening the deeper Knowledge Base.

The blog is not being created as a public route in this planning pass.

Planned future public routes may include:

    /blog/
    /blog/ai-coding/
    /blog/homelab/
    /blog/tools-and-models/
    /blog/local-ai/
    /blog/build-lessons/

These routes should not be created until the first public blog implementation branch.

---

## Core Role

The TENSA Engineering Blog should serve as the public, readable, problem-first layer between short-form discovery content and the deeper Knowledge Base.

It should answer questions people are already asking, explain common technical misunderstandings in plain language, and route readers toward better engineering habits.

The blog should help readers move from:

    confusion -> explanation -> better workflow -> deeper TENSA concept

The blog should not become a generic AI news site, content farm, affiliate catalog, or random personal journal.

---

## Relationship to Other Site Sections

### Blog

The blog is the fast-moving public content layer.

It should cover:

- timely topics
- practical frustrations
- tool and model confusion
- homelab planning lessons
- hardware and upgrade judgment
- local AI experiments
- short build lessons
- search-driven questions
- future affiliate-friendly buying guides when appropriate

Blog posts can be shorter, more conversational, and more responsive to public interest than Knowledge Base articles.

### Knowledge Base

The Knowledge Base remains the durable teaching layer.

It should cover:

- controlled AI systems
- AI Operations
- persistent AI memory
- local-first AI
- safe tool interaction
- Linux diagnostics
- troubleshooting training
- NeuroCore architecture

Knowledge Base content should be more evergreen, structured, polished, and concept-first.

### Build Notes

Build Notes should summarize meaningful TENSA development milestones.

The blog may contain lightweight build lessons, but public Build Notes should not be replaced by casual blog posts.

### Project Pages

Project pages explain NeuroCore, Argus ACLI, and Argus Lab.

The blog may reference project lessons, but it should not become the source of truth for project maturity, install status, feature availability, or product claims.

---

## Editorial Positioning

The blog should sound like a serious builder explaining practical problems to intelligent readers.

Preferred tone:

- plainspoken
- practical
- direct
- mildly conversational
- technically honest
- builder-focused
- educational without talking down
- skeptical of hype
- useful before promotional

Avoid:

- generic AI startup language
- shallow trend chasing
- hype-heavy tool worship
- "top 10" posts without judgment
- fake certainty about model quality
- unsupported product claims
- affiliate-first writing
- content written only because a keyword exists

The blog should preserve the core TENSA voice:

    Less guessing, more signal.

---

## Target Reader Groups

The blog can serve multiple reader groups without being locked into one lane.

### AI-Assisted Coders and Vibe Coders

Readers who are using ChatGPT, Claude, Cursor, Claude Code, GitHub Copilot, coding agents, or similar tools and are frustrated when the model:

- forgets project context
- misunderstands instructions
- changes files it should not change
- breaks code that worked once
- invents packages, APIs, or architecture
- gets worse when the project gets bigger
- seems less capable than the newest model hype promised
- needs the same explanation repeated every session

The goal is not to mock these readers.

The goal is to explain that models are not magic and that better outcomes usually require better context, source-of-truth documents, tests, review habits, boundaries, and project workflow.

### Homelab and Infrastructure Builders

Readers who are interested in servers, racks, networking gear, cable management, mini PCs, storage, virtualization, cloud labs, home networking, and Linux systems.

Some readers buy impressive hardware before they know what problem they are solving.

The blog should teach:

- plan before buying
- start with the workload
- use VMs when free virtualization is enough
- grow deliberately
- upgrade only when the bottleneck is real
- build labs around learning goals, not just hardware aesthetics
- understand power, noise, heat, networking, backups, and maintenance
- choose gear based on the next practical step

This category can later support affiliate-friendly posts, but the advice must remain honest.

### Tool and Model Chasers

Readers who follow every new model, editor, agent, or coding tool release hoping the next one will solve their workflow problem.

The blog should explain:

- model quality matters, but workflow matters too
- different tools have different strengths
- agentic tools need boundaries
- a stronger model can still fail with weak project context
- benchmarks do not guarantee project success
- tool choice should follow the job being done

### Local AI and Practical Systems Builders

Readers interested in Ollama, local models, GPU limits, local inference, private AI tools, local-first design, and AI systems that understand real files or machines.

The blog should connect these topics to NeuroCore without overstating product maturity.

### Curious Beginners and Future Learners

Readers who may not yet know the right technical terms.

They may search plain questions like:

- Why does AI forget my project?
- Why did Cursor break my app?
- Do I need to know coding to use AI?
- Should I buy a server for a homelab?
- What is a homelab actually for?
- What is the best AI coding model?

Blog posts should answer these questions directly and then guide readers toward stronger concepts.

---

## Initial Blog Categories

The blog should start broad enough to grow, but not so broad that it becomes unfocused.

### AI Coding Frustrations

Problem-first explanations for people using AI to write, fix, or refactor code.

Examples:

- Why AI Code Breaks After It Works Once
- Why Your AI Coding Assistant Keeps Forgetting Your Project
- The New Coding Model Is Not Your Problem. Your Workflow Is.
- Why AI Coding Agents Change Files You Never Asked Them To Touch
- Stop Asking AI to Fix Your Project Without Giving It the Project

Primary deeper links:

- AI Operations
- Persistent AI Memory
- Safe Tool Interaction
- Controlled AI Systems

### Purposeful Homelab

Practical guidance for people building or upgrading home labs, server closets, Linux labs, networking setups, and training environments.

This category should teach readers to connect hardware decisions to actual goals.

Examples:

- What Is a Homelab Actually For?
- Stop Buying Homelab Gear Before You Know the Workload
- When a VM Is Better Than Another Server
- How to Plan a Homelab That Can Grow
- Cable Management Is Nice, But Purpose Matters More

Primary deeper links:

- Linux Diagnostics
- Troubleshooting Training
- Argus Lab
- Local-First AI

### Tools and Models

Plain-English posts about AI coding tools, models, editors, agents, and practical tradeoffs.

This category should not become shallow release coverage.

Examples:

- Claude Code vs ChatGPT vs Cursor: What Problem Are You Actually Solving?
- Why a Better Coding Model Still Needs Better Context
- What Makes an AI Coding Tool Useful on a Real Project?
- Coding Agents Need Job Descriptions, Not Just Prompts

Primary deeper links:

- AI Operations
- Safe Tool Interaction
- Controlled AI Systems
- NeuroCore Architecture

### Local AI and Infrastructure

Posts about local AI, hardware constraints, GPUs, local model runtime, privacy, and real-system awareness.

Examples:

- Do You Actually Need a Local AI Model?
- What Local AI Is Good For And What It Is Not
- GPU Limits Matter More Than Model Hype
- Why Local-First AI Matters for Real System Work

Primary deeper links:

- Local-First AI
- Persistent AI Memory
- NeuroCore

### Build Lessons

Short, public-friendly lessons from building TENSA, NeuroCore, Argus ACLI, and Argus Lab.

This category should be more practical than promotional.

Examples:

- Why Argus ACLI Starts Read-Only
- What Building a Diagnostic Tool Teaches About AI Trust
- Why Documentation Became the Memory Layer
- Real Skill Comes From Solving Real Problems

Primary deeper links:

- Projects
- Story
- Knowledge Base
- Build Notes if created later

### Buying Guides and Practical Recommendations

Future category for gear, tools, books, courses, software, and hardware recommendations.

This should not be created until there is enough traffic, credibility, and review discipline.

Potential future topics:

- homelab starter hardware
- networking cable labeling and organization
- mini PCs vs old enterprise servers
- UPS sizing basics
- SSDs and storage planning
- AI coding subscriptions
- local AI GPU considerations
- Linux learning resources

Affiliate links, if ever used, belong here or in directly related tool/hardware posts.

---

## Problem-First Article Pattern

Many blog posts should start from a real frustration or question.

Suggested structure:

1. State the reader's problem in plain English.
2. Give the direct answer early.
3. Explain what the reader probably thinks is happening.
4. Explain what is actually happening.
5. Show the better workflow or decision path.
6. Connect the lesson to a deeper TENSA concept.
7. Link to one or two related pages.

Example flow:

    Your AI coding assistant did not randomly become dumb.
    It is probably working from incomplete context, stale assumptions, or unclear authority boundaries.

Then explain the workflow problem.

---

## Homelab Article Pattern

Homelab posts should start from purpose, not gear.

Suggested structure:

1. What the reader wants to build or buy.
2. What they think the hardware will solve.
3. What problem they are actually trying to learn or run.
4. Whether VMs, an old laptop, mini PC, cloud lab, or server hardware is enough.
5. When an upgrade becomes justified.
6. What to plan before spending money.
7. How the lesson connects to Linux diagnostics, troubleshooting, local AI, or Argus Lab.

The blog should respect cool hardware while still teaching disciplined upgrade decisions.

The message should be:

    Cool gear is fine. Purpose comes first.

---

## Tool and Model Article Pattern

Tool and model posts should avoid hype and unsupported rankings.

Suggested structure:

1. What the tool or model is.
2. What people expect it to solve.
3. What it is actually good at.
4. Where it commonly fails.
5. What workflow makes it more reliable.
6. Who should consider it.
7. Who should not rush into it.
8. What to verify before making it part of a serious project.

Tool posts should be based on current research, hands-on experience, or clearly labeled public source review.

Do not publish tool comparison claims from memory.

---

## Pain-Point Research Workflow

Future content research should identify what people are actually asking before posts are written.

Useful research sources:

- Google Trends
- Google Search autocomplete
- People Also Ask
- Google Search Console after TENSA pages are live and indexed
- Reddit threads
- YouTube comments
- TikTok comments
- Stack Overflow questions
- GitHub issues and discussions
- Hacker News discussion when relevant
- tool documentation and release notes
- model provider documentation and changelogs

Research should collect:

- exact questions people ask
- repeated frustrations
- misunderstood terms
- tool/model names appearing repeatedly
- buying-intent queries
- signs that people are solving the wrong problem
- topics that naturally connect to TENSA concepts

The goal is not to copy trends.

The goal is to use public frustration as a signal for useful education.

---

## SEO and Search Intent Rules

Blog posts should be written for humans first, but each post should still have a clear search purpose.

Each post should answer one primary question.

Good blog targets:

- Why does AI forget my project?
- Why does AI-generated code break?
- What is a homelab used for?
- Should I buy a server for a homelab?
- Do I need a local AI model?
- What is the best AI coding tool for a real project?

Avoid:

- vague AI buzzword posts
- thin tool summaries
- low-effort listicles
- posts that chase a trend without adding builder judgment
- unsupported claims about product quality or future availability

Each post should include:

- a clear title
- a direct answer near the top
- useful headings
- natural internal links
- current-vs-future boundaries when discussing TENSA projects
- source links when making current claims about tools, models, prices, regulations, or public events

---

## Internal Link Strategy

The blog should route readers into the rest of the site.

Preferred reader flows:

    AI coding frustration -> AI Operations -> Persistent AI Memory -> NeuroCore

    AI coding agent concern -> Safe Tool Interaction -> Controlled AI Systems -> NeuroCore

    homelab gear question -> Linux Diagnostics -> Troubleshooting Training -> Argus Lab

    local AI question -> Local-First AI -> Persistent AI Memory -> NeuroCore

    tool/model comparison -> AI Operations -> Safe Tool Interaction -> Blog follow-up posts

Public pages should not link to internal planning docs.

Blog posts should link to existing public pages only.

Do not create dead links to planned pages.

---

## Affiliate and Monetization Boundary

Affiliate marketing may become useful later, especially for homelab hardware, networking gear, AI coding tools, local AI hardware, books, courses, and practical builder resources.

Affiliate content must not damage trust.

Rules:

- No affiliate links in core Knowledge Base doctrine pages.
- No affiliate links in core project architecture pages.
- Affiliate links belong only in blog posts, buying guides, resources pages, or tool/hardware recommendation pages where buying intent is natural.
- Recommendations should be honest and practical.
- Do not recommend hardware just because it looks impressive.
- Explain when a free VM, existing laptop, mini PC, or cloud lab is enough.
- Use clear affiliate disclosure when affiliate links exist.
- Mark sponsored or affiliate links appropriately in HTML when implemented.

The blog should be able to monetize later, but trust comes first.

---

## Source and Accuracy Rules

Blog posts may be less formal than Knowledge Base articles, but factual discipline still matters.

Do not invent:

- model capabilities
- tool pricing
- product availability
- benchmark results
- release status
- hardware specs
- affiliate relationships
- TENSA product maturity
- Argus ACLI availability
- Argus Lab availability
- NeuroCore features not supported by current source docs

Use current research for:

- current AI model comparisons
- current AI tool pricing
- current hardware recommendations
- current market availability
- public controversies or incidents
- affiliate program details
- legal or disclosure rules

If a blog post references TENSA projects, it must preserve current-vs-future boundaries.

---

## Public Structure Recommendation

When the blog is ready for a public implementation branch, start small.

Recommended first public structure:

    /blog/index.html
    /blog/ai-coding/index.html
    /blog/ai-coding/why-ai-code-breaks-after-it-works-once.html

Optional first homelab structure after that:

    /blog/homelab/index.html
    /blog/homelab/what-is-a-homelab-actually-for.html

Do not create every category at once.

Start with one or two proof posts, then expand based on research and Search Console evidence.

---

## First Candidate Posts

These are planning candidates only, not approved final article assignments.

### AI Coding Frustrations

- Why AI Code Breaks After It Works Once
- Why Your AI Coding Assistant Keeps Forgetting Your Project
- The New Coding Model Is Not Your Problem. Your Workflow Is.
- Why AI Coding Agents Change Files You Never Asked Them To Touch
- Stop Asking AI to Fix Your Project Without Giving It the Project
- Why AI Hallucinates Packages, APIs, and Files
- Why Better Prompts Are Not Enough for Bigger Projects

### Purposeful Homelab

- What Is a Homelab Actually For?
- Stop Buying Homelab Gear Before You Know the Workload
- When a VM Is Better Than Another Server
- How to Plan a Homelab That Can Grow
- Cable Management Is Nice, But Purpose Matters More
- The Difference Between Learning Linux and Collecting Hardware
- When to Upgrade Your Homelab and When to Wait

### Tools and Models

- Why a Better Coding Model Still Needs Better Context
- Claude Code vs ChatGPT vs Cursor: What Problem Are You Actually Solving?
- What Makes an AI Coding Tool Useful on a Real Project?
- Coding Agents Need Job Descriptions, Not Just Prompts
- Model Benchmarks Do Not Replace Project Discipline

### Local AI and Infrastructure

- Do You Actually Need a Local AI Model?
- What Local AI Is Good For And What It Is Not
- Why Local-First AI Matters for Real System Work
- GPU Limits Matter More Than Model Hype
- Local AI, Privacy, and Real System Awareness

### Build Lessons

- Why Argus ACLI Starts Read-Only
- Why Documentation Became the Memory Layer
- What Building a Diagnostic Tool Teaches About AI Trust
- Real Skill Comes From Solving Real Problems
- Why Continuity Has to Be Engineered

---

## First Public Build Recommendation

The first public blog branch should not attempt to launch a full content operation.

Recommended first implementation goal:

    Create the blog index, one category index, and one proof post.

Recommended branch name:

    feature/blog-public-foundation

Recommended first public post:

    /blog/ai-coding/why-ai-code-breaks-after-it-works-once.html

Recommended second public post:

    /blog/homelab/what-is-a-homelab-actually-for.html

The first post validates the AI-assisted coding lane.

The second post validates the purposeful homelab lane.

Together, they prevent the blog from being pigeonholed as only AI coding frustration content.

---

## Current Planning Boundary

This document is internal planning only.

It does not create:

- public blog routes
- public blog posts
- public navigation links
- sitemap entries
- affiliate links
- product claims
- deployment claims

Future public blog implementation should happen on a separate branch with local browser review and internal-link validation.
