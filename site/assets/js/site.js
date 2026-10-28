/* Buduj z Kaszubami — site.js
   Bez zależności. Wszystko to progresywne ulepszenia: strona działa bez tego pliku. */
(function () {
  "use strict";

  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------------- Nagłówek: stan po przewinięciu ---------------- */
  var header = $(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-stuck", window.scrollY > 24);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---------------- Nawigacja ---------------- */
  var toggle = $(".nav-toggle");
  var nav = $("#site-nav");

  function setNav(open) {
    if (!toggle || !nav) return;
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    toggle.setAttribute("aria-label", open ? "Zamknij menu" : "Otwórz menu");
    nav.classList.toggle("is-open", open);
    if (header) header.classList.toggle("is-nav-open", open);
    document.body.style.overflow = open ? "hidden" : "";
    if (!open) {
      $$(".submenu", nav).forEach(function (s) { s.classList.remove("is-open"); });
      $$(".nav__sub-toggle", nav).forEach(function (b) { b.setAttribute("aria-expanded", "false"); });
    }
  }

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      setNav(toggle.getAttribute("aria-expanded") !== "true");
    });

    $$(".nav__sub-toggle", nav).forEach(function (btn) {
      btn.addEventListener("click", function () {
        var sub = document.getElementById(btn.getAttribute("aria-controls"));
        var open = btn.getAttribute("aria-expanded") === "true";
        btn.setAttribute("aria-expanded", open ? "false" : "true");
        if (sub) sub.classList.toggle("is-open", !open);
      });
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        setNav(false);
        toggle.focus();
      }
    });

    nav.addEventListener("click", function (e) {
      var a = e.target.closest ? e.target.closest("a") : null;
      if (a && window.innerWidth < 1000) setNav(false);
    });

    var lastW = window.innerWidth;
    window.addEventListener("resize", function () {
      var w = window.innerWidth;
      if (w >= 1000 && lastW < 1000) setNav(false);
      lastW = w;
    });
  }

  /* ---------------- Wejście elementów przy przewijaniu ---------------- */
  var revealTargets = ".card, .service-row, .fact, .person, .gallery__item, .contact-box, .related a, .usp__item, .feature__body, .section-head";

  function initReveal() {
    var authored = $$(".reveal, .reveal-img");

    if (reduce || !("IntersectionObserver" in window)) {
      authored.forEach(function (el) { el.classList.add("is-in"); });
      return;
    }

    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) {
            en.target.classList.add("is-in");
            io.unobserve(en.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -5% 0px" }
    );

    authored.forEach(function (el) {
      if (el.getBoundingClientRect().top < window.innerHeight * 0.95) el.classList.add("is-in");
      else io.observe(el);
    });

    $$(revealTargets).forEach(function (el, i) {
      if (el.classList.contains("reveal") || el.classList.contains("reveal-img")) return;
      if (el.getBoundingClientRect().top > window.innerHeight * 0.95) {
        el.classList.add("reveal");
        el.style.setProperty("--d", (i % 4) * 60 + "ms");
        io.observe(el);
      }
    });
  }

  initReveal();

  /* ---------------- Liczniki ---------------- */
  var counters = $$(".count[data-count]");
  if (counters.length) {
    var runCounter = function (el) {
      var target = parseInt(el.getAttribute("data-count"), 10) || 0;
      if (reduce || !window.requestAnimationFrame) {
        el.textContent = String(target);
        return;
      }
      var start = null;
      var step = function (ts) {
        if (start === null) start = ts;
        var p = Math.min((ts - start) / 1100, 1);
        el.textContent = String(Math.round(target * (1 - Math.pow(1 - p, 3))));
        if (p < 1) window.requestAnimationFrame(step);
        else el.textContent = String(target);
      };
      el.textContent = "0";
      window.requestAnimationFrame(step);
    };

    if ("IntersectionObserver" in window) {
      var io2 = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (en) {
            if (en.isIntersecting) {
              runCounter(en.target);
              io2.unobserve(en.target);
            }
          });
        },
        { threshold: 0.6 }
      );
      counters.forEach(function (c) { io2.observe(c); });
    }
  }

  /* ---------------- Lightbox galerii ---------------- */
  var lb = $("#lightbox");
  var links = $$(".gallery__link");

  if (lb && links.length) {
    var img = $("#lb-img");
    var counter = $("#lb-counter");
    var caption = $("#lb-caption");
    var btnPrev = $("#lb-prev");
    var btnNext = $("#lb-next");
    var btnClose = $("#lb-close");
    var current = 0;
    var lastFocus = null;

    var render = function (i) {
      current = (i + links.length) % links.length;
      var a = links[current];
      img.src = a.getAttribute("data-full");
      img.alt = a.getAttribute("data-alt") || "";
      img.width = a.getAttribute("data-w") || 800;
      img.height = a.getAttribute("data-h") || 600;
      counter.textContent = current + 1 + " / " + links.length;
      caption.textContent = a.getAttribute("data-alt") || "";
    };

    var open = function (i) {
      lastFocus = document.activeElement;
      render(i);
      lb.removeAttribute("hidden");
      lb.classList.add("is-open");
      document.body.style.overflow = "hidden";
      btnClose.focus();
    };

    var close = function () {
      lb.classList.remove("is-open");
      lb.setAttribute("hidden", "");
      document.body.style.overflow = "";
      img.removeAttribute("src");
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    };

    links.forEach(function (a, i) {
      a.addEventListener("click", function (e) {
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.button !== 0) return;
        e.preventDefault();
        open(i);
      });
    });

    btnClose.addEventListener("click", close);
    btnPrev.addEventListener("click", function () { render(current - 1); });
    btnNext.addEventListener("click", function () { render(current + 1); });

    lb.addEventListener("click", function (e) {
      if (e.target === lb || e.target.classList.contains("lb__stage")) close();
    });

    document.addEventListener("keydown", function (e) {
      if (!lb.classList.contains("is-open")) return;
      if (e.key === "Escape") { e.preventDefault(); close(); }
      else if (e.key === "ArrowRight") { e.preventDefault(); render(current + 1); }
      else if (e.key === "ArrowLeft") { e.preventDefault(); render(current - 1); }
      else if (e.key === "Tab") {
        var f = $$("button, a[href], [tabindex]:not([tabindex='-1'])", lb);
        if (!f.length) return;
        var first = f[0], last = f[f.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });

    var x0 = null;
    lb.addEventListener("touchstart", function (e) { x0 = e.changedTouches[0].clientX; }, { passive: true });
    lb.addEventListener("touchend", function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 55) render(current + (dx < 0 ? 1 : -1));
      x0 = null;
    }, { passive: true });
  }

  /* ---------------- Mapa ---------------- */

})();
