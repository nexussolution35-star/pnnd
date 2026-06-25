#!/usr/bin/env python3
"""Full multi-page generator for PNND Kitchens.

Builds every secondary page as its own file (about, gallery, service-areas,
process, articles, contact), the All Services index, and 7 service detail
pages — all sharing one prefix-aware nav/footer so every nav item links to
its own dedicated page. Structure mirrors Cloud Nine (Website A); visual
language mirrors Twelve (Website B). index.html is hand-built separately.
"""
import os
ROOT = os.path.dirname(__file__)
SVC_DIR = os.path.join(ROOT, "services")
os.makedirs(SVC_DIR, exist_ok=True)

NAV = [
    ("kitchen-remodelling", "Kitchen Remodelling"),
    ("cabinet-construction-installation", "Cabinet Construction &amp; Installation"),
    ("closet-construction-installation", "Closet Construction &amp; Installation"),
    ("custom-closet-design", "Custom Closet Design"),
    ("custom-carpentry", "Custom Carpentry"),
    ("cabinet-closet-repair", "Cabinet &amp; Closet Repair"),
    ("deck-construction", "Deck Construction"),
]

# ---------------------------------------------------------------- service data
S = {
 "kitchen-remodelling": {"label":"Kitchen Remodelling","eyebrow":"kitchen remodelling","hero":"p01",
  "tagline":"Designed, built and installed by one accountable team.","head":"Kitchen Remodelling in Pretoria",
  "intro":"When your kitchen stops working for the way you live, a remodel is the honest fix — not another patch. We redesign, build and install the whole thing, then walk you through the result.",
  "overview":[("Kitchen Remodelling, Done By The Owner","Most kitchen companies run a sales team. PNND runs an owner. The person who quotes your kitchen is the one who measures it, builds it in our Arcadia workshop, and is on site when it's installed."),
    ("One Workshop, Every Trade","Cabinetry, counters, splashbacks, lighting coordination and finishes are handled under one roof. Fewer trades, fewer delays, and a single team accountable for the result."),
    ("What The Consultation Covers","Every consultation is free and on your timeline. We measure, photograph the space, talk through layout and finishes, and follow up the same week with drawings and a written quote."),
    ("What Honest Pricing Looks Like","Your quote is line-itemed — cabinetry, counters, hardware, removal and installation. You see every number, with no bundled mystery totals.")],
  "why":["The owner measures, builds and installs — you deal with one person","Line-item written quote, no bundled mystery numbers","Solid timber, quality board and premium fittings","Our own crews on every project — never subcontracted"],
  "included":["Full design &amp; 3D layout","Custom cabinetry &amp; carcasses","Countertops &amp; splashbacks","Soft-close hinges &amp; runners","Lighting &amp; electrical coordination","Removal of the old kitchen","Professional installation","Final snag &amp; clean-up"],
  "faq":[("How long does a kitchen remodel take?","Most kitchens take 3–6 weeks from sign-off, depending on size and finishes. You get a written schedule before we begin."),("Can you work with my existing layout?","Yes — we can refresh within your current footprint or redesign the layout entirely. We advise on what adds the most value."),("What does a kitchen cost in Pretoria?","Most remodels run between R80,000 and R350,000. We quote after a free measure-up so the price fits your space and finishes.")],
  "gallery":["p02","p13","p14"],"related":["cabinet-construction-installation","custom-carpentry","closet-construction-installation"]},
 "cabinet-construction-installation": {"label":"Cabinet Construction &amp; Installation","eyebrow":"cabinet construction","hero":"p03",
  "tagline":"Made to measure, built by hand, installed by our own team.","head":"Custom Cabinets, Built &amp; Installed",
  "intro":"Made-to-measure cabinets for kitchens, sculleries, TV units and storage — built in our Pretoria workshop and fitted by the same team that built them.",
  "overview":[("Cabinetry, Done By The Owner","The person who quotes your cabinets measures, builds and installs them. No sales rep hand-off, no subcontracted fitters — one accountable craftsman from first measure to final screw."),
    ("Built To The Millimetre","We build to your exact dimensions, so there are no filler panels or awkward gaps. Every carcass is square, every door aligned, every drawer soft-close."),
    ("What The Consultation Covers","A free on-site measure-up where we discuss finishes, hardware and layout, then follow up with a written quote and finish samples the same week."),
    ("What Honest Pricing Looks Like","Carcasses, doors, hardware, edging and installation are itemised separately. You see every number before any work begins — no surprises on install day.")],
  "why":["One craftsman from measure to install — never subcontracted","Built to the millimetre — no fillers, no gaps","Quality board, solid timber and soft-close hardware as standard","Fixed written quote before any work starts"],
  "included":["On-site measure &amp; design","Custom carcasses &amp; doors","Soft-close hinges &amp; runners","Edging &amp; finishing","Handles &amp; accessories","Delivery &amp; installation","Levelling &amp; alignment","Snag &amp; clean-up"],
  "faq":[("What materials do you use?","Quality moisture-resistant board, solid timber and real veneers, with soft-close hardware as standard. We'll show samples at the consultation."),("Do you install what you build?","Always. The team that builds your cabinets installs them, so quality is owned end to end."),("Can you match an existing kitchen?","Yes — we colour- and finish-match to extend or repair existing cabinetry wherever possible.")],
  "gallery":["p04","p11","p06"],"related":["kitchen-remodelling","closet-construction-installation","cabinet-closet-repair"]},
 "closet-construction-installation": {"label":"Closet Construction &amp; Installation","eyebrow":"closets &amp; wardrobes","hero":"p04",
  "tagline":"Floor-to-ceiling built-ins, scribed and fitted to your walls.","head":"Built-in Closets &amp; Wardrobes",
  "intro":"Floor-to-ceiling built-in cupboards and wardrobes, designed around your room and the way you store — then built and installed by our own team.",
  "overview":[("Closets, Done By The Owner","From first measure to final fit, one team is responsible. The owner plans your closet, builds it, and is there when it goes in."),
    ("Storage That Uses Every Centimetre","Hanging space, drawers, shelving and shoe racks, laid out to fit your life — not an off-the-shelf module. We scribe to your walls so it reads as part of the house."),
    ("What The Consultation Covers","A free measure-up where we plan zones, discuss door styles and finishes, and follow up with a layout and written quote the same week."),
    ("What Honest Pricing Looks Like","Carcasses, internals, doors and installation are itemised. You see every number up front, with a fixed quote before we build.")],
  "why":["Planned, built and installed by one team","Scribed to the wall for a true built-in finish","Internals tailored to how you actually store","Fixed written quote, no mystery numbers"],
  "included":["On-site measure &amp; design","Custom carcasses &amp; doors","Internal hanging &amp; shelving","Soft-close drawers","Mirrors &amp; accessories (optional)","Delivery &amp; installation","Scribing to walls","Snag &amp; clean-up"],
  "faq":[("Hinged or sliding doors?","Both. Sliding doors suit tight rooms; hinged doors give full access. We advise based on your space at the measure-up."),("Can you fit into an alcove or sloped ceiling?","Yes — built-ins are ideal for awkward spaces. We scribe and build to fit exactly."),("How long does installation take?","Most built-in closets are installed in 1–3 days once built, with minimal disruption.")],
  "gallery":["p05","p12","p10"],"related":["custom-closet-design","cabinet-construction-installation","kitchen-remodelling"]},
 "custom-closet-design": {"label":"Custom Closet Design","eyebrow":"custom closet design","hero":"p05",
  "tagline":"Walk-in and dressing-room design, planned in 3D.","head":"Custom Closet &amp; Dressing Room Design",
  "intro":"For walk-in closets and dressing rooms, design is everything. We plan zones for hanging, folding, shoes and accessories, then craft a system that's entirely yours.",
  "overview":[("Design, Done By The Owner","You work directly with the person who will build your closet — no design-to-build hand-off where detail gets lost."),
    ("Designed Around Your Wardrobe","Every closet is planned around what you own and how you use it, not a template. Lighting, glass fronts, valet rails and drawers are specified to suit."),
    ("What The Consultation Covers","A free design consultation and 3D layout, so you can see and adjust the closet before we build a thing."),
    ("What Honest Pricing Looks Like","Design, build and installation are itemised, with a fixed written quote after the consultation. You approve the number before we start.")],
  "why":["Every closet planned around your wardrobe, not a template","3D design so you see it before it's built","Boutique detailing — lighting, glass fronts, valet rails","Design, build and install from one studio"],
  "included":["Consultation &amp; 3D design","Zoned hanging &amp; storage plan","Drawers, shelving &amp; rails","Optional integrated lighting","Glass-front &amp; display options","Build &amp; installation","Finishing &amp; alignment","Snag &amp; clean-up"],
  "faq":[("Do you provide 3D drawings?","Yes — every custom closet starts with a 3D design so you can see and adjust the layout before we build."),("Can you add lighting?","Absolutely. Integrated LED strip and sensor lighting are popular options we coordinate during the build."),("How much does a walk-in closet cost?","It depends on size and detailing. We quote a fixed price after the free design consultation.")],
  "gallery":["p10","p12","p07"],"related":["closet-construction-installation","custom-carpentry","kitchen-remodelling"]},
 "custom-carpentry": {"label":"Custom Carpentry","eyebrow":"custom carpentry","hero":"p06",
  "tagline":"Bespoke joinery for every room — residential and commercial.","head":"Custom Carpentry &amp; Joinery",
  "intro":"Vanities, media units, desks, shelving, wine racks and feature joinery — if it can be built in timber, we can craft it, to measure, for your home or business.",
  "overview":[("Carpentry, Done By The Owner","Tell us what you need and where it goes; the owner designs, builds and installs it. One craftsman, accountable from sketch to fit."),
    ("Truly Bespoke, Not Catalogue","These are one-off pieces made for your space and use, finished to furniture standard — not flat-pack furniture in disguise."),
    ("What The Consultation Covers","A free measure-up and design chat, with a written quote and material options the same week."),
    ("What Honest Pricing Looks Like","Design, build, materials and installation are itemised. You approve a fixed quote before any timber is cut.")],
  "why":["One-off pieces, designed and built for your space","Joinery finished to furniture standard","Residential and commercial projects welcome","Matched to existing furniture where possible"],
  "included":["Design &amp; measure","Bespoke build in our workshop","Quality timber &amp; finishes","Hardware &amp; fittings","Delivery &amp; installation","Finishing &amp; alignment","Commercial &amp; residential","Snag &amp; clean-up"],
  "faq":[("What kinds of carpentry do you take on?","Vanities, media units, desks, shelving, wine storage, feature panelling and more — residential and commercial."),("Can you match existing furniture?","Yes, we colour- and finish-match wherever possible so new pieces feel original to the space."),("Do you do commercial fit-outs?","We do — reception counters, retail joinery and office storage are all within our scope.")],
  "gallery":["p08","p15","p17"],"related":["cabinet-construction-installation","cabinet-closet-repair","deck-construction"]},
 "cabinet-closet-repair": {"label":"Cabinet &amp; Closet Repair","eyebrow":"cabinet &amp; closet repair","hero":"p11",
  "tagline":"Repairs and refits — for a fraction of a new build.","head":"Cabinet &amp; Closet Repair",
  "intro":"Not everything needs replacing. Sagging doors, broken hinges, blown board, worn runners and tired finishes can often be repaired or refitted for far less than a new build.",
  "overview":[("Repairs, Done By The Owner","The owner assesses your units in person and tells you straight whether a repair makes sense — no upsell to a full replacement you don't need."),
    ("Repair Before You Replace","If the carcasses are sound, a repair is usually the smart call. We re-align doors, replace runners, swap blown panels and refresh finishes."),
    ("What The Assessment Covers","A free on-site assessment of doors, hinges, drawers, panels and finishes, with an honest recommendation and a fixed quote."),
    ("What Honest Pricing Looks Like","You get a clear, itemised quote for exactly what needs doing — and a straight answer when a repair isn't worth it.")],
  "why":["Honest assessment — repair vs replace, told straight","A fraction of the cost of a new build","Fast, scheduled and tidy work","Free assessment and quote in Pretoria"],
  "included":["On-site assessment","Hinge &amp; door alignment","Runner &amp; drawer repair","Board &amp; panel replacement","Re-edging &amp; refinishing","Handle &amp; hardware swaps","Water-damage repairs","Fixed written quote"],
  "faq":[("Is it worth repairing or should I replace?","If the carcasses are sound, repair is usually the smart call. We assess on site and advise honestly."),("Can you fix water-damaged cupboards?","Often yes — we replace affected panels and refinish so it blends in. Severe cases may need a partial rebuild."),("Do you charge for a quote?","Assessment and quoting are free within Pretoria and surrounds.")],
  "gallery":["p03","p06","p16"],"related":["cabinet-construction-installation","custom-carpentry","kitchen-remodelling"]},
 "deck-construction": {"label":"Deck Construction","eyebrow":"deck construction","hero":"p08",
  "tagline":"Solid timber decks, engineered and sealed to last.","head":"Deck Construction in Pretoria",
  "intro":"Outdoor living, done properly. We build solid timber decks, pergolas and outdoor woodwork engineered to handle the Highveld — sealed and finished to last.",
  "overview":[("Decks, Done By The Owner","The owner assesses the site, designs the deck and is on the build. One team responsible for structure, timber and finish."),
    ("Built For The Highveld","Properly framed and fixed, in hardwood or treated timber, sealed against sun and rain so your deck still looks good seasons later."),
    ("What The Consultation Covers","A free site assessment where we discuss layout, levels, balustrades and pergolas, followed by a written quote."),
    ("What Honest Pricing Looks Like","Substructure, decking, finishing and any extras are itemised. You approve a fixed quote before we break ground.")],
  "why":["Engineered and sealed for Highveld weather","Designed around your home and how you entertain","Carpentry-grade build quality, inside and out","Fixed written quote, no surprises"],
  "included":["Site assessment &amp; design","Framing &amp; substructure","Quality timber decking","Balustrades &amp; steps (optional)","Pergolas &amp; screens (optional)","Sealing &amp; finishing","Hardware &amp; fixings","Clean-up &amp; handover"],
  "faq":[("What timber do you use for decks?","Hardwoods and properly treated timber suited to outdoor use, sealed to resist sun and rain. We'll recommend options to suit your budget."),("Do you build pergolas and balustrades too?","Yes — pergolas, screens, steps and balustrades can all be part of the project."),("How long does a deck take?","Most decks are built within 1–2 weeks depending on size and structure.")],
  "gallery":["p09","p18","p02"],"related":["custom-carpentry","kitchen-remodelling","cabinet-construction-installation"]},
}

