#!/usr/bin/env python3
"""Generate dedicated service pages + an All Services index for PNND Kitchens.

Mirrors Website A's (Cloud Nine) service-page structure & design:
hero (bold uppercase headline, body copy, dual CTAs) -> multi-block
overview -> 'why us' numbered list beside 'what's included' checkbox grid ->
ring process -> gallery -> FAQ -> 'you may also need' cross-sell -> CTA form.
Rendered with PNND branding (Oswald headings, gold accent, Twelve imagery).
"""
import os

OUT = os.path.join(os.path.dirname(__file__), "services")
os.makedirs(OUT, exist_ok=True)

NAV = [
    ("kitchen-remodelling", "Kitchen Remodelling"),
    ("cabinet-construction-installation", "Cabinet Construction &amp; Installation"),
    ("closet-construction-installation", "Closet Construction &amp; Installation"),
    ("custom-closet-design", "Custom Closet Design"),
    ("custom-carpentry", "Custom Carpentry"),
    ("cabinet-closet-repair", "Cabinet &amp; Closet Repair"),
    ("deck-construction", "Deck Construction"),
]

S = {
 "kitchen-remodelling": {
  "label":"Kitchen Remodelling","eyebrow":"kitchen remodelling","hero":"p01",
  "tagline":"Designed, built and installed by one accountable team.",
  "head":"Kitchen Remodelling in Pretoria",
  "intro":"When your kitchen stops working for the way you live, a remodel is the honest fix — not another patch. We redesign, build and install the whole thing, then walk you through the result.",
  "overview":[
    ("Kitchen Remodelling, Done By The Owner","Most kitchen companies run a sales team. PNND runs an owner. The person who quotes your kitchen is the one who measures it, builds it in our Arcadia workshop, and is on site when it's installed."),
    ("One Workshop, Every Trade","Cabinetry, counters, splashbacks, lighting coordination and finishes are handled under one roof. Fewer trades, fewer delays, and a single team accountable for the result."),
    ("What The Consultation Covers","Every consultation is free and on your timeline. We measure, photograph the space, talk through layout and finishes, and follow up the same week with drawings and a written quote."),
    ("What Honest Pricing Looks Like","Your quote is line-itemed — cabinetry, counters, hardware, removal and installation. You see every number, with no bundled mystery totals. If anything changes, we call before the crew arrives."),
  ],
  "why":["The owner measures, builds and installs — you deal with one person",
         "Line-item written quote, no bundled mystery numbers",
         "Solid timber, quality board and premium fittings",
         "Our own crews on every project — never subcontracted"],
  "included":["Full design &amp; 3D layout","Custom cabinetry &amp; carcasses","Countertops &amp; splashbacks",
              "Soft-close hinges &amp; runners","Lighting &amp; electrical coordination","Removal of the old kitchen",
              "Professional installation","Final snag &amp; clean-up"],
  "faq":[("How long does a kitchen remodel take?","Most kitchens take 3–6 weeks from sign-off, depending on size and finishes. You get a written schedule before we begin."),
         ("Can you work with my existing layout?","Yes — we can refresh within your current footprint or redesign the layout entirely. We advise on what adds the most value."),
         ("What does a kitchen cost in Pretoria?","Most remodels run between R80,000 and R350,000. We quote after a free measure-up so the price fits your space and finishes.")],
  "gallery":["p02","p13","p14"],
  "related":["cabinet-construction-installation","custom-carpentry","closet-construction-installation"],
 },
 "cabinet-construction-installation": {
  "label":"Cabinet Construction &amp; Installation","eyebrow":"cabinet construction","hero":"p03",
  "tagline":"Made to measure, built by hand, installed by our own team.",
  "head":"Custom Cabinets, Built &amp; Installed",
  "intro":"Made-to-measure cabinets for kitchens, sculleries, TV units and storage — built in our Pretoria workshop and fitted by the same team that built them.",
  "overview":[
    ("Cabinetry, Done By The Owner","The person who quotes your cabinets measures, builds and installs them. No sales rep hand-off, no subcontracted fitters — one accountable craftsman from first measure to final screw."),
    ("Built To The Millimetre","We build to your exact dimensions, so there are no filler panels or awkward gaps. Every carcass is square, every door aligned, every drawer soft-close."),
    ("What The Consultation Covers","A free on-site measure-up where we discuss finishes, hardware and layout, then follow up with a written quote and finish samples the same week."),
    ("What Honest Pricing Looks Like","Carcasses, doors, hardware, edging and installation are itemised separately. You see every number before any work begins — no surprises on install day."),
  ],
  "why":["One craftsman from measure to install — never subcontracted",
         "Built to the millimetre — no fillers, no gaps",
         "Quality board, solid timber and soft-close hardware as standard",
         "Fixed written quote before any work starts"],
  "included":["On-site measure &amp; design","Custom carcasses &amp; doors","Soft-close hinges &amp; runners",
              "Edging &amp; finishing","Handles &amp; accessories","Delivery &amp; installation",
              "Levelling &amp; alignment","Snag &amp; clean-up"],
  "faq":[("What materials do you use?","Quality moisture-resistant board, solid timber and real veneers, with soft-close hardware as standard. We'll show samples at the consultation."),
         ("Do you install what you build?","Always. The team that builds your cabinets installs them, so quality is owned end to end."),
         ("Can you match an existing kitchen?","Yes — we colour- and finish-match to extend or repair existing cabinetry wherever possible.")],
  "gallery":["p04","p11","p06"],
  "related":["kitchen-remodelling","closet-construction-installation","cabinet-closet-repair"],
 },
 "closet-construction-installation": {
  "label":"Closet Construction &amp; Installation","eyebrow":"closets &amp; wardrobes","hero":"p04",
  "tagline":"Floor-to-ceiling built-ins, scribed and fitted to your walls.",
  "head":"Built-in Closets &amp; Wardrobes",
  "intro":"Floor-to-ceiling built-in cupboards and wardrobes, designed around your room and the way you store — then built and installed by our own team.",
  "overview":[
    ("Closets, Done By The Owner","From first measure to final fit, one team is responsible. The owner plans your closet, builds it, and is there when it goes in."),
    ("Storage That Uses Every Centimetre","Hanging space, drawers, shelving and shoe racks, laid out to fit your life — not an off-the-shelf module. We scribe to your walls so it reads as part of the house."),
    ("What The Consultation Covers","A free measure-up where we plan zones, discuss door styles and finishes, and follow up with a layout and written quote the same week."),
    ("What Honest Pricing Looks Like","Carcasses, internals, doors and installation are itemised. You see every number up front, with a fixed quote before we build."),
  ],
  "why":["Planned, built and installed by one team",
         "Scribed to the wall for a true built-in finish",
         "Internals tailored to how you actually store",
         "Fixed written quote, no mystery numbers"],
  "included":["On-site measure &amp; design","Custom carcasses &amp; doors","Internal hanging &amp; shelving",
              "Soft-close drawers","Mirrors &amp; accessories (optional)","Delivery &amp; installation",
              "Scribing to walls","Snag &amp; clean-up"],
  "faq":[("Hinged or sliding doors?","Both. Sliding doors suit tight rooms; hinged doors give full access. We advise based on your space at the measure-up."),
         ("Can you fit into an alcove or sloped ceiling?","Yes — built-ins are ideal for awkward spaces. We scribe and build to fit exactly."),
         ("How long does installation take?","Most built-in closets are installed in 1–3 days once built, with minimal disruption.")],
  "gallery":["p05","p12","p10"],
  "related":["custom-closet-design","cabinet-construction-installation","kitchen-remodelling"],
 },
 "custom-closet-design": {
  "label":"Custom Closet Design","eyebrow":"custom closet design","hero":"p05",
  "tagline":"Walk-in and dressing-room design, planned in 3D.",
  "head":"Custom Closet &amp; Dressing Room Design",
  "intro":"For walk-in closets and dressing rooms, design is everything. We plan zones for hanging, folding, shoes and accessories, then craft a system that's entirely yours.",
  "overview":[
    ("Design, Done By The Owner","You work directly with the person who will build your closet — no design-to-build hand-off where detail gets lost."),
    ("Designed Around Your Wardrobe","Every closet is planned around what you own and how you use it, not a template. Lighting, glass fronts, valet rails and drawers are specified to suit."),
    ("What The Consultation Covers","A free design consultation and 3D layout, so you can see and adjust the closet before we build a thing."),
    ("What Honest Pricing Looks Like","Design, build and installation are itemised, with a fixed written quote after the consultation. You approve the number before we start."),
  ],
  "why":["Every closet planned around your wardrobe, not a template",
         "3D design so you see it before it's built",
         "Boutique detailing — lighting, glass fronts, valet rails",
         "Design, build and install from one studio"],
  "included":["Consultation &amp; 3D design","Zoned hanging &amp; storage plan","Drawers, shelving &amp; rails",
              "Optional integrated lighting","Glass-front &amp; display options","Build &amp; installation",
              "Finishing &amp; alignment","Snag &amp; clean-up"],
  "faq":[("Do you provide 3D drawings?","Yes — every custom closet starts with a 3D design so you can see and adjust the layout before we build."),
         ("Can you add lighting?","Absolutely. Integrated LED strip and sensor lighting are popular options we coordinate during the build."),
         ("How much does a walk-in closet cost?","It depends on size and detailing. We quote a fixed price after the free design consultation.")],
  "gallery":["p10","p12","p07"],
  "related":["closet-construction-installation","custom-carpentry","kitchen-remodelling"],
 },
 "custom-carpentry": {
  "label":"Custom Carpentry","eyebrow":"custom carpentry","hero":"p06",
  "tagline":"Bespoke joinery for every room — residential and commercial.",
  "head":"Custom Carpentry &amp; Joinery",
  "intro":"Vanities, media units, desks, shelving, wine racks and feature joinery — if it can be built in timber, we can craft it, to measure, for your home or business.",
  "overview":[
    ("Carpentry, Done By The Owner","Tell us what you need and where it goes; the owner designs, builds and installs it. One craftsman, accountable from sketch to fit."),
    ("Truly Bespoke, Not Catalogue","These are one-off pieces made for your space and use, finished to furniture standard — not flat-pack furniture in disguise."),
    ("What The Consultation Covers","A free measure-up and design chat, with a written quote and material options the same week."),
    ("What Honest Pricing Looks Like","Design, build, materials and installation are itemised. You approve a fixed quote before any timber is cut."),
  ],
  "why":["One-off pieces, designed and built for your space",
         "Joinery finished to furniture standard",
         "Residential and commercial projects welcome",
         "Matched to existing furniture where possible"],
  "included":["Design &amp; measure","Bespoke build in our workshop","Quality timber &amp; finishes",
              "Hardware &amp; fittings","Delivery &amp; installation","Finishing &amp; alignment",
              "Commercial &amp; residential","Snag &amp; clean-up"],
  "faq":[("What kinds of carpentry do you take on?","Vanities, media units, desks, shelving, wine storage, feature panelling and more — residential and commercial."),
         ("Can you match existing furniture?","Yes, we colour- and finish-match wherever possible so new pieces feel original to the space."),
         ("Do you do commercial fit-outs?","We do — reception counters, retail joinery and office storage are all within our scope.")],
  "gallery":["p08","p15","p17"],
  "related":["cabinet-construction-installation","cabinet-closet-repair","deck-construction"],
 },
 "cabinet-closet-repair": {
  "label":"Cabinet &amp; Closet Repair","eyebrow":"cabinet &amp; closet repair","hero":"p11",
  "tagline":"Repairs and refits — for a fraction of a new build.",
  "head":"Cabinet &amp; Closet Repair",
  "intro":"Not everything needs replacing. Sagging doors, broken hinges, blown board, worn runners and tired finishes can often be repaired or refitted for far less than a new build.",
  "overview":[
    ("Repairs, Done By The Owner","The owner assesses your units in person and tells you straight whether a repair makes sense — no upsell to a full replacement you don't need."),
    ("Repair Before You Replace","If the carcasses are sound, a repair is usually the smart call. We re-align doors, replace runners, swap blown panels and refresh finishes."),
    ("What The Assessment Covers","A free on-site assessment of doors, hinges, drawers, panels and finishes, with an honest recommendation and a fixed quote."),
    ("What Honest Pricing Looks Like","You get a clear, itemised quote for exactly what needs doing — and a straight answer when a repair isn't worth it."),
  ],
  "why":["Honest assessment — repair vs replace, told straight",
         "A fraction of the cost of a new build",
         "Fast, scheduled and tidy work",
         "Free assessment and quote in Pretoria"],
  "included":["On-site assessment","Hinge &amp; door alignment","Runner &amp; drawer repair",
              "Board &amp; panel replacement","Re-edging &amp; refinishing","Handle &amp; hardware swaps",
              "Water-damage repairs","Fixed written quote"],
  "faq":[("Is it worth repairing or should I replace?","If the carcasses are sound, repair is usually the smart call. We assess on site and advise honestly."),
         ("Can you fix water-damaged cupboards?","Often yes — we replace affected panels and refinish so it blends in. Severe cases may need a partial rebuild."),
         ("Do you charge for a quote?","Assessment and quoting are free within Pretoria and surrounds.")],
  "gallery":["p03","p06","p16"],
  "related":["cabinet-construction-installation","custom-carpentry","kitchen-remodelling"],
 },
 "deck-construction": {
  "label":"Deck Construction","eyebrow":"deck construction","hero":"p08",
  "tagline":"Solid timber decks, engineered and sealed to last.",
  "head":"Deck Construction in Pretoria",
  "intro":"Outdoor living, done properly. We build solid timber decks, pergolas and outdoor woodwork engineered to handle the Highveld — sealed and finished to last.",
  "overview":[
    ("Decks, Done By The Owner","The owner assesses the site, designs the deck and is on the build. One team responsible for structure, timber and finish."),
    ("Built For The Highveld","Properly framed and fixed, in hardwood or treated timber, sealed against sun and rain so your deck still looks good seasons later."),
    ("What The Consultation Covers","A free site assessment where we discuss layout, levels, balustrades and pergolas, followed by a written quote."),
    ("What Honest Pricing Looks Like","Substructure, decking, finishing and any extras are itemised. You approve a fixed quote before we break ground."),
  ],
  "why":["Engineered and sealed for Highveld weather",
         "Designed around your home and how you entertain",
         "Carpentry-grade build quality, inside and out",
         "Fixed written quote, no surprises"],
  "included":["Site assessment &amp; design","Framing &amp; substructure","Quality timber decking",
              "Balustrades &amp; steps (optional)","Pergolas &amp; screens (optional)","Sealing &amp; finishing",
              "Hardware &amp; fixings","Clean-up &amp; handover"],
  "faq":[("What timber do you use for decks?","Hardwoods and properly treated timber suited to outdoor use, sealed to resist sun and rain. We'll recommend options to suit your budget."),
         ("Do you build pergolas and balustrades too?","Yes — pergolas, screens, steps and balustrades can all be part of the project."),
         ("How long does a deck take?","Most decks are built within 1–2 weeks depending on size and structure.")],
  "gallery":["p09","p18","p02"],
  "related":["custom-carpentry","kitchen-remodelling","cabinet-construction-installation"],
 },
}

