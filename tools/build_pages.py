#!/usr/bin/env python3
"""FITCare prototype page generator.

Authors all site/*.html pages from one shared header/footer template so
navigation stays consistent. Run from the repo root:

    python3 tools/build_pages.py

The committed HTML output is the deliverable — a developer never needs to
run this. It exists so nav/footer edits happen in exactly one place.
"""
import os, sys, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")

LEAF = '<svg width="15" height="15" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 21C3 9 9 3 21 3 21 15 15 21 3 21Z" fill="currentColor"/></svg>'
PHONE = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
STAR = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01z"/></svg>'
STARS5 = '<div class="stars" aria-label="5 out of 5 stars">' + STAR * 5 + "</div>"

HEAD = """<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="FITCare Support Services">
<link rel="stylesheet" href="@/css/tokens.css">
<link rel="stylesheet" href="@/css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

HEADER = """<header class="site-head">
  <div class="wrap">
    <a class="logo" href="@/index.html" aria-label="FITCare Support Services — home">
      <span class="logo-line">
        <span class="logo-fit">F<span class="logo-i">I<svg class="logo-leaf" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 21C3 9 9 3 21 3 21 15 15 21 3 21Z" fill="currentColor"/></svg></span>T</span><span class="logo-care">Care</span>
      </span>
      <span class="logo-sub">Support Services</span>
    </a>
    <nav class="nav" aria-label="Main">
      <a href="@/services/index.html"{cur_services}>Services</a>
      <a href="@/locations/index.html"{cur_locations}>Service areas</a>
      <a href="@/team/index.html"{cur_team}>Our team</a>
      <a href="@/activities.html"{cur_activities}>Activities</a>
      <a href="@/coordinators.html"{cur_coordinators}>For coordinators</a>
    </nav>
    <div class="head-cta">
      <a class="call-chip" href="tel:1300348227">PHONE_ICON 1300 348 227</a>
      <a class="btn btn--primary btn--head" href="@/get-started.html">Get started</a>
    </div>
  </div>
</header>
<main id="main">
""".replace("PHONE_ICON", PHONE)

FOOTER = """</main>
<footer class="foot">
  <div class="wrap">
    <div class="foot-main">
      <div class="foot-brand">
        <span class="logo" aria-hidden="true">
          <span class="logo-line"><span class="logo-fit">FIT</span><span class="logo-care">Care</span></span>
          <span class="logo-sub">Support Services</span>
        </span>
        <p>Healthy support workers delivering healthy support work across the Sunshine Coast and South East Queensland.</p>
        <p>Suite 10, 102 Wises Road<br>Maroochydore QLD 4558</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="@/services/daily-living-support.html">Daily living support</a></li>
          <li><a href="@/services/social-community-participation.html">Social &amp; community</a></li>
          <li><a href="@/services/health-fitness-wellbeing.html">Health, fitness &amp; wellbeing</a></li>
          <li><a href="@/services/transport-travel.html">Transport &amp; travel</a></li>
          <li><a href="@/services/aged-care-supports.html">Aged care supports</a></li>
        </ul>
      </div>
      <div>
        <h4>FITCare</h4>
        <ul>
          <li><a href="@/team/index.html">Our team</a></li>
          <li><a href="@/activities.html">Activities</a></li>
          <li><a href="@/coordinators.html">For coordinators</a></li>
          <li><a href="@/about.html">About us</a></li>
          <li><a href="@/careers.html">Careers</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact &amp; resources</h4>
        <ul>
          <li><a href="tel:1300348227">1300 348 227</a></li>
          <li><a href="mailto:info@fitcaresupportservices.com.au">info@fitcaresupportservices.com.au</a></li>
          <li><a href="https://members.fitcaresupportservices.com.au/community/fitcare">Members portal</a></li>
          <li><a href="@/resources/feedback-complaints.html">Feedback &amp; complaints</a></li>
          <li><a href="https://fitcaresupportservices.com.au/storage/fitcare-participant-handbook.pdf">Participant handbook (PDF)</a></li>
          <li><a href="@/resources/new-to-the-ndis.html">New to the NDIS?</a></li>
        </ul>
      </div>
    </div>
    <div class="compliance">
      <p><strong>FITCare Support Services is a registered NDIS provider.</strong> We're committed to the NDIS Practice Standards and the NDIS Code of Conduct. Feedback and complaints are welcome — they make us better.</p>
      <p>Registration categories: Core 0107 · 0108 · 0120 · 0125 · 0136 &nbsp;|&nbsp; Capacity Building 0116 · 0117 · 0125 · 0126</p>
    </div>
    <div class="foot-legal">
      <a href="@/privacy.html">Privacy policy</a>
      <a href="@/terms.html">Terms &amp; conditions</a>
      <a href="@/accessibility.html">Accessibility statement</a>
      <span class="spacer"></span>
      <span>&copy; 2026 FITCare Support Services</span>
    </div>
  </div>
</footer>
<div class="callbar">
  <a class="btn btn--ghost" href="tel:1300348227">Call us</a>
  <a class="btn btn--primary" href="@/get-started.html">Get started</a>
</div>
<script src="@/js/site.js" defer></script>
</body>
</html>
"""

# --------------------------------------------------------------------------
# shared fragments
# --------------------------------------------------------------------------

TRUST_BAR = """<div class="trust" role="group" aria-label="Why trust FITCare">
  <div class="wrap">
    <div class="trust-item"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg><span><strong>Registered NDIS provider</strong><br>quality &amp; safeguards met</span></div>
    <div class="trust-item"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg><span><strong>60+ local support workers</strong><br>most from health &amp; fitness backgrounds</span></div>
    <div class="trust-item"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg><span><strong>Sunshine Coast to North Brisbane</strong><br>incl. Gympie &amp; Moreton Bay</span></div>
    <div class="trust-item"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg><span><strong>We reply within 1 business day</strong><br>or call us right now</span></div>
  </div>
