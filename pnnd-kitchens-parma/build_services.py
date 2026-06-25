#!/usr/bin/env python3
"""Generate dedicated service pages for PNND Kitchens.

Structure follows Website A's service-page conversion framework
(hero -> overview -> info grid -> what's included -> why -> process ->
gallery -> FAQ -> 'you may also need' cross-sell -> CTA form), rendered
in Website B's (Twelve) minimalist visual language. Shared nav/footer.
"""
import os, html

OUT = os.path.join(os.path.dirname(__file__), "services")
os.makedirs(OUT, exist_ok=True)

# nav order (slug, label)
NAV = [
    ("kitchen-remodelling", "Kitchen Remodelling"),
    ("cabinet-construction-installation", "Cabinet Construction &amp; Installation"),
    ("closet-construction-installation", "Closet Construction &amp; Installation"),
    ("custom-closet-design", "Custom Closet Design"),
    ("custom-carpentry", "Custom Carpentry"),
    ("cabinet-closet-repair", "Cabinet &amp; Closet Repair"),
    ("deck-construction", "Deck Construction"),
]

# per-service content
S = {
 "kitchen-remodelling": {
  "label":"Kitchen Remodelling","eyebrow":"kitchen remodelling","hero":"p01",
  "head":"kitchen remodelling in pretoria, done by hand",
  "lede":["A new kitchen is the single biggest change you can make to a home — and the one most worth getting right. We remodel kitchens end to end: layout, cabinetry, counters, lighting and finishes, designed around how you actually cook and live.",
          "From a first free measure-up to the final clean-up, the same owner-led team handles your project. No subcontracted chaos, no surprise charges — just one accountable workshop in Arcadia."],
  "info":[("Design","3D layouts and finish boards before a single board is cut."),
          ("Materials","Solid timber, quality board, stone and premium fittings."),
          ("Timeline","A written schedule, agreed up front and kept to."),
          ("Guarantee","Workmanship we stand behind, with aftercare you can reach.")],
  "included":["Full design &amp; 3D layout","Custom cabinetry &amp; carcasses","Countertops &amp; splashbacks",
              "Soft-close hinges &amp; runners","Lighting &amp; electrical coordination","Removal of the old kitchen",
              "Professional installation","Final snag &amp; clean-up"],
  "why":[("Owner-led","The person who quotes your kitchen is on site building it."),
         ("One team","Design, build and install under one roof — fewer trades, fewer delays."),
         ("Fixed quote","Every line explained and priced before work starts.")],
  "faq":[("How long does a kitchen remodel take?","Most kitchens take 3–6 weeks from sign-off, depending on size and finishes. You get a written schedule before we begin."),
         ("Can you work with my existing layout?","Yes — we can refresh within your current footprint or redesign the layout entirely. We advise on what adds the most value."),
         ("What does a kitchen cost in Pretoria?","Most remodels run between R80,000 and R350,000. We quote after a free measure-up so the price fits your space and finishes.")],
  "gallery":["p02","p13","p14"],
  "related":["cabinet-construction-installation","custom-carpentry","closet-construction-installation"],
 },
 "cabinet-construction-installation": {
  "label":"Cabinet Construction &amp; Installation","eyebrow":"cabinet construction","hero":"p03",
  "head":"custom cabinets, built &amp; installed by hand",
  "lede":["Made-to-measure cabinets for kitchens, sculleries, TV units and storage — built in our Pretoria workshop and installed by the same team. Every carcass is square, every door aligned, every runner soft-close.",
          "We build to the millimetre for your space, so there are no filler panels or awkward gaps — just clean, considered cabinetry that looks built-in because it is."],
  "info":[("Made to measure","Built to your exact dimensions, not flat-pack sizes."),
          ("Finishes","Melamine, veneer, spray-paint and wrap options."),
          ("Hardware","Blum-style soft-close hinges &amp; runners."),
          ("Install","Fitted and levelled by our own carpenters.")],
  "included":["On-site measure &amp; design","Custom carcasses &amp; doors","Soft-close hardware",
              "Edging &amp; finishing","Handles &amp; accessories","Delivery &amp; installation",
              "Levelling &amp; alignment","Snag &amp; clean-up"],
  "why":[("Precision","Built to the millimetre — no fillers, no gaps."),
         ("Durability","Quality board and timber that survives daily use."),
         ("Accountable","One team from measure to final screw.")],
  "faq":[("What materials do you use?","Quality moisture-resistant board, solid timber and real veneers, with soft-close hardware as standard. We'll show samples at the consultation."),
         ("Do you install what you build?","Always. The team that builds your cabinets installs them, so quality is owned end to end."),
         ("Can you match an existing kitchen?","Yes — we colour- and finish-match to extend or repair existing cabinetry wherever possible.")],
  "gallery":["p04","p11","p06"],
  "related":["kitchen-remodelling","closet-construction-installation","cabinet-closet-repair"],
 },
 "closet-construction-installation": {
  "label":"Closet Construction &amp; Installation","eyebrow":"closets &amp; wardrobes","hero":"p04",
  "head":"built-in closets that use every centimetre",
  "lede":["Floor-to-ceiling built-in cupboards and wardrobes, designed around your room and the way you store. Hanging space, drawers, shelving and shoe racks — laid out to fit your life, not an off-the-shelf module.",
          "Built and installed by our own team, with finishes that match your bedroom or remodelled kitchen."],
  "info":[("Made to measure","Floor-to-ceiling, wall-to-wall — zero wasted space."),
          ("Interiors","Hanging, drawers, shelving and accessory options."),
          ("Finishes","Matched to your room and existing joinery."),
          ("Install","Scribed and fitted flush to your walls.")],
  "included":["On-site measure &amp; design","Custom carcasses &amp; doors","Internal hanging &amp; shelving",
              "Soft-close drawers","Mirrors &amp; accessories (optional)","Delivery &amp; installation",
              "Scribing to walls","Snag &amp; clean-up"],
  "why":[("Space-smart","Designed around your room and your storage habits."),
         ("Seamless","Scribed to the wall so it reads as part of the house."),
         ("One team","Designed, built and fitted by the same crew.")],
  "faq":[("Hinged or sliding doors?","Both. Sliding doors suit tight rooms; hinged doors give full access. We advise based on your space at the measure-up."),
         ("Can you fit into an alcove or sloped ceiling?","Yes — built-ins are ideal for awkward spaces. We scribe and build to fit exactly."),
         ("How long does installation take?","Most built-in closets are installed in 1–3 days once built, with minimal disruption.")],
  "gallery":["p05","p12","p10"],
  "related":["custom-closet-design","cabinet-construction-installation","kitchen-remodelling"],
 },
 "custom-closet-design": {
  "label":"Custom Closet Design","eyebrow":"custom closet design","hero":"p05",
  "head":"walk-in &amp; dressing room design, tailored to you",
  "lede":["For walk-in closets and dressing rooms, design is everything. We plan zones for hanging, folding, shoes and accessories, then craft a system that feels calm, considered and entirely yours.",
          "You'll see the layout in 3D before we build, so you know exactly how it works the day it's installed."],
  "info":[("3D design","See your closet before it's built."),
          ("Zoning","Dedicated space for every category."),
          ("Lighting","Integrated LED options for that boutique feel."),
          ("Bespoke","Drawers, glass fronts, valet rails and more.")],
  "included":["Consultation &amp; 3D design","Zoned hanging &amp; storage plan","Drawers, shelving &amp; rails",
              "Optional integrated lighting","Glass-front &amp; display options","Build &amp; installation",
              "Finishing &amp; alignment","Snag &amp; clean-up"],
  "why":[("Tailored","Every closet is planned around your wardrobe, not a template."),
         ("Boutique feel","Lighting, finishes and detailing that elevate the room."),
         ("End to end","Design, build and install from one studio.")],
  "faq":[("Do you provide 3D drawings?","Yes — every custom closet starts with a 3D design so you can see and adjust the layout before we build."),
         ("Can you add lighting?","Absolutely. Integrated LED strip and sensor lighting are popular options we coordinate during the build."),
         ("How much does a walk-in closet cost?","It depends on size and detailing. We quote a fixed price after the free design consultation.")],
  "gallery":["p10","p12","p07"],
  "related":["closet-construction-installation","custom-carpentry","kitchen-remodelling"],
 },
 "custom-carpentry": {
  "label":"Custom Carpentry","eyebrow":"custom carpentry","hero":"p06",
  "head":"bespoke joinery for every room",
  "lede":["Vanities, media units, study desks, shelving, wine racks and feature joinery — if it can be built in timber, we can craft it. One-off pieces made to measure for your home or business.",
          "Tell us what you need and where it goes; we'll design, build and install it to last."],
  "info":[("Anything bespoke","Vanities, desks, shelving, feature walls."),
          ("Materials","Solid timber, veneer and quality board."),
          ("Made to measure","Built for your exact space and use."),
          ("Install","Fitted cleanly by our own carpenters.")],
  "included":["Design &amp; measure","Bespoke build in our workshop","Quality timber &amp; finishes",
              "Hardware &amp; fittings","Delivery &amp; installation","Finishing &amp; alignment",
              "Commercial &amp; residential","Snag &amp; clean-up"],
  "why":[("Truly bespoke","One-off pieces, not catalogue furniture."),
         ("Craftsmanship","Joinery finished to furniture standard."),
         ("Flexible","Residential and commercial projects welcome.")],
  "faq":[("What kinds of carpentry do you take on?","Vanities, media units, desks, shelving, wine storage, feature panelling and more — residential and commercial."),
         ("Can you match existing furniture?","Yes, we colour- and finish-match wherever possible so new pieces feel original to the space."),
         ("Do you do commercial fit-outs?","We do — reception counters, retail joinery and office storage are all within our scope.")],
  "gallery":["p08","p15","p17"],
  "related":["cabinet-construction-installation","cabinet-closet-repair","deck-construction"],
 },
 "cabinet-closet-repair": {
  "label":"Cabinet &amp; Closet Repair","eyebrow":"cabinet &amp; closet repair","hero":"p11",
  "head":"repairs &amp; refits that bring units back to life",
  "lede":["Not everything needs replacing. Sagging doors, broken hinges, blown board, worn runners and tired finishes can often be repaired or refitted for a fraction of a new build.",
          "We assess honestly — if a repair makes sense, we'll fix it; if it doesn't, we'll tell you. Either way you get a fair, fixed quote."],
  "info":[("Doors &amp; hinges","Re-aligned, re-hung or replaced."),
          ("Drawers","New runners and soft-close mechanisms."),
          ("Surfaces","Re-edging, re-wrapping and refinishing."),
          ("Honest advice","Repair vs replace, told straight.")],
  "included":["On-site assessment","Hinge &amp; door alignment","Runner &amp; drawer repair",
              "Board &amp; panel replacement","Re-edging &amp; refinishing","Handle &amp; hardware swaps",
              "Water-damage repairs","Fixed written quote"],
  "why":[("Cost-smart","Repair for a fraction of replacement, where it makes sense."),
         ("Fast","Most repairs are quick, scheduled and tidy."),
         ("Honest","We tell you when a repair isn't worth it.")],
  "faq":[("Is it worth repairing or should I replace?","If the carcasses are sound, repair is usually the smart call. We assess on site and advise honestly."),
         ("Can you fix water-damaged cupboards?","Often yes — we replace affected panels and refinish so it blends in. Severe cases may need a partial rebuild."),
         ("Do you charge for a quote?","Assessment and quoting are free within Pretoria and surrounds.")],
  "gallery":["p03","p06","p16"],
  "related":["cabinet-construction-installation","custom-carpentry","kitchen-remodelling"],
 },
 "deck-construction": {
  "label":"Deck Construction","eyebrow":"deck construction","hero":"p08",
  "head":"solid timber decks built for the highveld",
  "lede":["Outdoor living, done properly. We build solid timber decks, pergolas and outdoor woodwork engineered to handle Pretoria sun, rain and seasons — sealed and finished to last.",
          "From a raised entertainment deck to a simple poolside platform, we design and build to suit your space and budget."],
  "info":[("Materials","Hardwood and treated timber, sealed to last."),
          ("Structure","Properly framed, fixed and weatherproofed."),
          ("Design","Raised, multi-level or poolside layouts."),
          ("Finish","Sanded, sealed and ready to enjoy.")],
  "included":["Site assessment &amp; design","Framing &amp; substructure","Quality timber decking",
              "Balustrades &amp; steps (optional)","Pergolas &amp; screens (optional)","Sealing &amp; finishing",
              "Hardware &amp; fixings","Clean-up &amp; handover"],
  "why":[("Built to last","Engineered and sealed for Highveld weather."),
         ("Bespoke","Designed around your home and how you entertain."),
         ("One team","Carpentry-grade build quality, inside and out.")],
  "faq":[("What timber do you use for decks?","Hardwoods and properly treated timber suited to outdoor use, sealed to resist sun and rain. We'll recommend options to suit your budget."),
         ("Do you build pergolas and balustrades too?","Yes — pergolas, screens, steps and balustrades can all be part of the project."),
         ("How long does a deck take?","Most decks are built within 1–2 weeks depending on size and structure.")],
  "gallery":["p09","p18","p02"],
  "related":["custom-carpentry","kitchen-remodelling","cabinet-construction-installation"],
 },
}