def nav(active):
    items = '          <li><a href="all-services.html">All Services</a></li>\n'
    for slug, label in NAV:
        cls = ' class="active"' if slug == active else ''
        items += f'          <li><a href="{slug}.html"{cls}>{label}</a></li>\n'
    svc_active = ' class="active"' if active else ''
    return f'''<nav class="nav" id="nav">
  <div class="container">
    <a class="nav-logo" href="../index.html" aria-label="PNND Kitchens"><img src="../img/logo.svg" alt="PNND Kitchens"></a>
    <ul class="menu" id="menu">
      <li><a href="../index.html">home</a></li>
      <li><a href="../index.html#about">about</a></li>
      <li class="has-sub">
        <a href="all-services.html"{svc_active}>services</a>
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
    out = ""
    for i,(h,p) in enumerate(STEPS):
        out += f'''      <div class="step reveal">
        <div class="ring"><svg viewBox="0 0 100 100">{RINGS[i]}</svg><span class="rn">0{i+1}</span></div>
        <h3>{h}</h3><p>{p}</p>
      </div>\n'''
    return out

def cta_form():
    opts = "".join(f'            <option>{l}</option>\n' for _,l in NAV)
    return f'''<section class="section cta-band" id="cta-form">
  <div class="cta-bg"><img src="../img/p13.jpg" alt=""></div>
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
      <div class="map-embed">
        <iframe title="PNND Kitchens location" loading="lazy" src="https://maps.google.com/maps?q=160%20Pine%20St%20Arcadia%20Pretoria%200083&t=m&z=14&output=embed&iwloc=near"></iframe>
      </div>
    </div>
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

