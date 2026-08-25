#!/usr/bin/env node
"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");

function walk(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
    if (entry.name === ".git") return [];
    const full = path.join(dir, entry.name);
    return entry.isDirectory() ? walk(full) : [full];
  });
}

function attrs(tag) {
  const result = {};
  for (const match of tag.matchAll(/([\w:-]+)\s*=\s*(["'])(.*?)\2/gs)) {
    result[match[1]] = match[3];
  }
  return result;
}

const htmlFiles = walk(root).filter((file) => file.endsWith(".html"));
const publicHtml = htmlFiles.filter((file) => !path.relative(root, file).startsWith(`tools${path.sep}pdf${path.sep}`));
let affiliateCount = 0;
let ctaCount = 0;
const shopCounts = { amazon: 0, rakuten: 0 };
const products = new Map();

for (const file of publicHtml) {
  const relative = path.relative(root, file);
  const html = fs.readFileSync(file, "utf8");
  const mainScripts = [...html.matchAll(/<script\b[^>]*src\s*=\s*(["'])[^"']*js\/main\.js[^"']*\1[^>]*>/gis)];
  assert.equal(mainScripts.length, 1, `${relative}: main.js must be loaded exactly once`);
  assert.match(html.slice(0, mainScripts[0].index), /function\s+gtag\s*\(/, `${relative}: gtag must be defined before main.js`);
  assert.equal((html.match(/lp_cta_click/g) || []).length, 0, `${relative}: legacy inline CTA tracking remains`);

  const ctaTags = [...html.matchAll(/<a\b[^>]*\bdata-cta\s*=\s*(["'])[^"']+\1[^>]*>/gis)];
  ctaCount += ctaTags.length;

  for (const match of html.matchAll(/<a\b[^>]*href\s*=\s*(["'])[^"']*af\.moshimo\.com[^"']*\1[^>]*>/gis)) {
    affiliateCount += 1;
    const linkAttrs = attrs(match[0]);
    assert.equal(linkAttrs["data-cta"], undefined, `${relative}: affiliate link must not also be a CTA`);

    const before = html.slice(0, match.index);
    const boxStart = before.lastIndexOf("<div");
    const candidateTags = [...before.slice(Math.max(0, before.length - 8000)).matchAll(/<div\b[^>]*\bclass\s*=\s*(["'])[^"']*\bproduct-box\b[^"']*\1[^>]*>/gis)];
    assert.ok(candidateTags.length > 0 && boxStart >= 0, `${relative}: affiliate link is outside product-box`);
    const boxAttrs = attrs(candidateTags[candidateTags.length - 1][0]);
    assert.ok(boxAttrs["data-product-id"], `${relative}: data-product-id is missing`);
    assert.ok(boxAttrs["data-product-name"], `${relative}: data-product-name is missing`);

    const previousName = products.get(boxAttrs["data-product-id"]);
    if (previousName) {
      assert.equal(boxAttrs["data-product-name"], previousName, `${relative}: product name differs for the same product ID`);
    } else {
      products.set(boxAttrs["data-product-id"], boxAttrs["data-product-name"]);
    }

    const decoded = decodeURIComponent(linkAttrs.href.replaceAll("&amp;", "&"));
    if ((linkAttrs.class || "").split(/\s+/).includes("rakuten") || decoded.includes("rakuten.co.jp")) {
      shopCounts.rakuten += 1;
    } else if (decoded.includes("amazon.co.jp")) {
      shopCounts.amazon += 1;
    } else {
      assert.fail(`${relative}: unsupported affiliate shop`);
    }
  }
}

assert.equal(affiliateCount, 34, "affiliate link count changed unexpectedly");
assert.equal(ctaCount, 13, "CTA count changed unexpectedly");
assert.deepEqual(shopCounts, { amazon: 19, rakuten: 15 });
assert.equal(products.size, 12, "canonical product count changed unexpectedly");

// main.jsを依存ライブラリなしで実行し、イベントの漏れ・二重発火・例外を確認する。
const clickHandlers = [];
const events = [];
const classList = { add() {}, toggle() { return false; }, contains() { return false; } };
const documentMock = {
  documentElement: { classList },
  querySelector() { return null; },
  querySelectorAll() { return []; },
  addEventListener(type, handler) {
    if (type === "click") clickHandlers.push(handler);
  }
};
const context = {
  document: documentMock,
  window: { scrollY: 0, addEventListener() {}, scrollTo() {}, matchMedia() { return { matches: true }; } },
  history: { pushState() {} },
  location: { pathname: "/articles/article16.html" },
  requestAnimationFrame() {},
  setTimeout() {},
  gtag(...args) { events.push(args); }
};
vm.runInNewContext(fs.readFileSync(path.join(root, "js/main.js"), "utf8"), context, { filename: "js/main.js" });

function targetFor({ type, href = "", classes = [], label = "", productId = "4434265792", productName = "一番わかりやすいエンディングノート（リベラル社）", placement = "まず1冊、渡すなら" }) {
  const box = {
    getAttribute(name) {
      return { "data-product-id": productId, "data-product-name": productName }[name] || null;
    },
    querySelector(selector) {
      return selector === "h3" ? { textContent: placement } : null;
    }
  };
  const anchor = {
    classList: { contains(name) { return classes.includes(name); } },
    getAttribute(name) {
      return { href, "data-cta": label }[name] || null;
    },
    closest(selector) {
      return selector === ".product-box" ? box : null;
    }
  };
  return {
    closest(selector) {
      if (selector === "a[data-cta]") return type === "cta" ? anchor : null;
      if (selector === 'a[href*="af.moshimo.com"]') return type === "affiliate" ? anchor : null;
      return null;
    }
  };
}

function dispatch(options) {
  events.length = 0;
  const event = { target: targetFor(options), preventDefault() {} };
  clickHandlers.forEach((handler) => handler(event));
  return events.slice();
}

let fired = dispatch({ type: "cta", label: "hero_official" });
assert.equal(fired.length, 1, "CTA must fire exactly once");
assert.equal(fired[0][1], "lp_cta_click");

fired = dispatch({
  type: "affiliate",
  href: "https://af.moshimo.com/af/c/click?url=https%3A%2F%2Fwww.amazon.co.jp%2Fdp%2F4434265792"
});
assert.equal(fired.length, 1, "affiliate click must fire exactly once");
assert.equal(fired[0][1], "affiliate_click");
assert.equal(fired[0][2].shop, "amazon");
assert.equal(fired[0][2].product_id, "4434265792");
assert.equal(fired[0][2].product, "一番わかりやすいエンディングノート（リベラル社）");
assert.equal(fired[0][2].placement, "まず1冊、渡すなら");

fired = dispatch({
  type: "affiliate",
  href: "https://af.moshimo.com/af/c/click?url=https%3A%2F%2Fitem.rakuten.co.jp%2Fbook%2F1",
  classes: ["rakuten"]
});
assert.equal(fired.length, 1, "Rakuten click must fire exactly once");
assert.equal(fired[0][2].shop, "rakuten");

fired = dispatch({ type: "affiliate", href: "https://af.moshimo.com/af/c/click?url=%ZZ" });
assert.equal(fired.length, 1, "malformed affiliate URL must not stop tracking");
assert.equal(fired[0][2].shop, "other");

fired = dispatch({ type: "other" });
assert.equal(fired.length, 0, "untracked click must not fire an event");

console.log(`CLICK TRACKING CHECKS PASSED (public HTML: ${publicHtml.length}, affiliate links: ${affiliateCount}, CTAs: ${ctaCount}, products: ${products.size})`);