# ------------------------------------------------------------- link helpers
def ap(loc): return "" if loc == "root" else "../"
def home_l(loc): return ap(loc) + "index.html"
def sec_l(loc, p): return ap(loc) + p
def svc_l(loc, s): return (ap(loc) + "services/" + s) if loc == "root" else s

# ------------------------------------------------------------------- chrome
def topbar():
    return '''<div class="topbar">
  <div class="container">
    <div class="tb-contact">
      <a href="tel:+27817966895">081 796 6895</a>
      <a class="tb-mail" href="https://maps.google.com/?q=160+Pine+St+Arcadia+Pretoria+0083">160 Pine St, Arcadia, Pretoria</a>
    </div>
    <a class="tb-cta" href="#cta-form">Book a Free Consultation</a>
  </div>
</div>'''

def nav(loc, active=None, active_slug=None):
    a = lambda k: ' class="active"' if active == k else ''
    drop = '          <li><a href="%s">All Services</a></li>\n' % svc_l(loc, "all-services.html")
    for slug, label in NAV:
        cls = ' class="active"' if active_slug == slug else ''
        drop += '          <li><a href="%s"%s>%s</a></li>\n' % (svc_l(loc, slug + ".html"), cls, label)
    return f'''<nav class="nav" id="nav">
  <div class="container">
    <a class="nav-logo" href="{home_l(loc)}" aria-label="PNND Kitchens"><img src="{ap(loc)}img/logo.svg" alt="PNND Kitchens"></a>
    <ul class="menu" id="menu">
      <li><a href="{home_l(loc)}"{a('home')}>home</a></li>
      <li><a href="{sec_l(loc,'about.html')}"{a('about')}>about</a></li>
      <li class="has-sub">
        <a href="{svc_l(loc,'all-services.html')}"{a('services')}>services</a>
        <ul class="submenu">
{drop}        </ul>
      </li>
      <li><a href="{sec_l(loc,'gallery.html')}"{a('gallery')}>gallery</a></li>
      <li><a href="{sec_l(loc,'service-areas.html')}"{a('areas')}>service areas</a></li>
      <li><a href="{sec_l(loc,'process.html')}"{a('process')}>process</a></li>
      <li><a href="{sec_l(loc,'articles.html')}"{a('articles')}>articles</a></li>
      <li><a href="{sec_l(loc,'contact.html')}"{a('contact')}>contact</a></li>
    </ul>
    <div class="nav-cta">
      <div class="nav-phone">we're available now<b>081 796 6895</b></div>
      <a class="btn" href="#cta-form">Free Consultation</a>
      <button class="nav-toggle" id="navToggle" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</nav>'''

