#!/usr/bin/env python3
"""Build the single-file wired-up demo of the whole prototype.

Bundles every site/ page into one HTML file with a tiny hash router:
shared header/footer render once, page <main> contents become routes,
all internal links become #/route links, images and fonts are inlined
once (deduped via a JS asset map). Output: prototype/fitcare-demo.html

Run from repo root:  python3 tools/build_demo.py
"""
import base64, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")
OUT = os.path.join(ROOT, "prototype", "fitcare-demo.html")

# route order = nav sanity; every .html page except the self-contained
# component library (its own CSS would clash inside the bundle)
PAGES = []
for root, _, files in os.walk(SITE):
    for f in sorted(files):
        if f.endswith(".html") and f != "components.html":
            rel = os.path.relpath(os.path.join(root, f), SITE)
            PAGES.append(rel)
PAGES.sort(key=lambda p: (p != "index.html", p))

def route_of(rel):
    return rel[:-5]  # strip .html

# ---- css with fonts inlined ----
tokens = open(os.path.join(SITE, "css/tokens.css")).read()
for fn in ["bricolage-grotesque.woff2", "figtree.woff2", "dancing-script.woff2"]:
    b64 = base64.b64encode(open(os.path.join(SITE, "assets/fonts", fn), "rb").read()).decode()
    tokens = tokens.replace("url('../assets/fonts/%s')" % fn,
                            "url(data:font/woff2;base64,%s)" % b64)
sitecss = open(os.path.join(SITE, "css/site.css")).read()
js = open(os.path.join(SITE, "js/site.js")).read()

# ---- asset map (each image embedded exactly once) ----
ASSETS, asset_keys = {}, {}
def asset_key(abspath):
    if abspath not in asset_keys:
        key = "a%d" % len(asset_keys)
        mime = "image/png" if abspath.endswith(".png") else "image/jpeg"
        ASSETS_b64 = base64.b64encode(open(abspath, "rb").read()).decode()
        ASSETS[key] = "data:%s;base64,%s" % (mime, ASSETS_b64)
        asset_keys[abspath] = key
    return asset_keys[abspath]

routes_set = {route_of(p) for p in PAGES}

def process_body(rel, html):
    srcdir = os.path.dirname(rel)
    m = re.search(r"<main id=\"main\">(.*?)</main>", html, re.S)
    body = m.group(1)

    def map_href(mm):
        href = mm.group(1)
        if href.startswith(("http", "tel:", "mailto:")):
            return mm.group(0)
        if href.startswith("#"):
            return 'href="%s" data-anchor' % href  # in-page anchor
        path = href
        query = ""
        if "?" in path:
            path, query = path.split("?", 1)
        frag = ""
        if "#" in path:
            path, frag = path.split("#", 1)
        norm = os.path.normpath(os.path.join(srcdir, path))
        r = route_of(norm) if norm.endswith(".html") else norm
        if r in routes_set:
            out = "#/" + r
            if query:
                out += "?" + query
            if frag:
                out += "&anchor=" + frag
            return 'href="%s"' % out
        return mm.group(0)  # PDFs, unknown → leave (external)

    def map_src(mm):
        src = mm.group(1)
        if src.startswith(("http", "data:")):
            return mm.group(0)
        p = os.path.normpath(os.path.join(SITE, srcdir, src))
        if os.path.exists(p):
            return 'src="" data-asset="%s"' % asset_key(p)
        return mm.group(0)

    body = re.sub(r'href="([^"]+)"', map_href, body)
    body = re.sub(r'src="([^"]+)"', map_src, body)
    title = re.search(r"<title>(.*?)</title>", html, re.S).group(1)
    return body, title

sections, titles = [], {}
for rel in PAGES:
    html = open(os.path.join(SITE, rel)).read()
    body, title = process_body(rel, html)
    r = route_of(rel)
    titles[r] = title
    sections.append('<section class="route" data-route="%s" hidden>\n%s\n</section>' % (r, body))

# ---- shared chrome from index.html, links rewritten the same way ----
index_html = open(os.path.join(SITE, "index.html")).read()
def chrome(pattern):
    m = re.search(pattern, index_html, re.S)
    frag = m.group(0)
    def map_href(mm):
        href = mm.group(1)
        if href.startswith(("http", "tel:", "mailto:", "#")):
            return mm.group(0)
        path = href.split("?")[0]
        q = ("?" + href.split("?", 1)[1]) if "?" in href else ""
        r = route_of(os.path.normpath(path)) if path.endswith(".html") else None
        if r in routes_set:
            return 'href="#/%s%s"' % (r, q)
        return mm.group(0)
    frag = re.sub(r'href="([^"]+)"', map_href, frag)
    def map_src(mm):
        src = mm.group(1)
        p = os.path.normpath(os.path.join(SITE, src))
        if os.path.exists(p):
            return 'src="" data-asset="%s"' % asset_key(p)
        return mm.group(0)
    return re.sub(r'src="([^"]+)"', map_src, frag)

