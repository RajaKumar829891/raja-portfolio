"""Builds the SEO landing pages from one shared template.

Run:  python3 tools/build_pages.py
Each page is written to <slug>/index.html. Edit PAGES below to change content.
"""
import json
from pathlib import Path

SITE = "https://raja-portfolio-lyart.vercel.app"
ROOT = Path(__file__).resolve().parent.parent

NAV_LINKS = [
    ("/odoo-developer/", "Hire an Odoo developer"),
    ("/odoo-developer-india/", "Odoo developer in India"),
    ("/odoo-implementation/", "Odoo implementation"),
    ("/zoho-to-odoo-migration/", "Zoho to Odoo migration"),
    ("/blog/odoo-community-vs-enterprise/", "Community vs Enterprise"),
]

PERSON = {
    "@type": "Person",
    "@id": f"{SITE}/#raja",
    "name": "Raja Kumar",
    "jobTitle": "Senior Odoo Developer & ERP Consultant",
    "url": f"{SITE}/",
    "image": f"{SITE}/avatar.jpg",
    "address": {"@type": "PostalAddress", "addressLocality": "Bhopal", "addressRegion": "Madhya Pradesh", "addressCountry": "IN"},
    "sameAs": ["https://www.linkedin.com/in/raja-kumar-cseaiml", "https://github.com/RajaKumar829891"],
}


def faq_html(faqs):
    out = []
    for i, (q, a) in enumerate(faqs):
        out.append(f'  <details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>')
    return "\n".join(out)


def page(p):
    url = f"{SITE}{p['slug']}"
    graph = [
        PERSON,
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Raja Kumar", "item": f"{SITE}/"},
                {"@type": "ListItem", "position": 2, "name": p["crumb"], "item": url},
            ],
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in p["faqs"]
            ],
        },
    ]
    graph.append(p["schema"](url))
    related = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV_LINKS if h != p["slug"])
    footer_links = " · ".join(f'<a href="{h}">{t}</a>' for h, t in NAV_LINKS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{p['title']}</title>
<meta name="description" content="{p['description']}">
<meta name="author" content="Raja Kumar">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#714B67">
<link rel="icon" href="/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="{p.get('og_type', 'website')}">
<meta property="og:site_name" content="Raja Kumar – Odoo Developer">
<meta property="og:title" content="{p['og_title']}">
<meta property="og:description" content="{p['description']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/pages.css">
<script type="application/ld+json">
{json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False)}
</script>
</head>
<body>

<nav class="nav" aria-label="Main">
  <div class="container nav-inner">
    <a class="brand" href="/"><img src="/avatar.jpg" alt="" width="36" height="36">Raja Kumar</a>
    <div style="display:flex;gap:10px">
      <a class="btn btn-ghost" href="/odoo-developer/">Odoo developer</a>
      <a class="btn btn-primary" href="/#contact">Hire me</a>
    </div>
  </div>
</nav>

<div class="container crumbs"><a href="/">Raja Kumar</a> / {p['crumb']}</div>

<header class="page-hero">
  <div class="container">
    <p class="eyebrow">{p['eyebrow']}</p>
    <h1>{p['h1']}</h1>
    <p class="lead">{p['lead']}</p>
    <div class="hero-ctas">
      <a class="btn btn-primary" href="mailto:rajakumar829891@gmail.com?subject=Odoo%20project">{p.get('cta', 'Discuss your Odoo project →')}</a>
      <a class="btn btn-ghost" href="/">See portfolio</a>
    </div>
    <div class="facts">
      <div class="fact"><b>10+</b><span>ERP projects</span></div>
      <div class="fact"><b>100+</b><span>Custom Odoo modules</span></div>
      <div class="fact"><b>100K+</b><span>Records migrated</span></div>
      <div class="fact"><b>17 · 18 · 19</b><span>Odoo versions</span></div>
    </div>
  </div>
</header>

<main class="container">
{p['body']}

<section>
  <h2>{p['faq_title']}</h2>
{faq_html(p['faqs'])}
</section>