RINGS = ['<circle cx="50" cy="50" r="46" fill="none" stroke="#e0ddd7" stroke-width="3"/><circle cx="50" cy="50" r="46" fill="none" stroke="#161616" stroke-width="3" stroke-dasharray="72 217"/>',
         '<circle cx="50" cy="50" r="46" fill="none" stroke="#e0ddd7" stroke-width="3"/><circle cx="50" cy="50" r="46" fill="none" stroke="#161616" stroke-width="3" stroke-dasharray="145 144"/>',
         '<circle cx="50" cy="50" r="46" fill="none" stroke="#e0ddd7" stroke-width="3"/><circle cx="50" cy="50" r="46" fill="none" stroke="#161616" stroke-width="3" stroke-dasharray="217 72"/>',
         '<circle cx="50" cy="50" r="46" fill="none" stroke="#161616" stroke-width="3"/>']
STEPS = [("consultation","A free home visit. We measure, listen, and understand exactly how you live."),
         ("design","Drawings and a fixed written quote — every line explained before you commit."),
         ("build","Crafted by hand in our Pretoria workshop using quality timber and fittings."),
         ("install","Our own team fits everything cleanly, then walks you through the result.")]
def process_steps():
    out = ""
    for i,(h,p) in enumerate(STEPS):
        out += f'''      <div class="step reveal">
        <div class="ring"><svg viewBox="0 0 100 100">{RINGS[i]}</svg><span class="rn">0{i+1}</span></div>
        <h3>{h}</h3><p>{p}</p>
      </div>\n'''
    return out

