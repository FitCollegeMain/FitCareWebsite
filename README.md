# FITCare Support Services — Website Rebuild Prototype

High-fidelity, fully navigable website prototype for [FITCare Support Services](https://fitcaresupportservices.com.au) — a registered NDIS provider in South East Queensland. This prototype is the definitive reference for the production build: the developer's job is translation, not interpretation.

## Source documents

| Document | Purpose |
|---|---|
| [`docs/PROJECT-BRIEF.md`](docs/PROJECT-BRIEF.md) | The build brief — deliverable, stack, IA, components, accessibility requirements, phases |
| [`docs/fitcare-website-content-audit.md`](docs/fitcare-website-content-audit.md) | Faithful audit of the current site — source of truth for existing content, compliance must-carry-overs, redirect map |
| [`docs/mini-brand-guide-fitcare.pdf`](docs/mini-brand-guide-fitcare.pdf) | Official brand: blue `#1E4689`, black, white; fonts Bilo + Gardenisa |

## Phase status

| Phase | Deliverable | Status |
|---|---|---|
| 1. Foundations | Design tokens, type, homepage concept — `prototype/phase1-homepage-concept.html` | ✅ **Approved 3 Jul 2026** |
| 2. Component library | `prototype/phase2-component-library.html` — all §7 brief components, working + documented | ✅ **Approved 3 Jul 2026** |
| 3. Core pages | `site/` — Home, Services hub, Health/Fitness/Wellbeing service page, Sunshine Coast location page, Get Started flow + shared `css/tokens.css`, `css/site.css`, `js/site.js` | ✅ **Approved 3 Jul 2026** |
| 4. Remaining pages | All service/location instances, Team + profile template, Activities, Coordinators, About, Careers, Contact, Resources (NDIS guide, FAQs, News + article template, Feedback & Complaints), Accessibility Statement | ✅ **Approved 3 Jul 2026** |
| 5. Handoff pack | [`README-FOR-DEVELOPER.md`](README-FOR-DEVELOPER.md) · [`docs/redirect-map.md`](docs/redirect-map.md) · [`docs/placeholder-register.md`](docs/placeholder-register.md) | ✅ **Delivered 3 Jul 2026** |

## Handoff

The prototype is complete. The production developer starts at
[`README-FOR-DEVELOPER.md`](README-FOR-DEVELOPER.md) — architecture, tokens,
components, form logic, the 301 redirect map, accessibility requirements and the
pre-launch checklist. The launch gate is an empty
[`docs/placeholder-register.md`](docs/placeholder-register.md): every sample item
is chip-flagged in the prototype and listed there with an owner.

## Approved design decisions (Phase 1, 3 Jul 2026)

1. **Palette** — brand blue `#1E4689` primary scale + warm "sun" amber accent (`#FFB528` family) + blue-biased neutrals. All text combinations verified ≥ 4.5:1 (WCAG 2.2 AA).
2. **Type** — free stand-ins for the licensed brand faces: Bricolage Grotesque (display, for Bilo), Figtree (body, for Bilo text), Dancing Script (script, for Gardenisa). Approved for prototype and production.
3. **Dark mode** — ships alongside light; token-level theming.
4. **Voice** — participant-first-person: *"With the right support, I do it my way."* Family and coordinator pages keep their own registers per the brief.
5. **Outstanding asset** — production logo as SVG / transparent PNG (primary + secondary versions). Header wordmark is currently a live-text recreation.

## Repository layout

```
site/                    ← THE PROTOTYPE (open site/index.html in a browser — no server, no build step)
  css/tokens.css           the one shared token file (colours, type, spacing, radii, shadows)
  css/site.css              all component styles, token-driven
  js/site.js                the one shared JS file (all progressive enhancement)
  assets/fonts/             self-hosted woff2 (Bricolage Grotesque, Figtree, Dancing Script)
  index.html                home
  get-started.html          multi-step enquiry/referral flow (?who=coordinator pre-routes)
  services/                 hub + 1 built landing page + 4 Phase-4 stubs
  locations/                1 built landing page (Sunshine Coast) + hub/3 stubs
  components.html           Phase 2 component library (self-contained, documentation)
  …                         every IA page exists — unbuilt ones are labelled stubs so all nav resolves
tools/build_pages.py     ← page generator (header/footer/nav live in one place); output is committed
prototype/               ← Phase 1 & 2 review snapshots (self-contained single files)
docs/                    ← brief, content audit, brand guide
```

## Viewing the prototype

Open `site/index.html` straight from disk — every page works with `file://`, JS disabled included. Phase 1/2 snapshot files in `prototype/` are fully self-contained (fonts inlined).
