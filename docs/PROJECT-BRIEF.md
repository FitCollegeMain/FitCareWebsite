# FITCare Support Services — Website Rebuild Prototype
## Project brief for Claude Code

You are building a high-fidelity, fully navigable website prototype for FITCare Support Services, a registered NDIS provider in South East Queensland. This prototype will be handed to an external web developer as the definitive reference for the production build. It must be good enough that the developer's job is translation, not interpretation.

Work iteratively. At the end of each phase (defined in §10), stop and present the work for review before continuing. Nothing is "final" without explicit approval from Stanley.

---

## 1. Context

- **Business:** FITCare Support Services (fitcaresupportservices.com.au) — registered NDIS provider (RTO-partnered with FIT College), ~60 support workers servicing Sunshine Coast, Gympie, Moreton Bay and North Brisbane. Also offers aged care fitness supports.
- **Differentiator:** "Healthy support workers delivering healthy support work" — staff with health, fitness and wellbeing backgrounds. This verbal identity must survive the rebuild.
- **Why rebuild:** The current site has heavy content duplication, a confusing three-form conversion architecture, a 30-field referral wall, zero testimonials, one video, no audience segmentation, and no accessibility provisions. Full findings are in `fitcare-website-content-audit.md` in this folder — **read it in full before writing any code.** It is the source of truth for existing content, compliance must-carry-overs, and the redirect map.

## 2. Deliverable & stack

- **Multi-page static site**: semantic HTML, Tailwind CSS (via CDN or build — your choice, but keep the toolchain minimal), vanilla JS only where behaviour demands it. No React, no framework. Every component must be inspectable, copy-pasteable HTML/CSS that any developer can port to WordPress, Webflow, Laravel Blade or anything else.
- One shared CSS token file (colours, type scale, spacing, radii, shadows) and one shared JS file. Components must be visually consistent because they share tokens, not because styles are duplicated.
- All pages interlinked with working navigation. Forms are functional front-end only (validation, multi-step logic, success states) — no backend; submissions log to console and show the success state.
- Include a `README-FOR-DEVELOPER.md` explaining structure, tokens, components, form logic, and the 301 redirect map from the audit.

## 3. Brand & visual direction

- **Do not invent a palette.** Extract brand colours from the existing logo (`https://fitcaresupportservices.com.au/images/fit-care-support-services-logo-LARGE.png`) and current site assets. Then propose a modernised token set (primary, secondary, accent, neutrals, semantic states) derived from those brand colours and present swatches for approval **before** building any pages.
- **Aesthetic:** modern, contemporary, warm and energetic — closer to a premium health/wellness brand than a clinical care provider. Generous whitespace, large friendly type, rounded imagery, real photography over illustration. Avoid: corporate stock-photo sterility, NDIS-sector beige, and generic AI-startup gradients.
- Typography: one distinctive display face + one highly legible body face (system-adjacent or Google Fonts). Minimum 16px body, comfortable line-height — this audience skews toward users who benefit from clear, unfussy type.
- Motion: subtle and purposeful only. All animation must respect `prefers-reduced-motion`.

## 4. Audiences & journeys (this drives everything)

Three primary audiences with distinct needs. The IA, homepage and CTAs must let each self-select within seconds:

1. **Participants** — want to see people like them, activities, and an easy low-pressure way to start. Tone: warm, direct, second person, plain English.
2. **Families & carers** — want trust signals: qualifications, screening, safety, registration, testimonials from other families. Tone: reassuring, evidence-backed.
3. **Support coordinators** (major referral channel, currently unserved) — want speed: services and registration categories at a glance, service areas, capacity/availability signal, a fast referral pathway, and a downloadable referral pack. Tone: professional, efficient, zero fluff.

Secondary audience: **job seekers** (careers pathway, kept clearly separate from participant journeys).

## 5. Information architecture

```
Home
├── Services (hub)
│   ├── Daily Living Support          [landing page template]
│   ├── Social & Community Participation [landing page template]
│   ├── Health, Fitness & Wellbeing   [landing page template]
│   ├── Transport & Travel            [landing page template]
│   └── Aged Care Supports            [landing page template]
├── Service Areas (hub)
│   ├── Sunshine Coast                [landing page template]
│   ├── Gympie                        [landing page template]
│   ├── Moreton Bay                   [landing page template]
│   └── North Brisbane                [landing page template]
├── Our Team (support worker directory + profile template)
├── Activities (calendar/schedule page)
├── For Support Coordinators (dedicated page)
├── About (incl. registration categories, values, FIT College partnership)
├── Resources
│   ├── New to the NDIS (expanded from register-for-ndis + learn-more pages)
│   ├── FAQs
│   ├── News (index + article template)
│   ├── Feedback & Complaints
│   └── Participant Handbook (PDF link)
├── Careers
├── Get Started (multi-step enquiry/referral — the primary conversion flow)
└── Contact
Footer: Privacy, Terms, Members portal link, NDIS registration statement, accessibility statement
```

Build every page listed. Landing-page-template pages (services × 5, locations × 4) share one template with per-page content variation — build the template excellently once, then instantiate.

## 6. Landing page template (services & locations)

