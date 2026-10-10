# TENSA Website State

This page holds only the facts no other doc owns: branding and asset use, deployment and exposure facts, and open decisions. It is not a status report, a page list, a file tree, a work log or a rule book, and it must not grow back into one. Next steps live in the note. Rules live in `docs/ai-operations/operating_rules.md`.

Change it only when a branding choice, a deployment fact or an open decision changes.

## Branding and asset use

Which logo goes where. Paths are under `assets/images/branding/`. Checked against the public HTML on 2026-10-10.

- Page header, every public page: `tensa/tensa-horizontal-header-transparent.png`. This version drops the small subtitle line so it stays readable at navigation size.
- Hero on TENSA pages, including the homepage, Projects, the Knowledge Base index and Story: `tensa/tensa-stacked-logo-transparent.png`.
- Hero on each project page: `neurocore/neurocore-stacked-transparent.png`, `argus-acli/argus-acli-system-intelligence-stacked-transparent.png`, `argus-lab/argus-lab-interactive-analysis-stacked-transparent.png`.
- Project cards on the homepage and Projects page: the horizontal transparent version of those same three.
- Knowledge Base articles and the Glossary carry TENSA site branding only.
- Social preview image on every public page: `assets/images/social/tensa-og-image.png`.

Variants:

- Argus ACLI: the "System Intelligence" variants show the product role and are the ones in use. The "NeuroCore" variants show that it is built on NeuroCore; they are kept and not used on any current page.
- Argus Lab: the "Interactive Analysis" variants show the training and analysis direction and are the ones in use. The "NeuroCore" variants show that it belongs to the NeuroCore ecosystem; they are kept and not used on any current page.
- Transparent PNGs are used wherever a baked black background would show. The originals are kept.
- The full TENSA horizontal and stacked logos are kept for larger or future uses.

Favicon:

- A simplified TENSA T-symbol with a transparent background and no wordmark, chosen so it reads at browser-tab size. It is deliberately simpler than the full logo.
- Every public page links the root `favicon.ico`, `tensa/favicon-32x32.png` and `tensa/apple-touch-icon.png`. The `android-chrome` icons and `tensa-icon-512.png` are kept beside them.

Visual direction: black backgrounds, a neon green signal and circuit motif, blue and purple accents for architecture and model-explanation sections, hexagonal system geometry, modern technical typography.

Asset handling rules:

- Keep branding assets organized by project.
- No loose PNGs in the repository root.
- Preserve original logo files where useful.
- Use the transparent PNG for website rendering when a baked black background is visible.
- Use the header-optimized TENSA logo in navigation headers.
- Do not rename inherited assets without a clear reason.

Blog images, none of which exist yet:

- Keep them organized by category under `assets/images/blog/`.
- Prefer useful diagrams, screenshots, article-specific preview cards and real supporting visuals.
- No generic stock imagery and no hype-heavy AI visuals.

## Deployment and exposure

- GitHub Pages builds from `main` at the repository root, deploy from a branch. Verified 2026-10-10.
- Custom domain `tensaengineering.dev` through the `CNAME` file. DNS is at Cloudflare. HTTPS is enabled.
- The Pages settings page showed "DNS Check in Progress" for the custom domain on 2026-10-10 while the site was live. Not investigated.
- `_config.yml` excludes `docs/` and `README.md` from the published site (commit `b5fe6b3`, Pages build 38). Verified 2026-10-10: the internal doc addresses return 404.
- The repository is public on GitHub, so every branch and every file under `docs/` is readable there.
- Rich states the GitHub account is on the free plan; not checked in billing settings. As far as known, Pages from a private repository needs a paid plan; not tested.
- Public contact address: `contact@tensaengineering.dev`, through Cloudflare Email Routing, configured and tested before the Contact page was published.

## Open decisions

- Whether to move the internal docs to a private repository. The exclude hides them from the website only.
- Public technical artifact strategy: what to publish, and when.
- Public repository or open-component strategy.

## Where everything else lives

- Pages, their status and next actions: `docs/planning/page_inventory.md`
- Navigation and links: `docs/planning/internal_linking_strategy.md`
- Sitemap, robots, search-console state and open live checks: `docs/planning/search_indexing_strategy.md`
- Long-term structure, including retiring the old Argus ACLI site: `docs/planning/website_information_architecture.md`
- Blog research and candidates: `docs/planning/blog_strategy.md`
- History: the tag `archive/pre-slim-20261010`