<div class="cta">
  <h2>{p['cta_title']}</h2>
  <p>{p['cta_text']}</p>
  <div class="hero-ctas" style="margin-top:0">
    <a class="btn btn-primary" href="mailto:rajakumar829891@gmail.com?subject=Odoo%20project">Email rajakumar829891@gmail.com</a>
    <a class="btn btn-ghost" href="https://www.linkedin.com/in/raja-kumar-cseaiml" rel="noopener">Message on LinkedIn</a>
  </div>
  <div class="related">{related}</div>
</div>

</main>

<footer>
  <div class="container">
    <span>© 2026 Raja Kumar — Senior Odoo Developer &amp; ERP Consultant, India</span>
    <span><a href="/">Home</a> · {footer_links}</span>
  </div>
</footer>
</body>
</html>
"""


PAGES = [
    {
        "slug": "/odoo-developer-india/",
        "crumb": "Odoo developer in India",
        "title": "Odoo Developer in India | Senior Freelance Odoo Developer – Raja Kumar",
        "og_title": "Senior Odoo Developer in India – Raja Kumar",
        "description": "Hire a senior Odoo developer from India for Odoo 17, 18 and 19, Community and Enterprise. Remote Odoo implementation, customization and migration for clients in Europe, the Middle East, the US and Australia.",
        "eyebrow": "Odoo developer in India · Bhopal · Remote worldwide",
        "h1": 'A senior <span>Odoo developer in India</span>, working in your time zone',
        "lead": "I'm <strong>Raja Kumar</strong>, a senior Odoo developer and ERP consultant based in Bhopal, India. I build and support <strong>Odoo 17, 18 and 19</strong> for companies across India, the Middle East, Europe, the US and Australia, combining Indian cost levels with senior-level, hands-on Odoo work.",
        "body": """<section>
  <h2>Why hire an Odoo developer from India</h2>
  <p>India has a large Odoo developer community, and many businesses outsource Odoo work here for a simple reason: you can get senior Python and Odoo skills at a fraction of the cost of a local partner. The difference is in who you hire. Working directly with an experienced developer, rather than a large outsourcing agency, gives you that cost advantage without losing quality or communication.</p>
  <div class="grid-2">
    <div class="card"><h3>Lower cost, senior skills</h3><p>Typically up to 75% less than a traditional ERP partner, with a senior developer writing your code rather than a junior team.</p></div>
    <div class="card"><h3>Time-zone overlap</h3><p>India (IST) overlaps well with Europe and the Middle East, and I adjust hours for calls with US and Australian clients.</p></div>
    <div class="card"><h3>Clear communication</h3><p>Fluent English, written scopes, regular updates and a staging database you can test before anything goes live.</p></div>
    <div class="card"><h3>Proven international work</h3><p>I currently run the Odoo 19 Enterprise ERP for a solar energy group with seven companies across several countries, from India.</p></div>
  </div>
</section>

<section>
  <h2>What I do as your Odoo developer</h2>
  <ul>
    <li><strong>Odoo implementation</strong> for CRM, Sales, Inventory, Purchase, Accounting, Manufacturing, HR, Project and Website. <a href="/odoo-implementation/">How implementation works →</a></li>
    <li><strong>Custom Odoo module development</strong> in Python, OWL/JavaScript and QWeb.</li>
    <li><strong>Migration</strong> from Zoho, spreadsheets or legacy ERPs, and Odoo version upgrades. <a href="/zoho-to-odoo-migration/">Zoho to Odoo migration →</a></li>
    <li><strong>Integrations</strong> with WhatsApp, Meta Lead Ads, payment gateways, Google Maps, IoT devices and AI.</li>
    <li><strong>Odoo.sh and Docker hosting</strong>, staging environments and automated backups.</li>
  </ul>
</section>

<section>
  <h2>Clients and regions I work with</h2>
  <p>Over 10+ ERP projects I've worked with companies in <strong>India</strong>, the <strong>Middle East</strong> and <strong>Europe</strong> (including Belgium), across solar energy, travel and logistics, education, real estate and services. I also work with clients in the <strong>United States</strong> and <strong>Australia</strong> remotely.</p>
  <h3>A typical engagement</h3>
  <ol class="steps">
    <li><strong>Call and scope.</strong> We go through your processes and I send a written plan with timeline and cost.</li>
    <li><strong>Build on staging.</strong> I configure Odoo and develop modules on a copy of your database for you to test.</li>
    <li><strong>Go live and support.</strong> Data migration, training and ongoing fixes or new features.</li>
  </ol>