def nav(active):
    items = ""
    for slug, label in NAV:
        cls = ' class="active"' if slug == active else ''
        items += f'          <li><a href="{slug}.html"{cls}>{label}</a></li>\n'
    return f'''<nav class="nav" id="nav">
  <div class="container">
    <a class="nav-logo" href="../index.html" aria-label="PNND Kitchens"><img src="../img/logo.svg" alt="PNND Kitchens"></a>
    <ul class="menu" id="menu">
      <li><a href="../index.html">home</a></li>
      <li><a href="../index.html#about">about</a></li>
      <li class="has-sub">
        <a href="../index.html#services" class="active">services</a>
        <ul class="submenu">
{items}        </ul>
      </li>
      <li><a href="../index.html#gallery">gallery</a></li>
      <li><a href="../index.html#service-area">service areas</a></li>
      <li><a href="../index.html#process">process</a></li>
      <li><a href="../index.html#blog">articles</a></li>
      <li><a href="#cta-form">contact</a></li>
    </ul>
    <div class="nav-cta">
      <div class="nav-phone">we're available now<b>081 796 6895</b></div>
      <a class="btn" href="#cta-form">Free Consultation</a>
      <button class="nav-toggle" id="navToggle" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</nav>'''

TOPBAR = '''<div class="topbar">
  <div class="container">
    <div class="tb-contact">
      <a href="tel:+27817966895">081 796 6895</a>
      <a class="tb-mail" href="https://maps.google.com/?q=160+Pine+St+Arcadia+Pretoria+0083">160 Pine St, Arcadia, Pretoria</a>
    </div>
    <a class="tb-cta" href="#cta-form">Book a Free Consultation</a>
  </div>
</div>'''

