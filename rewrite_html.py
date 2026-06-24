#!/usr/bin/env python3
"""Phase 2: transcribe each rendered page into a self-hosted static page.

 - strip all <script> (framework hydration + tracking)
 - strip <base href> and external perf hints (dns-prefetch/preconnect)
 - remove reCAPTCHA artifacts (invisible iframes + badge)
 - rewrite every self-hosted asset URL to its local mirrored path
 - relink internal navigation between captured routes to local .html files
"""
import os, re, json, html, posixpath
from urllib.parse import urlsplit, unquote

SRC, OUT = "/home/user/pnnd/_source", "/home/user/pnnd"
SITE = "mcgeerkitchens-alberton.co.za"
SELF = {SITE, "fonts.googleapis.com", "fonts.gstatic.com"}

def local_path_for(url):
    s = urlsplit(url); host = s.netloc.lower(); path = unquote(s.path)
    if host == SITE:
        rel = path.lstrip("/")
        return rel + "index.html" if (rel == "" or rel.endswith("/")) else rel
    if host == "fonts.googleapis.com":
        fam = re.search(r"family=([^&:]+)", s.query)
        return f"fonts.googleapis.com/{(fam.group(1) if fam else 'fonts').lower()}.css"
    return f"{host}/{path.lstrip('/') or 'index'}"

routes = json.load(open(os.path.join(SRC, "_routes.json")))
PAGES = {r["url"]: r["file"] for r in routes}

asset_re = re.compile(
    r"https?://(?:" + re.escape(SITE) +
    r"|fonts\.googleapis\.com|fonts\.gstatic\.com)/[^\s\"'`)\]<>]+", re.I)

# strip helpers
script_re   = re.compile(r"<script\b[^>]*>.*?</script\s*>", re.I | re.S)
script_self = re.compile(r"<script\b[^>]*/>", re.I)
base_re     = re.compile(r"<base\b[^>]*>", re.I)
hint_re     = re.compile(r"<link\b[^>]*\brel=[\"'](?:dns-prefetch|preconnect)[\"'][^>]*>", re.I)
recaptcha_iframe = re.compile(r"<iframe\b[^>]*\bsrc=\"[^\"]*(?:google\.com/recaptcha|gstatic\.com/recaptcha)[^\"]*\"[^>]*>.*?</iframe\s*>", re.I | re.S)
recaptcha_badge  = re.compile(r"<div\b[^>]*class=\"[^\"]*grecaptcha-badge[^\"]*\"[^>]*>.*?</div>", re.I | re.S)
# dead WordPress endpoints exposed via <link> metadata (RSS/oEmbed/RSD/REST/wlw)
deadlink_re = re.compile(
    r"<link\b[^>]*\b(?:rel=\"(?:alternate|EditURI|wlwmanifest|pingback|https://api\.w\.org/)\"|"
    r"href=\"https://mcgeerkitchens-alberton\.co\.za/(?:feed|comments/feed|wp-json|xmlrpc\.php)[^\"]*\")[^>]*>",
    re.I)

TRAIL_ENT = re.compile(r"(&quot;|&#0?34;|&#0?39;|&apos;)$", re.I)

def rewrite_assets(text):
    def sub(m):
        raw = m.group(0)
        suffix = ""                      # entity-quote that closes an inline url("...")
        me = TRAIL_ENT.search(raw)
        if me:
            suffix = me.group(0); raw_core = raw[:-len(suffix)]
        else:
            raw_core = raw
        canon = html.unescape(raw_core).split("#")[0].rstrip(".,;)")
        lp = local_path_for(canon)
        if os.path.exists(os.path.join(OUT, lp)):
            # pages live at root, so relative path == local path
            return lp + suffix
        return raw
    return asset_re.sub(sub, text)

def rewrite_routes(text):
    # longest URLs first so /our-work/ isn't shadowed by /
    for url in sorted(PAGES, key=len, reverse=True):
        local = PAGES[url]
        for q in ('"', "'"):
            text = text.replace(f'href={q}{url}{q}', f'href={q}{local}{q}')
    return text

count = 0
for f in sorted(os.listdir(SRC)):
    if not f.endswith(".html"):
        continue
    t = open(os.path.join(SRC, f), encoding="utf-8", errors="ignore").read()
    t = script_re.sub("", t)
    t = script_self.sub("", t)
    t = base_re.sub("", t)
    t = hint_re.sub("", t)
    t = recaptcha_iframe.sub("", t)
    t = recaptcha_badge.sub("", t)
    t = deadlink_re.sub("", t)
    t = rewrite_assets(t)
    t = rewrite_routes(t)
    open(os.path.join(OUT, f), "w", encoding="utf-8").write(t)
    count += 1
    print(f"  wrote {f}  ({len(t)} bytes)")

print(f"rewrote {count} pages")
