import os
import json

districts = [
    {
        "id": "alappuzha",
        "name": "Alappuzha",
        "alias": "Alleppey",
        "lat": "9.4981",
        "lng": "76.3388",
        "industries": "Houseboat & Backwater Tourism, Coir Manufacturing, Seafood Processing, and Houseboat operators.",
        "description": "Dubbed the 'Venice of the East', Alappuzha is Kerala's premier tourism destination. With hundreds of houseboat operators and luxury resorts competing for the same travelers, having a visible online presence on search engines is non-negotiable.",
        "marketing_desc": "For Alappuzha's travel brands, I focus on local and international SEO, optimizing websites for direct booking conversion, and implementing Google Search ads that capture high-intent travelers planning their trips.",
        "subtitle_suffix": "for resorts, houseboats, and coir brands.",
        "keywords": ["resorts", "houseboats", "coir brands"]
    },
    {
        "id": "ernakulam",
        "name": "Ernakulam",
        "alias": "Kochi",
        "lat": "9.9816",
        "lng": "76.2999",
        "industries": "Commercial Capital, Startups & Tech (Infopark), Maritime & Shipping, Real Estate, Luxury Retail, and Tourism.",
        "description": "Ernakulam, with its metropolitan heart Kochi, is the undisputed commercial and startup capital of Kerala. The competition here is fierce, with businesses in every sector vying for local dominance and global expansion.",
        "marketing_desc": "In Kochi, I run comprehensive multi-channel digital campaigns. From optimizing local businesses for the high-volume Ernakulam map pack to building hyper-focused conversion funnels for startups at Infopark, my strategy is aggressive and data-first.",
        "subtitle_suffix": "for startups and enterprises.",
        "keywords": ["startups", "enterprises"]
    },
    {
        "id": "idukki",
        "name": "Idukki",
        "alias": "Munnar",
        "lat": "9.9189",
        "lng": "77.1025",
        "industries": "Hill Tourism, Spice Plantations (Cardamom/Tea), Hydroelectric Power, and Eco-resorts.",
        "description": "Idukki is Kerala's rugged mountain district, home to spice plantations and wildlife reserves. With destinations like Munnar attracting global visitors, digital visibility is crucial for accommodation and tourism players.",
        "marketing_desc": "I design SEO strategies specifically for nature resorts and adventure tours in Idukki. My focus is capturing direct bookings and ranking for destination keywords locally and internationally.",
        "subtitle_suffix": "for spice exporters and homestays.",
        "keywords": ["spice exporters", "homestays"]
    },
    {
        "id": "kannur",
        "name": "Kannur",
        "alias": "Cannanore",
        "lat": "11.8745",
        "lng": "75.3704",
        "industries": "Handloom Textiles, Kannur International Airport Hub, Cashew Processing, and Malabar Tourism.",
        "description": "Kannur is famous for its handloom industry and beautiful beaches. The international airport makes it a key growth hub for Malabar, connecting local manufacturers with global consumers.",
        "marketing_desc": "I build conversion-optimized search funnels for Kannur's exporters and handloom industries, utilizing international SEO and paid ads to tap into global markets.",
        "subtitle_suffix": "for handlooms, cashew exporters, and hotels.",
        "keywords": ["handlooms", "cashew exporters", "hotels"]
    },
    {
        "id": "kasaragod",
        "name": "Kasaragod",
        "alias": "Kasaragod",
        "lat": "12.5102",
        "lng": "74.9852",
        "industries": "Coir & Coconut Products, Red Clay Industry, Handloom, and Fort Tourism (Bekal).",
        "description": "Kasaragod is the northernmost district of Kerala, famous for Bekal Fort and coconut products. It holds rich potential for localized businesses seeking online visibility in regional markets.",
        "marketing_desc": "I optimize Google Business Profiles and local map packs for Kasaragod brands, driving footprint and inquiries for local service providers.",
        "subtitle_suffix": "for coir processors, local startups, and homestays.",
        "keywords": ["coir processors", "local startups", "homestays"]
    },
    {
        "id": "kollam",
        "name": "Kollam",
        "alias": "Quilon",
        "lat": "8.8932",
        "lng": "76.6141",
        "industries": "Cashew Processing & Export, Kollam Port & Maritime Trade, Clay & Minerals, and Ashtamudi Backwater Tourism.",
        "description": "Kollam is the cashew capital of the world and a historic trading port. It features active industrial segments alongside backwater tourism sectors competing for digital leads.",
        "marketing_desc": "I establish corporate web structures and B2B organic growth models for Kollam's export companies and luxury resorts on Ashtamudi lake.",
        "subtitle_suffix": "for cashew traders, exporters, and resorts.",
        "keywords": ["cashew traders", "exporters", "resorts"]
    },
    {
        "id": "kottayam",
        "name": "Kottayam",
        "alias": "Kottayam",
        "lat": "9.5916",
        "lng": "76.5222",
        "industries": "Natural Rubber Cultivation, Publishing & Printing Houses, Kumarakom Tourism, and Food Processing.",
        "description": "Kottayam is the land of letters, latex, and lakes, boasting major publishing houses, rubber estates, and the serene backwaters of Kumarakom.",
        "marketing_desc": "For Kottayam businesses, I execute strategic B2B optimization and Google Ads funnels that target rubber product dealers, book buyers, and tourists planning resort stays.",
        "subtitle_suffix": "for publishers, rubber industries, and resorts.",
        "keywords": ["publishers", "rubber industries", "resorts"]
    },
    {
        "id": "kozhikode",
        "name": "Kozhikode",
        "alias": "Calicut",
        "lat": "11.2588",
        "lng": "75.7804",
        "industries": "Malabar Trading Hub, Food & Culinary Enterprises, IT & Startups (Cyberpark), Timber, and Footwear.",
        "description": "Kozhikode is the historic spice trading port of Malabar, renowned today for its food, IT Cyberpark startups, and large-scale retail sectors.",
        "marketing_desc": "I help Kozhikode enterprises scale with localized content marketing, search ads, and local SEO that positions them as leaders in the Malabar region.",
        "subtitle_suffix": "for restaurants, Cyberpark IT firms, and retail brands.",
        "keywords": ["restaurants", "Cyberpark IT firms", "retail brands"]
    },
    {
        "id": "malappuram",
        "name": "Malappuram",
        "alias": "Malappuram",
        "lat": "11.0735",
        "lng": "76.0740",
        "industries": "Gulf-remittance Economy, Healthcare & Hospitals, Educational Institutions, and Food Processing.",
        "description": "Malappuram is one of the most populated districts, driven by remittance and a booming consumer market with high purchasing power.",
        "marketing_desc": "I deploy paid social campaigns and local SEO for Malappuram's healthcare facilities, retail networks, and institutes to maximize local customer acquisition.",
        "subtitle_suffix": "for clinics, educational institutions, and retail shops.",
        "keywords": ["clinics", "educational institutions", "retail shops"]
    },
    {
        "id": "palakkad",
        "name": "Palakkad",
        "alias": "Palghat",
        "lat": "10.7867",
        "lng": "76.6547",
        "industries": "Granite & Manufacturing, Kanjikode Industrial Zone, Rice Milling, and Wind Power Generation.",
        "description": "Palakkad is the gateway to Kerala, home to the Kanjikode industrial belt and extensive paddy fields, forming a unique mix of manufacturing and agriculture.",
        "marketing_desc": "I create search landing pages and B2B campaigns targeting corporate buyers and distributors for Palakkad's industrial companies.",
        "subtitle_suffix": "for factories, rice mills, and manufacturers.",
        "keywords": ["factories", "rice mills", "manufacturers"]
    },
    {
        "id": "pathanamthitta",
        "name": "Pathanamthitta",
        "alias": "Pathanamthitta",
        "lat": "9.2644",
        "lng": "76.7870",
        "industries": "Pilgrim Tourism (Sabarimala), NRI Investments, Agriculture (Spices/Rubber), and Eco-tourism.",
        "description": "Pathanamthitta is the headquarters of pilgrimage tourism in Kerala, with a strong NRI-backed economy and quiet eco-tourism retreats.",
        "marketing_desc": "I build lead funnels for financial institutions, real estate developments, and pilgrim hospitality services in Pathanamthitta.",
        "subtitle_suffix": "for travel agencies, NRI-funded ventures, and farms.",
        "keywords": ["travel agencies", "NRI-funded ventures", "farms"]
    },
    {
        "id": "thiruvananthapuram",
        "name": "Thiruvananthapuram",
        "alias": "Trivandrum",
        "lat": "8.5241",
        "lng": "76.9366",
        "industries": "Administrative Capital, Technopark IT Hub, Space Research & Aero-tech, Kovalam Beach Tourism, and Healthcare.",
        "description": "Thiruvananthapuram is the capital of Kerala, home to Technopark, one of India's largest IT parks, and major government institutions.",
        "marketing_desc": "I consult for Technopark IT exporters on global search visibility, while simultaneously driving local search strategies for Kovalam hoteliers and clinics.",
        "subtitle_suffix": "for Technopark IT companies, clinics, and hotels.",
        "keywords": ["Technopark IT companies", "clinics", "hotels"]
    },
    {
        "id": "thrissur",
        "name": "Thrissur",
        "alias": "Trichur",
        "lat": "10.5276",
        "lng": "76.2144",
        "industries": "Gold Jewelry Manufacturing, Ayurvedic Medicine Hubs, Thrissur Pooram Tourism, Banking & NBFCs.",
        "description": "Thrissur is the cultural capital of Kerala, famous for gold design, ayurveda clusters, and major financial institutions.",
        "marketing_desc": "I set up local SEO campaigns for ayurvedic wellness centers and lead generation funnels for gold retailers and financial services in Thrissur.",
        "subtitle_suffix": "for gold showrooms, ayurvedic clinics, and NBFCs.",
        "keywords": ["gold showrooms", "ayurvedic clinics", "NBFCs"]
    },
    {
        "id": "wayanad",
        "name": "Wayanad",
        "alias": "Wayanad",
        "lat": "11.6854",
        "lng": "76.1320",
        "industries": "Hill Tourism & Adventure, Coffee & Tea Plantations, Spices, and Organic Farming.",
        "description": "Wayanad is a pristine hill station, rich with coffee plantations and adventure tourism spots, attracting domestic and foreign holidaymakers.",
        "marketing_desc": "I help Wayanad resorts and adventure tours rank for travel planning keywords, streamlining the path from search queries to direct bookings.",
        "subtitle_suffix": "for plantation owners, resorts, and spice exporters.",
        "keywords": ["plantation owners", "resorts", "spice exporters"]
    }
]