</div>"""

STEPS = """<div class="steps">
  <div class="step"><span class="step-n" aria-hidden="true">1</span><h3>Say hello</h3><p>Call us or answer a few quick questions online. It takes about two minutes — we reply within one business day.</p></div>
  <div class="step"><span class="step-n" aria-hidden="true">2</span><h3>Meet &amp; greet</h3><p>Sit down with your Service Coordinator — your first point of contact. Tell us what a good week looks like for you.</p></div>
  <div class="step"><span class="step-n" aria-hidden="true">3</span><h3>Get matched</h3><p>We match you with support workers who fit your interests, goals and personality. Not the right fit? We'll rematch, no fuss.</p></div>
</div>"""

def team_card(name, tags, media_label="Photo"):
    chips = "".join('<span class="chip">%s</span>' % t for t in tags)
    return ('<div class="tw"><div class="media media--square" role="img" aria-label="Placeholder for %s\'s photo">'
            '<div class="media-label"><strong>Placeholder</strong>%s</div></div>'
            '<div class="tw-body"><h3>%s</h3><div class="tw-tags">%s</div>'
            '<a class="tw-link" href="@/team/index.html">View profile →</a></div></div>'
            % (name, media_label, name, chips))

def faq(items):
    out = ['<div class="faq">']
    for q, a in items:
        out.append("<details><summary>%s</summary><div class=\"faq-a\">%s</div></details>" % (q, a))
    out.append("</div>")
    return "\n".join(out)

def cta_final(h, p):
    return """<section class="section">
  <div class="wrap">
    <div class="cta-final">
      <svg class="leaf-bg" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 21C3 9 9 3 21 3 21 15 15 21 3 21Z" fill="currentColor"/></svg>
      <h2>%s</h2>
      <p>%s</p>
      <div class="hero-ctas">
        <a class="btn btn--light" href="@/get-started.html">Get started online</a>
        <a class="btn btn--outline-light" href="tel:1300348227">Call 1300 348 227</a>
      </div>
      <p class="cta-small">Support coordinators: <a href="@/get-started.html?who=coordinator" style="color:#fff">start a referral here</a>.</p>
    </div>
  </div>
</section>""" % (h, p)

REVIEW_CAROUSEL = """<div class="carousel" data-carousel>
  <div class="car-track-wrap">
    <div class="car-track" data-car-track>
      <div class="car-slide"><div class="review"><span class="chip chip--sample">Sample review</span>STARS<p>"[Sample] The activities calendar got my daughter out of the house three times a week. She's made real friends."</p><p class="who">[Name] — family member</p></div></div>
      <div class="car-slide"><div class="review"><span class="chip chip--sample">Sample review</span>STARS<p>"[Sample] As a coordinator I need providers who answer the phone. FITCare's intake team actually does."</p><p class="who">[Name] — support coordinator</p></div></div>
      <div class="car-slide"><div class="review"><span class="chip chip--sample">Sample review</span>STARS<p>"[Sample] My support worker gets me to the pool every Tuesday. With the right support, I do it my way."</p><p class="who">[Name] — FITCare participant</p></div></div>
    </div>
  </div>
  <div class="car-controls">
    <button class="car-btn" type="button" data-car-prev aria-label="Previous review"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg></button>
    <span class="car-status" data-car-status aria-live="polite">Review 1 of 3</span>
    <button class="car-btn" type="button" data-car-next aria-label="Next review"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg></button>
  </div>