RINGS = ['<circle cx="50" cy="50" r="46" fill="none" stroke="#e0ddd7" stroke-width="3"/><circle cx="50" cy="50" r="46" fill="none" stroke="#161616" stroke-width="3" stroke-dasharray="72 217"/>',
         '<circle cx="50" cy="50" r="46" fill="none" stroke="#e0ddd7" stroke-width="3"/><circle cx="50" cy="50" r="46" fill="none" stroke="#161616" stroke-width="3" stroke-dasharray="145 144"/>',
         '<circle cx="50" cy="50" r="46" fill="none" stroke="#e0ddd7" stroke-width="3"/><circle cx="50" cy="50" r="46" fill="none" stroke="#161616" stroke-width="3" stroke-dasharray="217 72"/>',
         '<circle cx="50" cy="50" r="46" fill="none" stroke="#161616" stroke-width="3"/>']
STEPS = [("consultation","A free home visit. We measure, listen, and understand exactly how you live."),
         ("design","Drawings and a fixed written quote — every line explained before you commit."),
         ("build","Crafted by hand in our Pretoria workshop using quality timber and fittings."),
         ("install","Our own team fits everything cleanly, then walks you through the result.")]

def process():
    cells = ""
    for i,(h,p) in enumerate(STEPS):
        cells += f'''      <div class="step reveal">
        <div class="ring"><svg viewBox="0 0 100 100">{RINGS[i]}</svg><span class="rn">0{i+1}</span></div>
        <h3>{h}</h3><p>{p}</p>
      </div>\n'''
    return cells

