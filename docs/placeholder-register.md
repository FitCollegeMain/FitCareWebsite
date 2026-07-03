# Placeholder Content Register

Everything the client (FITCare) must supply — or decide — before launch.
Every item below is visibly flagged in the prototype with an amber
`SAMPLE CONTENT` / `[PLACEHOLDER]` chip; nothing sample can accidentally pass
as real. Owner column: **C** = client, **D** = developer, **C+D** = both.

## 1. Brand assets

| Item | Where it's used | Owner |
|---|---|---|
| ~~Logo~~ **DELIVERED 3 Jul 2026** — transparent PNG (4344px original in `assets/img/originals/`, web versions `logo.png` + all-white `logo-white.png` live in header/footer). Vector SVG still preferred for print/production if available. | header + footer on every page | ✔ |
| Favicon set generated from the leaf mark | site-wide | D |

## 2. Photography & video

| Item | Where | Owner |
|---|---|---|
| ~~Home hero photo~~ **DELIVERED & LIVE 3 Jul 2026** — coastal-lookout selfie embedded at `assets/img/hero-lookout-selfie.jpg`. **Confirm participant consent is on file** for this and every participant photo. | home | ✔ / consent: C |
| Service page heroes — **Social &amp; Community DELIVERED** (boat-outing photo, live). Still needed: training session, daily-living, transport, aged-care class. | 4 remaining service pages | C |
| Location heroes: one genuine local shot per region (×4) | location pages | C |
| Support worker portraits — **standard set &amp; first portrait LIVE 3 Jul 2026** (Brooke, black FITCare polo on plain background, `assets/img/team/brooke.jpg`). Remaining 39+ portraits to the same standard. | team directory + profiles + team sections | C |
| Activities photo **DELIVERED** (beach selfie, live on Activities) — source is 206px; supply a higher-resolution original if one exists. | activities | C |
| Activity photos (one per recurring activity) | activities + home + location highlights | C |
| Team/group shot | careers | C |
| Every image needs descriptive alt text at upload — no filename junk | site-wide | C+D |

## 3. Testimonials & reviews (the site's biggest missing trust element)

| Item | Notes | Owner |
|---|---|---|
| Consent programme for participant/family stories | written consent, photo optional, withdrawal process | C |
| 1 featured story (quote + name/relationship + photo or video) | home + story card component | C |
| 4–6 short reviews for the carousel | service/location pages | C |
| Google Reviews feed decision | carousel is API-shape-ready; needs Places API key + place ID if wanted | C+D |

## 4. Content & data

| Item | Where | Owner |
|---|---|---|
| Real activities schedule (names, days, times, venues) mapped to the 4 categories (Fitness/Social/Creative/Outings) | activities page | C |
| Support worker bios (60–90 words, own voice) + speciality tags + availability status | team profiles | C |
| Suburb coverage lists per region (marked placeholder on all 4 location pages) | location pages | C |
| Capacity indicators per region + an owner/cadence for updating them (recommend monthly, intake team) | coordinators page | C |
| Referral pack PDF (categories, areas, intake contacts, blank referral summary) | coordinators page | C+D |
| News: migrate existing `/news` posts into the article template | resources/news | C+D |
| Existing support-worker slug list exported from old site (for per-profile 301s) | redirect map | D |

## 5. Compliance & legal

| Item | Notes | Owner |
|---|---|---|
| NDIS registration number displayed on About + footer | flagged on About page | C |
| "We support the NDIS" logo usage confirmed against current guidelines | audit §5.11 | C |
| Privacy Policy — updated for the new forms (enquiry, careers, feedback collect personal info; the flow deliberately avoids health info) | /privacy (stub) | C (legal) |
| Terms & Conditions — reviewed and republished | /terms (stub) | C (legal) |
| Internal complaints-handling timeframes (acknowledgement/resolution) | feedback page success copy | C |
| Vehicle/insurance policy wording for transport supports | transport page note | C |
| Participant Handbook PDF carried over at same path | footer/resources | D |

## 6. Technical (developer)

| Item | Notes |
|---|---|
| Form backends for all 4 forms (get-started, careers, contact, feedback) + intake email notifications + spam protection | swap-in points marked in `js/site.js` |
| Full tag inventory of the old site verified before teardown; LinkedIn Insight pixel (pid 6368148) carried over; GA4 decision | audit §1 |
| 301 map implemented (`docs/redirect-map.md`) and spot-checked post-launch | |
| Accessibility re-audit on the production build; known limitations recorded on `/accessibility` | |
| Easy Read versions of key pages (Home, Get Started, Feedback) | recommended post-launch enhancement |
| `sitemap.xml`, `robots.txt`, canonical URLs, OG images, LocalBusiness structured data | |

## Sign-off rule

An item leaves this register only when its real content is live **and** the
amber placeholder chip is removed from the page. The launch gate is an empty
register — nothing sample ships.