def cta_form(loc, with_map=True):
    opts = "".join('            <option>%s</option>\n' % l for _, l in NAV)
    mp = f'''      <div class="map-embed">
        <iframe title="PNND Kitchens location" loading="lazy" src="https://maps.google.com/maps?q=160%20Pine%20St%20Arcadia%20Pretoria%200083&t=m&z=14&output=embed&iwloc=near"></iframe>
      </div>
''' if with_map else ""
    return f'''<section class="section cta-band" id="cta-form">
  <div class="cta-bg"><img src="{ap(loc)}img/p13.jpg" alt=""></div>
  <div class="container">
    <div class="reveal">
      <span class="eyebrow">ready to start?</span>
      <h2>Book Your Free Consultation Today</h2>
      <p class="lead">Tell us about your project. We will measure it, walk you through the options, and give you a written quote the same week — with no obligation.</p>
      <div class="contact-rows">
        <a class="contact-row" href="tel:+27817966895"><span class="cr-ic">&#9742;</span><span><small>Call us</small><b>081 796 6895</b></span></a>
        <a class="contact-row" href="sms:+27817966895"><span class="cr-ic">&#9993;</span><span><small>Text message</small><b>081 796 6895</b></span></a>
        <a class="contact-row" href="https://maps.google.com/?q=160+Pine+St+Arcadia+Pretoria+0083"><span class="cr-ic">&#8982;</span><span><small>Visit the workshop</small><b>160 Pine St, Arcadia, Pretoria, 0083</b></span></a>
      </div>
{mp}    </div>
    <div class="lead-card lead-card--dark reveal">
      <h3>Request My Free Quote</h3>
      <div class="lc-sub">We reply the same week — promise.</div>
      <form class="lead-form" novalidate>
        <div class="form-grid">
          <input class="field" type="text" name="name" placeholder="Your Name" required>
          <input class="field" type="tel" name="phone" placeholder="Phone Number" required>
          <input class="field full" type="email" name="email" placeholder="Email Address" required>
          <select class="field full" name="service" required>
            <option value="" selected disabled>How Can We Help?</option>
{opts}          </select>
        </div>
        <button class="btn btn-block" type="submit" style="margin-top:14px">Get My Free Quote →</button>
        <p class="disclaimer">We will never send you unsolicited messages. No obligation. No pressure.</p>
        <div class="form-success">Thank you &mdash; your request has been received. We'll be in touch shortly.</div>
      </form>
    </div>
  </div>
</section>'''