def cta_form():
    opts = "".join(f'            <option>{l}</option>\n' for _,l in NAV)
    return f'''<section class="section cta-band" id="cta-form">
  <div class="cta-bg"><img src="../img/p13.jpg" alt=""></div>
  <div class="container">
    <div class="reveal">
      <span class="eyebrow">ready to start?</span>
      <h2>book your free consultation today</h2>
      <p class="lead">Tell us about your project. We will measure it, walk you through the options, and give you a written quote the same week — with no obligation.</p>
      <div class="contact-rows">
        <a class="contact-row" href="tel:+27817966895"><span class="cr-ic">&#9742;</span><span><small>Call us</small><b>081 796 6895</b></span></a>
        <a class="contact-row" href="sms:+27817966895"><span class="cr-ic">&#9993;</span><span><small>Text message</small><b>081 796 6895</b></span></a>
        <a class="contact-row" href="https://maps.google.com/?q=160+Pine+St+Arcadia+Pretoria+0083"><span class="cr-ic">&#8982;</span><span><small>Visit the workshop</small><b>160 Pine St, Arcadia, Pretoria, 0083</b></span></a>
      </div>
      <div class="map-embed">
        <iframe title="PNND Kitchens location" loading="lazy" src="https://maps.google.com/maps?q=160%20Pine%20St%20Arcadia%20Pretoria%200083&t=m&z=14&output=embed&iwloc=near"></iframe>
      </div>
    </div>
    <div class="lead-card reveal">
      <h3>request my free quote</h3>
      <div class="lc-sub">We reply the same week — promise.</div>
      <form class="lead-form" novalidate>
        <div class="form-grid">
          <input class="field" type="text" name="name" placeholder="Your Name" required>
          <input class="field" type="tel" name="phone" placeholder="Phone Number" required>
          <input class="field full" type="email" name="email" placeholder="Email Address" required>
          <select class="field full" name="service" required>
            <option value="" selected disabled>Which service do you need?</option>
{opts}          </select>
        </div>
        <button class="btn btn-block" type="submit" style="margin-top:14px">Book My Free Consultation</button>
        <p class="disclaimer">We will never send you unsolicited messages. No obligation. No pressure.</p>
        <div class="form-success">Thank you &mdash; your request has been received. We'll be in touch shortly.</div>
      </form>
    </div>
  </div>
</section>'''

