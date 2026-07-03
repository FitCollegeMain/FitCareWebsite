#!/usr/bin/env python3
"""FITCare prototype — Phase 4 pages.

All remaining IA pages: service instances, location instances + hub,
team directory + profile template, activities, coordinator hub, about,
resources, careers, contact, accessibility statement.

Run from the repo root (after/with build_pages.py):

    python3 tools/build_pages.py
    python3 tools/pages_phase4.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_pages as bp

LEAF, PHONE, STARS5 = bp.LEAF, bp.PHONE, bp.STARS5

# --------------------------------------------------------------------------
# reusable body builders
# --------------------------------------------------------------------------

def hero_page(eyebrow, h1, sub, media_label, aside="", img=None, img_alt=""):
    if img:
        media = ('<div class="media media--hero"><img class="media-img" src="%s" alt="%s"></div>'
                 % (img, img_alt))
    else:
        media = ("""<div class="media media--hero" role="img" aria-label="Placeholder photo">
      <svg class="leaf-bg" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 21C3 9 9 3 21 3 21 15 15 21 3 21Z" fill="currentColor"/></svg>
      <div class="media-label"><strong>Placeholder</strong>%s</div>
    </div>""" % media_label)
    return """
<section class="hero hero--page">
  <div class="wrap">
    <div class="hero-copy">
      <span class="eyebrow">LEAF %s</span>
      <h1>%s</h1>
      <p class="hero-sub">%s</p>
      <div class="hero-ctas">
        <a class="btn btn--primary" href="@/get-started.html">Get started</a>
        <a class="btn btn--ghost" href="tel:1300348227">PHONE Call 1300 348 227</a>
      </div>
      %s
    </div>
    %s
  </div>
</section>""" % (eyebrow, h1, sub, aside, media)

def what_we_help(title, sub, cards):
    c = "".join("<div class=\"svc\"><h3>%s</h3><p>%s</p></div>" % (t, d) for t, d in cards)
    return """
<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF What we help with</span>
      <h2>%s</h2>
      <p>%s</p>
    </div>
    <div class="svc-grid">%s</div>
  </div>
</section>""" % (title, sub, c)

def how_it_works(note=""):
    n = ""
    if note:
        n = """<div class="steps-note">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
      <span>%s</span>
    </div>""" % note
    return """
<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF How it works</span>
      <h2>Three easy steps to the right support worker</h2>
    </div>
    STEPS
    %s
  </div>
</section>""" % n

def faq_section(title, faq_html):
    return """
<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head sec-head--center">
      <span class="eyebrow">LEAF Good to know</span>
      <h2>%s</h2>
    </div>
    %s
  </div>
</section>""" % (title, faq_html)

def carousel_section():
    return """
<section class="section" aria-label="Reviews">
  <div class="wrap">
    <div class="sec-head sec-head--center">
      <span class="eyebrow">LEAF What people say</span>
      <h2>Don't take our word for it</h2>
    </div>
    REVIEW_CAROUSEL
  </div>
</section>"""

def team_section(sub):
    return """
<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF Meet some of the team</span>
      <h2>Support workers who get it</h2>
      <p>%s <span class="chip chip--sample">Sample presentation</span></p>
    </div>
    <div class="team-grid">
      TEAM_CARDS
    </div>
    <p style="margin-top:22px"><a href="@/team/index.html"><strong>See the whole team →</strong></a></p>
  </div>
</section>""" % sub

def service_body(eyebrow, h1, sub, media_label, ww_title, ww_sub, cards, note, faq_html, cta, img=None, img_alt=""):
    return (hero_page(eyebrow, h1, sub, media_label, img=img, img_alt=img_alt)
            + "\nTRUST_BAR\n"
            + what_we_help(ww_title, ww_sub, cards)
            + how_it_works(note)
            + carousel_section()
            + faq_section("Questions about this support", faq_html)
            + cta)

# --------------------------------------------------------------------------
# service instances
# --------------------------------------------------------------------------

DAILY_LIVING = service_body(
    "Services · Daily living support",
    'The everyday, sorted <span class="hl">your way.</span>',
    "Reliable help with the things every day needs — done how you like them, by people you actually like having around.",
    "Photo — support worker and participant cooking / gardening together (consent required)",
    "A hand where you want one",
    "You stay in charge — we bring the energy and the extra pair of hands.",
    [("Personal care", "Respectful, reliable support with daily personal activities — always on your terms."),
     ("Household tasks", "Cleaning, laundry, dishes and the jobs that pile up during a busy week."),
     ("Gardening &amp; maintenance", "Keeping your outdoor space something to enjoy, not stress about."),
     ("Errands &amp; shopping", "Groceries, post office, chemist — done together or done for you."),
     ("Appointments", "Getting there on time, every time — with company if you want it."),
     ("Life skills", "Cooking, budgeting, routines — building the skills for more independent living.")],
    "<strong>Delivered under our registered supports</strong> — personal activities (0107), household tasks (0120) and daily living &amp; life skills development (0117).",
    bp.faq([
        ("Can I choose how and when support happens?",
         "Yes — that's the point. Your supports are built around your routine and preferences at the meet &amp; greet, and they flex when life changes."),
        ("Can I keep the same support worker?",
         "We match you with workers who fit, and consistency is the goal. If it's ever not working, we'll rematch — no fuss, no awkwardness."),
        ("What funding covers daily living support?",
         "Usually your core funding. Life-skills development can also be delivered through capacity building. Bring your plan to the meet &amp; greet and we'll walk through it."),
        ("How do I get started?",
         "Call 1300 348 227 or use the Get Started form. We'll set up a relaxed meet &amp; greet with a Service Coordinator."),
    ]),
    bp.cta_final("Ready for easier days?",
                 "Tell us a little about you — or call and chat it through. We'll reply within one business day."))

SOCIAL_COMMUNITY = service_body(
    "Services · Social &amp; community participation",
    'Get out there. <span class="hl">We\'re coming too.</span>',
    "Sport, events, groups and outings with support workers who genuinely love being out and about — because a good week has people in it.",
    "Photo — group activity or community outing (consent required)",
    "More people, more places, more often",
    "From weekly groups to one-on-one outings — whatever social looks like for you.",
    [("Group activities", "Lawn bowls, games afternoons, group fitness — see the weekly calendar."),
     ("Outings &amp; events", "Markets, movies, concerts, footy games — out in the community, doing real things."),
     ("Sport &amp; recreation", "Join a team, learn a sport, or just have a kick with someone keen."),
     ("Life skills coaching", "Confidence for public transport, ordering, budgeting a day out — learned by doing."),
     ("Making connections", "Meet people with shared interests through our activities and groups."),
     ("One-on-one time", "Groups aren't for everyone — your support worker plans outings around you.")],
    "<strong>Delivered under our registered supports</strong> — community, social and civic participation (0125), group and centre-based activities (0136) and innovative community participation (0116).",
    bp.faq([
        ("What activities are on?",
         "There's something on every week — fitness, social, creative and outings. Check the <a href=\"@/activities.html\">activities calendar</a> or ask your Service Coordinator."),
        ("Do I have to join a group?",
         "No. Plenty of participants prefer one-on-one outings. Your support worker plans around what you enjoy."),
        ("Can FITCare help me get there?",
         "Yes — transport and travel assistance (0108) is one of our registered supports, so getting there is part of the plan."),
        ("How do I get started?",
         "Call 1300 348 227 or use the Get Started form. We'll set up a relaxed meet &amp; greet with a Service Coordinator."),
    ]),
    bp.cta_final("Your community's waiting",
                 "Tell us what a good week looks like — or call and chat it through. We'll reply within one business day."),
    img="@/assets/img/story-boat-outing.jpg",
    img_alt="A FITCare support worker and participant sit arm in arm, smiling, on a boat cruising calm coastal waters with waterfront homes behind them")

TRANSPORT = service_body(
    "Services · Transport &amp; travel",
    'Places to be? <span class="hl">Let\'s go.</span>',
    "Appointments, activities, work or the beach — reliable transport support that keeps your week moving.",
    "Photo — support worker and participant arriving somewhere good (consent required)",
    "Wherever the day takes you",
    "It's more than a lift — it's company, confidence and a plan.",
    [("Appointments", "Medical, allied health, NDIS meetings — on time, with support if you want it."),
     ("Activities &amp; events", "Getting to the calendar's best bits — groups, outings and events."),
     ("Work &amp; study", "Dependable transport for the commitments that matter most."),
     ("Shopping &amp; errands", "The weekly shop and life admin, sorted together."),
     ("Travel confidence", "Learning routes and public transport with someone beside you, until you don't need them there."),
     ("Social visits", "Family, friends, community — staying connected across town.")],
    "<strong>Delivered under our registered supports</strong> — transport and travel assistance (0108). <span class=\"chip chip--sample\">[PLACEHOLDER — confirm vehicle/insurance policy wording with FITCare before launch]</span>",
    bp.faq([
        ("Who does the driving?",
         "Your FITCare support worker. Travel is planned with you — where, when and how often."),
        ("Can transport combine with other supports?",
         "Absolutely — most participants pair it with community participation or daily living support so the whole outing is covered."),
        ("Can you help me learn to travel independently?",
         "Yes. Travel training is one of our favourite capacity building supports — building routes and confidence at your pace."),
        ("How do I get started?",
         "Call 1300 348 227 or use the Get Started form. We'll set up a relaxed meet &amp; greet with a Service Coordinator."),
    ]),
    bp.cta_final("Let's get you moving",
                 "Tell us where you need to be — or call and chat it through. We'll reply within one business day."))

AGED_CARE = service_body(
    "Services · Aged care supports",
    'Stay active. <span class="hl">Stay you.</span>',
    "Gentle, fun fitness supports for older Queenslanders — yoga, pilates, chair aerobics and water-based fitness with people who make it a highlight of the week.",
    "Photo — aged care fitness class (consent required)",
    "Movement that feels good",
    "Group classes or one-on-one — always at your pace, always with a laugh.",
    [("Yoga", "Gentle strength, balance and calm — no experience needed."),
     ("Pilates", "Core strength and mobility, adapted to every body."),
     ("Chair aerobics", "A proper workout from the comfort of a chair — seriously good fun."),
     ("Water-based fitness", "Low-impact aqua sessions that are easy on joints and big on energy."),
     ("One-on-one wellness", "A personal program built around your health goals and your GP's advice."),
     ("Social connection", "Classes are half the fitness, half the friendships.")],
    "<strong>Not an NDIS service</strong> — our aged care supports sit alongside our NDIS work. Get in touch and we'll talk through options for you or your loved one.",
    bp.faq([
        ("Is this part of the NDIS?",
         "No — these supports are for older adults outside the NDIS. FITCare delivers them with the same healthy-support-work approach as our NDIS services."),
        ("Do I need to be fit to join?",
         "Not at all. Every class is adapted to the people in the room — the only requirement is turning up."),
        ("Can sessions be one-on-one?",
         "Yes. Group classes are popular, but plenty of clients prefer a personal session at home or at the pool."),
        ("How do I get started?",
         "Call 1300 348 227 or use the contact form and choose \"Aged care\" — we'll reply within one business day."),
    ]),
    bp.cta_final("It's never too late to find your fit",
                 "Call us or send a note — we'll reply within one business day."))

# --------------------------------------------------------------------------
# locations
# --------------------------------------------------------------------------

def location_body(region, h1, sub, media_label, suburbs, map_label, faq_html, cta, extra_note=""):
    chips = "".join('<span class="chip">%s</span>' % s for s in suburbs) + '<span class="chip">…and surrounds</span>'
    note = ""
    if extra_note:
        note = '<p style="margin-top:18px;color:var(--muted)">%s</p>' % extra_note
    return (hero_page("Service areas · " + region, h1, sub, media_label)
            + "\nTRUST_BAR\n"
            + """
