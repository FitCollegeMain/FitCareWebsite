/* ==========================================================================
   FITCare Support Services — shared behaviour (the one site JS file)
   Everything is progressive enhancement: pages remain fully readable
   and navigable with JS disabled. No dependencies.
   ========================================================================== */
(function () {
  "use strict";

  /* ---- video facade: inject player only on demand ---- */
  document.querySelectorAll("[data-video]").forEach(function (block) {
    var btn = block.querySelector("[data-video-play]");
    if (!btn) return;
    btn.addEventListener("click", function () {
      var src = block.getAttribute("data-video-src");
      var panel = document.createElement("div");
      panel.className = "video-loaded";
      if (src) {
        panel.innerHTML =
          '<iframe src="' + src + '" title="Video" loading="lazy" allowfullscreen ' +
          'style="width:100%;height:100%;border:0"></iframe>';
      } else {
        panel.innerHTML =
          "<p>▶ [PLACEHOLDER] The player (YouTube/Vimeo iframe or native " +
          "&lt;video&gt; with captions) is injected here on demand — " +
          "nothing loads until this click.</p>";
      }
      block.appendChild(panel);
      btn.setAttribute("hidden", "");
      panel.setAttribute("tabindex", "-1");
      panel.focus();
    });
  });

  /* ---- review carousel: buttons only, no auto-advance ---- */
  document.querySelectorAll("[data-carousel]").forEach(function (car) {
    var track = car.querySelector("[data-car-track]");
    var slides = track.children.length;
    var status = car.querySelector("[data-car-status]");
    var i = 0;
    function go(n) {
      i = (n + slides) % slides;
      track.style.transform = "translateX(-" + i * 100 + "%)";
      status.textContent = "Review " + (i + 1) + " of " + slides;
    }
    car.querySelector("[data-car-prev]").addEventListener("click", function () { go(i - 1); });
    car.querySelector("[data-car-next]").addEventListener("click", function () { go(i + 1); });
  });

  /* ---- tag filters (worker directory + activities share this) ---- */
  document.querySelectorAll("[data-filter-group]").forEach(function (group) {
    var name = group.getAttribute("data-filter-group");
    var items = document.querySelectorAll("[data-filter-items='" + name + "'] [data-tags]");
    group.addEventListener("click", function (e) {
      var btn = e.target.closest("[data-filter]");
      if (!btn) return;
      group.querySelectorAll("[data-filter]").forEach(function (b) {
        b.setAttribute("aria-pressed", String(b === btn));
      });
      var f = btn.getAttribute("data-filter");
      items.forEach(function (el) {
        var show = f === "all" ||
          (" " + el.getAttribute("data-tags") + " ").indexOf(" " + f + " ") > -1;
        el.classList.toggle("is-hidden", !show);
      });
    });
  });

  /* ---- multi-step Get Started flow ---- */
  var gs = document.querySelector("[data-gs]");
  if (gs) {
    var steps = gs.querySelectorAll("[data-gs-step]");
    var progress = gs.querySelectorAll("[data-gs-progress] li");
    var back = gs.querySelector("[data-gs-back]");
    var next = gs.querySelector("[data-gs-next]");
    var skip = gs.querySelector("[data-gs-skip]");
    var foot = gs.querySelector("[data-gs-foot]");
    var escapeBar = gs.querySelector("[data-gs-escape]");
    var success = gs.querySelector("[data-gs-success]");
    var cur = 1;

    var headings2 = {
      participant: "Nice to meet you. How do we reach you?",
      family: "Thanks for looking out for them. How do we reach you?",
      coordinator: "Let's make this quick. Your details:",
      other: "No worries. How do we reach you?"
    };
    var thanks = {
      participant: "Thanks! We've got it.",
      family: "Thanks — we've got it.",
      coordinator: "Referral started — we're on it.",
      other: "Thanks! We've got it."
    };

    /* deep links: get-started.html?who=coordinator pre-answers step 1
       (used by the coordinator panel and "Request this worker" actions) */
    var pre = new URLSearchParams(window.location.search).get("who");
    if (pre) {
      var preInput = gs.querySelector("input[name='who'][value='" + pre + "']");
      if (preInput) preInput.checked = true;
    }

    function who() {
      var r = gs.querySelector("input[name='who']:checked");
      return r ? r.value : null;
    }

    function render(focusHeading) {
      steps.forEach(function (s) {
        s.classList.toggle("active", Number(s.getAttribute("data-gs-step")) === cur);
      });
      progress.forEach(function (p, idx) {
        if (idx + 1 < cur) { p.classList.add("done"); p.removeAttribute("aria-current"); }
        else if (idx + 1 === cur) { p.classList.remove("done"); p.setAttribute("aria-current", "step"); }
        else { p.classList.remove("done"); p.removeAttribute("aria-current"); }
      });
      back.style.display = cur > 1 ? "block" : "none";
      skip.style.display = cur === 3 ? "block" : "none";
      next.textContent = cur === 3 ? "Send it" : "Continue";
      if (focusHeading) {
        var h = gs.querySelector(".gs-step.active h3");
        if (h) { h.setAttribute("tabindex", "-1"); h.focus(); }
      }
    }

    function validate() {
      var ok = true;
      if (cur === 1) {
        var fs = gs.querySelector("[data-req='who']");
        var valid = !!who();
        fs.classList.toggle("invalid", !valid);
        if (!valid) ok = false;
      }
      if (cur === 2) {
        var nameF = gs.querySelector("[data-req='name']");
        var nameOk = nameF.querySelector("input").value.trim().length > 0;
        nameF.classList.toggle("invalid", !nameOk);
        var contactF = gs.querySelector("[data-contact]");
        var phone = gs.querySelector("#gs-phone").value.trim();
        var email = gs.querySelector("#gs-email").value.trim();
        var contactOk = phone.length > 0 || email.length > 0;
        contactF.classList.toggle("invalid", !contactOk);
        ok = nameOk && contactOk;
      }
      if (!ok) {
        var firstInvalid = gs.querySelector(".invalid input, fieldset.invalid input");
        if (firstInvalid) firstInvalid.focus();
      }
      return ok;
    }

    function submit() {
      var data = {};
      new FormData(gs).forEach(function (v, k) {
        if (data[k] !== undefined) { data[k] = [].concat(data[k], v); } else { data[k] = v; }
      });
      /* Backend swap-in point: POST `data` to the production endpoint here. */
      console.log("Get Started submission:", data);
      steps.forEach(function (s) { s.classList.remove("active"); });
      foot.style.display = "none";
      escapeBar.style.display = "none";
      progress.forEach(function (p) { p.classList.add("done"); p.removeAttribute("aria-current"); });
      var h = gs.querySelector("[data-gs-thanks]");
      h.textContent = thanks[who() || "other"];
      success.classList.add("show");
      h.setAttribute("tabindex", "-1");
      h.focus();
    }

    next.addEventListener("click", function () {
      if (!validate()) return;
      if (cur === 1) {
        var w = who() || "other";
        gs.querySelector("[data-gs-heading2]").textContent = headings2[w];
        var org = gs.querySelector("[data-org]");
        if (org) org.hidden = (w !== "coordinator");
      }
      if (cur < 3) { cur++; render(true); } else { submit(); }
    });
    back.addEventListener("click", function () { if (cur > 1) { cur--; render(true); } });
    skip.addEventListener("click", function () { submit(); });

    gs.addEventListener("input", function (e) {
      var f = e.target.closest(".field.invalid, fieldset.invalid");
      if (f) f.classList.remove("invalid");
    });

    render(false);
  }
})();