def footer(loc):
    svcs = "".join('        <a href="%s">%s</a>\n' % (svc_l(loc, s + ".html"), l) for s, l in NAV)
    return f'''<footer class="footer">
  <div class="container">
    <div class="fcols">
      <div class="fbrand">
        <img src="{ap(loc)}img/logo.svg" alt="PNND Kitchens">
        <p>Arcadia's owner-led studio for kitchen remodelling, custom cabinets, closets, carpentry and decks. Design &middot; Quality &middot; Perfection.</p>
      </div>
      <div>
        <h4>Services</h4>
{svcs}      </div>
      <div>
        <h4>Quick Links</h4>
        <a href="{sec_l(loc,'about.html')}">About</a>
        <a href="{sec_l(loc,'gallery.html')}">Gallery</a>
        <a href="{sec_l(loc,'service-areas.html')}">Service Areas</a>
        <a href="{sec_l(loc,'process.html')}">Process</a>
        <a href="{sec_l(loc,'articles.html')}">Articles</a>
        <a href="{sec_l(loc,'contact.html')}">Contact</a>
      </div>
      <div>
        <h4>Get in Touch</h4>
        <a href="tel:+27817966895">081 796 6895</a>
        <a href="sms:+27817966895">Text message</a>
        <a href="https://maps.google.com/?q=160+Pine+St+Arcadia+Pretoria+0083">160 Pine St, Arcadia, Pretoria, 0083</a>
        <a href="{sec_l(loc,'contact.html')}" class="hours" style="margin-top:10px"><span>Mon &ndash; Thu</span><b>7:00 &ndash; 17:30</b></a>
        <a href="{sec_l(loc,'contact.html')}" class="hours"><span>Fri</span><b>7:00 &ndash; 16:00</b></a>
        <a href="{sec_l(loc,'contact.html')}" class="hours"><span>Sat</span><b>8:00 &ndash; 14:00</b></a>
        <a class="btn btn-light" href="#cta-form" style="margin-top:14px">Free Consultation</a>
      </div>
    </div>
    <div class="fbar">
      <span>&copy; 2026 PNND Kitchens. All rights reserved.</span>
      <span>Design &middot; Quality &middot; Perfection</span>
    </div>
  </div>
</footer>'''

def mobile():
    return '''<div class="mobile-bar">
  <a class="mb-call" href="tel:+27817966895">Call Now</a>
  <a class="mb-cta" href="#cta-form">Free Consultation</a>
</div>'''

def head(loc, title, desc, hero=None):
    pl = '\n<link rel="preload" as="image" href="%simg/%s.jpg">' % (ap(loc), hero) if hero else ''
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/svg+xml" href="{ap(loc)}img/logo.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{ap(loc)}css/style.css">{pl}
<script>document.documentElement.className+=' js';</script>
</head>
<body class="svc-page">'''

def hero(loc, crumbs, eyebrow, title, sub):
    bc = '<a href="%s">home</a>' % home_l(loc)
    for label, href in crumbs:
        bc += '<span>/</span>' + (('<a href="%s">%s</a>' % (href, label)) if href else label)
    return f'''<header class="hero hero--service">
  <div class="hero-bg"><img src="{ap(loc)}img/{ {'h':1} and 'p01' }.jpg" alt=""></div>
  <div class="container">
    <div class="hero-copy reveal">
      <div class="breadcrumb">{bc}</div>
      <span class="eyebrow">{eyebrow}</span>
      <h1>{title}</h1>
      <p class="hero-sub">{sub}</p>
      <div class="hero-cta">
        <a class="btn btn-light" href="#cta-form">Get My Free Quote →</a>
        <a class="btn btn-light" href="tel:+27817966895" style="background:transparent;color:#fff;border-color:rgba(255,255,255,.5)">Call 081 796 6895</a>
      </div>
    </div>
  </div>
</header>'''

def hero_img(loc, crumbs, eyebrow, title, sub, img):
    bc = '<a href="%s">home</a>' % home_l(loc)
    for label, href in crumbs:
        bc += '<span>/</span>' + (('<a href="%s">%s</a>' % (href, label)) if href else label)
    return f'''<header class="hero hero--service">
  <div class="hero-bg"><img src="{ap(loc)}img/{img}.jpg" alt="PNND Kitchens"></div>
  <div class="container">
    <div class="hero-copy reveal">
      <div class="breadcrumb">{bc}</div>
      <span class="eyebrow">{eyebrow}</span>
      <h1>{title}</h1>
      <p class="hero-sub">{sub}</p>
      <div class="hero-cta">
        <a class="btn btn-light" href="#cta-form">Get My Free Quote →</a>
        <a class="btn btn-light" href="tel:+27817966895" style="background:transparent;color:#fff;border-color:rgba(255,255,255,.5)">Call 081 796 6895</a>
      </div>
    </div>
  </div>
</header>'''

def wrap(loc, active, title, desc, hero_img_id, crumbs, eyebrow, htitle, hsub, body):
    return f'''{head(loc,title,desc,hero_img_id)}

{topbar()}

{nav(loc, active=active)}
<span id="top"></span>

{hero_img(loc,crumbs,eyebrow,htitle,hsub,hero_img_id)}

{body}

{footer(loc)}

{mobile()}

