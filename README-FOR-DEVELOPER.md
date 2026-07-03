# FITCare Support Services — Developer Handoff

This folder is the definitive reference for the production build of
fitcaresupportservices.com.au. It is a complete, navigable, accessibility-verified
prototype: your job is translation to your stack, not interpretation.
If a design question comes up, the answer is on a page in `site/` or in this document.

**Companion documents**
- `docs/fitcare-website-content-audit.md` — what the old site contained; compliance must-carry-overs
- `docs/PROJECT-BRIEF.md` — the original build brief
- `docs/redirect-map.md` — the full 301 map (also summarised in §7 below)
- `docs/placeholder-register.md` — every piece of content the client must supply before launch
- `docs/mini-brand-guide-fitcare.pdf` — official brand (blue `#1E4689`, black, white)

---

## 1. Quick start

Open `site/index.html` in a browser. Everything works from `file://` — no server,
no build step, no dependencies. Test with JavaScript disabled too: every page
remains readable and navigable (JS is progressive enhancement only).

The HTML pages are generated from `tools/build_pages.py` + `tools/pages_phase4.py`
(header/footer/nav live in one place). The committed HTML is the deliverable —
you never need to run Python. If you do want to regenerate:
`python3 tools/build_pages.py && python3 tools/pages_phase4.py` from the repo root.

## 2. Architecture

```
site/
  css/tokens.css     ← ALL design decisions (colours, type, spacing, radii, shadows, dark theme)
  css/site.css       ← every component style; reads tokens only, no raw colour values
  js/site.js         ← the one JS file: video facade, carousel, filters, multi-step flow, simple forms
  assets/fonts/      ← self-hosted woff2 (see §4)
  *.html             ← plain semantic HTML; copy-paste any component into any stack
  components.html    ← the documented component library (self-contained file)
```

Rules the prototype follows and production must keep:
- **Components are consistent because they share tokens**, not because styles are
  duplicated. Change a colour once in `tokens.css`, it changes everywhere.
- Pages use semantic landmarks (`header/nav/main/footer`), one `h1` per page,
  ordered headings, and a skip link — preserve this structure when templating.
- Every interactive behaviour is a `data-*` attribute hook (`data-gs`, `data-carousel`,
  `data-filter-group`, `data-video`, `data-simple-form`) — port the JS as-is or
  re-implement per hook; the markup contract is the attribute.

## 3. Design tokens (approved 3 Jul 2026)

Full set in `site/css/tokens.css`. The load-bearing values:

| Token | Value | Use | Contrast |
|---|---|---|---|
| Brand blue `--primary-600` | `#1E4689` | buttons, links, headlines accents | 9.2:1 on white |
| `--primary-800` | `#16345F` | bands, button hover | 12.4:1 |
| `--primary-500` | `#2E62B8` | focus rings | 5.9:1 |
| Sun accent `--sun-400` | `#FFB528` | highlights, script accents (sparingly) | ink on it: 10.1:1 |
| `--ink` | `#111826` | headings | 17.8:1 |
| `--body-c` | `#3D4657` | body text | 9.5:1 |
| `--muted` | `#5A6478` | secondary text | 6.0:1 |
| `--error` | `#B42318` | form errors | 6.6:1 |

Dark theme: tokens are redefined under `@media (prefers-color-scheme: dark)` and
`:root[data-theme="dark"]` — style through tokens and dark mode is free.
Type scale: body minimum 17px/1.7; display sizes are `clamp()`-fluid.

## 4. Fonts

Approved free stand-ins for the licensed brand faces (Bilo / Gardenisa):

| Role | Face | Weights used | Licence |
|---|---|---|---|
| Display | Bricolage Grotesque (variable) | 600, 800 | OFL |
| Body | Figtree (variable) | 400, 600, 800 | OFL |
| Script | Dancing Script | 600 — wordmark + tagline band ONLY | OFL |

Self-host the woff2 files in `site/assets/fonts/` (already subset to latin).
Do not substitute Inter/Roboto "equivalents" — the pairing is a brand decision.
The script face is never used for body copy or below ~28px.

## 5. Components

`site/components.html` documents all eight components with dev notes. Inventory:
video facade (lazy player injection), testimonial system (story card / carousel /
pull-quote band), worker card + directory filter + profile template, multi-step
Get Started flow, activities schedule, click-to-call (header chip + mobile sticky
bar), trust/compliance strip, coordinator referral panel.