/* ---- simple forms (careers / contact / feedback): validate, log, success ---- */
(function () {
  "use strict";
  document.querySelectorAll("[data-simple-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var ok = true;
      form.querySelectorAll("[required]").forEach(function (inp) {
        var f = inp.closest(".field");
        var valid = inp.value.trim().length > 0;
        if (f) f.classList.toggle("invalid", !valid);
        if (!valid) ok = false;
      });
      if (!ok) {
        var fi = form.querySelector(".field.invalid input, .field.invalid textarea, .field.invalid select");
        if (fi) fi.focus();
        return;
      }
      var data = {};
      new FormData(form).forEach(function (v, k) {
        data[k] = data[k] !== undefined ? [].concat(data[k], v) : v;
      });
      /* Backend swap-in point: POST `data` to the production endpoint here. */
      console.log("Form submission:", data);
      form.classList.add("done");
      var s = form.querySelector(".form-success h3");
      if (s) { s.setAttribute("tabindex", "-1"); s.focus(); }
    });
    form.addEventListener("input", function (e) {
      var f = e.target.closest(".field.invalid");
      if (f) f.classList.remove("invalid");
    });
  });
})();

/* ---- motion system (Tiers 1–3): reveals, hero entrance, ambience ----
   Engages only when the user has NOT asked for reduced motion. Without
   this running (old browser, JS off), no content is ever hidden. */
(function () {
  "use strict";
  if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  if (!("IntersectionObserver" in window)) return;
  document.documentElement.classList.add("has-motion");

  /* Tier 1 — tag reveal units, stagger siblings within the same container */
  var units = document.querySelectorAll(
    ".sec-head,.svc,.path,.step,.tw,.act,.stile,.info-card,.quote-card," +
    ".story-card,.profile,.coord,.cta-final,.trust-strip,.pull-band," +
    ".map-ph,.gs,.sform,.faq details,.tbl-wrap,.video-block"
  );
  var perParent = new Map();
  units.forEach(function (el) {
    if (el.closest(".hero")) return; /* hero has its own entrance */
    var p = el.parentElement;
    var n = perParent.get(p) || 0;
    perParent.set(p, n + 1);
    el.classList.add("rv");
    el.style.transitionDelay = Math.min(n, 7) * 70 + "ms";
  });
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.classList.add("in");
        io.unobserve(e.target);
      }
    });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
  document.querySelectorAll(".rv").forEach(function (el) { io.observe(el); });

  /* Tier 3 — count-up on trust-bar figures (two digits or more, e.g. 60+) */
  document.querySelectorAll(".trust-item strong").forEach(function (strong) {
    var m = /^(\d{2,})\+/.exec(strong.textContent);
    if (!m) return;
    var target = parseInt(m[1], 10);
    var rest = strong.textContent.slice(m[1].length);
    var span = document.createElement("span");
    span.textContent = "0";
    strong.textContent = "";
    strong.appendChild(span);
    strong.appendChild(document.createTextNode(rest));
    var counted = false;
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting || counted) return;
        counted = true;
        cio.unobserve(strong);
        var t0 = null;
        function tick(t) {
          if (!t0) t0 = t;
          var k = Math.min((t - t0) / 900, 1);
          span.textContent = String(Math.round(target * (1 - Math.pow(1 - k, 3))));
          if (k < 1) requestAnimationFrame(tick);
        }
        requestAnimationFrame(tick);
      });
    }, { threshold: 0.4 });
    cio.observe(strong);
  });

  /* Tier 3 — header shadow once the page scrolls */
  var head = document.querySelector(".site-head");
  if (head) {
    var onScroll = function () {
      head.classList.toggle("scrolled", window.scrollY > 8);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }
})();