</div>""".replace("STARS", STARS5)

GS_FORM = """<form class="gs" data-gs novalidate>
  <div class="gs-head">
    <ol class="gs-progress" data-gs-progress>
      <li aria-current="step"><span>1 · Who</span><div class="gs-bar"></div></li>
      <li><span>2 · Contact</span><div class="gs-bar"></div></li>
      <li><span>3 · Optional</span><div class="gs-bar"></div></li>
    </ol>
  </div>
  <div class="gs-body">
    <div class="gs-step active" data-gs-step="1">
      <h3>Hi there — who are we chatting with?</h3>
      <p class="gs-sub">This just helps us point you the right way. Takes about two minutes all up.</p>
      <fieldset data-req="who">
        <legend class="sr-only">Who is enquiring</legend>
        <div class="opts">
          <label class="opt"><input type="radio" name="who" value="participant"><span>I'm looking for support for myself</span></label>
          <label class="opt"><input type="radio" name="who" value="family"><span>I'm a family member or carer<small>Asking on behalf of someone I love</small></span></label>
          <label class="opt"><input type="radio" name="who" value="coordinator"><span>I'm a support coordinator<small>Referring a participant</small></span></label>
          <label class="opt"><input type="radio" name="who" value="other"><span>Something else</span></label>
        </div>
        <p class="err">Choose one so we know how to help.</p>
      </fieldset>
    </div>
    <div class="gs-step" data-gs-step="2">
      <h3 data-gs-heading2>Nice to meet you. How do we reach you?</h3>
      <p class="gs-sub">We'll be in touch within one business day.</p>
      <div class="gs-row">
        <div class="field" data-req="name"><label for="gs-name">Your name</label><input id="gs-name" name="name" type="text" autocomplete="name"><p class="err">We need a name to say hello properly.</p></div>
        <div class="field" data-org hidden><label for="gs-org">Organisation <small>(optional)</small></label><input id="gs-org" name="org" type="text" autocomplete="organization"></div>
      </div>
      <div class="gs-row">
        <div class="field" data-contact><label for="gs-phone">Phone</label><input id="gs-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel"><p class="err">Add a phone number or an email — whichever suits.</p></div>
        <div class="field"><label for="gs-email">Email</label><input id="gs-email" name="email" type="email" autocomplete="email"></div>
      </div>
      <fieldset>
        <legend>How do you prefer we contact you?</legend>
        <div class="opts opts--chips">
          <label class="opt"><input type="radio" name="pref" value="phone" checked><span>Phone call</span></label>
          <label class="opt"><input type="radio" name="pref" value="sms"><span>SMS</span></label>
          <label class="opt"><input type="radio" name="pref" value="email"><span>Email</span></label>
        </div>
      </fieldset>
      <div class="field">
        <label for="gs-region">Your area</label>
        <select id="gs-region" name="region">
          <option value="">Choose a region (optional)</option>
          <option>Sunshine Coast</option>
          <option>Gympie</option>
          <option>Moreton Bay</option>
          <option>North Brisbane</option>
          <option>Somewhere else / not sure</option>
        </select>
      </div>
    </div>
    <div class="gs-step" data-gs-step="3">
      <h3 data-gs-heading3>Anything you'd like us to know? All of this is optional.</h3>
      <div class="privacy-note">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        <span>Share only what you're comfortable with. Detailed support needs and NDIS plan information wait until the meet &amp; greet — never a web form.</span>
      </div>
      <fieldset>
        <legend>NDIS status <small style="font-weight:400;color:var(--muted)">(optional)</small></legend>
        <div class="opts opts--chips">
          <label class="opt"><input type="radio" name="ndis" value="have-plan"><span>Have a plan</span></label>
          <label class="opt"><input type="radio" name="ndis" value="waiting"><span>Waiting on a plan</span></label>
          <label class="opt"><input type="radio" name="ndis" value="not-yet"><span>Not on the NDIS yet</span></label>
          <label class="opt"><input type="radio" name="ndis" value="not-sure"><span>Not sure</span></label>
        </div>
      </fieldset>
      <fieldset>
        <legend>Interests <small style="font-weight:400;color:var(--muted)">(pick any)</small></legend>
        <div class="opts opts--chips">
          <label class="opt"><input type="checkbox" name="interests" value="fitness"><span>Fitness</span></label>
          <label class="opt"><input type="checkbox" name="interests" value="social"><span>Social</span></label>
          <label class="opt"><input type="checkbox" name="interests" value="creative"><span>Creative</span></label>
          <label class="opt"><input type="checkbox" name="interests" value="outings"><span>Outings</span></label>
          <label class="opt"><input type="checkbox" name="interests" value="everyday"><span>Everyday support</span></label>
        </div>
      </fieldset>
      <div class="field"><label for="gs-notes">Anything else? <small>(optional)</small></label><textarea id="gs-notes" name="notes" placeholder="Tell us as much or as little as you like."></textarea></div>
    </div>
    <div class="gs-success" data-gs-success>
      <span class="gs-ok"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></span>
      <h3 data-gs-thanks>Thanks! We've got it.</h3>
      <p>A real person will be in touch within <b>one business day</b>. If it's easier to chat now, call <a href="tel:1300348227"><b>1300 348 227</b></a>.</p>
    </div>
  </div>
  <div class="gs-foot" data-gs-foot>
    <button class="gs-back" type="button" data-gs-back>← Back</button>
    <span class="spacer"></span>
    <button class="gs-skip" type="button" data-gs-skip>Skip this step</button>
    <button class="btn btn--primary" type="button" data-gs-next>Continue</button>
  </div>
  <div class="gs-escape" data-gs-escape>Save time — skip the form and call <a href="tel:1300348227">1300 348 227</a></div>
</form>"""

# --------------------------------------------------------------------------
# page bodies (use @/ for site-root-relative links)
# --------------------------------------------------------------------------

HOME_BODY = """
<section class="hero" id="top">
  <div class="wrap">
    <div class="hero-copy">
      <span class="eyebrow">LEAF Registered NDIS provider · Sunshine Coast &amp; SEQ</span>
      <h1>With the right support, I do it <span class="hl">my way.</span></h1>
      <p class="hero-sub">FITCare matches you with healthy, energetic support workers — 60+ locals who bring fitness, wellbeing and genuine care to every visit, from everyday supports to training to become our next Olympian.</p>
      <div class="hero-ctas">
        <a class="btn btn--primary" href="@/get-started.html">Get started</a>
        <a class="btn btn--ghost" href="tel:1300348227">PHONE Call 1300 348 227</a>
      </div>
      <a class="hero-aside-link" href="@/team/index.html">Meet our support workers →</a>
    </div>
    <div class="media media--hero" role="img" aria-label="Placeholder for hero photo or video: support worker and participant enjoying an outdoor activity">
      <svg class="leaf-bg" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 21C3 9 9 3 21 3 21 15 15 21 3 21Z" fill="currentColor"/></svg>
      <div class="media-label"><strong>Placeholder — hero media</strong>Real photo or the existing hero video (fitcare-web-edit.mp4), re-edited with captions</div>
    </div>
  </div>
</section>

TRUST_BAR

<section class="section" id="pathways">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF Start here</span>
      <h2>Tell us who you are, and we'll show you the way</h2>
      <p>Three different journeys, one friendly team. Pick yours.</p>
    </div>
    <div class="paths">
      <a class="path" href="@/get-started.html?who=participant">
        <span class="path-ico"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 0 0-16 0"/></svg></span>
        <h3>I'm looking for support</h3>
        <p>See our activities, meet the team, and start with a friendly chat. No pressure, no long forms — just tell us a little about you.</p>
        <span class="path-go">Find your fit →</span>
      </a>
      <a class="path" href="@/about.html">
        <span class="path-ico"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7z"/></svg></span>
        <h3>I'm supporting someone I love</h3>
        <p>You want to know who's walking through the door. See our screening, our credentials and the people themselves — before you decide.</p>
        <span class="path-go">Why families choose FITCare →</span>
      </a>
      <a class="path" href="#coordinators">
        <span class="path-ico"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M16 13H8"/><path d="M16 17H8"/><path d="M10 9H8"/></svg></span>
        <h3>I'm a support coordinator</h3>
        <p>Registration categories, service areas and a fast referral pathway — everything you need on one page, no digging.</p>
        <span class="path-go">Go to the coordinator hub →</span>
      </a>
    </div>
    <p class="paths-careers">Looking for a job you'll love instead? <a href="@/careers.html"><strong>Careers at FITCare →</strong></a></p>
  </div>