</section>""",
        "faq_title": "Hiring an Odoo developer in India: FAQ",
        "faqs": [
            ("Is it safe to hire a freelance Odoo developer from India?", "Yes, if you hire someone with a verifiable track record. You can review my LinkedIn, GitHub and project history, start with a small paid task, and test everything on a staging database before it goes live."),
            ("How much does an Odoo developer in India cost?", "Rates vary with experience. Working directly with me is typically up to 75% cheaper than a traditional ERP partner. Share your scope for a fixed quote or an hourly estimate."),
            ("Can you work during European or US business hours?", "Yes. India overlaps well with Europe and the Middle East, and I schedule calls in US or Australian hours when needed."),
            ("Do you work with Odoo Community and Enterprise?", "Yes, Odoo 17, 18 and 19 in both editions, on Odoo Online, Odoo.sh or your own server."),
        ],
        "cta_title": "Hire a senior Odoo developer from India",
        "cta_text": "Tell me about your Odoo project, your location and your timeline, and I'll reply with next steps.",
        "schema": lambda url: {
            "@type": "ProfessionalService",
            "name": "Raja Kumar – Odoo Developer in India",
            "url": url,
            "image": f"{SITE}/og-image.png",
            "founder": {"@id": f"{SITE}/#raja"},
            "address": {"@type": "PostalAddress", "addressLocality": "Bhopal", "addressRegion": "Madhya Pradesh", "addressCountry": "IN"},
            "areaServed": ["India", "United Arab Emirates", "Saudi Arabia", "Europe", "United States", "Australia"],
            "email": "rajakumar829891@gmail.com",
            "telephone": "+91-8298913646",
        },
    },
    {
        "slug": "/odoo-implementation/",
        "crumb": "Odoo implementation",
        "title": "Odoo Implementation Services | Odoo ERP Setup for Community & Enterprise – Raja Kumar",
        "og_title": "Odoo Implementation Services – Raja Kumar",
        "description": "End-to-end Odoo ERP implementation for Odoo 17, 18 and 19: requirement analysis, configuration, custom modules, data migration, training and go-live support. Community or Enterprise, single or multi-company.",
        "eyebrow": "Odoo ERP implementation · Community & Enterprise",
        "h1": '<span>Odoo implementation</span>, done properly from day one',
        "lead": "A good <strong>Odoo implementation</strong> isn't about installing apps. It's about mapping how your business really works, configuring standard Odoo first, and only then adding the custom code that pays off. I take you from first call to go-live and beyond, on <strong>Odoo Community or Enterprise</strong>.",
        "body": """<section>
  <h2>What's included in an Odoo implementation</h2>
  <div class="grid-2">
    <div class="card"><h3>Requirement analysis</h3><p>Workshops to map your sales, purchasing, stock, accounting and HR processes, and decide what Odoo covers as standard.</p></div>
    <div class="card"><h3>Configuration</h3><p>Companies, users and access rights, products, warehouses, taxes, chart of accounts, workflows, email templates and reports.</p></div>
    <div class="card"><h3>Customisation</h3><p>Custom Odoo modules only where they add real value: automation, approvals, dashboards, portals and integrations.</p></div>
    <div class="card"><h3>Data migration &amp; training</h3><p>Customers, products, open orders and balances imported and validated, plus hands-on training for each team.</p></div>
  </div>
</section>

<section>
  <h2>Odoo apps I implement</h2>
  <ul>
    <li><strong>CRM &amp; Sales</strong>: pipelines, quotations, pricelists, lead assignment and integrations with Meta Lead Ads or WhatsApp.</li>
    <li><strong>Inventory, Purchase &amp; Barcode</strong>: multi-warehouse stock, routes, reordering rules, barcode scanning and label printing.</li>
    <li><strong>Accounting &amp; Invoicing</strong>: chart of accounts, taxes, bank reconciliation, payment providers and financial reports.</li>
    <li><strong>Manufacturing</strong>: bills of materials, work orders and production planning.</li>
    <li><strong>HR, Attendance &amp; Fleet</strong>: employees, attendance (including biometric devices), assets and vehicles.</li>
    <li><strong>Project &amp; Timesheets</strong>, and <strong>Website, eCommerce &amp; Portal</strong>.</li>
  </ul>
