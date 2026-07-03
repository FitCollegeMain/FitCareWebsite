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
| 2. Component library | `prototype/phase2-component-library.html` — all §7 brief components, working + documented | 🟡 **Built — awaiting review** |
| 3. Core pages | Home, Services hub + one service page, one location page, Get Started flow | ⬜ |
| 4. Remaining pages | All other service/location pages, Team, Activities, Coordinators, About, Resources, Careers, Contact | ⬜ |
| 5. Handoff pack | Developer README, redirect map, accessibility notes, placeholder register | ⬜ |

## Approved design decisions (Phase 1, 3 Jul 2026)

1. **Palette** — brand blue `#1E4689` primary scale + warm "sun" amber accent (`#FFB528` family) + blue-biased neutrals. All text combinations verified ≥ 4.5:1 (WCAG 2.2 AA).
2. **Type** — free stand-ins for the licensed brand faces: Bricolage Grotesque (display, for Bilo), Figtree (body, for Bilo text), Dancing Script (script, for Gardenisa). Approved for prototype and production.
3. **Dark mode** — ships alongside light; token-level theming.
4. **Voice** — participant-first-person: *"With the right support, I do it my way."* Family and coordinator pages keep their own registers per the brief.
5. **Outstanding asset** — production logo as SVG / transparent PNG (primary + secondary versions). Header wordmark is currently a live-text recreation.

## Viewing the prototype

Every prototype file is self-contained (fonts inlined as data URIs, no external requests). Open any `.html` file straight from disk in a browser — no server, no build step.