<script src="{ap(loc)}js/main.js"></script>
</body>
</html>
'''

# --------------------------------------------------------- service detail page
def service_page(slug, d):
    loc = "svc"
    overview = "".join(f'      <div class="ov-block reveal"><h2>{h}</h2><p>{p}</p></div>\n' for h,p in d["overview"])
    why = "".join(f'        <li class="why-item reveal"><span class="why-num">{i+1}</span><span>{w}</span></li>\n' for i,w in enumerate(d["why"]))
    inc = "".join(f'        <div class="inc-card reveal"><span class="cb">✓</span><span>{x}</span></div>\n' for x in d["included"])
    gallery = "".join(f'      <a href="../img/{g}.jpg"><img src="../img/{g}.jpg" alt="{d["label"]} project by PNND Kitchens"></a>\n' for g in d["gallery"])
    faq = "".join(f'''      <div class="faq-item reveal"><button class="faq-q">{q}<span class="ic">+</span></button>
        <div class="faq-a"><p>{a}</p></div></div>\n''' for q,a in d["faq"])
    related = ""
    for rs in d["related"]:
        r = S[rs]
        related += f'''      <a class="svc-card reveal" href="{rs}.html"><img src="../img/{r["hero"]}.jpg" alt="{r["label"]}">
        <div class="svc-body"><h3>{r["eyebrow"]}</h3><p>Learn more about our {r["label"].lower()} work.</p><span class="more">View service &rarr;</span></div></a>\n'''
    plain = d["label"].replace("&amp;","and")
    body = f'''<!-- OVERVIEW -->
<section class="section bg-grid">
  <div class="container" style="max-width:980px">
{overview}  </div>
</section>

<!-- WHY + INCLUDED -->
<section class="section bg-alt">
  <div class="container svc-split">
    <div>
      <span class="eyebrow reveal">why pnnd</span>
      <h2 class="reveal" style="margin-bottom:24px">Why PNND For {d["label"]}</h2>
      <ul class="why-list">
{why}      </ul>
    </div>
    <div>
      <span class="eyebrow reveal">scope of work</span>
      <h2 class="reveal" style="margin-bottom:24px">What's Included</h2>
      <div class="inc-grid">
{inc}      </div>
    </div>
  </div>
</section>

<!-- PROCESS -->
<section class="section">
  <div class="container">
    <div class="section-head center"><span class="eyebrow reveal">how it works</span><h2 class="reveal">Four Steps, No Surprises</h2></div>
    <div class="steps">
{process_steps()}    </div>
  </div>
</section>

<!-- GALLERY -->
<section class="section bg-alt">
  <div class="container">
    <div class="section-head center"><span class="eyebrow reveal">our work</span><h2 class="reveal">Recent {d["label"]} Projects</h2></div>
    <div class="gallery3 reveal">
{gallery}    </div>
  </div>
</section>

<!-- FAQ -->
<section class="section">
  <div class="container">
    <div class="section-head center"><span class="eyebrow reveal">questions</span><h2 class="reveal">Common Questions</h2></div>
    <div class="faq">
{faq}    </div>
  </div>
</section>

<!-- YOU MAY ALSO NEED -->
<section class="section bg-alt">
  <div class="container">
    <div class="section-head center"><span class="eyebrow reveal">you may also need</span><h2 class="reveal">Explore Our Other Services</h2></div>
    <div class="related">
{related}    </div>
  </div>
</section>

{cta_form(loc)}'''
    page = f'''{head(loc, plain+" in Pretoria | PNND Kitchens", plain+" by PNND Kitchens — owner-led carpentry in Arcadia, Pretoria. Designed, built and installed by hand. Free consultation. Call 081 796 6895.", d["hero"])}

{topbar()}

{nav(loc, active="services", active_slug=slug)}
<span id="top"></span>

{hero_img(loc, [("services", "all-services.html"), (d["eyebrow"], None)], d["tagline"], d["head"], d["intro"], d["hero"])}

{body}

{footer(loc)}

{mobile()}

<script src="../js/main.js"></script>
</body>
</html>
'''
    return page

def all_services():
    loc = "svc"
    cards = ""
    for slug,label in NAV:
        d = S[slug]
        cards += f'''      <a class="svc-card reveal" href="{slug}.html"><img src="../img/{d["hero"]}.jpg" alt="{label}">
        <div class="svc-body"><h3>{d["eyebrow"]}</h3><p>{d["tagline"]}</p><span class="more">View service &rarr;</span></div></a>\n'''
    body = f'''<section class="section">
  <div class="container">
    <div class="section-head center"><span class="eyebrow reveal">what we do</span><h2 class="reveal">One Workshop, Every Detail</h2></div>
    <div class="services-grid">
{cards}    </div>
  </div>
</section>

{cta_form(loc)}'''
    return f'''{head(loc,"All Services | PNND Kitchens","All services from PNND Kitchens — kitchen remodelling, cabinets, closets, custom carpentry, repairs and decks in Pretoria. Free consultation. Call 081 796 6895.","p01")}

{topbar()}

{nav(loc, active="services")}
<span id="top"></span>

{hero_img(loc, [("services", None)], "kitchen remodelling &amp; bespoke carpentry", "Our Services", "Everything we design, build, install and repair — one accountable Arcadia workshop. Pick a service to see exactly what's involved.", "p01")}

{body}

{footer(loc)}

{mobile()}

<script src="../js/main.js"></script>
</body>
</html>
'''

# ---------------------------------------------------------- secondary pages (root)
def page_about():
    loc="root"
    body = '''<section class="section">
  <div class="container split">
    <div class="split-media reveal"><img src="img/p07.jpg" alt="PNND Kitchens craftsmanship"><div class="tag"><b>5.0★</b><span>Google rated</span></div></div>
    <div class="reveal">
      <span class="eyebrow">meet the master carpenter</span>
      <h2>Owner-Led. Local. Made In Pretoria.</h2>
      <p class="lead" style="margin-bottom:8px">PNND Kitchens is the Arcadia workshop your neighbours recommend by name. The owner answers every call, measures every room, and stays on every project until the last hinge is aligned and the floor is swept.</p>
      <blockquote class="mission">"To be the Pretoria studio homeowners recommend by name when a friend needs a new kitchen."</blockquote>
      <ul class="values">
        <li><b>Honest design.</b> Clear quotes, no pressure, no surprise charges.</li>
        <li><b>Documented work.</b> Every stage photographed and explained.</li>
        <li><b>Local hands.</b> Our own carpentry team — never subcontracted.</li>
        <li><b>Build, install &amp; repair.</b> One team for new work and fixes.</li>
      </ul>
    </div>
  </div>
