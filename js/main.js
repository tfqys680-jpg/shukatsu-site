// はじめての終活ガイド 共通スクリプト（最小限）
(function () {
  "use strict";

  // モバイルナビ開閉
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".global-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // ページ内アンカーのスムーススクロール（CSS scroll-behavior 非対応環境向け）
  document.addEventListener("click", function (e) {
    var link = e.target.closest('a[href^="#"]');
    if (!link) return;
    var id = link.getAttribute("href").slice(1);
    if (!id) return;
    var target = document.getElementById(id);
    if (!target) return;
    e.preventDefault();
    target.scrollIntoView({ behavior: "smooth", block: "start" });
    if (history.pushState) history.pushState(null, "", "#" + id);
  });

  // ページ上へ戻るボタン
  var toTop = document.querySelector(".to-top");
  if (toTop) {
    window.addEventListener("scroll", function () {
      toTop.classList.toggle("show", window.scrollY > 600);
    }, { passive: true });
    toTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  // フッターの年表示
  var year = document.querySelector(".js-year");
  if (year) year.textContent = String(new Date().getFullYear());
})();


// スクロール演出（2026-07-11 追加）
// JSが無効な環境・prefers-reduced-motion 環境では何もしない（全文が通常表示される）
(function () {
  "use strict";
  var root = document.documentElement;
  root.classList.add("js");

  // ヒーローの登場演出（初期スタイル適用後の次フレームで発火）
  // バックグラウンドタブ等で rAF が動かない環境向けにタイムアウトでも発火させる
  var markLoaded = function () { root.classList.add("is-loaded"); };
  requestAnimationFrame(function () {
    requestAnimationFrame(markLoaded);
  });
  setTimeout(markLoaded, 500);

  // ヘッダーのスクロール反応
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () { header.classList.toggle("is-scrolled", window.scrollY > 8); };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  if (!("IntersectionObserver" in window)) return;

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        io.unobserve(entry.target);
      }
    });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });

  function arm(el, delayMs) {
    el.classList.add("reveal");
    if (delayMs) el.style.transitionDelay = delayMs + "ms";
    io.observe(el);
  }

  // ブロック単位（各セクションの直下要素・記事本文の各要素）
  var blockSelectors = [
    ".section .container > *",
    ".closing-cta .container > *",
    ".article-container article > *",
    ".article-container.page-body > *"
  ];
  document.querySelectorAll(blockSelectors.join(",")).forEach(function (el) { arm(el, 0); });

  // リスト項目は順番にずらして表示（ステガー）
  var itemGroups = [
    ".worry-list", ".card-grid", ".rank-list", ".reason-grid", ".article-list",
    ".task-grid", ".q-list", ".value-list", ".first5", ".ease-list",
    ".faq-list", ".cl-wrap"
  ];
  document.querySelectorAll(itemGroups.join(",")).forEach(function (group) {
    Array.prototype.forEach.call(group.children, function (child, i) {
      arm(child, Math.min(i * 70, 490));
    });
  });
})();