# GA4 tag code
GA4_SCRIPT = """<!-- Google Analytics (GA4) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-Y586J4M1L8"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    def gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-Y586J4M1L8');
  </script>"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Primary SEO -->
  <title>{meta_title}</title>
  <meta name="description" content="{meta_desc}">
  <meta name="keywords" content="{meta_keywords}">
  <link rel="canonical" href="{canonical_url}">

  <!-- Open Graph -->
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{og_desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical_url}">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../style.css">

  {ga4_script}

  <!-- Structured Data: LocalBusiness Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "{schema_name}",
    "image": "https://abinvinod.in/assets/project1.png",
    "@id": "{canonical_url}#localbusiness",
    "url": "{canonical_url}",
    "telephone": "",
    "priceRange": "$$",
    "address": {{
      "@type": "PostalAddress",
      "addressLocality": "{district_name}",
      "addressRegion": "Kerala",
      "addressCountry": "IN"
    }},
    "geo": {{
      "@type": "GeoCoordinates",
      "latitude": "{lat}",
      "longitude": "{lng}"
    }},
    "openingHoursSpecification": {{
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
      ],
      "opens": "09:00",
      "closes": "18:00"
    }},
    "sameAs": [
      "https://www.linkedin.com/in/abinvinod-aby/",
      "https://www.instagram.com/abin_vinod_aby/"
    ]
  }}
  </script>

  <!-- Structured Data: FAQ Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "{faq_q1}",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "{faq_a1}"
        }}
      }},
      {{
        "@type": "Question",
        "name": "{faq_q2}",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "{faq_a2}"
        }}
      }}
    ]
  }}
  </script>
  
  <style>
    .local-hero {{
      padding: 180px 0 100px 0;
      position: relative;
    }}
    .local-intro {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 60px;
      padding: 80px 0;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }}
    @media (max-width: 768px) {{
      .local-intro {{
        grid-template-columns: 1fr;
        gap: 40px;
      }}
    }}
    .local-intro h2 {{
      font-family: 'Syne', sans-serif;
      font-size: 2.2rem;
      line-height: 1.2;
    }}
    .local-intro-right p {{
      color: #94a3b8;
      font-size: 1.1rem;
      line-height: 1.7;
      margin-bottom: 25px;
    }}
    .local-industries {{
      background: rgba(124, 58, 237, 0.05);
      border: 1px solid rgba(124, 58, 237, 0.15);
      padding: 25px;
      border-radius: 12px;
      margin-top: 30px;
    }}
    .local-industries h4 {{
      color: var(--accent-cyan);
      font-size: 1rem;
      font-weight: 700;
      margin-bottom: 10px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .local-industries p {{
      color: #ffffff;
      margin: 0;
      font-size: 1rem;
      line-height: 1.5;
    }}
    .link-other-districts {{
      padding: 80px 0;
      text-align: center;
    }}
    .link-other-districts h3 {{
      font-family: 'Syne', sans-serif;
      font-size: 1.8rem;
      margin-bottom: 30px;
    }}
    .dist-list {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 15px;
      list-style: none;
      padding: 0;
    }}
    .dist-list a {{
      color: #94a3b8;
      text-decoration: none;
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 8px 18px;
      border-radius: 100px;
      font-size: 0.9rem;
      transition: all 0.2s ease;
    }}
    .dist-list a:hover {{
      border-color: var(--accent-cyan);
      color: var(--accent-cyan);
      background: rgba(6, 182, 212, 0.05);
    }}
    .breadcrumb {{
      display: flex;
      gap: 10px;
      color: #64748b;
      font-size: 0.9rem;
      margin-bottom: 20px;
    }}
    .breadcrumb a {{
      color: #94a3b8;
      text-decoration: none;
    }}
    .breadcrumb a:hover {{
      color: var(--accent-cyan);
    }}
  </style>
</head>
<body>

  <div class="custom-cursor" id="custom-cursor"></div>
  <div class="custom-cursor-dot" id="custom-cursor-dot"></div>
  <div class="glow-orb orb-1"></div>
  <div class="glow-orb orb-2"></div>

  <header class="header">
    <div class="header-container">
      <a href="/" class="logo magnetic" id="nav-logo">ABIN<span>VINOD</span></a>
      <nav class="nav-links" aria-label="Main Navigation">
        <a href="/#services" class="nav-link magnetic">Services</a>
        <a href="/#work" class="nav-link magnetic">Work</a>
        <a href="/#about" class="nav-link magnetic">About</a>
        <a href="/blog" class="nav-link magnetic">Blog</a>
        <a href="/{other_category_dir}" class="nav-link magnetic" style="color: var(--accent-cyan)">{other_category_nav}</a>
        <a href="/#contact" class="nav-link magnetic">Contact</a>
      </nav>
      <div class="hire-badge">
        <span class="pulse-dot"></span>
        <span class="badge-text">Available for Hire</span>
      </div>
    </div>
  </header>

  <main>
    <!-- ========== HERO SECTION ========== -->
    <section class="local-hero">
      <div class="container">
        <div class="breadcrumb">
          <a href="/">Home</a> / <a href="./">Districts</a> / <span>{district_name}</span>
        </div>
        <span class="section-tag">{district_upper} DISTRICT EDITION</span>
        <h1 class="section-title" style="margin-top: 15px;">
          {hero_h1}
        </h1>
        <p class="section-subtitle">{hero_subtitle}</p>
        <div style="margin-top: 40px; display: flex; gap: 20px;">
          <a href="#contact" class="btn btn-primary magnetic">Free Consultation</a>
          <a href="./" class="btn btn-secondary magnetic">All Districts</a>
        </div>
      </div>
    </section>

    <!-- ========== LOCAL ANALYSIS ========== -->
    <section class="local-details-sec" style="background: rgba(255,255,255,0.01);">
      <div class="container">
        <div class="local-intro">
          <div>
            <h2>DOMINATE SEARCH &amp; WEB TRAFFIC IN {district_upper}</h2>
            <div class="local-industries">
              <h4>Key Industries Covered</h4>
              <p>{industries}</p>
            </div>
          </div>
          <div class="local-intro-right">
            <p>{description}</p>
            <p>{marketing_desc}</p>
            <p>Whether you're looking to run hyper-targeted local campaigns in Malayalam to reach the district's residents, or want to scale your operations nationally, my custom solutions deliver results with clear ROI metrics.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ========== LOCAL SERVICES SUMMARY ========== -->
    <section class="services" style="padding: 100px 0;">
      <div class="container">
        <div class="section-header">
          <span class="section-tag">SERVICES</span>
          <h2>CUSTOM SEO &amp; MARKETING CAPABILITIES</h2>
          <p class="section-subtitle">A comprehensive suite of growth services designed to put your business ahead of the local competition.</p>
        </div>
        
        <div class="services-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 25px;">
          <div class="service-card" style="padding: 25px;">
            <div class="service-icon"><i data-lucide="search"></i></div>
            <h3>Local SEO Optimization</h3>
            <p>Ensure your business appears in the Local Map Pack and on top of organic searches when clients in {district_name} look for your services.</p>
          </div>
          <div class="service-card" style="padding: 25px;">
            <div class="service-icon"><i data-lucide="target"></i></div>
            <h3>Google &amp; Meta Ads</h3>
            <p>Targeted lead generation campaigns to convert searchers and social media users into high-intent paying customers.</p>
          </div>
          <div class="service-card" style="padding: 25px;">
            <div class="service-icon"><i data-lucide="share-2"></i></div>
            <h3>Social Media Branding</h3>
            <p>Engage the local community with strategic content calendars, reels, and stories that build trusted brand equity.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ========== LOCAL FAQ ========== -->
    <section class="faq" style="padding: 80px 0; border-top: 1px solid rgba(255, 255, 255, 0.08);">
      <div class="container">
        <div class="section-header">
          <span class="section-tag">QUESTIONS &amp; ANSWERS</span>
          <h2>FREQUENTLY ASKED QUESTIONS</h2>
        </div>
        <div class="faq-list" style="max-width: 800px; margin: 40px auto 0 auto;">
          <details class="faq-item" open>
            <summary class="faq-question">
              <span>{faq_q1}</span>
              <i data-lucide="chevron-down" class="faq-icon"></i>
            </summary>
            <div class="faq-answer">
              <p>{faq_a1}</p>
            </div>
          </details>
          <details class="faq-item">
            <summary class="faq-question">
              <span>{faq_q2}</span>
              <i data-lucide="chevron-down" class="faq-icon"></i>
            </summary>
            <div class="faq-answer">
              <p>{faq_a2}</p>
            </div>
          </details>
        </div>
      </div>
    </section>

    <!-- ========== CONTACT FORM ========== -->
    <section class="contact" id="contact" style="padding: 100px 0; border-top: 1px solid rgba(255, 255, 255, 0.08);">
      <div class="container contact-container">
        <div class="contact-header">
          <span class="section-tag">CONTACT</span>
          <h2 class="section-title">START A PROJECT IN {district_upper}</h2>
          <p class="contact-subtitle">Get in touch to receive a free audit and customized strategy session for your business.</p>
          <div class="contact-methods">
            <a href="mailto:itsme@abinvinod.in" class="contact-method magnetic">
              <i data-lucide="mail"></i>
              <span>itsme@abinvinod.in</span>
            </a>
          </div>
        </div>
        
        <div class="contact-form-container">
          <form class="contact-form" id="contact-form">
            <div class="form-group">
              <input type="text" id="form-name" name="name" required placeholder=" " autocomplete="name">
              <label for="form-name">Your Name</label>
            </div>
            <div class="form-group">
              <input type="email" id="form-email" name="email" required placeholder=" " autocomplete="email">
              <label for="form-email">Your Email</label>
            </div>
            <div class="form-group">
              <input type="text" id="form-business" name="business" placeholder=" ">
              <label for="form-business">Your Business / Website</label>
            </div>
            <div class="form-group">
              <textarea id="form-message" name="message" required rows="5" placeholder=" "></textarea>
              <label for="form-message">Tell me about your project goals in {district_name}</label>
            </div>
            <button type="submit" class="btn btn-primary magnetic" id="form-submit">
              Get Free Consultation <i data-lucide="send"></i>
            </button>
            <div class="form-status" id="form-status"></div>
          </form>
        </div>
      </div>
    </section>

    <!-- ========== DISTRICT MESHLINKING ========== -->
    <section class="link-other-districts" style="background: rgba(255, 255, 255, 0.02); border-top: 1px solid rgba(255,255,255,0.05);">
      <div class="container">
        <h3>Other {mesh_heading}</h3>
        <ul class="dist-list">
          {mesh_links}
          <li><a href="./" class="magnetic" style="border-color: var(--accent); color: var(--accent);">View All Districts</a></li>
        </ul>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container footer-container">
      <div class="footer-main">
        <a href="/" class="footer-logo">ABIN<span>VINOD</span></a>
        <p class="footer-tagline">{footer_tagline}</p>
      </div>
      <div class="footer-bottom">
        <p class="copyright">&copy; 2026 Abin Vinod — Digital Marketing Expert &amp; SEO Expert in Kerala. All rights reserved.</p>
        <a href="#" class="back-to-top magnetic" id="back-to-top">Back to Top <i data-lucide="arrow-up"></i></a>
      </div>
    </div>
  </footer>

  <script src="https://unpkg.com/lucide@latest"></script>
  <script>lucide.createIcons();</script>
  <script src="../app.js"></script>
</body>
</html>"""