<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF Where we work</span>
      <h2>Around %s</h2>
      <p><span class="chip chip--sample">Placeholder list — confirm exact coverage with intake before launch</span></p>
    </div>
    <div class="suburbs">%s</div>
    %s
    <div class="map-ph" style="margin-top:28px" role="img" aria-label="Placeholder for embedded service area map">
      [PLACEHOLDER — embedded map of the %s service area]<br>%s
    </div>
  </div>
</section>""" % (region, chips, note, region, map_label)
            + how_it_works()
            + """
<section class="section" aria-label="Local testimonial">
  <div class="wrap">
    <div class="pull-band">
      <svg class="leaf-bg" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 21C3 9 9 3 21 3 21 15 15 21 3 21Z" fill="currentColor"/></svg>
      <span class="chip chip--sample" style="margin-bottom:16px">Sample content</span>
      <p>"They didn't just find me a support worker. They found me a training partner."</p>
      <p class="who">[Name] — FITCare participant, %s</p>
    </div>
  </div>
</section>""" % region
            + team_section("Matched from our 60+ local support workers.")
            + faq_section(region + " questions", faq_html)
            + cta)

GYMPIE = location_body(
    "Gympie",
    'Gympie, <span class="hl">we\'ve got you.</span>',
    "Our support workers have been part of the Gympie community for years — real locals, real energy, real support.",
    "Photo — genuine Gympie local shot",
    ["Gympie", "Southside", "Monkland", "Jones Hill", "Araluen", "Cooloola Cove", "Tin Can Bay"],
    "Intake: 1300 348 227 · info@fitcaresupportservices.com.au",
    bp.faq([
        ("Do you service my part of the Gympie region?",
         "Very likely — our team covers Gympie and surrounds. Call 1300 348 227 and we'll confirm on the spot."),
        ("What supports are available in Gympie?",
         "The full range — daily living, social and community participation, health and fitness, and transport. Group activities vary by region; ask us what's on."),
        ("How do I get started?",
         "Call us or use the Get Started form. We'll set up a relaxed meet &amp; greet with a Service Coordinator, then match you with local support workers."),
    ]),
    bp.cta_final("Ready when you are, Gympie",
                 "Tell us a little about you — or call and chat it through. We'll reply within one business day."))

MORETON_BAY = location_body(
    "Moreton Bay",
    'Moreton Bay, <span class="hl">let\'s move.</span>',
    "From Caboolture to the coast — FITCare support workers across the Moreton Bay region bring health, energy and genuine care to every visit.",
    "Photo — genuine Moreton Bay local shot",
    ["Caboolture", "Morayfield", "Burpengary", "North Lakes", "Redcliffe", "Deception Bay", "Bribie Island"],
    "Intake: 1300 348 227 · info@fitcaresupportservices.com.au",
    bp.faq([
        ("Do you service my suburb in Moreton Bay?",
         "Our team covers the Moreton Bay region broadly. Call 1300 348 227 and we'll confirm your suburb on the spot."),
        ("What supports are available locally?",
         "The full range — daily living, social and community participation, health and fitness, and transport. Ask us which group activities run near you."),
        ("How do I get started?",
         "Call us or use the Get Started form. We'll set up a relaxed meet &amp; greet with a Service Coordinator, then match you with local support workers."),
    ]),
    bp.cta_final("Ready when you are, Moreton Bay",
                 "Tell us a little about you — or call and chat it through. We'll reply within one business day."))

NORTH_BRISBANE = location_body(
    "North Brisbane",
    'North Brisbane, <span class="hl">we\'re here.</span>',
    "One of our newest areas — and growing. FITCare is expanding across Brisbane's north with the same healthy support work we're known for up the coast.",
    "Photo — genuine North Brisbane local shot",
    ["Chermside", "Strathpine", "Albany Creek", "Everton Park", "Bracken Ridge", "Aspley"],
    "Intake: 1300 348 227 · info@fitcaresupportservices.com.au",
    bp.faq([
        ("Do you have support workers near me?",
         "We're growing across North Brisbane — call 1300 348 227 and we'll tell you exactly where things stand for your suburb."),
        ("Are you expanding further into Brisbane?",
         "Yes — we're expanding into parts of Brisbane and the Gold Coast. If we're not in your area yet, get in touch anyway; it may be sooner than you think."),
        ("How do I get started?",
         "Call us or use the Get Started form. We'll set up a relaxed meet &amp; greet with a Service Coordinator."),
    ]),
    bp.cta_final("Ready when you are, North Brisbane",
                 "Tell us a little about you — or call and chat it through. We'll reply within one business day."),
    extra_note="North Brisbane is one of our newest service areas — coverage is growing month by month.")

LOCATIONS_HUB = """
<section class="section" style="padding-bottom:clamp(32px,5vw,56px)">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:0">
      <span class="eyebrow">LEAF Service areas</span>
      <h1 style="font-size:clamp(2.1rem,4.6vw,3.2rem);font-weight:800">Local support, wherever you are</h1>
      <p>60+ support workers across four South East Queensland regions — most living in the communities they support. Pick your patch.</p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="svc-grid" style="grid-template-columns:repeat(2,1fr)">
      <a class="svc" href="@/locations/sunshine-coast.html" style="grid-column:auto"><h3>Sunshine Coast</h3><p>Home base — our Maroochydore office and the biggest slice of the team.</p><span class="svc-go">Explore →</span></a>
      <a class="svc" href="@/locations/gympie.html" style="grid-column:auto"><h3>Gympie</h3><p>Real locals delivering the full range of supports across the Gympie region.</p><span class="svc-go">Explore →</span></a>
      <a class="svc" href="@/locations/moreton-bay.html" style="grid-column:auto"><h3>Moreton Bay</h3><p>From Caboolture to the coast — supports across the whole region.</p><span class="svc-go">Explore →</span></a>
      <a class="svc" href="@/locations/north-brisbane.html" style="grid-column:auto"><h3>North Brisbane</h3><p>Our newest area, growing fast across Brisbane's north.</p><span class="svc-go">Explore →</span></a>
    </div>
    <div class="steps-note" style="margin-top:26px">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>
      <span><strong>Not on the list?</strong> We're expanding into parts of Brisbane and the Gold Coast — call 1300 348 227 and ask. It may be sooner than you think.</span>
    </div>
  </div>