</section>
<section class="section bg-alt">
  <div class="container split rev">
    <div class="split-media reveal"><img src="img/p10.jpg" alt="PNND Kitchens workshop"><div class="tag"><b>500+</b><span>projects built</span></div></div>
    <div class="reveal">
      <span class="eyebrow">why homeowners choose us</span>
      <h2>Crafted For Your Home</h2>
      <p class="lead" style="margin-bottom:8px">Kitchens, cabinets and carpentry across Pretoria and Gauteng. We live here. Your guarantee is good with someone who is not leaving town.</p>
      <ul class="values">
        <li><b>One accountable team</b> — design, build and install, never subcontracted.</li>
        <li><b>Premium materials</b> — solid timber, quality board and fittings.</li>
        <li><b>On time, on budget</b> — a written schedule and a fixed written quote.</li>
        <li><b>Repairs too</b> — we fix and refit, not just build new.</li>
      </ul>
    </div>
  </div>
</section>
<section class="section">
  <div class="container center">
    <div class="section-head"><span class="eyebrow reveal">what clients say</span><h2 class="reveal">5.0★ On Google</h2></div>
    <div class="review-grid">
      <div class="review reveal"><div class="stars">★★★★★</div><p>"Highly recommend PNND Kitchens! They remodelled our kitchen and fitted the cupboards — flawless finish, right on schedule."</p><div class="who"><span class="av">T</span><span><b>Thabo M.</b><small>Arcadia, Pretoria</small></span></div></div>
      <div class="review reveal"><div class="stars">★★★★★</div><p>"Everything was handled by the owner himself. Our built-in closets are a work of art."</p><div class="who"><span class="av">L</span><span><b>Lerato D.</b><small>Centurion</small></span></div></div>
      <div class="review reveal"><div class="stars">★★★★★</div><p>"True craftsmen. Honest advice, fair price, cabinetry that feels like fine furniture."</p><div class="who"><span class="av">J</span><span><b>Johan v.</b><small>Waterkloof</small></span></div></div>
    </div>
  </div>
</section>
''' + cta_form(loc)
    return wrap(loc,"about","About | PNND Kitchens","About PNND Kitchens — owner-led kitchen remodelling and carpentry in Arcadia, Pretoria. 5.0★ on Google. Free consultation, call 081 796 6895.","p07",
                [("about",None)],"owner-led &middot; made in pretoria","About PNND Kitchens","One accountable Arcadia workshop for kitchen remodelling, cabinets, closets and carpentry.",body)

def page_gallery():
    loc="root"
    imgs=["p01","p13","p02","p14","p05","p12","p03","p11","p06","p10","p08","p17"]
    g="".join(f'      <a href="img/{i}.jpg"><img src="img/{i}.jpg" alt="PNND Kitchens project in Pretoria"></a>\n' for i in imgs)
    body=f'''<section class="section">
  <div class="container">
    <div class="section-head center"><span class="eyebrow reveal">our work</span><h2 class="reveal">Projects We Have Built</h2><p class="lead center reveal" style="margin-top:14px">A sample of recent Pretoria kitchens, cabinetry, closets and carpentry. Tap any photo to see the detail.</p></div>
    <div class="gallery">
{g}    </div>
  </div>
</section>
{cta_form(loc)}'''
    return wrap(loc,"gallery","Gallery | PNND Kitchens","Gallery of PNND Kitchens projects — kitchen remodels, cabinetry, closets and carpentry across Pretoria & Gauteng.","p13",
                [("gallery",None)],"recent projects","Our Work","A look at the kitchens, cabinets, closets and carpentry we've built across Pretoria.",body)

def page_areas():
    loc="root"
    areas=["Arcadia","Hatfield","Brooklyn","Menlyn","Lynnwood","Waterkloof","Centurion","Montana"]
    a="".join(f'      <span class="area">{x}</span>\n' for x in areas)
    body=f'''<section class="section">
  <div class="container center">
    <div class="section-head"><span class="eyebrow reveal">where we work</span><h2 class="reveal">Serving Pretoria &amp; Gauteng</h2><p class="lead center reveal" style="margin-top:14px">Based in Arcadia, working across the city. We live here, we work here, and we stand behind every project nearby.</p></div>
    <div class="areas reveal">
{a}    </div>
    <div class="map-embed reveal" style="margin-top:34px"><iframe title="PNND Kitchens location" loading="lazy" src="https://maps.google.com/maps?q=160%20Pine%20St%20Arcadia%20Pretoria%200083&t=m&z=12&output=embed&iwloc=near"></iframe></div>
  </div>