</section>

<section class="section section--alt" id="services">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF What we do</span>
      <h2>Support for every part of your day</h2>
      <p>From help at home to getting out and getting active — delivered your way, around your goals.</p>
    </div>
    <div class="svc-grid svc-grid--centerlast">
      <a class="svc" href="@/services/daily-living-support.html">
        <span class="svc-ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 9.5 12 3l9 6.5"/><path d="M5 10v10h14V10"/><path d="M9 20v-6h6v6"/></svg></span>
        <h3>Daily living support</h3><p>A hand with the everyday — personal care, household tasks, gardening, errands and appointments.</p><span class="svc-go">Learn more →</span>
      </a>
      <a class="svc" href="@/services/social-community-participation.html">
        <span class="svc-ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></span>
        <h3>Social &amp; community participation</h3><p>Group activities, outings, sport and events — building skills and friendships in your community.</p><span class="svc-go">Learn more →</span>
      </a>
      <a class="svc" href="@/services/health-fitness-wellbeing.html">
        <span class="svc-ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.42 4.58a5.4 5.4 0 0 0-7.65 0l-.77.78-.77-.78a5.4 5.4 0 0 0-7.65 7.65l8.42 8.42 8.42-8.42a5.4 5.4 0 0 0 0-7.65z"/></svg></span>
        <h3>Health, fitness &amp; wellbeing</h3><p>One-on-one wellness programs, exercise physiology and personal training — find your fit and make it fun.</p><span class="svc-go">Learn more →</span>
      </a>
      <a class="svc" href="@/services/transport-travel.html">
        <span class="svc-ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 17h14l-1.5-4.5h-11z"/><circle cx="7.5" cy="17.5" r="2"/><circle cx="16.5" cy="17.5" r="2"/><path d="M5 12.5V7a1 1 0 0 1 1-1h9l3 6.5"/></svg></span>
        <h3>Transport &amp; travel</h3><p>Getting you where you need to be — appointments, activities, work or wherever the day takes you.</p><span class="svc-go">Learn more →</span>
      </a>
      <a class="svc" href="@/services/aged-care-supports.html">
        <span class="svc-ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><path d="M9 9h.01"/><path d="M15 9h.01"/></svg></span>
        <h3>Aged care supports</h3><p>Yoga, pilates, chair aerobics and water-based fitness — staying active and social at every age.</p><span class="svc-go">Learn more →</span>
      </a>
    </div>
  </div>
</section>

<section class="section" id="how">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF How it works</span>
      <h2>Three easy steps to the right support worker</h2>
    </div>
    STEPS
    <div class="steps-note">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
      <span><strong>No fitness goals required</strong> — and if your plan doesn't fund personal training, our supports can often be delivered through your core or capacity building funding.</span>
    </div>
  </div>
</section>

<section class="band" aria-label="Our promise">
  <svg class="leaf-bg" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 21C3 9 9 3 21 3 21 15 15 21 3 21Z" fill="currentColor"/></svg>
  <svg class="leaf-bg leaf-bg--2" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 21C3 9 9 3 21 3 21 15 15 21 3 21Z" fill="currentColor"/></svg>
  <div class="wrap">
    <span class="band-script">Healthy support workers</span>
    <p class="band-main">delivering healthy support work.</p>
    <p class="band-sub">It's been our promise since day one — and it's why over half our team hold fitness qualifications.</p>
  </div>
</section>

<section class="section" id="team">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF Meet the team</span>
      <h2>Real people, and plenty of them</h2>
      <p>40+ support workers — including swim instructors, yoga teachers, footy coaches and distance runners. <span class="chip chip--sample">Sample presentation — real photos &amp; bios from the current directory</span></p>
    </div>
    <div class="team-grid">
      TEAM_CARDS
    </div>
    <p style="margin-top:22px"><a href="@/team/index.html"><strong>See the whole team →</strong></a></p>
  </div>
</section>

<section class="section section--alt" id="activities">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF Group activities</span>
      <h2>Something on every week</h2>
      <p>Fitness, social, creative and outings — a real calendar, readable by everyone (and by Google, too). <span class="chip chip--sample">Sample cards — real schedule migrates in Phase 4</span></p>
    </div>
    <div class="act-grid">
      <div class="act"><div class="media media--wide" role="img" aria-label="Placeholder photo: lawn bowls"><div class="media-label"><strong>Placeholder</strong>Photo — lawn bowls</div></div><div class="act-body"><span class="chip">Social</span><h3>Lawn bowls &amp; lunch</h3><div class="act-when"><span>[Day &amp; time]</span></div><p>A friendly roll-up followed by lunch with the crew. All abilities welcome.</p></div></div>
      <div class="act"><div class="media media--wide" role="img" aria-label="Placeholder photo: pottery class"><div class="media-label"><strong>Placeholder</strong>Photo — pottery</div></div><div class="act-body"><span class="chip">Creative</span><h3>Pottery studio</h3><div class="act-when"><span>[Day &amp; time]</span></div><p>Get your hands dirty and make something worth keeping.</p></div></div>
      <div class="act"><div class="media media--wide" role="img" aria-label="Placeholder photo: group fitness session"><div class="media-label"><strong>Placeholder</strong>Photo — group fitness</div></div><div class="act-body"><span class="chip">Fitness</span><h3>Group fitness</h3><div class="act-when"><span>[Day &amp; time]</span></div><p>Move at your own pace with a team that cheers you on.</p></div></div>
    </div>
    <p style="margin-top:22px"><a href="@/activities.html"><strong>See what's on →</strong></a></p>
  </div>
</section>

