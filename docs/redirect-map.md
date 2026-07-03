# 301 Redirect Map — fitcaresupportservices.com.au

Source: page inventory in `fitcare-website-content-audit.md` §2 (23 URL groups).
Implement as **301 (permanent)** redirects at the server/host level, live from the
moment the new site deploys. URLs below are clean production paths; adapt to the
final routing scheme.

## Page redirects

| # | Old URL | New URL | Notes |
|---|---------|---------|-------|
| 1 | `/` | `/` | — |
| 2 | `/services` | `/services/` | hub retained |
| 3 | `/about` | `/about` | — |
| 3a | `/why-fitcare` | `/about` | legacy URL seen in the wild |
| 4 | `/locations` | `/locations/` | hub retained |
| 5 | `/locations/sunshine-coast` | `/locations/sunshine-coast` | same slug |
| 5a | `/locations/gympie` | `/locations/gympie` | same slug |
| 5b | `/locations/moreton-bay` | `/locations/moreton-bay` | same slug |
| 5c | `/locations/north-brisbane` | `/locations/north-brisbane` | same slug |
| 6 | `/careers` | `/careers` | — |
| 7 | `/activities` | `/activities` | calendar now server-rendered HTML |
| 8 | `/book-a-support-worker` | `/get-started` | replaced by multi-step flow |
| 9 | `/referral` | `/get-started?who=coordinator` | 30-field form retired; sensitive data now collected at meet & greet |
| 10 | `/contact` | `/contact` | — |
| 11 | `/support-workers` | `/team/` | directory |
| 11a | `/support-workers/{first-name}` (40+ pages) | `/team/{first-name}` | once profiles migrate; interim fallback `/team/`. Export the exact slug list from the old site before teardown. |
| 12 | `/register-for-ndis` | `/resources/new-to-the-ndis` | merged |
| 13 | `/learn-more-about-ndis` | `/resources/new-to-the-ndis` | merged |
| 14 | `/nutrition-advice` | `/services/health-fitness-wellbeing` | fixes the audit's URL/content mismatch ("One on One Supports" at a nutrition URL) |
| 15 | `/fitness-programs` | `/services/health-fitness-wellbeing` | "Wellness Programs" content absorbed |
| 16 | `/news` | `/resources/news` | migrate posts; per-post redirects once slugs are known |
| 17 | `/faqs` | `/resources/faqs` | — |
| 18 | `/feedback` | `/resources/feedback-complaints` | compliance page — must never 404 |
| 21 | `/terms` | `/terms` | — |
| 22 | `/privacy-policy` | `/privacy` | — |

## Assets — carry over at identical paths (no redirect needed)

| Old path | Action |
|---|---|
| `/storage/fitcare-participant-handbook.pdf` | copy file to same path (linked from footer + resources) |
| `/storage/FITCare Support Worker JD.pdf` | copy file to same path (linked from careers) |
| `/video/fitcare-web-edit.mp4` | copy (re-edited + captioned version preferred — see placeholder register) |

## Needs a client/developer decision

| Old URL | Question |
|---|---|
| `/login`, `/password/reset` | Audit found the relationship to `members.fitcaresupportservices.com.au` unclear. If accounts live on the members subdomain, 301 both to `https://members.fitcaresupportservices.com.au/community/fitcare`; otherwise confirm what these serve before redirecting. |

## Verification

After deploy: crawl the old sitemap + top landing pages from Search Console,
confirm every old URL answers 301 → 200 (no chains, no 404s), then submit the
new sitemap. The Feedback & Complaints and Participant Handbook URLs are
compliance-critical — verify those two by hand.