def head(title, desc, hero=None):
    pl = '\n<link rel="preload" as="image" href="../img/%s.jpg">' % hero if hero else ''
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/svg+xml" href="../img/logo.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/style.css">{pl}
<script>document.documentElement.className+=' js';</script>
</head>
<body class="svc-page">'''

def page(slug, d):
    overview = ""
    for h,p in d["overview"]:
        overview += f'      <div class="ov-block reveal"><h2>{h}</h2><p>{p}</p></div>\n'
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
    return f'''{head(plain+" in Pretoria | PNND Kitchens",
                     plain+" by PNND Kitchens — owner-led carpentry in Arcadia, Pretoria. Designed, built and installed by hand. Free consultation. Call 081 796 6895.",
                     d["hero"])}

{TOPBAR}

{nav(slug)}
<span id="top"></span>

<!-- HERO -->
<header class="hero hero--service">
  <div class="hero-bg"><img src="../img/{d["hero"]}.jpg" alt="{plain} by PNND Kitchens in Pretoria"></div>
  <div class="container">
    <div class="hero-copy reveal">
      <div class="breadcrumb"><a href="../index.html">home</a><span>/</span><a href="all-services.html">services</a><span>/</span>{d["eyebrow"]}</div>
      <span class="eyebrow">{d["tagline"]}</span>
      <h1>{d["head"]}</h1>
      <p class="hero-sub">{d["intro"]}</p>
      <div class="hero-cta">
        <a class="btn btn-light" href="#cta-form">Get My Free Quote →</a>
        <a class="btn btn-light" href="tel:+27817966895" style="background:transparent;color:#fff;border-color:rgba(255,255,255,.5)">Call 081 796 6895</a>
      </div>
    </div>
  </div>