</section>
{cta_form(loc, with_map=False)}'''
    return wrap(loc,"areas","Service Areas | PNND Kitchens","PNND Kitchens serves Pretoria & Gauteng — Arcadia, Hatfield, Brooklyn, Menlyn, Lynnwood, Waterkloof, Centurion and Montana.","p10",
                [("service areas",None)],"pretoria &amp; gauteng","Service Areas","Local crews across Pretoria and the wider Gauteng area, run from our Arcadia workshop.",body)

def page_process():
    loc="root"
    body=f'''<section class="section">
  <div class="container">
    <div class="section-head center"><span class="eyebrow reveal">how it works</span><h2 class="reveal">Four Steps, No Surprises</h2><p class="lead center reveal" style="margin-top:14px">Consultation. Design. Build. Install. Each step photographed and explained — you are in control the whole way.</p></div>
    <div class="steps">
{process_steps()}    </div>
  </div>
</section>
<section class="section bg-alt">
  <div class="container" style="max-width:980px">
    <div class="ov-block reveal"><h2>You're In Control At Every Step</h2><p style="color:#46443f;font-weight:300">No pressure, no obligation, no surprise charges. We document each stage, explain what we're doing and why, and call before anything changes. The same owner-led team runs your project from the first measure to the final clean-up.</p></div>
    <div class="ov-block reveal"><h2>Honest, Written Pricing</h2><p style="color:#46443f;font-weight:300">Your quote is line-itemed and fixed before any work begins, so you always know exactly what you're paying for.</p></div>
  </div>
</section>
{cta_form(loc)}'''
    return wrap(loc,"process","Our Process | PNND Kitchens","How PNND Kitchens works — consultation, design, build and install. Owner-led, documented, with a fixed written quote.","p04",
                [("process",None)],"how it works","Our Process","From first measure to final fit — a clear four-step process with no surprises.",body)

def page_articles():
    loc="root"
    posts=[("p16","What A Kitchen Remodel Costs In Pretoria In 2026","Most kitchen remodels in Pretoria run between R80,000 and R350,000. What drives the number, and how to read an honest quote."),
           ("p17","Why Solid Timber &amp; Quality Board Beat Flat-Pack","The materials behind a cabinet decide how it ages. Here's what to look for — and what quietly fails after a few years."),
           ("p18","Planning Built-in Closets That Last","When built-in closets beat free-standing furniture, and how to design storage around the rooms you actually use."),
           ("p05","Choosing The Right Kitchen Layout","Galley, L-shape, island or peninsula — how to pick a layout that fits how you actually cook."),
           ("p08","Caring For A Timber Deck In The Highveld","Sealing, cleaning and seasonal upkeep that keeps a Pretoria deck looking good for years."),
           ("p12","Small Kitchen, Smart Storage","Clever cabinetry tricks that make a compact Pretoria kitchen feel twice the size.")]
    cards="".join(f'''      <article class="post reveal"><div class="ph"><img src="img/{i}.jpg" alt="{t}"></div>
        <div class="pb"><h3>{t}</h3><p>{x}</p><a class="more" href="contact.html">Read more →</a></div></article>\n''' for i,t,x in posts)
    body=f'''<section class="section">
  <div class="container">
    <div class="section-head center"><span class="eyebrow reveal">knowledge &amp; advice</span><h2 class="reveal">Kitchen &amp; Carpentry Tips For Pretoria Homeowners</h2><p class="lead center reveal" style="margin-top:14px">Plain-spoken guidance from carpenters who build these projects every week.</p></div>
    <div class="posts">
{cards}    </div>
  </div>
</section>
{cta_form(loc)}'''
    return wrap(loc,"articles","Articles | PNND Kitchens","Kitchen and carpentry tips from PNND Kitchens — remodelling costs, materials, closet planning and more, for Pretoria homeowners.","p16",
                [("articles",None)],"knowledge &amp; advice","Articles","Plain-spoken guidance from the workshop — costs, materials and ideas for your project.",body)

def page_contact():
    loc="root"
    body=f'''<section class="section">
  <div class="container">
    <div class="section-head center"><span class="eyebrow reveal">opening hours</span><h2 class="reveal">When You Can Reach Us</h2></div>
    <div class="areas reveal" style="grid-template-columns:repeat(4,1fr)">
      <span class="area">Mon–Thu<br><b style="color:var(--ink)">7:00–17:30</b></span>
      <span class="area">Friday<br><b style="color:var(--ink)">7:00–16:00</b></span>
      <span class="area">Saturday<br><b style="color:var(--ink)">8:00–14:00</b></span>
      <span class="area">Sunday<br><b style="color:var(--ink)">Closed</b></span>
    </div>
  </div>
</section>
{cta_form(loc)}'''
    return wrap(loc,"contact","Contact | PNND Kitchens","Contact PNND Kitchens in Arcadia, Pretoria — call or text 081 796 6895, or request a free quote. Mon–Sat.","p01",
                [("contact",None)],"book a free consultation","Contact Us","Call, text or send us your project — we reply the same week, with no obligation.",body)

# ---------------------------------------------------------------------- write
if __name__ == "__main__":
    for slug, d in S.items():
        open(os.path.join(SVC_DIR, slug + ".html"), "w", encoding="utf-8").write(service_page(slug, d))
        print("services/%s.html" % slug)
    open(os.path.join(SVC_DIR, "all-services.html"), "w", encoding="utf-8").write(all_services())
    print("services/all-services.html")
    for name, fn in [("about", page_about), ("gallery", page_gallery), ("service-areas", page_areas),
                     ("process", page_process), ("articles", page_articles), ("contact", page_contact)]:
        open(os.path.join(ROOT, name + ".html"), "w", encoding="utf-8").write(fn())
        print(name + ".html")
    print("done")