<section class="section" aria-label="What families say">
  <div class="wrap">
    <div class="quote-card">
      <span class="chip chip--sample">Sample content — real testimonials pending consent program</span>
      <span class="quote-mark" aria-hidden="true">"</span>
      <blockquote>The best part isn't the gym sessions — it's that his support worker turns up with a plan and a smile, every single time.</blockquote>
      STARS
      <p class="quote-who"><strong>[Name]</strong> — parent of a FITCare participant</p>
    </div>
  </div>
</section>

<section class="section" id="coordinators" style="padding-top:0">
  <div class="wrap">
    <div class="coord">
      <div class="coord-copy">
        <span class="eyebrow">LEAF For support coordinators</span>
        <h2>Refer in minutes, not meetings</h2>
        <p>Everything you need at a glance — our registration categories, service areas and a direct line to intake. Start a referral online and we'll pick it up within one business day, or call us and sort it now.</p>
        <div class="coord-ctas">
          <a class="btn btn--light" href="@/get-started.html?who=coordinator">Start a referral</a>
          <a class="btn btn--outline-light" href="@/coordinators.html">Coordinator hub →</a>
        </div>
      </div>
      <div class="coord-facts">
        <div class="fact"><h4>Registered categories — Core</h4><div class="codes"><span>0107 Personal Activities</span><span>0108 Transport &amp; Travel</span><span>0120 Household Tasks</span><span>0125 Community Participation</span><span>0136 Group &amp; Centre Based</span></div></div>
        <div class="fact"><h4>Registered categories — Capacity Building</h4><div class="codes"><span>0116 Innovative Community Participation</span><span>0117 Daily Living &amp; Life Skills</span><span>0125 Community Participation</span><span>0126 Exercise Physiology &amp; PT</span></div></div>
        <div class="fact"><h4>Intake</h4><p>1300 348 227 · info@fitcaresupportservices.com.au<br>Sunshine Coast · Gympie · Moreton Bay · North Brisbane</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt" id="faq">
  <div class="wrap">
    <div class="sec-head sec-head--center">
      <span class="eyebrow">LEAF Good to know</span>
      <h2>Questions people ask us</h2>
    </div>
    HOME_FAQ
  </div>
</section>

HOME_CTA
"""

SERVICES_HUB_BODY = """
<section class="section" style="padding-bottom:clamp(32px,5vw,56px)">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:0">
      <span class="eyebrow">LEAF Services</span>
      <h1 style="font-size:clamp(2.1rem,4.6vw,3.2rem);font-weight:800">Support for every part of your day</h1>
      <p>Every support is person-centred and built around your goals — delivered by healthy, energetic locals across the Sunshine Coast and South East Queensland. Pick a service to see how it works.</p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="svc-grid svc-grid--centerlast">
      <a class="svc" href="@/services/daily-living-support.html"><span class="svc-ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 9.5 12 3l9 6.5"/><path d="M5 10v10h14V10"/><path d="M9 20v-6h6v6"/></svg></span><h3>Daily living support</h3><p>Personal care, household tasks, gardening, errands and appointments — a reliable hand with the everyday, your way.</p><span class="svc-go">Learn more →</span></a>
      <a class="svc" href="@/services/social-community-participation.html"><span class="svc-ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></span><h3>Social &amp; community participation</h3><p>Group activities, outings, sport, life-skills coaching and events — building confidence and friendships in your community.</p><span class="svc-go">Learn more →</span></a>
      <a class="svc" href="@/services/health-fitness-wellbeing.html"><span class="svc-ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.42 4.58a5.4 5.4 0 0 0-7.65 0l-.77.78-.77-.78a5.4 5.4 0 0 0-7.65 7.65l8.42 8.42 8.42-8.42a5.4 5.4 0 0 0 0-7.65z"/></svg></span><h3>Health, fitness &amp; wellbeing</h3><p>Wellness programs, exercise physiology and personal training with support workers who train too. Find your fit.</p><span class="svc-go">Learn more →</span></a>
      <a class="svc" href="@/services/transport-travel.html"><span class="svc-ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 17h14l-1.5-4.5h-11z"/><circle cx="7.5" cy="17.5" r="2"/><circle cx="16.5" cy="17.5" r="2"/><path d="M5 12.5V7a1 1 0 0 1 1-1h9l3 6.5"/></svg></span><h3>Transport &amp; travel</h3><p>Getting you where you need to be — appointments, activities, work or wherever the day takes you.</p><span class="svc-go">Learn more →</span></a>
      <a class="svc" href="@/services/aged-care-supports.html"><span class="svc-ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><path d="M9 9h.01"/><path d="M15 9h.01"/></svg></span><h3>Aged care supports</h3><p>Yoga, pilates, chair aerobics and water-based fitness — staying active, social and independent at every age.</p><span class="svc-go">Learn more →</span></a>
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
<section class="section">
  <div class="wrap" style="display:grid;gap:28px">
    <div class="trust-strip">
      <span><b>Registered NDIS provider</b></span><span class="dot">•</span>
      <span>Core 0107 · 0108 · 0120 · 0125 · 0136</span><span class="dot">•</span>
      <span>Capacity Building 0116 · 0117 · 0125 · 0126</span><span class="dot">•</span>
      <span>Regulated by the NDIS Quality &amp; Safeguards Commission</span><span class="dot">•</span>
      <a href="@/resources/feedback-complaints.html">Feedback &amp; complaints</a>
    </div>
  </div>
</section>
HUB_CTA
"""

SERVICE_PAGE_BODY = """
<section class="hero hero--page">
  <div class="wrap">
    <div class="hero-copy">
      <span class="eyebrow">LEAF Services · Health, fitness &amp; wellbeing</span>
      <h1>Feel stronger <span class="hl">every week.</span></h1>
      <p class="hero-sub">Gym, pool, park or living room — our support workers train alongside you and make wellness genuinely fun. No fitness goals required to start.</p>
      <div class="hero-ctas">
        <a class="btn btn--primary" href="@/get-started.html">Get started</a>
        <a class="btn btn--ghost" href="tel:1300348227">PHONE Call 1300 348 227</a>
      </div>
    </div>
    <div class="media media--hero" role="img" aria-label="Placeholder for photo: support worker and participant training together">
      <svg class="leaf-bg" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 21C3 9 9 3 21 3 21 15 15 21 3 21Z" fill="currentColor"/></svg>
      <div class="media-label"><strong>Placeholder</strong>Photo — training session, real participant &amp; worker (consent required)</div>
    </div>
  </div>