Each landing page follows this proven conversion structure:
1. **Hero:** benefit-led H1, one-sentence supporting line, primary CTA ("Get started") + click-to-call button, authentic photo/video.
2. **Trust bar:** Registered NDIS Provider badge/statement, "60+ local support workers", years operating, review rating placeholder.
3. **What we help with:** 3–6 concrete, plain-English support examples (not category codes).
4. **How it works:** 3 steps — Enquire → Meet & greet with a Service Coordinator → Matched with your support worker. (This process exists today — see FAQ content in audit.)
5. **Testimonial block** (component §7.2).
6. **Meet some of the team:** 3–4 support worker cards filtered to relevance, linking to profiles.
7. **Video block** (component §7.1) where relevant.
8. **FAQ accordion:** 3–5 page-specific questions (proper `<details>`/ARIA pattern).
9. **Final CTA band:** Get started + phone + "Refer a participant" link for coordinators.
Location pages additionally include: suburbs/regions served list, local activity highlights, embedded map placeholder.

## 7. Required components (build as a documented component library page at /components.html)

1. **Video block** — responsive 16:9 embed pattern supporting YouTube/Vimeo iframe and native `<video>`; poster image, accessible play control, lazy-loaded, captions track slot. Use the existing hero video URL and clearly-labelled placeholders elsewhere.
2. **Testimonial/review system** — (a) featured story card (photo, quote, name/relationship, optional video variant); (b) review carousel (accessible: buttons not just swipe, no auto-advance) with star ratings styled to accommodate a future Google Reviews feed; (c) short pull-quote band. All testimonial content is `[PLACEHOLDER — real testimonials pending consent programme]` and visibly watermarked as sample content.
3. **Support worker card + profile template** — photo, name, specialities/interests tags, short bio, "Request this support worker" action. Directory page with simple tag filtering (vanilla JS).
4. **Multi-step Get Started flow** — replaces the current 30-field wall. Step 1: who's enquiring (participant / family or carer / support coordinator / other) — routes tone and fields. Step 2: contact basics + preferred contact method (phone/email/SMS). Step 3 (optional, skippable): NDIS status, region, interests. Progress indicator, back navigation, "save time — call us instead" escape hatch on every step, explicit privacy reassurance line before any health-related field, success state confirming the 1-business-day promise. Sensitive fields (disability description, NDIS number, plan dates) are deferred to the meet-and-greet — collect the minimum needed to start a conversation.
5. **Activities schedule** — server-renderable HTML list/grid grouped by week with clean category tags (Fitness, Social, Creative, Outings), each activity as a card (image, day/time, location, description). Progressive-enhancement filter. Must be fully readable with JS disabled (fixes current SEO/accessibility failure).
6. **Click-to-call** — persistent, prominent `tel:` action in header on all viewports; sticky mobile bottom bar with Call + Get Started.
7. **Trust/compliance strip** — NDIS registration statement, registration category codes (exact codes in audit §3), Quality & Safeguards Commission reference, feedback & complaints link.
8. **Coordinator referral panel** — on the For Support Coordinators page: services + registration codes table, service area map, direct phone/email of intake, "Download referral pack (PDF)" placeholder, and a shortcut into the Get Started flow pre-set to the coordinator path.

## 8. Accessibility — hard requirements, not aspirations

Target **WCAG 2.2 AA** throughout. Non-negotiables: semantic landmarks and heading hierarchy; visible focus states everywhere; 4.5:1 minimum text contrast (verify the extracted brand palette and adjust shades if needed — flag any changes); full keyboard operability incl. carousel and multi-step form; labelled form fields with inline error messaging tied via `aria-describedby`; alt text on all images (no filename junk); skip-to-content link; `prefers-reduced-motion` respected; no information conveyed by colour alone. Include an Accessibility Statement page and add an accessibility notes section to the developer README. An NDIS provider's website failing accessibility is a brand failure — treat this as a first-class design constraint.

## 9. Content rules

- Reuse and improve the genuine copy inventoried in the audit — kill the triplicated nine-block content; each fact lives in one place.
- Preserve exactly: registration category codes, contact details (standardised to Suite 10, 102 Wises Road, Maroochydore QLD 4558), 1300 348 227, the brand tagline, FAQ substance, compliance pages.
- British/Australian spelling. Plain English (aim for reading grade ~7 on participant-facing pages). No prices anywhere.
- Anything invented (testimonials, review counts, video slots, stats not in the audit) must be visibly marked `[PLACEHOLDER]` — never let sample content pass as real.

## 10. Build phases (stop for review after each)

1. **Foundations:** read audit → extract palette → propose design tokens, type choices and one homepage design concept (single HTML page, no nav needed yet). STOP for approval.
2. **Component library:** /components.html with all §7 components built and documented. STOP.
3. **Core pages:** Home, Services hub + one service landing page, one location landing page, Get Started flow. STOP.
4. **Remaining instances & sections:** all other service/location pages, Team, Activities, Coordinators, About, Resources, Careers, Contact.
5. **Handoff pack:** developer README, redirect map, accessibility notes, placeholder-content register (everything the client must supply before launch).

## 11. Definition of done

A developer can open the folder and produce the production site without asking a single design question. Every page navigable, every component documented, every placeholder registered, accessibility verified, and the whole thing looks like a contemporary health-and-wellbeing brand — not a template, and not the 2023 site with new paint.