</section>
LOCATIONS_CTA
""".replace("LOCATIONS_CTA", bp.cta_final("Find support near you",
    "Tell us where you are and what you're after — we'll reply within one business day."))

# --------------------------------------------------------------------------
# team directory + profile template
# --------------------------------------------------------------------------

def dir_card(name, tags, tagslug, img=None):
    chips = "".join('<span class="chip">%s</span>' % t for t in tags)
    if img:
        media = ('<div class="media media--square"><img class="media-img" src="%s" '
                 'alt="Portrait of %s, FITCare support worker, in the black FITCare polo"></div>' % (img, name))
    else:
        media = ('<div class="media media--square" role="img" aria-label="Placeholder for %s\'s photo">'
                 '<div class="media-label"><strong>Placeholder</strong>Photo</div></div>' % name)
    return ('<div class="tw" data-tags="%s">%s'
            '<div class="tw-body"><h3>%s</h3><div class="tw-tags">%s</div>'
            '<a class="tw-link" href="@/team/profile-template.html">View profile →</a></div></div>'
            % (tagslug, media, name, chips))

TEAM_PAGE = """
<section class="section" style="padding-bottom:clamp(32px,5vw,56px)">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:0">
      <span class="eyebrow">LEAF Our team</span>
      <h1 style="font-size:clamp(2.1rem,4.6vw,3.2rem);font-weight:800">Real people, and plenty of them</h1>
      <p>40+ support workers across South East Queensland — over half with fitness qualifications, plus swim instructors, yoga teachers, football coaches and distance runners. Find someone who gets you.</p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <p style="margin-bottom:18px"><span class="chip chip--sample">Sample tags &amp; presentation — full 40+ directory migrates from the current site with real photos &amp; bios</span></p>
    <div class="filter-row" data-filter-group="workers" role="group" aria-label="Filter support workers by speciality">
      <button class="fbtn" type="button" data-filter="all" aria-pressed="true">All</button>
      <button class="fbtn" type="button" data-filter="fitness" aria-pressed="false">Fitness</button>
      <button class="fbtn" type="button" data-filter="swimming" aria-pressed="false">Swimming</button>
      <button class="fbtn" type="button" data-filter="yoga" aria-pressed="false">Yoga</button>
      <button class="fbtn" type="button" data-filter="community" aria-pressed="false">Community</button>
      <button class="fbtn" type="button" data-filter="creative" aria-pressed="false">Creative</button>
    </div>
    <div class="team-grid" data-filter-items="workers">
      DIR_CARDS
      <div class="tw" data-tags="all">
        <div class="tw-body" style="align-content:center;text-align:center;min-height:220px">
          <h3>+ 30 more</h3>
          <p style="color:var(--muted);font-size:.9375rem">The full 40+ profile directory migrates here from the current site.</p>
          <a class="tw-link" href="@/get-started.html">Get matched →</a>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="band band--slim" aria-label="Our promise">
  <svg class="leaf-bg" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 21C3 9 9 3 21 3 21 15 15 21 3 21Z" fill="currentColor"/></svg>
  <div class="wrap">
    <span class="band-script">Healthy support workers</span>
    <p class="band-main">delivering healthy support work.</p>
  </div>