</section>

TRUST_BAR

<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF What we help with</span>
      <h2>Real support, real movement</h2>
      <p>Plain and simple — here's what a health &amp; wellbeing support can look like with FITCare.</p>
    </div>
    <div class="svc-grid">
      <div class="svc"><h3>Gym sessions together</h3><p>Train with a support worker who actually trains — spotting, encouraging and keeping it safe.</p></div>
      <div class="svc"><h3>Swimming &amp; aqua fitness</h3><p>Pool sessions with confident swimmers — including qualified swim instructors on the team.</p></div>
      <div class="svc"><h3>Walking &amp; running groups</h3><p>From a gentle lap of the park to training for a fun run — at your pace, always.</p></div>
      <div class="svc"><h3>Yoga, pilates &amp; chair aerobics</h3><p>Gentler movement for strength and balance — popular with our aged care participants too.</p></div>
      <div class="svc"><h3>Your own wellness program</h3><p>A program built around your goals — in the gym or through activities you already love.</p></div>
      <div class="svc"><h3>Exercise physiology &amp; PT</h3><p>Registered capacity building support (0126) with qualified professionals.</p></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF How it works</span>
      <h2>Three easy steps to the right support worker</h2>
    </div>
    STEPS
    <div class="steps-note">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
      <span><strong>No personal training funding in your plan?</strong> These supports can often be delivered through your core and/or capacity building funding — ask us how at the meet &amp; greet.</span>
    </div>
  </div>
</section>

<section class="section" aria-label="Reviews">
  <div class="wrap">
    <div class="sec-head sec-head--center">
      <span class="eyebrow">LEAF What people say</span>
      <h2>Don't take our word for it</h2>
    </div>
    REVIEW_CAROUSEL
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF Meet some of the team</span>
      <h2>Support workers who love this stuff</h2>
      <p>Over half our team hold fitness qualifications. <span class="chip chip--sample">Sample presentation</span></p>
    </div>
    <div class="team-grid">
      TEAM_CARDS
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF Watch</span>
      <h2>See a session in action</h2>
    </div>
    <div class="video-block" data-video>
      <svg class="leaf-bg" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 21C3 9 9 3 21 3 21 15 15 21 3 21Z" fill="currentColor"/></svg>
      <button class="video-play" type="button" data-video-play>
        <span class="video-play-btn" aria-hidden="true"><svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
        <span>Play: wellness session <em>([PLACEHOLDER — video to be produced])</em></span>
      </button>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head sec-head--center">
      <span class="eyebrow">LEAF Good to know</span>
      <h2>Questions about fitness supports</h2>
    </div>
    SERVICE_FAQ
  </div>
</section>

SERVICE_CTA
"""

LOCATION_PAGE_BODY = """
<section class="hero hero--page">
  <div class="wrap">
    <div class="hero-copy">
      <span class="eyebrow">LEAF Service areas · Sunshine Coast</span>
      <h1>Your Sunshine Coast <span class="hl">support crew.</span></h1>
      <p class="hero-sub">Our home turf — the FITCare office is in Maroochydore, and most of our 60+ support workers live and work right here on the Coast.</p>
      <div class="hero-ctas">
        <a class="btn btn--primary" href="@/get-started.html">Get started</a>
        <a class="btn btn--ghost" href="tel:1300348227">PHONE Call 1300 348 227</a>
      </div>
    </div>
    <div class="media media--hero" role="img" aria-label="Placeholder for photo: FITCare activity on the Sunshine Coast">
      <svg class="leaf-bg" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 21C3 9 9 3 21 3 21 15 15 21 3 21Z" fill="currentColor"/></svg>
      <div class="media-label"><strong>Placeholder</strong>Photo — genuine local shot (beach walk, group activity)</div>
    </div>
  </div>
</section>

TRUST_BAR

<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF Where we work</span>
      <h2>Across the Coast, from Caloundra to Noosa</h2>
      <p><span class="chip chip--sample">Placeholder list — confirm exact coverage with intake before launch</span></p>
    </div>
    <div class="suburbs">
      <span class="chip">Maroochydore</span><span class="chip">Mooloolaba</span><span class="chip">Kawana</span><span class="chip">Caloundra</span><span class="chip">Buderim</span><span class="chip">Sippy Downs</span><span class="chip">Nambour</span><span class="chip">Coolum</span><span class="chip">Noosa</span><span class="chip">Beerwah</span><span class="chip">…and surrounds</span>
    </div>
    <div class="map-ph" style="margin-top:28px" role="img" aria-label="Placeholder for embedded service area map">
      [PLACEHOLDER — embedded map of the Sunshine Coast service area]<br>Office: Suite 10, 102 Wises Road, Maroochydore QLD 4558
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF How it works</span>
      <h2>Three easy steps to the right support worker</h2>
    </div>
    STEPS
  </div>
</section>