FOOTER = '''<footer class="footer">
  <div class="container">
    <div class="fcols">
      <div class="fbrand">
        <img src="../img/logo.svg" alt="PNND Kitchens">
        <p>Arcadia's owner-led studio for kitchen remodelling, custom cabinets, closets, carpentry and decks. Design &middot; Quality &middot; Perfection.</p>
      </div>
      <div>
        <h4>Services</h4>
%SERVICES%      </div>
      <div>
        <h4>Opening Hours</h4>
        <a href="#cta-form" class="hours"><span>Mon &ndash; Thu</span><b>7:00 &ndash; 17:30</b></a>
        <a href="#cta-form" class="hours"><span>Friday</span><b>7:00 &ndash; 16:00</b></a>
        <a href="#cta-form" class="hours"><span>Saturday</span><b>8:00 &ndash; 14:00</b></a>
        <a href="#cta-form" class="hours"><span>Sunday</span><b>Closed</b></a>
      </div>
      <div>
        <h4>Get in Touch</h4>
        <a href="tel:+27817966895">081 796 6895</a>
        <a href="sms:+27817966895">Text message</a>
        <a href="https://maps.google.com/?q=160+Pine+St+Arcadia+Pretoria+0083">160 Pine St, Arcadia, Pretoria, 0083</a>
        <p style="margin:16px 0 12px">Planning a project? Call today.</p>
        <a class="btn btn-light" href="#cta-form">Free Consultation</a>
      </div>
    </div>
    <div class="fbar">
      <span>&copy; 2026 PNND Kitchens. All rights reserved.</span>
      <span>Design &middot; Quality &middot; Perfection</span>
    </div>
  </div>
</footer>'''.replace("%SERVICES%", "".join(f'        <a href="{s}.html">{l}</a>\n' for s,l in NAV))

MOBILE = '''<div class="mobile-bar">
  <a class="mb-call" href="tel:+27817966895">Call Now</a>
  <a class="mb-cta" href="#cta-form">Free Consultation</a>
</div>'''

def page(slug, d):
    info = "".join(f'      <div class="info-card reveal"><div class="ic-h">{h}</div><p>{p}</p></div>\n' for h,p in d["info"])
    included = "".join(f'        <li><b>{x}</b></li>\n' for x in d["included"])
    why = "".join(f'      <div class="reveal"><h3>{h}</h3><p style="color:var(--muted);font-weight:300;margin:8px 0 0">{p}</p></div>\n' for h,p in d["why"])
    faq = "".join(f'''      <div class="faq-item reveal"><button class="faq-q">{q}<span class="ic">+</span></button>
        <div class="faq-a"><p>{a}</p></div></div>\n''' for q,a in d["faq"])
    gallery = "".join(f'      <a href="../img/{g}.jpg"><img src="../img/{g}.jpg" alt="{d["label"]} project by PNND Kitchens"></a>\n' for g in d["gallery"])
    related = ""
    for rs in d["related"]:
        r = S[rs]
        related += f'''      <a class="svc-card reveal" href="{rs}.html"><img src="../img/{r["hero"]}.jpg" alt="{r["label"]}">
        <div class="svc-body"><h3>{r["eyebrow"]}</h3><p>Learn more about our {r["label"].lower()} work.</p><span class="more">View service &rarr;</span></div></a>\n'''
    lede = "".join(f'      <p class="lead" style="margin-bottom:14px">{p}</p>\n' for p in d["lede"])
    plain = d["label"].replace("&amp;","and")
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{plain} in Pretoria | PNND Kitchens</title>
<meta name="description" content="{plain} by PNND Kitchens — owner-led carpentry in Arcadia, Pretoria. Designed, built and installed by hand. Free consultation. Call 081 796 6895.">
<link rel="icon" type="image/svg+xml" href="../img/logo.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/style.css">
<link rel="preload" as="image" href="../img/{d["hero"]}.jpg">
<script>document.documentElement.className+=' js';</script>
</head>
<body>