</section>
TEAM_CTA
""".replace("DIR_CARDS", "\n".join([
    dir_card("Allison", ["Swimming", "Community outings"], "swimming community"),
    dir_card("Anna", ["Yoga", "Daily living"], "yoga"),
    dir_card("Ashli", ["Fitness", "Creative"], "fitness creative"),
    dir_card("Brigitte", ["Community", "Outings"], "community"),
    dir_card("Brooke", ["Swimming", "Fitness"], "swimming fitness", img="@/assets/img/team/brooke.jpg"),
    dir_card("Bruce", ["Strength training", "Lawn bowls"], "fitness community"),
    dir_card("Carissa", ["Yoga", "Daily living"], "yoga"),
    dir_card("Dan", ["Running", "Footy"], "fitness"),
    dir_card("Priscila", ["Fitness", "Social"], "fitness community"),
])).replace("TEAM_CTA", bp.cta_final("Found someone you'd like to meet?",
    "Tell us who caught your eye — or let us match you. Either way, the meet &amp; greet is relaxed and obligation-free."))

PROFILE_TEMPLATE = """
<section class="section">
  <div class="wrap">
    <p style="margin-bottom:18px"><span class="chip chip--sample">Profile template shown with Brooke's real portrait — bio, tags and availability are placeholders pending her own words</span></p>
    <div class="profile">
      <div class="media"><img class="media-img" src="@/assets/img/team/brooke.jpg" alt="Portrait of Brooke, FITCare support worker, smiling in the black FITCare polo against a plain light background"></div>
      <div class="profile-body">
        <span class="chip chip--ok">Taking new participants</span>
        <h3>Brooke</h3>
        <div class="profile-meta"><span class="chip">Swimming</span><span class="chip">Fitness</span><span class="chip">Sunshine Coast</span></div>
        <p>[PLACEHOLDER bio — 60–90 words in Brooke's own voice: background, what a great day of support looks like, one personal detail participants can connect over.]</p>
        <blockquote style="margin:0;padding:8px 0 8px 22px;border-left:4px solid var(--sun-400);font-family:'Bricolage Grotesque',sans-serif;font-weight:600;color:var(--ink)">"[Sample pull-quote from a participant or family member — pending consent program]"</blockquote>
        <div class="profile-ctas">
          <a class="btn btn--primary" href="@/get-started.html?worker=brooke">Request Brooke</a>
          <a class="btn btn--ghost" href="@/team/index.html">Back to the team</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""

# --------------------------------------------------------------------------
# activities
# --------------------------------------------------------------------------

def act_card(cat, title, desc, img=None, img_alt=""):
    if img:
        media = ('<div class="media media--wide"><img class="media-img" src="%s" alt="%s"></div>' % (img, img_alt))
    else:
        media = ('<div class="media media--wide" role="img" aria-label="Placeholder photo: %s">'
                 '<div class="media-label"><strong>Placeholder</strong>Photo</div></div>' % title)
    return ('<div class="act" data-tags="%s">%s'
            '<div class="act-body"><span class="chip">%s</span><h3>%s</h3>'
            '<div class="act-when"><span>[Day]</span><span>[Time]</span><span>[Venue]</span></div><p>%s</p></div></div>'
            % (cat.lower(), media, cat, title, desc))

ACTIVITIES_PAGE = """
<section class="section" style="padding-bottom:clamp(32px,5vw,56px)">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:0">
      <span class="eyebrow">LEAF Activities</span>
      <h1 style="font-size:clamp(2.1rem,4.6vw,3.2rem);font-weight:800">Something on every week</h1>
      <p>Group activities across fitness, social, creative and outings — all abilities welcome, support workers included. This calendar is plain HTML: readable by everyone, with or without JavaScript. <span class="chip chip--sample">Sample schedule — real calendar content migrates from the current site</span></p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="filter-row" data-filter-group="acts" role="group" aria-label="Filter activities by category">
      <button class="fbtn" type="button" data-filter="all" aria-pressed="true">All</button>
      <button class="fbtn" type="button" data-filter="fitness" aria-pressed="false">Fitness</button>
      <button class="fbtn" type="button" data-filter="social" aria-pressed="false">Social</button>
      <button class="fbtn" type="button" data-filter="creative" aria-pressed="false">Creative</button>
      <button class="fbtn" type="button" data-filter="outings" aria-pressed="false">Outings</button>
    </div>
    <div data-filter-items="acts">
      <section class="week" aria-labelledby="wk1">
        <h3 id="wk1">This week <small>[dates from calendar]</small></h3>
        <div class="act-grid">
          WK1
        </div>
      </section>
      <section class="week" aria-labelledby="wk2">
        <h3 id="wk2">Next week <small>[dates from calendar]</small></h3>
        <div class="act-grid">
          WK2
        </div>
      </section>
    </div>
    <div class="steps-note">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
      <span><strong>Want in?</strong> Ask your Service Coordinator or call 1300 348 227 — we'll help with transport too.</span>
    </div>
  </div>
</section>
ACT_CTA
""".replace("WK1", "\n".join([
    act_card("Social", "Lawn bowls &amp; lunch", "A friendly roll-up followed by lunch with the crew. All abilities welcome."),
    act_card("Fitness", "Group fitness", "Move at your own pace with a team that cheers you on."),
    act_card("Creative", "Pottery studio", "Get your hands dirty and make something worth keeping."),
])).replace("WK2", "\n".join([
    act_card("Outings", "Local markets trip", "Wander the stalls, grab a coffee, take home something good."),
    act_card("Fitness", "Aqua fitness", "Low-impact, high-fun water workout with the swim crew."),
    act_card("Outings", "Beach walk &amp; smoothies", "Sea air, soft sand and a smoothie at the end. All paces welcome.",
             img="@/assets/img/activities-beach-selfie.jpg",
             img_alt="Two smiling FITCare community members take a selfie on the beach on an overcast day"),
    act_card("Creative", "Art &amp; craft", "Paint, paper, glue and good company — beginners very welcome."),
])).replace("ACT_CTA", bp.cta_final("See something you like?",
    "Tell us which activity caught your eye and we'll sort the rest — including getting there."))

# --------------------------------------------------------------------------
# coordinators
# --------------------------------------------------------------------------

COORDINATORS_PAGE = """
<section class="section" style="padding-bottom:clamp(32px,5vw,48px)">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:24px;max-width:760px">
      <span class="eyebrow">LEAF For support coordinators</span>
      <h1 style="font-size:clamp(2.1rem,4.6vw,3.2rem);font-weight:800">Referrals without the runaround</h1>
      <p>Everything you need on one page: registration categories, service areas, capacity and a direct line to intake. We reply within one business day — usually faster.</p>
    </div>
    <div class="hero-ctas">
      <a class="btn btn--primary" href="@/get-started.html?who=coordinator">Start a referral</a>
      <a class="btn btn--ghost" href="tel:1300348227">PHONE Call intake — 1300 348 227</a>
      <a class="btn btn--ghost" href="#pack">Referral pack (PDF) <span class="chip chip--sample" style="margin-left:6px">Placeholder</span></a>
    </div>
  </div>
</section>

<section class="section section--alt" style="padding-block:clamp(48px,6vw,72px)">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF Registration</span>
      <h2>Registered support categories</h2>
      <p>Registered NDIS provider, meeting the Quality and Safeguards Commission's requirements.</p>
    </div>
    <div class="tbl-wrap">
      <table class="tbl">
        <thead><tr><th scope="col">Group</th><th scope="col">Code</th><th scope="col">Support category</th></tr></thead>
        <tbody>
          <tr><td><b>Core</b></td><td>0107</td><td>Assistance with Personal Activities</td></tr>
          <tr><td><b>Core</b></td><td>0108</td><td>Transport and Travel Assistance</td></tr>
          <tr><td><b>Core</b></td><td>0120</td><td>Household Tasks</td></tr>
          <tr><td><b>Core</b></td><td>0125</td><td>Participation in Community, Social and Civic Activities</td></tr>
          <tr><td><b>Core</b></td><td>0136</td><td>Group and Centre Based Activities</td></tr>
          <tr><td><b>Capacity Building</b></td><td>0116</td><td>Innovative Community Participation</td></tr>
          <tr><td><b>Capacity Building</b></td><td>0117</td><td>Development of Daily Living and Life Skills</td></tr>
          <tr><td><b>Capacity Building</b></td><td>0125</td><td>Participation in Community, Social &amp; Civic Activities</td></tr>
          <tr><td><b>Capacity Building</b></td><td>0126</td><td>Exercise Physiology and Personal Training</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF Coverage &amp; capacity</span>
      <h2>Service areas at a glance</h2>
    </div>
    <div class="info-grid">
      <div class="info-card"><h3>Sunshine Coast</h3><p>Home base — office in Maroochydore, largest team.</p><span class="chip chip--ok">Taking new participants</span></div>
      <div class="info-card"><h3>Gympie</h3><p>Established team of local support workers.</p><span class="chip chip--ok">Taking new participants</span></div>
      <div class="info-card"><h3>Moreton Bay</h3><p>Full coverage across the region.</p><span class="chip chip--ok">Taking new participants</span></div>
      <div class="info-card"><h3>North Brisbane</h3><p>Newest area — expanding month by month.</p><span class="chip chip--sample">Capacity — check with intake</span></div>
    </div>
    <p style="margin-top:16px"><span class="chip chip--sample">Capacity indicators are placeholders — updated by intake in production (recommend monthly)</span></p>
    <div class="map-ph" style="margin-top:24px" role="img" aria-label="Placeholder for service area map">[PLACEHOLDER — combined SEQ service area map]</div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF Process</span>
      <h2>How a referral runs</h2>
    </div>
    <div class="steps">
      <div class="step"><span class="step-n" aria-hidden="true">1</span><h3>Send the referral</h3><p>Two minutes online — participant name, your details, region. No plan documents needed upfront.</p></div>
      <div class="step"><span class="step-n" aria-hidden="true">2</span><h3>We confirm</h3><p>Intake replies within one business day with next steps and a meet &amp; greet time.</p></div>
      <div class="step"><span class="step-n" aria-hidden="true">3</span><h3>Meet &amp; greet + match</h3><p>A Service Coordinator meets the participant, then matches from 40+ profiled support workers. You stay in the loop.</p></div>
    </div>
    <div class="steps-note">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>
      <span><strong>Privacy by design:</strong> sensitive details (disability description, NDIS number, plan dates) are collected at the meet &amp; greet — not through web forms.</span>
    </div>
  </div>
</section>

<section class="section" id="pack">
  <div class="wrap">
    <div class="coord">
      <div class="coord-copy">
        <span class="eyebrow">LEAF Intake</span>
        <h2>Talk to a human, fast</h2>
        <p>Direct line to intake — no phone trees, no call-backs-next-week. Or grab the referral pack for everything in one PDF.</p>
        <div class="coord-ctas">
          <a class="btn btn--light" href="@/get-started.html?who=coordinator">Start a referral</a>
          <a class="btn btn--outline-light" href="#pack">Download referral pack <span class="chip chip--sample" style="margin-left:4px">PDF placeholder</span></a>
        </div>
      </div>
      <div class="coord-facts">
        <div class="fact"><h4>Intake</h4><p>1300 348 227<br>info@fitcaresupportservices.com.au<br>Replies within 1 business day</p></div>
        <div class="fact"><h4>Office</h4><p>Suite 10, 102 Wises Road<br>Maroochydore QLD 4558</p></div>
        <div class="fact"><h4>Why FITCare</h4><p>60+ support workers, over half with fitness qualifications · extensive screening and training program · weekly group activities calendar</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head sec-head--center">
      <span class="eyebrow">LEAF Good to know</span>
      <h2>Coordinator questions</h2>
    </div>
    COORD_FAQ
  </div>
</section>
""".replace("COORD_FAQ", bp.faq([
    ("How fast do you respond to referrals?",
     "Within one business day, every time — that's a published commitment. Phone referrals are actioned on the call."),
    ("What information do you need upfront?",
     "The minimum: who's referring, participant name and contact, and region. Plan details, support needs and documents come at the meet &amp; greet — deliberately not through web forms."),
    ("How do you signal capacity?",
     "Live availability indicators per region on this page, updated by intake. If a region is tight we'll tell you straight and give you a realistic timeframe."),
    ("Can participants choose their support worker?",
     "Yes — matching is the core of our model. Participants (and you) can browse 40+ worker profiles, and we rematch without fuss if the fit isn't right."),
]))

# --------------------------------------------------------------------------
# about
# --------------------------------------------------------------------------

ABOUT_PAGE = """
<section class="section" style="padding-bottom:clamp(32px,5vw,56px)">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:0;max-width:760px">
      <span class="eyebrow">LEAF About FITCare</span>
      <h1 style="font-size:clamp(2.1rem,4.6vw,3.2rem);font-weight:800">Care with real energy behind it</h1>
      <p>FITCare Support Services exists to empower people to get what they want out of life — by creating better access to all things. We're a registered NDIS provider on the Sunshine Coast, and we do it with the healthiest team in the business.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF Our values</span>
      <h2>The FITCare Community runs on five things</h2>
    </div>
    <div class="info-grid" style="grid-template-columns:repeat(5,1fr)">
      <div class="info-card"><h3>Quality</h3><p>Screened, trained, supported workers — and standards we're happy to be measured against.</p></div>
      <div class="info-card"><h3>Respect</h3><p>Your life, your calls. We turn up as guests and act like it.</p></div>
      <div class="info-card"><h3>Adaptability</h3><p>Plans change, people change — supports that flex with you.</p></div>
      <div class="info-card"><h3>Person-centred</h3><p>Everything starts with what you want out of life, not what's easy to roster.</p></div>
      <div class="info-card"><h3>Inclusion</h3><p>Community belongs to everyone. Our job is better access to all of it.</p></div>
    </div>
  </div>
</section>

<section class="band band--slim" aria-label="Our promise">
  <svg class="leaf-bg" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 21C3 9 9 3 21 3 21 15 15 21 3 21Z" fill="currentColor"/></svg>
  <div class="wrap">
    <span class="band-script">Healthy support workers</span>
    <p class="band-main">delivering healthy support work.</p>
    <p class="band-sub">Over half our 60+ team hold fitness qualifications — plus swim instructors, yoga teachers, football coaches and distance runners.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF Registration</span>
      <h2>A registered NDIS provider — in writing</h2>
      <p>FITCare meets the NDIS Quality and Safeguards Commission's requirements. These are our registered support categories:</p>
    </div>
    <div class="tbl-wrap">
      <table class="tbl">
        <thead><tr><th scope="col">Group</th><th scope="col">Code</th><th scope="col">Support category</th></tr></thead>
        <tbody>
          <tr><td><b>Core</b></td><td>0107</td><td>Assistance with Personal Activities</td></tr>
          <tr><td><b>Core</b></td><td>0108</td><td>Transport and Travel Assistance</td></tr>
          <tr><td><b>Core</b></td><td>0120</td><td>Household Tasks</td></tr>
          <tr><td><b>Core</b></td><td>0125</td><td>Participation in Community, Social and Civic Activities</td></tr>
          <tr><td><b>Core</b></td><td>0136</td><td>Group and Centre Based Activities</td></tr>
          <tr><td><b>Capacity Building</b></td><td>0116</td><td>Innovative Community Participation</td></tr>
          <tr><td><b>Capacity Building</b></td><td>0117</td><td>Development of Daily Living and Life Skills</td></tr>
          <tr><td><b>Capacity Building</b></td><td>0125</td><td>Participation in Community, Social &amp; Civic Activities</td></tr>
          <tr><td><b>Capacity Building</b></td><td>0126</td><td>Exercise Physiology and Personal Training</td></tr>
        </tbody>
      </table>
    </div>
    <p style="margin-top:16px"><span class="chip chip--sample">[PLACEHOLDER — display NDIS registration number + confirm "We support the NDIS" logo usage before launch]</span></p>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF Training pathway</span>
      <h2>Partnered with FIT College</h2>
      <p>Our RTO partnership means FITCare support workers train through the <strong>CHCSS00130 Individual Support – Disability Skillset</strong> — and keep developing inside the FITCare Community with ongoing training, resources and advancement.</p>
    </div>
    <div class="info-grid">
      <div class="info-card"><h3>Trained properly</h3><p>Nationally recognised skillset training through our RTO partner, FIT College.</p></div>
      <div class="info-card"><h3>Screened thoroughly</h3><p>An extensive screening and training program before anyone meets a participant.</p></div>
      <div class="info-card"><h3>Supported constantly</h3><p>The FITCare Community backs every worker with resources and a path to grow.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF Find us</span>
      <h2>Say hello in Maroochydore</h2>
    </div>
    <div class="info-grid">
      <div class="info-card"><h3>Office</h3><p>Suite 10, 102 Wises Road<br>Maroochydore QLD 4558</p></div>
      <div class="info-card"><h3>Phone</h3><p><a href="tel:1300348227">1300 348 227</a><br>We reply within 1 business day</p></div>
      <div class="info-card"><h3>Email</h3><p><a href="mailto:info@fitcaresupportservices.com.au">info@fitcaresupportservices.com.au</a></p></div>
    </div>
    <div style="margin-top:28px" class="trust-strip">
      <span><b>Registered NDIS provider</b></span><span class="dot">•</span>
      <span>Regulated by the NDIS Quality &amp; Safeguards Commission</span><span class="dot">•</span>
      <a href="@/resources/feedback-complaints.html">Feedback &amp; complaints</a><span class="dot">•</span>
      <a href="https://fitcaresupportservices.com.au/storage/fitcare-participant-handbook.pdf">Participant handbook (PDF)</a>
    </div>
  </div>
</section>
ABOUT_CTA
""".replace("ABOUT_CTA", bp.cta_final("Come meet the team",
    "The meet &amp; greet is relaxed, obligation-free and all about you. We'll reply within one business day."))

# --------------------------------------------------------------------------
# careers
# --------------------------------------------------------------------------

CAREERS_PAGE = hero_page(
    "Careers",
    'Do work that <span class="hl">keeps you moving.</span>',
    "Every person at FITCare shares a passion for health and wellbeing — many of us came from fitness backgrounds. If supporting people while staying active sounds like your kind of job, let's talk.",
    "Photo — FITCare team at a group activity (consent required)",
    '<a class="hero-aside-link" href="https://fitcaresupportservices.com.au/storage/FITCare%20Support%20Worker%20JD.pdf">Read the Support Worker job description (PDF) →</a>'
) + """
<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF Why FITCare</span>
      <h2>The FITCare Community has your back</h2>
    </div>
    <div class="info-grid">
      <div class="info-card"><h3>Training &amp; development</h3><p>Nationally recognised training via our FIT College partnership (CHCSS00130 Individual Support – Disability Skillset), plus ongoing resources.</p></div>
      <div class="info-card"><h3>A team like you</h3><p>60+ colleagues who'd rather be at the pool, the gym or the bowls green than behind a desk.</p></div>
      <div class="info-card"><h3>Room to grow</h3><p>The FITCare Community provides training, resources and real advancement pathways.</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF Apply</span>
      <h2>Become a FITCare support worker</h2>
      <p>Tell us a bit about yourself — we'll be in touch within one business day.</p>
    </div>
    <form class="sform" data-simple-form novalidate>
      <div class="form-fields">
        <div class="gs-row">
          <div class="field"><label for="ca-name">Your name</label><input id="ca-name" name="name" type="text" autocomplete="name" required><p class="err">We need a name to say hello properly.</p></div>
          <div class="field"><label for="ca-phone">Phone</label><input id="ca-phone" name="phone" type="tel" autocomplete="tel" required><p class="err">A phone number helps us move fast.</p></div>
        </div>
        <div class="field"><label for="ca-email">Email</label><input id="ca-email" name="email" type="email" autocomplete="email" required><p class="err">Add an email so we can reply in writing.</p></div>
        <div class="field">
          <label for="ca-region">Where are you based?</label>
          <select id="ca-region" name="region">
            <option value="">Choose a region (optional)</option>
            <option>Sunshine Coast</option><option>Gympie</option><option>Moreton Bay</option><option>North Brisbane</option><option>Somewhere else</option>
          </select>
        </div>
        <div class="field"><label for="ca-about">Tell us about you <small>(background, quals, what keeps you active)</small></label><textarea id="ca-about" name="about"></textarea></div>
        <p style="font-size:.875rem;color:var(--muted)">Resume upload: <span class="chip chip--sample">[PLACEHOLDER — file upload wired to backend in production]</span></p>
        <button class="btn btn--primary" type="submit">Send application</button>
      </div>
      <div class="form-success">
        <span class="gs-ok"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></span>
        <h3>Application received!</h3>
        <p>Thanks — a real person will be in touch within one business day. Meanwhile, the <a href="https://fitcaresupportservices.com.au/storage/FITCare%20Support%20Worker%20JD.pdf">job description (PDF)</a> has the full detail.</p>
      </div>
    </form>
  </div>
</section>
"""

# --------------------------------------------------------------------------
# contact
# --------------------------------------------------------------------------

CONTACT_PAGE = """
<section class="section" style="padding-bottom:clamp(32px,5vw,48px)">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:0">
      <span class="eyebrow">LEAF Contact</span>
      <h1 style="font-size:clamp(2.1rem,4.6vw,3.2rem);font-weight:800">Say hello</h1>
      <p>Questions, referrals, feedback or just a chat about what's possible — we reply within one business day.</p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap" style="display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(28px,4vw,56px);align-items:start">
    <form class="sform" data-simple-form novalidate style="max-width:none">
      <div class="form-fields">
        <div class="gs-row">
          <div class="field"><label for="co-name">Your name</label><input id="co-name" name="name" type="text" autocomplete="name" required><p class="err">We need a name to say hello properly.</p></div>
          <div class="field"><label for="co-phone">Phone <small>(or email below)</small></label><input id="co-phone" name="phone" type="tel" autocomplete="tel"></div>
        </div>
        <div class="field"><label for="co-email">Email</label><input id="co-email" name="email" type="email" autocomplete="email" required><p class="err">Add an email so we can reply.</p></div>
        <fieldset>
          <legend>What's it about?</legend>
          <div class="opts opts--chips">
            <label class="opt"><input type="radio" name="topic" value="ndis" checked><span>NDIS supports</span></label>
            <label class="opt"><input type="radio" name="topic" value="aged-care"><span>Aged care</span></label>
            <label class="opt"><input type="radio" name="topic" value="careers"><span>Careers</span></label>
            <label class="opt"><input type="radio" name="topic" value="other"><span>Something else</span></label>
          </div>
        </fieldset>
        <div class="field"><label for="co-msg">Your message</label><textarea id="co-msg" name="message" required></textarea><p class="err">Tell us a little so we can point you the right way.</p></div>
        <button class="btn btn--primary" type="submit">Send message</button>
      </div>
      <div class="form-success">
        <span class="gs-ok"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></span>
        <h3>Message sent!</h3>
        <p>A real person will reply within <b>one business day</b>. Need us now? Call <a href="tel:1300348227"><b>1300 348 227</b></a>.</p>
      </div>
    </form>
    <div style="display:grid;gap:20px">
      <div class="info-card"><h3>Call</h3><p><a href="tel:1300348227">1300 348 227</a> — the fastest way, especially for coordinators.</p></div>
      <div class="info-card"><h3>Email</h3><p><a href="mailto:info@fitcaresupportservices.com.au">info@fitcaresupportservices.com.au</a></p></div>
      <div class="info-card"><h3>Visit</h3><p>Suite 10, 102 Wises Road<br>Maroochydore QLD 4558</p></div>
      <div class="info-card"><h3>Feedback &amp; complaints</h3><p>Something to tell us — good or hard to hear? <a href="@/resources/feedback-complaints.html">We want it.</a></p></div>
      <div class="map-ph" role="img" aria-label="Placeholder for office map">[PLACEHOLDER — embedded map: Maroochydore office]</div>
    </div>
  </div>
</section>
"""

# --------------------------------------------------------------------------
# resources
# --------------------------------------------------------------------------

NEW_TO_NDIS = """
<section class="section" style="padding-bottom:clamp(32px,5vw,56px)">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:0;max-width:760px">
      <span class="eyebrow">LEAF Resources · New to the NDIS</span>
      <h1 style="font-size:clamp(2.1rem,4.6vw,3.2rem);font-weight:800">New to the NDIS? Start here.</h1>
      <p>The NDIS can feel like a lot of letters and forms. Here's the plain-English version — and exactly how we can help, wherever you're up to.</p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap" style="display:grid;gap:20px">
    <div class="info-grid">
      <div class="info-card"><h3>What is the NDIS?</h3><p>The National Disability Insurance Scheme funds supports for Australians with disability — help at home, in the community, and with health and wellbeing. It's your plan, built around your goals.</p></div>
      <div class="info-card"><h3>Not on the NDIS yet?</h3><p>Eligibility and applications happen through the NDIS itself. Start at <a href="https://www.ndis.gov.au">ndis.gov.au</a> — and if you'd like a hand understanding the steps, call us. We're happy to explain, no strings.</p></div>
      <div class="info-card"><h3>Have a plan, not sure how to use it?</h3><p>We work with great Support Coordinators and Plan Managers every day and can connect you with people who'll help you get the most from your plan.</p></div>
    </div>
    <div class="steps-note">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
      <span><strong>You don't need to have it all figured out.</strong> The meet &amp; greet is exactly for working out what supports fit your plan — bring your questions.</span>
    </div>
  </div>
</section>
<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF Then what?</span>
      <h2>Starting with FITCare is three easy steps</h2>
    </div>
    STEPS
  </div>
</section>
NDIS_CTA
""".replace("NDIS_CTA", bp.cta_final("Questions? Bring them all",
    "No question is too basic — that's what we're here for. We'll reply within one business day."))

FAQS_PAGE = """
<section class="section" style="padding-bottom:clamp(32px,5vw,48px)">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:0">
      <span class="eyebrow">LEAF Resources · FAQs</span>
      <h1 style="font-size:clamp(2.1rem,4.6vw,3.2rem);font-weight:800">Questions people ask us</h1>
      <p>The genuine article — straight answers to the things participants, families and coordinators actually ask.</p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap" style="display:grid;gap:36px">
    <div>
      <h2 style="font-size:1.3rem;margin-bottom:16px">About FITCare</h2>
      FAQ_ABOUT
    </div>
    <div>
      <h2 style="font-size:1.3rem;margin-bottom:16px">Getting started</h2>
      FAQ_START
    </div>
    <div>
      <h2 style="font-size:1.3rem;margin-bottom:16px">Funding &amp; goals</h2>
      FAQ_FUND
    </div>
  </div>
</section>
FAQS_CTA
""".replace("FAQ_ABOUT", bp.faq([
    ("Is FITCare a registered NDIS provider?",
     "Yes. FITCare Support Services is a registered NDIS provider, which means we meet the NDIS Quality and Safeguards Commission's requirements. Our registered support categories are listed on the <a href=\"@/about.html\">About page</a>."),
    ("What makes FITCare different from other providers?",
     "Every person on our team shares a passion for health and wellbeing — it's the hiring filter. Healthy support workers delivering healthy support work isn't a slogan; it's the whole model."),
    ("What qualifications do your support workers have?",
     "Just over half the team hold fitness qualifications, and the crew includes swimming instructors, yoga teachers, football coaches and distance runners — alongside disability support training through our FIT College partnership."),
])).replace("FAQ_START", bp.faq([
    ("Where does FITCare provide support?",
     "Our 60+ support workers currently service the Sunshine Coast, Moreton Bay and Gympie, and we're expanding into parts of Brisbane and the Gold Coast. See <a href=\"@/locations/index.html\">service areas</a>."),
    ("How do I get started?",
     "Use the <a href=\"@/get-started.html\">Get Started form</a> or call 1300 348 227. We'll arrange a meet and greet — relaxed, obligation-free."),
    ("What's a meet and greet?",
     "A sit-down with a Service Coordinator — your first point of contact at FITCare. They get to know you, your goals and your interests, then match you with the right support workers."),
])).replace("FAQ_FUND", bp.faq([
    ("I don't have personal training funding in my plan — can I still train?",
     "Very likely, yes. Our health and fitness supports can often be delivered through your core and/or capacity building funding. Bring your plan to the meet &amp; greet and we'll walk through it."),
    ("Do I need fitness goals to be a FITCare participant?",
     "No. Plenty of participants just want great everyday support. The fitness culture simply means you get energetic, positive people — whatever your goals are."),
])).replace("FAQS_CTA", bp.cta_final("Didn't find your answer?",
    "Ask us directly — no question is too small. We'll reply within one business day."))

NEWS_PAGE = """
<section class="section" style="padding-bottom:clamp(32px,5vw,48px)">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:0">
      <span class="eyebrow">LEAF Resources · News</span>
      <h1 style="font-size:clamp(2.1rem,4.6vw,3.2rem);font-weight:800">News &amp; stories</h1>
      <p>What the FITCare Community has been up to. <span class="chip chip--sample">Sample cards — existing posts migrate from the current site's /news</span></p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="news-grid">
      <a class="act" href="@/resources/news-article-template.html" style="text-decoration:none">
        <div class="media media--wide" role="img" aria-label="Placeholder article image"><div class="media-label"><strong>Placeholder</strong>Article image</div></div>
        <div class="act-body"><span class="chip">Community</span><h3>[PLACEHOLDER — article headline]</h3><p class="act-meta">[Date]</p><p>[Placeholder standfirst — one sentence that makes you want the rest.]</p></div>
      </a>
      <a class="act" href="@/resources/news-article-template.html" style="text-decoration:none">
        <div class="media media--wide" role="img" aria-label="Placeholder article image"><div class="media-label"><strong>Placeholder</strong>Article image</div></div>
        <div class="act-body"><span class="chip">Activities</span><h3>[PLACEHOLDER — article headline]</h3><p class="act-meta">[Date]</p><p>[Placeholder standfirst.]</p></div>
      </a>
      <a class="act" href="@/resources/news-article-template.html" style="text-decoration:none">
        <div class="media media--wide" role="img" aria-label="Placeholder article image"><div class="media-label"><strong>Placeholder</strong>Article image</div></div>
        <div class="act-body"><span class="chip">Team</span><h3>[PLACEHOLDER — article headline]</h3><p class="act-meta">[Date]</p><p>[Placeholder standfirst.]</p></div>
      </a>
    </div>
  </div>
</section>
"""

NEWS_ARTICLE = """
<section class="section">
  <div class="wrap">
    <article class="article">
      <p><span class="chip chip--sample">Article template — every production post uses this layout</span></p>
      <div class="article-meta"><span class="chip">Community</span><span>[Date]</span><span>[Author]</span></div>
      <h1>[PLACEHOLDER — article headline goes here]</h1>
      <p class="lede">[Placeholder standfirst — a single sentence that sets up the story and earns the scroll.]</p>
      <div class="media media--wide" role="img" aria-label="Placeholder article hero image"><div class="media-label"><strong>Placeholder</strong>Article hero image with descriptive alt text</div></div>
      <p>[Placeholder body copy — short paragraphs, plain English, one idea each. Photography with real alt text, headings every few paragraphs for scanners.]</p>
      <blockquote>"[Placeholder pull quote — the human moment of the story.]"</blockquote>
      <p>[Placeholder body copy continues. End with what the reader can do next — join the activity, meet the team, get started.]</p>
      <p><a href="@/resources/news.html"><strong>← Back to news</strong></a></p>
    </article>
  </div>
</section>
"""

FEEDBACK_PAGE = """
<section class="section" style="padding-bottom:clamp(32px,5vw,48px)">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:0;max-width:760px">
      <span class="eyebrow">LEAF Feedback &amp; complaints</span>
      <h1 style="font-size:clamp(2.1rem,4.6vw,3.2rem);font-weight:800">Your feedback makes us better</h1>
      <p>Compliments, suggestions or complaints — we genuinely want them all, and the NDIS Practice Standards guarantee your right to speak up safely. Complaints never affect your supports.</p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap" style="display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(28px,4vw,56px);align-items:start">
    <form class="sform" data-simple-form novalidate style="max-width:none">
      <div class="form-fields">
        <fieldset>
          <legend>What would you like to share?</legend>
          <div class="opts opts--chips">
            <label class="opt"><input type="radio" name="kind" value="feedback" checked><span>Feedback</span></label>
            <label class="opt"><input type="radio" name="kind" value="complaint"><span>Complaint</span></label>
            <label class="opt"><input type="radio" name="kind" value="compliment"><span>Compliment</span></label>
          </div>
        </fieldset>
        <div class="field"><label for="fb-msg">Tell us what happened</label><textarea id="fb-msg" name="message" required></textarea><p class="err">A few words is all we need to act on it.</p></div>
        <div class="gs-row">
          <div class="field"><label for="fb-name">Your name <small>(optional — anonymous is fine)</small></label><input id="fb-name" name="name" type="text"></div>
          <div class="field"><label for="fb-contact">Phone or email <small>(optional, if you'd like a reply)</small></label><input id="fb-contact" name="contact" type="text"></div>
        </div>
        <button class="btn btn--primary" type="submit">Send it</button>
      </div>
      <div class="form-success">
        <span class="gs-ok"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></span>
        <h3>Received — thank you.</h3>
        <p>If you left contact details, we'll respond within one business day. <span class="chip chip--sample">[PLACEHOLDER — confirm internal complaints-handling timeframes]</span></p>
      </div>
    </form>
    <div style="display:grid;gap:20px">
      <div class="info-card"><h3>Prefer to talk?</h3><p>Call <a href="tel:1300348227">1300 348 227</a> or email <a href="mailto:info@fitcaresupportservices.com.au">info@fitcaresupportservices.com.au</a>.</p></div>
      <div class="info-card"><h3>Want to go further?</h3><p>You can always raise a complaint directly with the <strong>NDIS Quality and Safeguards Commission</strong> — <a href="https://www.ndiscommission.gov.au">ndiscommission.gov.au</a> or 1800 035 544. Free, confidential, and you don't need to talk to us first.</p></div>
      <div class="info-card"><h3>Your handbook</h3><p>The <a href="https://fitcaresupportservices.com.au/storage/fitcare-participant-handbook.pdf">Participant Handbook (PDF)</a> explains your rights and our commitments in full.</p></div>
    </div>
  </div>
</section>
"""

ACCESSIBILITY_PAGE = """
<section class="section" style="padding-bottom:clamp(32px,5vw,48px)">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:0;max-width:760px">
      <span class="eyebrow">LEAF Accessibility statement</span>
      <h1 style="font-size:clamp(2.1rem,4.6vw,3.2rem);font-weight:800">This site is for everyone</h1>
      <p>FITCare supports people with disability — our website failing accessibility would be a brand failure, not just a technical one. This site targets <strong>WCAG 2.2 Level AA</strong>, and here's what that means in practice.</p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap" style="display:grid;gap:20px">
    <div class="info-grid">
      <div class="info-card"><h3>Keyboard first</h3><p>Every control — menus, forms, the review carousel, filters — works with a keyboard alone, with a visible focus indicator throughout.</p></div>
      <div class="info-card"><h3>Readable by design</h3><p>Minimum 17px body text, strong contrast (4.5:1 or better), plain English aimed at reading grade 7 on participant pages, and no information conveyed by colour alone.</p></div>
      <div class="info-card"><h3>Works without extras</h3><p>Every page is readable with JavaScript off; animation respects your reduced-motion setting; all images carry descriptive alt text.</p></div>
      <div class="info-card"><h3>Forms that help</h3><p>Every field is labelled, errors are explained in words next to the field, and sensitive questions simply aren't asked online.</p></div>
      <div class="info-card"><h3>Structure you can navigate</h3><p>Proper landmarks, heading order and a skip-to-content link on every page for screen reader and switch users.</p></div>
      <div class="info-card"><h3>Captions on video</h3><p>All produced video ships with captions. <span class="chip chip--sample">[PLACEHOLDER — Easy Read versions of key pages recommended as a post-launch enhancement]</span></p></div>
    </div>
    <div class="steps-note">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>
      <span><strong>Found something hard to use?</strong> Tell us — call <a href="tel:1300348227">1300 348 227</a> or email <a href="mailto:info@fitcaresupportservices.com.au">info@fitcaresupportservices.com.au</a>. Accessibility feedback goes to the top of the pile.</span>
    </div>
    <p style="color:var(--muted);font-size:.875rem">Statement prepared July 2026. <span class="chip chip--sample">[PLACEHOLDER — re-verify against the final production build and record known limitations before launch]</span></p>
  </div>
</section>
"""

# --------------------------------------------------------------------------
# registry + render
# --------------------------------------------------------------------------

PAGES4 = {
    "services/daily-living-support.html": ("Daily Living Support | FITCare Support Services",
        "Personal care, household tasks, gardening, errands and appointments — reliable NDIS daily living support across the Sunshine Coast and SEQ.", "services", DAILY_LIVING),
    "services/social-community-participation.html": ("Social & Community Participation | FITCare Support Services",
        "Group activities, outings, sport and life-skills coaching — NDIS community participation supports with energetic local support workers.", "services", SOCIAL_COMMUNITY),
    "services/transport-travel.html": ("Transport & Travel Assistance | FITCare Support Services",
        "Reliable NDIS transport support — appointments, activities, work and travel training across the Sunshine Coast and SEQ.", "services", TRANSPORT),
    "services/aged-care-supports.html": ("Aged Care Fitness Supports | FITCare Support Services",
        "Yoga, pilates, chair aerobics and water-based fitness for older Queenslanders — group classes and one-on-one wellness with FITCare.", "services", AGED_CARE),
    "locations/index.html": ("Service Areas | FITCare Support Services",
        "FITCare supports the Sunshine Coast, Gympie, Moreton Bay and North Brisbane — with 60+ local support workers and more areas coming.", "locations", LOCATIONS_HUB),
    "locations/gympie.html": ("NDIS Support Workers Gympie | FITCare Support Services",
        "Local FITCare support workers across the Gympie region — daily living, community participation, fitness and transport supports.", "locations", GYMPIE),
    "locations/moreton-bay.html": ("NDIS Support Workers Moreton Bay | FITCare Support Services",
        "FITCare support workers across Moreton Bay — Caboolture to the coast. Registered NDIS provider with a health and fitness difference.", "locations", MORETON_BAY),
    "locations/north-brisbane.html": ("NDIS Support Workers North Brisbane | FITCare Support Services",
        "FITCare is growing across North Brisbane — healthy, energetic NDIS support workers with the meet-and-greet matching model.", "locations", NORTH_BRISBANE),
    "team/index.html": ("Meet Our Support Workers | FITCare Support Services",
        "40+ FITCare support workers — over half with fitness qualifications. Browse the team and find someone who gets you.", "team", TEAM_PAGE),
    "team/profile-template.html": ("Support Worker Profile | FITCare Support Services",
        "FITCare support worker profile template — photo, specialities, bio and a direct request action.", "team", PROFILE_TEMPLATE),
    "activities.html": ("Activities Calendar | FITCare Support Services",
        "Weekly group activities across fitness, social, creative and outings — all abilities welcome, support workers included.", "activities", ACTIVITIES_PAGE),
    "coordinators.html": ("For Support Coordinators | FITCare Support Services",
        "Registration categories, service areas, capacity and a one-business-day referral pathway — everything coordinators need on one page.", "coordinators", COORDINATORS_PAGE),
    "about.html": ("About FITCare | Registered NDIS Provider Sunshine Coast",
        "FITCare's mission, values, NDIS registration categories and FIT College training partnership — care with real energy behind it.", None, ABOUT_PAGE),
    "careers.html": ("Careers | Support Worker Jobs Sunshine Coast & SEQ | FITCare",
        "Join 60+ health-and-fitness-minded support workers. Training via FIT College, real advancement, work that keeps you moving.", None, CAREERS_PAGE),
    "contact.html": ("Contact Us | FITCare Support Services",
        "Call 1300 348 227, email, or send a message — NDIS supports, aged care, careers or anything else. Reply within one business day.", None, CONTACT_PAGE),
    "resources/new-to-the-ndis.html": ("New to the NDIS? | FITCare Support Services",
        "The NDIS in plain English — what it is, how to apply, and how FITCare helps you use your plan, wherever you're up to.", None, NEW_TO_NDIS),
    "resources/faqs.html": ("FAQs | FITCare Support Services",
        "Straight answers about FITCare — registration, service areas, qualifications, funding and how to get started.", None, FAQS_PAGE),
    "resources/news.html": ("News & Stories | FITCare Support Services",
        "News and stories from the FITCare Community.", None, NEWS_PAGE),
    "resources/news-article-template.html": ("News Article | FITCare Support Services",
        "FITCare news article template.", None, NEWS_ARTICLE),
    "resources/feedback-complaints.html": ("Feedback & Complaints | FITCare Support Services",
        "Compliments, suggestions or complaints — how to tell FITCare, and how to reach the NDIS Quality and Safeguards Commission.", None, FEEDBACK_PAGE),
    "accessibility.html": ("Accessibility Statement | FITCare Support Services",
        "How this site targets WCAG 2.2 AA — keyboard access, contrast, plain English, reduced motion, and how to report barriers.", None, ACCESSIBILITY_PAGE),
}

def main():
    written = []
    for path, (title, desc, nav, body) in PAGES4.items():
        written.append(bp.render(path, title, desc, nav, body))
    print("wrote %d phase-4 pages" % len(written))
    for w in written:
        print("  ", os.path.relpath(w, bp.ROOT))

if __name__ == "__main__":
    main()