<section class="section" aria-label="Local testimonial">
  <div class="wrap">
    <div class="pull-band">
      <svg class="leaf-bg" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 21C3 9 9 3 21 3 21 15 15 21 3 21Z" fill="currentColor"/></svg>
      <span class="chip chip--sample" style="margin-bottom:16px">Sample content</span>
      <p>"They didn't just find me a support worker. They found me a training partner."</p>
      <p class="who">[Name] — FITCare participant, Sunshine Coast</p>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF Local team</span>
      <h2>Support workers near you</h2>
      <p><span class="chip chip--sample">Sample presentation — filtered to Sunshine Coast in production</span></p>
    </div>
    <div class="team-grid">
      TEAM_CARDS
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">LEAF What's on locally</span>
      <h2>Activity highlights on the Coast</h2>
      <p><span class="chip chip--sample">Sample cards — real schedule migrates in Phase 4</span></p>
    </div>
    <div class="act-grid">
      <div class="act"><div class="media media--wide" role="img" aria-label="Placeholder photo: lawn bowls"><div class="media-label"><strong>Placeholder</strong>Photo</div></div><div class="act-body"><span class="chip">Social</span><h3>Lawn bowls &amp; lunch</h3><div class="act-when"><span>[Day &amp; time]</span></div><p>A friendly roll-up followed by lunch with the crew.</p></div></div>
      <div class="act"><div class="media media--wide" role="img" aria-label="Placeholder photo: aqua fitness"><div class="media-label"><strong>Placeholder</strong>Photo</div></div><div class="act-body"><span class="chip">Fitness</span><h3>Aqua fitness</h3><div class="act-when"><span>[Day &amp; time]</span></div><p>Low-impact, high-fun water workout with the swim crew.</p></div></div>
      <div class="act"><div class="media media--wide" role="img" aria-label="Placeholder photo: local markets"><div class="media-label"><strong>Placeholder</strong>Photo</div></div><div class="act-body"><span class="chip">Outings</span><h3>Local markets trip</h3><div class="act-when"><span>[Day &amp; time]</span></div><p>Wander the stalls, grab a coffee, take home something good.</p></div></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head sec-head--center">
      <span class="eyebrow">LEAF Good to know</span>
      <h2>Sunshine Coast questions</h2>
    </div>
    LOCATION_FAQ
  </div>
</section>

LOCATION_CTA
"""

GET_STARTED_BODY = """
<section class="section" style="padding-bottom:clamp(24px,4vw,40px)">
  <div class="wrap">
    <div class="sec-head sec-head--center" style="margin-bottom:0">
      <span class="eyebrow">LEAF Get started</span>
      <h1 style="font-size:clamp(2.1rem,4.6vw,3.2rem);font-weight:800">Let's find your fit</h1>
      <p>A few quick questions — nothing personal, nothing you're not ready to share. We reply within one business day.</p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    GS_FORM
    <div class="gs-aside">
      <span class="chip chip--ok">No NDIS details needed today</span>
      <span class="chip chip--ok">Reply within 1 business day</span>
      <span class="chip chip--ok">Prefer to talk? 1300 348 227</span>
    </div>
    <p style="text-align:center;margin-top:26px;color:var(--muted);font-size:.9375rem">Looking for a job instead? Head to <a href="@/careers.html"><strong>Careers at FITCare</strong></a>.</p>
  </div>