header = chrome(r"<header class=\"site-head\">.*?</header>")
footer = chrome(r"<footer class=\"foot\">.*?</footer>")
callbar = chrome(r"<div class=\"callbar\">.*?</div>\n</div>|<div class=\"callbar\">.*?</div>\s*<script")
callbar = re.sub(r"\s*<script.*$", "", callbar, flags=re.S)

router_js = """
/* ---- demo hash router (demo bundle only — not part of the site) ---- */
(function () {
  "use strict";
  var ASSETS = __ASSETS__;
  var TITLES = __TITLES__;
  document.querySelectorAll("img[data-asset]").forEach(function (img) {
    img.src = ASSETS[img.getAttribute("data-asset")];
  });
  var routes = document.querySelectorAll(".route");
  function show(path, query, anchor, focus) {
    var found = false;
    routes.forEach(function (s) {
      var on = s.getAttribute("data-route") === path;
      s.hidden = !on;
      if (on) found = true;
    });
    if (!found) { path = "index"; routes.forEach(function (s) { s.hidden = s.getAttribute("data-route") !== "index"; }); }
    document.title = TITLES[path] || "FITCare demo";
    /* nav highlight */
    document.querySelectorAll("nav.nav a").forEach(function (a) {
      var href = a.getAttribute("href") || "";
      var r = href.replace("#/", "").split("?")[0];
      var on = path === r || (r.indexOf("/") > -1 && path.indexOf(r.split("/")[0] + "/") === 0);
      if (on) { a.setAttribute("aria-current", "page"); } else { a.removeAttribute("aria-current"); }
    });
    /* gs deep link: ?who=... */
    if (query) {
      var mWho = query.match(/who=([a-z]+)/);
      if (mWho) {
        var input = document.querySelector("[data-gs] input[name='who'][value='" + mWho[1] + "']");
        if (input) input.checked = true;
      }
    }
    if (anchor) {
      var el = document.getElementById(anchor);
      if (el) { el.scrollIntoView(); return; }
    }
    window.scrollTo(0, 0);
    if (focus) {
      var h = document.querySelector(".route:not([hidden]) h1");
      if (h) { h.setAttribute("tabindex", "-1"); h.focus({ preventScroll: true }); }
    }
  }
  function parse(focus) {
    var h = window.location.hash || "#/index";
    if (h.indexOf("#/") !== 0) return;
    var rest = h.slice(2);
    var anchor = null;
    var query = "";
    if (rest.indexOf("?") > -1) {
      var parts = rest.split("?");
      rest = parts[0]; query = parts[1];
      var mA = query.match(/anchor=([\\w-]+)/);
      if (mA) anchor = mA[1];
    }
    show(rest, query, anchor, focus);
  }
  /* in-page anchors inside routes */
  document.addEventListener("click", function (e) {
    var a = e.target.closest("a[data-anchor]");
    if (!a) return;
    e.preventDefault();
    var el = document.querySelector(".route:not([hidden]) " + a.getAttribute("href"));
    if (el) el.scrollIntoView({ behavior: "smooth" });
  });
  window.addEventListener("hashchange", function () { parse(true); });
  parse(false);
})();
"""
router_js = router_js.replace("__ASSETS__", json.dumps(ASSETS)).replace("__TITLES__", json.dumps(titles))

demo_note = ('<div class="phase-note"><strong>Wired-up demo — the whole prototype in one page.</strong> '
             'Every link, form and filter works. Sample content is watermarked; PDFs and the members '
             'portal open the live site.</div>')

out = ("<title>FITCare — Full Website Demo</title>\n"
       "<style>\n" + tokens + "\n" + sitecss + "\n.route[hidden]{display:none}\n</style>\n"
       + demo_note + "\n" + header + "\n<main id=\"main\">\n" + "\n".join(sections)
       + "\n</main>\n" + footer + "\n" + callbar
       + "\n<script>\n" + js + "\n</script>\n<script>\n" + router_js + "\n</script>\n")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w").write(out)
print("built %s — %d routes, %d assets, %d KB" % (OUT, len(PAGES), len(ASSETS), len(out) // 1024))
