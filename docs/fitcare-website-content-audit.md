# FITCare Support Services — Website Content Audit
**Site:** fitcaresupportservices.com.au | **Audited:** 3 July 2026
**Purpose:** Faithful content and structure inventory of the current site, as the starting point for a full rebuild. This document is the source of truth for what exists today, what must carry over, and where the gaps are.

---

## 1. Technical snapshot

- **Platform:** The site presents as a custom build — meta CSRF tokens on every page suggest a Laravel (or similar PHP framework) backend, while imagery hosted at `global-uploads.webflow.com` indicates the design originated in Webflow and was migrated or partially rebuilt. The footer still carries a Webflow attribution link. **The developer should confirm the actual stack before scoping.**
- **Copyright notice:** "Copyright 2023" — stale, signals neglect.
- **Tracking:** LinkedIn Insight pixel present (pid 6368148). No visible GA4/Meta pixel in extracted markup (may be in scripts — developer to verify before teardown so tracking continuity isn't lost).
- **Members portal:** Separate subdomain — `members.fitcaresupportservices.com.au/community/fitcare`. Out of rebuild scope but must remain linked.
- **SEO metadata:** Present on most pages but inconsistent. All Open Graph and Twitter card fields are **empty site-wide** — poor social sharing appearance. The Referral and FAQ pages have **no meta description at all**.
- **Assets:** One hero video on homepage (`/video/fitcare-web-edit.mp4`). Photography is a mix of genuine staff/participant photos and visible stock (shutterstock filenames). Some image filenames are junk strings (e.g. `ubcsbdkuhsjdhochjaygsyc.jpg`, `D6ACEC06-...jpg`) — no alt-text discipline in places, poor for accessibility and SEO.

---

## 2. Page inventory (sitemap)

| # | Page | URL | Purpose | Notes |
|---|------|-----|---------|-------|
| 1 | Home | `/` | Brand intro, service overview, CTAs | Hero video + 9-block "why FITCare" content |
| 2 | Services | `/services` | Service descriptions | Largely duplicates homepage content |
| 3 | About | `/about` | Registration credentials, mission | Lists NDIS registration categories |
| 4 | Service Areas | `/locations` | Region hub | Links to 4 sub-pages: Sunshine Coast, Gympie, North Brisbane, Moreton Bay |
| 5 | Location sub-pages | `/locations/{region}` | Regional landing pages | Exist but thin (hub shows image + enquire button only) |
| 6 | Careers | `/careers` | Recruitment + application form | Duplicates registration categories from About |
| 7 | Activities | `/activities` | Activity calendar | **JavaScript calendar — content invisible to static crawlers/search engines.** Tag filters: Fun, Fitness, Strength, Socialise, Lawn Bowls, Markets, Pottery, Games, Rides etc. (tags are messy/duplicated with case variants) |
| 8 | Find a Support Worker | `/book-a-support-worker` | Lead capture form | Primary conversion page |
| 9 | Referral / EOI | `/referral` | Detailed referral form | Secondary (deeper) conversion page |
| 10 | Contact | `/contact` | General enquiry form | Enquiry type: NDIS / Aged Care / Career / Other |
| 11 | Meet Our Support Workers | `/support-workers` | Team directory | 40+ individual profile pages (first-name URLs) |
| 12 | Register for NDIS | `/register-for-ndis` | NDIS onboarding help | Very thin — one paragraph + CTA |
| 13 | Learn about NDIS | `/learn-more-about-ndis` | NDIS education | Linked from homepage |
| 14 | One on One Supports | `/nutrition-advice` | Service detail | **URL/content mismatch** — labelled "One on One Supports" but URL says nutrition-advice |
| 15 | Wellness Programs | `/fitness-programs` | Service detail | Very thin — a few sentences + CTA |
| 16 | News & Resources | `/news` | Blog/news | In Resources dropdown |
| 17 | FAQs | `/faqs` | 8 Q&As | Good genuine content, buried in dropdown |
| 18 | Feedback & Complaints | `/feedback` | Compliance requirement | **Must carry over — NDIS Practice Standards** |
| 19 | Participant Handbook | `/storage/fitcare-participant-handbook.pdf` | Compliance document | PDF download in nav |
| 20 | Support Worker JD | `/storage/FITCare Support Worker JD.pdf` | Careers PDF | Linked from Careers |
| 21 | Terms & Conditions | `/terms` | Legal | Footer |
| 22 | Privacy Policy | `/privacy-policy` | Legal | Footer |
| 23 | Login / Password Reset | `/login`, `/password/reset` | Account access | Footer; relationship to members subdomain unclear |

---

## 3. Content by page (verbatim-faithful summary)

### Home
- **Hero:** Background video. H1: "Experience the Difference with Our Dedicated & Healthy Support Workers." CTAs: *Enquire Today* → contact; *Find a FITCare Support Worker* → team directory; *Become a FITCare Support Worker* → careers.
- **Intro block ("FITCare Support Services"):** Mission — person-centred services enhancing quality of life for people with disabilities on the Sunshine Coast and SEQ. CTA "Browse Services" (→ links to /about, not /services — mislink).
- **Nine content blocks:** Assistance with Daily Living / Increased Social & Community Participation / Improved Health and Wellbeing / Mentoring Change / Employer of Choice / (FITCare Community values: Quality, Respect, Adaptability, Person-Centred, Inclusion) / Aged Care Supports (yoga, pilates, chair aerobics, water-based fitness) / RTO Partnership with FIT College / Why FITCare.
- **"How FITCare can help you?" card grid:** One-on-one supports, Health & Wellbeing Activities, Wellness Programs, Social & Community Activities, Become an NDIS Participant (external → ndis.gov.au), Register for NDIS, Learn about NDIS.
- **Tagline used repeatedly:** *"healthy support workers delivering healthy support work"* — this is the brand's core verbal identity. Also: *"From everyday supports to training to become our next Olympian."*

### Services
- Intro: exceptional care for individuals of all abilities across South East Queensland; trusted NDIS provider; mission to empower clients to live fulfilling, independent lives.
- Same nine blocks as homepage with slightly expanded copy. Notable specifics: daily living includes household maintenance, gardening, errands, appointments. RTO partnership names the **CHCSS00130 Individual Support – Disability Skillset**.
- Bottom cards: NDIS Support Workers → book form; Book Aged Care Supports → contact.

### About
- Positions registration credentials: Registered NDIS Provider meeting quality and safeguards requirements.
- **Registered support categories (compliance-critical, must carry over exactly):**
  - *Core:* 0107 Assist Personal Activities; 0108 Transport and Travel Assistance; 0120 Household Tasks; 0125 Participation in Community, Social and Civic Activities; 0136 Group and Centre Based Activities.
  - *Capacity Building:* 0116 Innovative Community Participation; 0117 Development of Daily Living and Life Skills; 0125 Participation in Community, Social & Civic Activities; 0126 Exercise Physiology and Personal Training.
- Commitment statement: empowering individuals to achieve what they want out of life "by creating better access to all things!"
- Office: Suite 10, 102 Wises Road, Maroochydore QLD 4558. Phone 1300 348 227. Email info@fitcaresupportservices.com.au.

### Service Areas
- Regions: **Sunshine Coast** (office location listed), **Gympie**, **North Brisbane**, **Moreton Bay**. Each card → thin sub-page + "Enquire Now" → generic contact.
- FAQ page adds: 60+ support workers currently servicing Sunshine Coast, Moreton Bay and Gympie; expanding into parts of Brisbane and the Gold Coast.

### Careers
- Pitch: all staff share a passion for health and wellbeing; many from health & fitness backgrounds; "FITCare Community" provides training, resources and advancement.
- Job description PDF download. On-page application form ("Become a Support Worker / Mentor" — personal details).
- Duplicates the registered support categories block. Note: address on this page reads "2nd, 15, 102 Wises Road" — inconsistent with the Suite 10 address used elsewhere.

### Book a Support Worker (primary conversion page)
- Form: First/Last Name, Email, Phone, State (all 8 AU states — unnecessary given QLD-only service), enquiry type (NDIS / Aged Care / Other), message. Promise: response within 1 business day.
- Below-form content: "one stop shop" positioning; extensive screening and training program; person-centred customised programs. Then repeats the same nine content blocks a third time.

### Referral / Expression of Interest (deep conversion page)
- Long single-page form, 8 sections: applicant details (incl. DOB, address); third-party/representative details; **describe your disability(s)** (required free text); NDIS status (4 options) + NDIS number + plan dates; additional medical support needs; how supports are managed (Support Coordinator / Self / Plan Manager / Other) with full coordinator & plan manager contact fields; other team supports (Allied Health etc.); interests and services required.
- **This form collects sensitive health information — privacy/consent handling must be explicit in the rebuild.**

### Contact
- Same base form as Book a Support Worker plus "Career with FITCare" option. 1-business-day promise.

### Meet Our Support Workers
- 40+ profiles by first name (Allison, Anna, Ashli, Brigitte, Brooke, Bruce, Carissa, Dan… Priscila…), each with an individual page. Strong differentiator and trust asset; currently just a name grid with empty social-link placeholders.

### Register for NDIS
- One paragraph: FITCare works with great Support Coordinators and Plan Managers — "contact us and we can hook you up!" CTA → contact.

### Wellness Programs (/fitness-programs)
- Short: customised wellness program for individual goals; gym or activities; "find your fit" and make wellness FUN. CTA → contact.

### FAQs (8 questions — genuine, keep and expand)
1. Registered NDIS provider? Yes.
2. Difference from other providers: all staff passionate about health and wellbeing.
3. Qualifications: just over 50% of staff have fitness qualifications; also swimming and yoga instructors, football coaches, distance runners.
4. Service areas: 60+ support workers; Sunshine Coast, Moreton Bay, Gympie; expanding to Brisbane and Gold Coast.
5. No PT funding in plan: supports can be delivered via core and/or capacity building funding.
6. Fitness goals not required.
7. Getting started: fill out referral form → "meet and greet" arranged.
8. Meet and greet: with a Service Coordinator — first point of contact, matches support workers.

### Footer (site-wide)
- Four link columns (FITCare / Legal / Services / Account) + contact block with map link. Socials: Facebook, LinkedIn, Instagram. Members portal link.

---

## 4. Forms inventory

| Form | Page | Fields | Sensitivity |
|------|------|--------|-------------|
| General enquiry | /contact | Name, email, phone, state, enquiry type (4), message | Low |
| Support worker enquiry | /book-a-support-worker | Same minus career option | Low |
| Referral / EOI | /referral | ~30 fields incl. disability description, NDIS number, plan dates, medical needs, coordinator/plan-manager contacts | **High — health information** |
| Careers application | /careers | Personal details (+ JD PDF) | Medium |

---

## 5. Key findings — friction & gaps

**Conversion friction**
1. **Confusing dual-CTA architecture.** "Find A Support Worker" and "Referral Form" sit side-by-side in the nav with no explanation of which to use when. The FAQ says the referral form is the way to start; the homepage pushes contact/enquiry. Three overlapping entry points (contact, book, referral) with near-identical forms behind two of them.
2. **The referral form is a wall.** ~30 fields on one page with required disability disclosure before any relationship is established. No multi-step flow, no save-and-resume, no indication of time required, no reassurance about privacy.
3. **Dead-weight fields** — a State dropdown listing all of Australia for a QLD-only provider.
4. **No phone-first pathway prominence** — 1300 number is footer-only on most pages; for this audience (and for support coordinators moving fast), click-to-call should be a primary action.
5. **Generic CTAs everywhere** — nearly every button routes to the same contact form; location pages, service pages and register-for-NDIS all funnel to one undifferentiated form.

**Content gaps (directly against the rebuild goals)**
6. **Zero testimonials or reviews anywhere on the site.** No participant stories, no family quotes, no Google review integration. This is the single biggest missing trust element for an NDIS provider.
7. **One video, no video strategy.** A single hero video; the support-worker profiles, activities and participant stories are all natural video content with nowhere to live.
8. **Massive content duplication** — the same nine blocks appear on Home, Services and Book a Support Worker. Thin unique content on the pages that should rank (locations, service details, register-for-NDIS).
9. **Activities calendar is invisible** to search engines and likely difficult for assistive tech (JS-only, `javascript:void(0)` tag links, chaotic tags).
10. **Audience segmentation absent.** Participants, families/carers and support coordinators all get the same journey. Coordinators — who drive a large share of NDIS referrals — have no dedicated pathway, no referral pack, no service/vacancy info.

**Trust/compliance observations**
11. Registered provider status is stated but not evidenced — no NDIS registration number displayed, no "We support the NDIS" logo usage guidelines check, no Quality & Safeguards Commission link.
12. Feedback & Complaints page and Participant Handbook exist (good — required) but are buried in a dropdown.
13. No visible accessibility features: no font-size controls, no Easy Read versions, no accessibility statement. For a disability services provider this is a reputational as well as practical failure. Rebuild must target WCAG 2.2 AA minimum.
14. Inconsistent NAP (two address formats), stale copyright, empty OG metadata.

---

## 6. Must-carry-over checklist (compliance & equity)

- [ ] Registered NDIS Provider status + all registration category codes (Section 3 → About)
- [ ] Feedback & Complaints page (NDIS Practice Standards requirement) — promote, don't bury
- [ ] Participant Handbook PDF
- [ ] Privacy Policy & Terms (review/update for new forms; referral form collects health info)
- [ ] Support worker profiles (40+) — retain the asset, redesign the presentation
- [ ] Members portal link (subdomain untouched)
- [ ] 1300 348 227, info@ email, Maroochydore address (standardise to one format)
- [ ] LinkedIn pixel + any other tracking (verify full tag inventory pre-teardown)
- [ ] FAQ content (retain and expand)
- [ ] Careers JD PDF + application pathway
- [ ] Existing URL map → 301 redirect plan for the new information architecture (incl. fixing /nutrition-advice mislabel)