def generate_pages():
    for cat in ["digital_marketer", "seo_expert"]:
        dir_name = "best_digital_marketer_kerala" if cat == "digital_marketer" else "best_seo-expert-kerala"
        
        # Ensure directories exist
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            
        for dist in districts:
            dist_id = dist["id"]
            dist_name = dist["name"]
            dist_upper = dist_name.upper()
            
            # Setup specific values depending on the category
            if cat == "digital_marketer":
                meta_title = f"Best Digital Marketer in {dist_name} | Top SEO Expert in {dist_name} — Abin Vinod"
                meta_desc = f"Scale organic traffic and rank #1 with the best SEO expert and digital marketer in {dist_name}. Abin Vinod provides high-ROI search engine optimization, Google Ads, and digital marketing strategies customized for {dist_name} brands."
                meta_keywords = f"best digital marketer in {dist_name}, best SEO expert in {dist_name}, digital marketing expert {dist_name}, SEO specialist {dist_name}, SEO expert {dist_name}, digital marketing {dist.get('alias', dist_name)}, Abin Vinod"
                
                og_title = f"Best SEO Expert & Digital Marketer in {dist_name}"
                og_desc = f"Customized SEO & digital marketing solutions for businesses in {dist_name}, Kerala. Drive organic traffic, scale leads, and grow revenue today."
                
                schema_name = f"Abin Vinod — SEO Expert & Digital Marketer in {dist_name}"
                
                faq_q1 = f"Why should I hire the best digital marketer and SEO expert in {dist_name}?"
                faq_a1 = f"Partnering with the best SEO expert and digital marketer in {dist_name} ensures your business optimizes for localized search behavior, regional industry clusters (like {dist['industries'].split(',')[0]}), and captures local leads on Google Map Pack and organic rankings."
                
                faq_q2 = f"What search and marketing services do you offer in {dist_name}?"
                faq_a2 = f"I provide customized search and growth services including Search Engine Optimization (SEO) tailored for local search patterns, high-ROI Google Search & Display Ads, Meta (Facebook & Instagram) campaigns, local map pack listing, and analytics setup."
                
                hero_h1 = f"THE BEST<br>\n          <span class=\"gradient-text\">SEO EXPERT</span> &amp;<br>\n          DIGITAL MARKETER IN {dist_upper}"
                hero_subtitle = f"Scale your revenue with the best SEO expert and digital marketer in {dist.get('alias', dist_name)}. Advanced SEO, link building, and performance ads {dist['subtitle_suffix']}"
                
                other_category_dir = "best_digital_marketer_kerala"
                other_category_nav = "Districts"
                
                mesh_heading = "SEO & Marketing Hubs in Kerala"
                footer_tagline = "Best Digital Marketer & SEO Expert in Kerala — SEO, Ads & Growth"
            else:
                # SEO Expert specific
                meta_title = f"Best SEO Expert in {dist_name} | Top Search Specialist in {dist_name} — Abin Vinod"
                meta_desc = f"Scale organic traffic and rank #1 with the best SEO expert in {dist_name}. Abin Vinod provides high-ROI search engine optimization, Google Ads, and digital marketing strategies customized for {dist_name} brands."
                meta_keywords = f"best SEO expert in {dist_name}, best digital marketer in {dist_name}, SEO expert {dist_name}, SEO specialist {dist_name}, digital marketing {dist.get('alias', dist_name)}, Abin Vinod"
                
                og_title = f"Best SEO Expert in {dist_name} | Search Specialist"
                og_desc = f"Customized SEO & digital marketing solutions for businesses in {dist_name}, Kerala. Drive organic traffic, scale leads, and grow revenue today."
                
                schema_name = f"Abin Vinod — SEO Expert in {dist_name}"
                
                faq_q1 = f"Why should I hire the best SEO expert in {dist_name}?"
                faq_a1 = f"Partnering with the best SEO expert in {dist_name} ensures your business optimizes for localized search behavior, regional industry clusters (like {dist['industries'].split(',')[0]}), and captures local leads on Google Map Pack and organic rankings."
                
                faq_q2 = f"What search engine optimization services do you offer in {dist_name}?"
                faq_a2 = f"I provide customized search and growth services including Search Engine Optimization (SEO) tailored for local search patterns, high-ROI Google Search & Display Ads, Meta (Facebook & Instagram) campaigns, local map pack listing, and analytics setup."
                
                hero_h1 = f"THE BEST<br>\n          <span class=\"gradient-text\">SEO EXPERT</span> IN {dist_upper}"
                hero_subtitle = f"Get more bookings with the best SEO expert and digital marketer in {dist.get('alias', dist_name)}. Custom search marketing {dist['subtitle_suffix']}"
                
                other_category_dir = "best_seo-expert-kerala"
                other_category_nav = "SEO Expert"
                
                mesh_heading = "SEO Expert Hubs in Kerala"
                footer_tagline = "Best SEO Expert in Kerala — SEO, Ads & Growth"

            canonical_url = f"https://abinvinod.in/{dir_name}/{dist_id}"
            
            # Mesh links generation (excluding current district, picking next 6 in rotation for pretty footer grid)
            curr_index = districts.index(dist)
            mesh_list = []
            for i in range(1, 7):
                idx = (curr_index + i) % len(districts)
                target_dist = districts[idx]
                mesh_list.append(f'<li><a href="{target_dist["id"]}" class="magnetic">{target_dist["name"]}</a></li>')
            mesh_links = "".join(mesh_list)
            
            # Format template
            html_content = TEMPLATE.format(
                meta_title=meta_title,
                meta_desc=meta_desc,
                meta_keywords=meta_keywords,
                canonical_url=canonical_url,
                og_title=og_title,
                og_desc=og_desc,
                ga4_script=GA4_SCRIPT,
                schema_name=schema_name,
                district_name=dist_name,
                lat=dist["lat"],
                lng=dist["lng"],
                faq_q1=faq_q1,
                faq_a1=faq_a1,
                faq_q2=faq_q2,
                faq_a2=faq_a2,
                other_category_dir=other_category_dir,
                other_category_nav=other_category_nav,
                district_upper=dist_upper,
                hero_h1=hero_h1,
                hero_subtitle=hero_subtitle,
                industries=dist["industries"],
                description=dist["description"],
                marketing_desc=dist["marketing_desc"],
                mesh_heading=mesh_heading,
                mesh_links=mesh_links,
                footer_tagline=footer_tagline
            )
            
            # Write file
            file_path = os.path.join(dir_name, f"{dist_id}.html")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(html_content)
                
    print("District landing pages programmatically generated successfully!")

if __name__ == "__main__":
    generate_pages()