{TOPBAR}

{nav(slug)}
<span id="top"></span>

<!-- HERO -->
<header class="hero hero--sm">
  <div class="hero-bg"><img src="../img/{d["hero"]}.jpg" alt="{plain} by PNND Kitchens in Pretoria"></div>
  <div class="container">
    <div class="hero-copy reveal">
      <div class="breadcrumb"><a href="../index.html">home</a><span>/</span><a href="../index.html#services">services</a><span>/</span>{d["eyebrow"]}</div>
      <span class="eyebrow">{d["eyebrow"]}</span>
      <h1>{d["head"]}</h1>
      <p class="hero-sub">Owner-led, made-to-measure and installed by our own team across Pretoria &amp; Gauteng.</p>
      <div class="hero-cta">
        <a class="btn btn-light" href="#cta-form">Book a Free Consultation</a>
        <a class="btn btn-light" href="tel:+27817966895" style="background:transparent;color:#fff;border-color:rgba(255,255,255,.5)">Call 081 796 6895</a>
      </div>
    </div>
  </div>
</header>

<!-- OVERVIEW -->
<section class="section">
  <div class="container" style="max-width:900px">
    <span class="eyebrow reveal">overview</span>
    <h2 class="reveal" style="margin-bottom:20px">{d["head"]}</h2>
{lede}  </div>
  <div class="container">
    <div class="info-grid">
{info}    </div>
  </div>
</section>

<!-- WHAT'S INCLUDED -->
<section class="section bg-alt">
  <div class="container">
    <div class="section-head center"><span class="eyebrow reveal">what's included</span><h2 class="reveal">every project, covered end to end</h2></div>
    <ul class="values included reveal" style="max-width:820px;margin:0 auto">
{included}    </ul>
  </div>
</section>

<!-- WHY -->
<section class="section">
  <div class="container">
    <div class="section-head center"><span class="eyebrow reveal">why pnnd</span><h2 class="reveal">why homeowners choose us</h2></div>
    <div class="steps" style="grid-template-columns:repeat(3,1fr)">
{why}    </div>
  </div>
</section>

<!-- PROCESS -->
<section class="section bg-alt" id="process">
  <div class="container">
    <div class="section-head center"><span class="eyebrow reveal">how it works</span><h2 class="reveal">four steps, no surprises</h2></div>
    <div class="steps">
{process()}    </div>
  </div>
</section>

<!-- GALLERY -->
<section class="section">
  <div class="container">
    <div class="section-head center"><span class="eyebrow reveal">our work</span><h2 class="reveal">recent {d["eyebrow"]} projects</h2></div>
    <div class="gallery3 reveal">
{gallery}    </div>
  </div>
</section>

<!-- FAQ -->
<section class="section bg-alt">
  <div class="container">
    <div class="section-head center"><span class="eyebrow reveal">questions</span><h2 class="reveal">common questions</h2></div>
    <div class="faq">
{faq}    </div>
  </div>
</section>

<!-- YOU MAY ALSO NEED -->
<section class="section">
  <div class="container">
    <div class="section-head center"><span class="eyebrow reveal">you may also need</span><h2 class="reveal">explore our other services</h2></div>
    <div class="related">
{related}    </div>
  </div>
</section>

{cta_form()}

{FOOTER}

{MOBILE}

<script src="../js/main.js"></script>
</body>
</html>
'''

for slug, d in S.items():
    open(os.path.join(OUT, slug + ".html"), "w", encoding="utf-8").write(page(slug, d))
    print("wrote services/%s.html" % slug)
print("done:", len(S), "service pages")