</section>

<section>
  <h2>How an Odoo implementation project runs</h2>
  <ol class="steps">
    <li><strong>Discover.</strong> Understand your processes, pain points, users and reporting needs.</li>
    <li><strong>Plan.</strong> A written scope covering apps, edition (Community or Enterprise), hosting, customisations, timeline and cost.</li>
    <li><strong>Build.</strong> Configure and develop on a staging database, with regular demos so you can give feedback early.</li>
    <li><strong>Test &amp; migrate.</strong> User acceptance testing, then migration of your live data.</li>
    <li><strong>Go live &amp; support.</strong> Switch-over, training and post-launch support, then new phases as you grow.</li>
  </ol>
  <p>For larger businesses I recommend a <strong>phased rollout</strong>: for example CRM and Sales first, then Inventory and Purchase, then Accounting. Each phase goes live on its own, which lowers risk and gets value sooner.</p>
</section>

<section>
  <h2>Multi-company Odoo implementations</h2>
  <p>I currently run an Odoo 19 Enterprise implementation for a solar energy group with <strong>seven companies</strong> in several countries, covering multi-company access rights, customer and installer portals, a webshop and a lead-to-project platform built as connected custom modules. If your group has several legal entities, Odoo can run them in one database with shared or separate data, and I can design that structure for you.</p>
</section>""",
        "faq_title": "Odoo implementation FAQ",
        "faqs": [
            ("How long does an Odoo implementation take?", "A focused rollout of one or two apps can go live in a few weeks. Multi-company or heavily customised implementations take longer and are best delivered in phases."),
            ("How much does an Odoo implementation cost?", "It depends on the number of apps, users, customisations and data to migrate. Working directly with me is typically up to 75% cheaper than a traditional ERP partner. I give a written scope and quote before work starts."),
            ("Do I need Odoo Enterprise, or is Community enough?", "Many small businesses run well on Community. Enterprise adds features such as full accounting, Studio, mobile apps, Odoo.sh hosting and official upgrades. See my Community vs Enterprise guide or ask me to compare them against your processes."),
            ("Can you take over an implementation another partner started?", "Yes. I can review the existing setup and custom modules, fix issues and continue the rollout."),
        ],
        "cta_title": "Planning an Odoo implementation?",
        "cta_text": "Tell me which apps you're considering and how many users you have, and I'll suggest a rollout plan.",
        "schema": lambda url: {
            "@type": "Service",
            "name": "Odoo implementation",
            "serviceType": "ERP implementation",
            "description": "End-to-end Odoo ERP implementation for Odoo 17, 18 and 19, Community and Enterprise.",
            "provider": {"@id": f"{SITE}/#raja"},
            "areaServed": "Worldwide",
            "url": url,
        },
    },
    {
        "slug": "/blog/odoo-community-vs-enterprise/",
        "crumb": "Odoo Community vs Enterprise",
        "og_type": "article",
        "title": "Odoo Community vs Enterprise: Which Should You Choose? (2026 Guide)",
        "og_title": "Odoo Community vs Enterprise – a practical guide",
        "description": "A practical comparison of Odoo Community and Odoo Enterprise: licensing, features, hosting, upgrades and cost, and how to choose the right edition for your business. By senior Odoo developer Raja Kumar.",
        "eyebrow": "Guide · Updated November 2026",
        "h1": 'Odoo <span>Community vs Enterprise</span>: which should you choose?',
        "lead": "One of the first decisions in any Odoo project is the edition. Both run on the same core, but they differ in licence, features, hosting and support. Here's a practical comparison from a <strong>senior Odoo developer</strong> who builds on both editions.",
        "cta": "Ask me which edition fits →",
        "body": """<section>
  <h2>The short answer</h2>
  <p><strong>Odoo Community</strong> is free and open source (LGPLv3). It covers CRM, Sales, Purchase, Inventory, Invoicing, Manufacturing, Project, Website and more, and suits many small and growing businesses, especially when paired with a developer who can fill gaps with custom modules.</p>
  <p><strong>Odoo Enterprise</strong> is a paid, per-user subscription on top of the same core. It adds extra apps and features, Odoo's official hosting options, version upgrades and support. It suits businesses that need full accounting, Studio, mobile apps or want Odoo SA to handle hosting and upgrades.</p>
