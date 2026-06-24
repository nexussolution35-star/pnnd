#!/usr/bin/env python3
"""Build a 100% self-hosted static clone from rendered-DOM HTML files.

Reads rendered pages from _source/, mirrors every asset locally, strips
framework hydration + tracking JS, and rewrites all references to relative
local paths. Output is written to OUT (repo root).
"""
import os, re, sys, json, html, subprocess, posixpath
from urllib.parse import urlsplit, urljoin, unquote

SRC  = "/home/user/pnnd/_source"
OUT  = "/home/user/pnnd"
SITE = "mcgeerkitchens-alberton.co.za"
SELF_HOST_HOSTS = {SITE, "fonts.googleapis.com", "fonts.gstatic.com"}

ASSET_EXT = ("css","png","jpg","jpeg","gif","svg","webp","avif","ico","woff","woff2",
             "ttf","eot","otf","mp4","webm","ogg","pdf","json","cur")

# routes that exist as local pages: url(with trailing slash) -> local html file
PAGES = {}  # filled from _routes.json

fetched = {}   # canonical_url -> local relative posix path (under OUT)
failed  = set()

def is_self_host(url):
    h = urlsplit(url).netloc.lower()
    return h in SELF_HOST_HOSTS

def local_path_for(url):
    """Return local relative posix path (under OUT) for a self-hosted url."""
    s = urlsplit(url)
    host = s.netloc.lower()
    path = unquote(s.path)
    if host == SITE:
        rel = path.lstrip("/")
        if rel == "" or rel.endswith("/"):
            rel = rel + "index.html"
        # query-based dynamic asset on own domain (rare) -> keep ext
        return rel
    # cross-origin -> namespace under host folder
    base = path.lstrip("/")
    if host == "fonts.googleapis.com":
        # css2?family=Roboto... -> deterministic filename from query
        q = s.query
        fam = re.search(r"family=([^&:]+)", q)
        name = (fam.group(1) if fam else "fonts").lower()
        return f"fonts.googleapis.com/{name}.css"
    if not base:
        base = "index"
    return f"{host}/{base}"

def curl(url, dest):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    r = subprocess.run(
        ["curl","-sSL","--compressed","--max-time","90",
         "-A","Mozilla/5.0 (clone-archiver)","-o",dest,
         "-w","%{http_code}", url],
        capture_output=True, text=True)
    code = (r.stdout or "").strip()[-3:]
    ok = code.startswith("2") and os.path.exists(dest) and os.path.getsize(dest) > 0
    return ok, code

CSS_URL_RE = re.compile(r"""url\(\s*['"]?([^'")]+?)['"]?\s*\)""", re.I)
IMPORT_RE  = re.compile(r"""@import\s+(?:url\()?\s*['"]([^'"]+)['"]""", re.I)

def process_css(css_url, local_rel):
    """After download, parse css for url()/@import, fetch deps, rewrite refs."""
    dest = os.path.join(OUT, local_rel)
    try:
        text = open(dest, "r", encoding="utf-8", errors="ignore").read()
    except Exception:
        return
    css_dir = posixpath.dirname(local_rel)
    refs = set()
    for m in CSS_URL_RE.finditer(text):
        refs.add(m.group(1).strip())
    for m in IMPORT_RE.finditer(text):
        refs.add(m.group(1).strip())

    repl = {}  # original ref string -> new relative ref
    for ref in refs:
        r = ref.strip()
        if r.startswith("data:") or r.startswith("#") or r == "":
            continue
        absu = urljoin(css_url, html.unescape(r))
        if not absu.startswith("http"):
            continue
        if not is_self_host(absu):
            continue
        target_local = fetch(absu)          # recursive
        if not target_local:
            continue
        newref = posixpath.relpath(target_local, css_dir or ".")
        repl[ref] = newref

    if repl:
        def sub_url(m):
            inner = m.group(1).strip()
            if inner in repl:
                return f"url({repl[inner]})"
            return m.group(0)
        def sub_imp(m):
            inner = m.group(1).strip()
            if inner in repl:
                return m.group(0).replace(inner, repl[inner])
            return m.group(0)
        text = CSS_URL_RE.sub(sub_url, text)
        text = IMPORT_RE.sub(sub_imp, text)
        open(dest, "w", encoding="utf-8").write(text)

def fetch(url):
    """Download a self-hosted asset (idempotent). Return local rel path or None."""
    canon = html.unescape(url).split("#")[0]
    if canon in fetched:
        return fetched[canon]
    if canon in failed:
        return None
    if not is_self_host(canon):
        return None
    local_rel = local_path_for(canon)
    dest = os.path.join(OUT, local_rel)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        fetched[canon] = local_rel
    else:
        ok, code = curl(canon, dest)
        if not ok:
            print(f"  FAIL {code} {canon}")
            failed.add(canon)
            return None
        fetched[canon] = local_rel
    if local_rel.endswith(".css"):
        process_css(canon, local_rel)
    return local_rel

# ---- main ----
routes = json.load(open(os.path.join(SRC, "_routes.json")))
for r in routes:
    PAGES[r["url"]] = r["file"]          # https://site/about-us/ -> about-us.html

html_files = [f for f in os.listdir(SRC) if f.endswith(".html")]
print(f"{len(html_files)} pages, {len(PAGES)} routes")

# 1) Discover + download all self-hosted assets referenced across pages
url_re = re.compile(
    r"https?://(?:" + re.escape(SITE) +
    r"|fonts\.googleapis\.com|fonts\.gstatic\.com)/[^\s\"'`)\]<>]+", re.I)

seed = set()
for f in html_files:
    txt = open(os.path.join(SRC, f), encoding="utf-8", errors="ignore").read()
    for m in url_re.finditer(txt):
        u = html.unescape(m.group(0)).rstrip(".,;")
        ext = u.split("?")[0].rsplit(".",1)[-1].lower()
        if "fonts.googleapis.com" in u or ext in ASSET_EXT:
            seed.add(u)
print(f"{len(seed)} seed asset URLs")

for i, u in enumerate(sorted(seed), 1):
    fetch(u)
    if i % 50 == 0:
        print(f"  fetched {i}/{len(seed)} (total local files: {len(fetched)})")

print(f"Downloaded {len(fetched)} assets, {len(failed)} failures")
json.dump(sorted(failed), open(os.path.join(OUT,"_failed.json"),"w"), indent=1)
print("asset phase done")