Non-negotiable behaviours:
- Carousel: buttons (no swipe-only), **no auto-advance**, position announced via `aria-live`.
- Video: nothing loads until the user clicks play; all produced video ships with captions.
- Filters and schedule: full content in HTML, filtering is enhancement (the old
  site's JS-only calendar was invisible to search engines — do not regress this).
- Testimonials: every quote carries the `chip--sample` watermark until replaced
  with consented content. Remove per-item, never globally.

## 6. Form logic

**Get Started (`get-started.html`, `[data-gs]`)** — the primary conversion flow.
- Step 1 (who) → routes step-2 heading/fields and success copy; coordinators get
  an organisation field. Deep link: `?who=participant|family|coordinator` pre-answers
  step 1 (used by the coordinator panel and audience cards). `?worker=<slug>` is
  reserved for "Request this support worker".
- Step 2: requires name + (phone OR email). Step 3 is optional and skippable.
- **Privacy by design:** the flow never asks for disability description, NDIS number
  or plan dates — those are collected at the meet & greet. Do not add fields
  without a privacy review; this fixes the old 30-field referral wall.
- Validation is per-step; errors inline next to the field; focus moves to the first
  invalid control. Success state confirms the 1-business-day promise.

**Simple forms (`[data-simple-form]`)** — careers, contact, feedback. Same inline
validation pattern; success panel replaces fields.

**Backend swap-in:** both handlers end at a marked `console.log` in `js/site.js`
(`Backend swap-in point`). POST the logged payload shape to your endpoint there.
Add server-side validation, spam protection (honeypot/turnstile — no visual
CAPTCHAs), and email notifications to intake. Referral/enquiry data is personal
information — transmit and store per the Privacy Policy (see placeholder register).

## 7. 301 redirect map (summary — full table in docs/redirect-map.md)

Implement as 301s at the web-server/host level before DNS cutover. Shown with
clean production URLs; map to your routing (the prototype uses `.html`).

| Old URL | New URL |
|---|---|
| `/` | `/` |
| `/services` | `/services/` |
| `/about`, `/why-fitcare` | `/about` |
| `/locations` | `/locations/` |
| `/locations/{region}` | `/locations/{region}` (same slugs) |
| `/careers` | `/careers` |
| `/activities` | `/activities` |
| `/book-a-support-worker` | `/get-started` |
| `/referral` | `/get-started?who=coordinator` |
| `/contact` | `/contact` |
| `/support-workers` | `/team/` |
| `/support-workers/{name}` (40+) | `/team/{name}` once profiles migrate; else `/team/` |
| `/register-for-ndis` | `/resources/new-to-the-ndis` |
| `/learn-more-about-ndis` | `/resources/new-to-the-ndis` |
| `/nutrition-advice` (mislabelled "One on One Supports") | `/services/health-fitness-wellbeing` |
| `/fitness-programs` | `/services/health-fitness-wellbeing` |
| `/news` | `/resources/news` |
| `/faqs` | `/resources/faqs` |
| `/feedback` | `/resources/feedback-complaints` |
| `/terms` | `/terms` |
| `/privacy-policy` | `/privacy` |
| `/storage/*.pdf` | keep paths — carry the PDFs over unchanged |
| `/login`, `/password/reset` | → members portal (confirm with client; see audit §2 note) |

Keep `members.fitcaresupportservices.com.au/community/fitcare` untouched and linked
from the footer.

## 8. Accessibility — WCAG 2.2 AA (preserve, don't regress)

Implemented and verified in this prototype:
- Semantic landmarks, ordered headings, skip-to-content link on every page
- Visible `:focus-visible` ring (3px, `--focus`) on all interactive elements
- All text combinations ≥ 4.5:1 (values in §3); no information by colour alone
- Full keyboard operability: nav, accordions (native `<details>`), carousel buttons,
  filters (`aria-pressed`), multi-step form (focus moves to each step's heading)
- Form fields labelled; errors as visible text adjacent to the field
- `prefers-reduced-motion` kills all transitions/animations globally
- Body text ≥ 17px; participant-facing copy aims at reading grade ~7
- Alt text conventions on all media placeholders — real photos MUST get descriptive
  alt text (no filename junk; the old site had `ubcsbdkuhsjdhochjaygsyc.jpg`)
- Everything works with JavaScript disabled

Before launch: re-run an audit on the production build (axe + manual keyboard +
screen reader pass), record known limitations on `/accessibility`, add captions
to all video, and consider Easy Read versions of key pages (recommended, see
placeholder register).

## 9. SEO & analytics notes

- Every page ships unique `<title>`, `meta description` and OG tags (the old site
  had empty OG fields site-wide). Add: canonical URLs, favicon set, `sitemap.xml`,
  `robots.txt`, and LocalBusiness/organisation structured data on contact/about.
- Carry over the LinkedIn Insight pixel (pid 6368148) and **verify the full tag
  inventory on the old site before teardown** (audit §1) so tracking continuity
  isn't lost. Add GA4 if the client wants it — get consent handling right.
- Update copyright year dynamically. The old site's said 2023.

## 10. Pre-launch checklist

1. All items in `docs/placeholder-register.md` supplied and swapped in
2. Real logo SVG in header/footer (currently a live-text recreation)
3. Forms wired to backend + notifications + spam protection tested
4. 301 map implemented and spot-checked (top 20 URLs from Search Console)
5. Accessibility re-audit on production build
6. NDIS registration number displayed; "We support the NDIS" logo usage confirmed
7. Privacy Policy & Terms updated for the new forms and republished
8. PDFs carried over at same paths; members portal link verified
9. OG images set; sitemap submitted; analytics verified live