</section>
"""

# --------------------------------------------------------------------------
# FAQs & CTAs
# --------------------------------------------------------------------------

HOME_FAQ = faq([
    ("Is FITCare a registered NDIS provider?",
     "Yes. FITCare Support Services is a registered NDIS provider, which means we meet the NDIS Quality and Safeguards Commission's requirements. You'll find our registration categories on our About page."),
    ("Where do you provide support?",
     "Our 60+ support workers currently service the Sunshine Coast, Moreton Bay and Gympie — and we're expanding into parts of Brisbane and the Gold Coast."),
    ("Do I need fitness goals to join?",
     "Not at all. Plenty of our participants just want great everyday support. The health and fitness background of our team simply means you get energetic, positive people — whatever your goals are."),
    ("How do I get started?",
     "Call us or use the Get Started form. We'll arrange a relaxed meet and greet with a Service Coordinator — your first point of contact — who'll get to know you and match you with the right support workers."),
])

SERVICE_FAQ = faq([
    ("My plan doesn't fund personal training — can I still do this?",
     "Very likely, yes. Our health and fitness supports can often be delivered through your core and/or capacity building funding. Bring your plan to the meet &amp; greet and we'll walk through it together."),
    ("Do I need to be sporty or have fitness goals?",
     "No. Some participants train hard, some just want a walk and a chat. Your program is built around what you enjoy — the only rule is that it should feel good."),
    ("Who runs the sessions?",
     "FITCare support workers — over half hold fitness qualifications, and the team includes swim instructors, yoga teachers, football coaches and distance runners. Exercise physiology and personal training are delivered under our registered capacity building supports."),
    ("Where do sessions happen?",
     "Wherever works for you — a gym, the pool, a park, or at home. Your support worker comes to you."),
])

LOCATION_FAQ = faq([
    ("Do you service my suburb?",
     "If you're on the Sunshine Coast, almost certainly — our office is in Maroochydore and most of our team live locally. Call 1300 348 227 and we'll confirm on the spot."),
    ("What if I'm outside the Sunshine Coast?",
     "We also service Gympie, Moreton Bay and North Brisbane, and we're expanding into parts of Brisbane and the Gold Coast. Get in touch and we'll let you know where things stand."),
    ("How do I get started?",
     "Call us or use the Get Started form. We'll set up a relaxed meet &amp; greet with a Service Coordinator, then match you with local support workers."),
])

HOME_CTA = cta_final("Ready when you are",
    "Answer a few quick questions — or skip the typing and give us a call. Either way, we'll get back to you within one business day.")
HUB_CTA = cta_final("Not sure which support fits?",
    "That's exactly what the meet &amp; greet is for. Start the conversation and we'll figure it out together.")
SERVICE_CTA = cta_final("Ready to find your fit?",
    "Tell us a little about you — or call and chat it through. We'll reply within one business day.")
LOCATION_CTA = cta_final("Ready when you are, Sunshine Coast",
    "Tell us a little about you — or call the Maroochydore office and chat it through. We'll reply within one business day.")

TEAM_CARDS = "\n".join([
    team_card("Allison", ["Swimming", "Community outings"]),
    team_card("Bruce", ["Strength training", "Lawn bowls"]),
    team_card("Carissa", ["Yoga", "Daily living"]),
    team_card("Dan", ["Running", "Footy"]),
])

# --------------------------------------------------------------------------
# page registry
# --------------------------------------------------------------------------

def fill(body):
    return (body
            .replace("TRUST_BAR", TRUST_BAR)
            .replace("STEPS", STEPS)
            .replace("TEAM_CARDS", TEAM_CARDS)
            .replace("REVIEW_CAROUSEL", REVIEW_CAROUSEL)
            .replace("GS_FORM", GS_FORM)
            .replace("HOME_FAQ", HOME_FAQ)
            .replace("SERVICE_FAQ", SERVICE_FAQ)
            .replace("LOCATION_FAQ", LOCATION_FAQ)
            .replace("HOME_CTA", HOME_CTA)
            .replace("HUB_CTA", HUB_CTA)
            .replace("SERVICE_CTA", SERVICE_CTA)
            .replace("LOCATION_CTA", LOCATION_CTA)
            .replace("STARS", STARS5)
            .replace("LEAF", LEAF)
            .replace("PHONE", PHONE))

PAGES = {
    "index.html": {
        "title": "FITCare Support Services | NDIS Support Workers Sunshine Coast & SEQ",
        "desc": "Registered NDIS provider with 60+ healthy, energetic support workers across the Sunshine Coast, Gympie, Moreton Bay and North Brisbane. With the right support, I do it my way.",
        "nav": None,
        "body": HOME_BODY,
    },
    "services/index.html": {
        "title": "NDIS Services | FITCare Support Services",
        "desc": "Daily living, social and community participation, health and fitness, transport, and aged care supports — person-centred and delivered your way across South East Queensland.",
        "nav": "services",
        "body": SERVICES_HUB_BODY,
    },
    "services/health-fitness-wellbeing.html": {
        "title": "Health, Fitness & Wellbeing Supports | FITCare Support Services",
        "desc": "Gym sessions, swimming, wellness programs, exercise physiology and personal training with NDIS support workers who train too. Sunshine Coast and South East Queensland.",
        "nav": "services",
        "body": SERVICE_PAGE_BODY,
    },
    "locations/sunshine-coast.html": {
        "title": "NDIS Support Workers Sunshine Coast | FITCare Support Services",
        "desc": "FITCare's home turf — Maroochydore office, local support workers and weekly activities across the Sunshine Coast. Registered NDIS provider.",
        "nav": "locations",
        "body": LOCATION_PAGE_BODY,
    },
    "get-started.html": {
        "title": "Get Started | FITCare Support Services",
        "desc": "Three quick steps to begin with FITCare — no long forms, no sensitive questions, reply within one business day. Or call 1300 348 227.",
        "nav": None,
        "body": GET_STARTED_BODY,
    },
}

STUBS = [
    ("services/daily-living-support.html", "Daily Living Support", "services"),
    ("services/social-community-participation.html", "Social & Community Participation", "services"),
    ("services/transport-travel.html", "Transport & Travel", "services"),
    ("services/aged-care-supports.html", "Aged Care Supports", "services"),
    ("locations/index.html", "Service Areas", "locations"),
    ("locations/gympie.html", "Gympie", "locations"),
    ("locations/moreton-bay.html", "Moreton Bay", "locations"),
    ("locations/north-brisbane.html", "North Brisbane", "locations"),
    ("team/index.html", "Meet Our Support Workers", "team"),
    ("activities.html", "Activities", "activities"),
    ("coordinators.html", "For Support Coordinators", "coordinators"),
    ("about.html", "About FITCare", None),
    ("careers.html", "Careers at FITCare", None),
    ("contact.html", "Contact Us", None),
    ("resources/new-to-the-ndis.html", "New to the NDIS?", None),
    ("resources/faqs.html", "FAQs", None),
    ("resources/news.html", "News & Resources", None),
    ("resources/feedback-complaints.html", "Feedback & Complaints", None),
    ("privacy.html", "Privacy Policy", None),
    ("terms.html", "Terms & Conditions", None),
    ("accessibility.html", "Accessibility Statement", None),
]

STUB_BODY = """
<div class="stub">
  <div class="stub-inner">
    <span class="chip">Coming in Phase {phase}</span>
    <h1>{title}</h1>
    <p>This page is scoped in the project brief and will be built in Phase {phase} of the prototype. The navigation is already final so every journey can be click-tested today.</p>
    <div class="hero-ctas" style="justify-content:center">
      <a class="btn btn--primary" href="@/get-started.html">Get started</a>
      <a class="btn btn--ghost" href="@/index.html">Back to home</a>
    </div>
  </div>
</div>
"""

def depth_prefix(path):
    d = path.count("/")
    return "../" * d

def render(path, title, desc, nav, body):
    root = depth_prefix(path)
    cur = {"services": "", "locations": "", "team": "", "activities": "", "coordinators": ""}
    if nav in cur:
        cur[nav] = ' aria-current="page"'
    html = (HEAD.format(title=title, desc=desc)
            + HEADER.format(cur_services=cur["services"], cur_locations=cur["locations"],
                            cur_team=cur["team"], cur_activities=cur["activities"],
                            cur_coordinators=cur["coordinators"])
            + fill(body)
            + FOOTER)
    html = html.replace("@/", root)
    out = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(html)
    return out

def main():
    written = []
    for path, meta in PAGES.items():
        written.append(render(path, meta["title"], meta["desc"], meta["nav"], meta["body"]))
    for path, title, nav in STUBS:
        phase = "5" if path in ("privacy.html", "terms.html", "accessibility.html") else "4"
        body = STUB_BODY.replace("{title}", title).replace("{phase}", phase)
        written.append(render(path, title + " | FITCare Support Services",
                              title + " — page under construction in the FITCare rebuild prototype.",
                              nav, body))
    print("wrote %d pages" % len(written))
    for w in written:
        print("  ", os.path.relpath(w, ROOT))

if __name__ == "__main__":
    main()
