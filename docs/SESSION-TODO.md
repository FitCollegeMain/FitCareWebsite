# Session To-Do List

Consolidated, prioritised list of everything left to take the approved prototype
to a production launch. Sourced from `docs/placeholder-register.md`,
`README-FOR-DEVELOPER.md` §10 (pre-launch checklist) and the current state of
`site/`. Owner column: **C** = client (FITCare), **D** = developer, **C+D** = both.

> Prototype status: Phases 1–5 approved & delivered (3 Jul 2026). No open PRs.
> The launch gate is an **empty placeholder register** — nothing sample ships.

---

## P0 — Launch blockers (must be done before go-live)

### Developer (technical)
- [ ] **Wire the 4 form backends** — get-started, careers, contact, feedback. Swap-in
      points are marked in `site/js/site.js` (`Backend swap-in point`). Add server-side
      validation, spam protection (honeypot/turnstile — no visual CAPTCHA), and intake
      email notifications. *(D)*
- [ ] **Implement the 301 redirect map** (`docs/redirect-map.md`) at the host/server level
      before DNS cutover; spot-check the top 20 URLs from Search Console post-launch. *(D)*
- [ ] **Export the old support-worker slug list** from the current site for per-profile
      301s (`/support-workers/{name}` → `/team/{name}`). *(D)*
- [ ] **Resolve the YouTube `UC…` channel ID** for `@fitcaresupportservices` and stand up
      the server-side RSS feed cache (hourly, stale-on-error fallback). Spec in
      README-FOR-DEVELOPER §8b. *(D)*
- [ ] **Verify the full tag inventory** on the old site before teardown; carry over the
      LinkedIn Insight pixel (pid 6368148); make the GA4 decision. *(C+D)*
- [ ] **Fill the two remaining stub pages** — `site/privacy.html` and `site/terms.html`
      — once legal copy is supplied. *(C legal → D)*
- [ ] Generate the **favicon set** from the leaf mark. *(D)*
- [ ] Add **`sitemap.xml`, `robots.txt`, canonical URLs, OG images**, and LocalBusiness /
      organisation structured data on contact/about. *(D)*

### Client (compliance & legal)
- [ ] **Privacy Policy** updated for the new forms (enquiry/careers/feedback collect
      personal info; the flow deliberately avoids health info). *(C legal)*
- [ ] **Terms & Conditions** reviewed and republished. *(C legal)*
- [ ] **NDIS registration number** supplied for display on About + footer. *(C)*
- [ ] Confirm **"We support the NDIS" logo usage** against current guidelines. *(C)*
- [ ] Provide **internal complaints-handling timeframes** (acknowledgement / resolution)
      for the feedback page success copy. *(C)*
- [ ] Provide **vehicle/insurance policy wording** for the transport-supports page note. *(C)*
- [ ] Confirm **participant consent is on file** for the home hero and every participant
      photo. *(C)*

---

## P1 — Content the client must supply (swap placeholder chips as they land)

Placeholder chips still live on these pages (counts from current `site/`):
coordinators (5), services (5 total across the 4 pages), 4 location pages (4 each),
resources/news (4), home (4), team/profile templates, activities, careers, contact,
feedback, accessibility.

- [ ] **Service page heroes** — training session, daily-living, transport, aged-care class
      (Social & Community already delivered). *(C)*
- [ ] **Location heroes** — one genuine local shot per region ×4. *(C)*
- [ ] **Support worker portraits** — remaining 39+ to the Brooke standard (black polo,
      plain background). *(C)*
- [ ] **Support worker bios** (60–90 words, own voice) + speciality tags + availability. *(C)*
- [ ] **Real activities schedule** — names, days, times, venues, mapped to the 4 categories
      (Fitness / Social / Creative / Outings). *(C)*
- [ ] **Suburb coverage lists** per region (all 4 location pages). *(C)*
- [ ] **Capacity indicators** per region + an owner/cadence for updates (recommend monthly,
      intake team). *(C)*
- [ ] **Referral pack PDF** (categories, areas, intake contacts, blank referral summary). *(C+D)*
- [ ] **Migrate existing `/news` posts** into the article template. *(C+D)*
- [ ] **Testimonials programme** — consent process, 1 featured story, 4–6 short reviews for
      the carousel. The single biggest missing trust element. *(C)*
- [ ] **Team/group shot** for careers. *(C)*
- [ ] Carry over the **Participant Handbook PDF** at the same path. *(D)*
- [ ] Descriptive **alt text** on every real image at upload (no filename junk). *(C+D)*

---

## P2 — Recommended enhancements (post-launch OK)

- [ ] **Accessibility re-audit** on the production build (axe + manual keyboard + screen
      reader); record known limitations on `/accessibility`; add captions to all video. *(D)*
- [ ] **Easy Read versions** of key pages (Home, Get Started, Feedback). *(D)*
- [ ] **Google Reviews feed** decision — carousel is API-shape-ready; needs Places API key
      + place ID if wanted. *(C+D)*
- [ ] Swap Unsplash activity-card stock for **genuine FITCare activity shots** when captured. *(C)*
- [ ] Supply a **higher-resolution original** for the activities hero (current source 206px). *(C)*
- [ ] Vector **logo SVG** for print/production (transparent PNG already live). *(C)*
- [ ] Confirm **members portal link** and keep
      `members.fitcaresupportservices.com.au/community/fitcare` untouched. *(D)*

---

## Definition of done

Per the sign-off rule: an item leaves the register only when its real content is
**live** *and* the amber placeholder chip is removed from the page. Launch when the
placeholder register is empty and every P0 box above is checked.