</header>

<!-- OVERVIEW -->
<section class="section bg-grid">
  <div class="container" style="max-width:980px">
{overview}  </div>
</section>

<!-- WHY + WHAT'S INCLUDED -->
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
<section class="section" id="process">
  <div class="container">
    <div class="section-head center"><span class="eyebrow reveal">how it works</span><h2 class="reveal">Four Steps, No Surprises</h2></div>
    <div class="steps">
{process()}    </div>
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

{cta_form()}

{FOOTER}

{MOBILE}

<script src="../js/main.js"></script>
</body>
</html>
'''

def all_services():
    cards = ""
    for slug,label in NAV:
        d = S[slug]
        cards += f'''      <a class="svc-card reveal" href="{slug}.html"><img src="../img/{d["hero"]}.jpg" alt="{label}">
        <div class="svc-body"><h3>{d["eyebrow"]}</h3><p>{d["tagline"]}</p><span class="more">View service &rarr;</span></div></a>\n'''
    return f'''{head("All Services | PNND Kitchens","All services from PNND Kitchens — kitchen remodelling, cabinets, closets, custom carpentry, repairs and decks in Pretoria. Free consultation. Call 081 796 6895.","p01")}

{TOPBAR}

{nav(None)}
<span id="top"></span>

<header class="hero hero--service">
  <div class="hero-bg"><img src="../img/p01.jpg" alt="PNND Kitchens services in Pretoria"></div>
  <div class="container">
    <div class="hero-copy reveal">
      <div class="breadcrumb"><a href="../index.html">home</a><span>/</span>services</div>
      <span class="eyebrow">kitchen remodelling &amp; bespoke carpentry</span>
      <h1>Our Services</h1>
      <p class="hero-sub">Everything we design, build, install and repair — one accountable Arcadia workshop. Pick a service to see exactly what's involved.</p>
      <div class="hero-cta">
        <a class="btn btn-light" href="#cta-form">Get My Free Quote →</a>
        <a class="btn btn-light" href="tel:+27817966895" style="background:transparent;color:#fff;border-color:rgba(255,255,255,.5)">Call 081 796 6895</a>
      </div>
    </div>
  </div>
</header>

<section class="section">
  <div class="container">
    <div class="section-head center"><span class="eyebrow reveal">what we do</span><h2 class="reveal">One Workshop, Every Detail</h2></div>
    <div class="services-grid">
{cards}    </div>
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
open(os.path.join(OUT, "all-services.html"), "w", encoding="utf-8").write(all_services())
print("wrote services/all-services.html")
print("done:", len(S)+1, "pages")