</section>

<section>
  <h2>Key differences</h2>
  <div class="grid-2">
    <div class="card"><h3>Licence &amp; cost</h3><p>Community: free, open source. Enterprise: paid subscription, priced per user. Check Odoo's current pricing page for exact numbers in your country.</p></div>
    <div class="card"><h3>Accounting</h3><p>Community includes invoicing and payments. Enterprise adds full accounting features such as bank synchronisation, advanced reporting and localisation packages.</p></div>
    <div class="card"><h3>Extra apps</h3><p>Enterprise adds apps such as Studio, Helpdesk, Field Service, Planning, Sign, Payroll and more, plus the official mobile apps.</p></div>
    <div class="card"><h3>Hosting &amp; upgrades</h3><p>Community runs on your own server or Docker. Enterprise can also run on Odoo Online or Odoo.sh and includes official version upgrade services.</p></div>
  </div>
</section>

<section>
  <h2>When Odoo Community is enough</h2>
  <ul>
    <li>You mainly need CRM, Sales, Purchase, Inventory, Invoicing, Manufacturing or Website.</li>
    <li>You're comfortable self-hosting (or having a developer host it on Docker or a VPS).</li>
    <li>You'd rather invest budget in a few targeted custom modules than in per-user licences.</li>
  </ul>
  <h2 style="margin-top:28px">When Odoo Enterprise is worth it</h2>
  <ul>
    <li>You need full accounting, payroll, Helpdesk, Field Service or Studio.</li>
    <li>You want managed hosting on Odoo Online or Odoo.sh and official upgrades.</li>
    <li>You run several companies or countries and want localisation packages and support from Odoo SA.</li>
  </ul>
</section>

<section>
  <h2>My recommendation</h2>
  <p>Start from your processes, not the edition. List what each team must do in Odoo, check which edition covers it as standard, and price the gap: licences on one side, custom development on the other. I run exactly this comparison as part of my <a href="/odoo-implementation/">Odoo implementation</a> work, and I build and maintain systems on both editions, including a seven-company Odoo 19 Enterprise setup.</p>
</section>""",
        "faq_title": "Community vs Enterprise FAQ",
        "faqs": [
            ("Can I upgrade from Odoo Community to Enterprise later?", "Yes. Enterprise is built on the same core, so a Community database can be moved to Enterprise later. Custom modules may need small adjustments."),
            ("Is Odoo Community really free?", "Yes. The software is free and open source under LGPLv3. You still pay for hosting, and for any implementation or development work you need."),
            ("Can a developer add Enterprise-like features to Community?", "Often, yes. Many gaps can be filled with custom or community modules, but some Enterprise apps are large products in their own right, so compare the cost of building against the licence."),
            ("Which edition do you work with?", "Both. I implement, customise and support Odoo 17, 18 and 19 in Community and Enterprise."),
        ],
        "cta_title": "Not sure which Odoo edition you need?",
        "cta_text": "Send me a short description of your business and I'll tell you which edition I'd recommend, and why.",
        "schema": lambda url: {
            "@type": "Article",
            "headline": "Odoo Community vs Enterprise: Which Should You Choose?",
            "description": "A practical comparison of Odoo Community and Odoo Enterprise.",
            "author": {"@id": f"{SITE}/#raja"},
            "publisher": {"@id": f"{SITE}/#raja"},
            "datePublished": "2026-11-09",
            "dateModified": "2026-11-09",
            "mainEntityOfPage": url,
            "image": f"{SITE}/og-image.png",
        },
    },
]

if __name__ == "__main__":
    for p in PAGES:
        out = ROOT / p["slug"].strip("/") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(p), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))
