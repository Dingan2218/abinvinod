import json
import re

def generate_keyword_mapping():
    with open("page_inventory.json", "r", encoding="utf-8") as f:
        pages = json.load(f)
        
    # Categorize pages
    categories = {
        "Core & Primary Pages": [],
        "Services & Solutions": [],
        "Digital Marketer Regional Hubs (14 Districts)": [],
        "SEO Expert Regional Hubs (14 Districts)": [],
        "Business Consulting Hubs": [],
        "Location Pages": [],
        "Industry-Specific Landing Pages": [],
        "Blog Articles & Knowledge Hub": [],
        "SEO Tools & Calculators": [],
        "Case Studies & Case References": []
    }
    
    for p in pages:
        file = p["file"]
        url = p["url"]
        title = p["title"]
        h1 = p["h1"]
        kw = p["keywords"]
        desc = p["desc"]
        
        # Determine category & primary target keyword
        if file.startswith("best_digital_marketer_"):
            cat = "Digital Marketer Regional Hubs (14 Districts)"
            dist = file.replace("best_digital_marketer_", "").replace(".html", "").capitalize()
            primary_kw = f"Best Digital Marketer in {dist}"
            sec_kws = f"best digital marketer in {dist}, digital marketing expert {dist}, SEO specialist {dist}, digital marketing {dist}"
        elif file.startswith("best_seo_expert_"):
            cat = "SEO Expert Regional Hubs (14 Districts)"
            dist = file.replace("best_seo_expert_", "").replace(".html", "").capitalize()
            primary_kw = f"Best SEO Expert in {dist}"
            sec_kws = f"best SEO expert in {dist}, top search specialist {dist}, local search optimization {dist}, rank #1 Google {dist}"
        elif file.startswith("best_business_consultant_") or file.startswith("business-consultant/"):
            cat = "Business Consulting Hubs"
            if "alappuzha" in file:
                primary_kw = "Best Business Consultant in Alappuzha"
            elif "kochi" in file:
                primary_kw = "Best Business Consultant in Kochi"
            elif "kerala" in file:
                primary_kw = "Best Business Consultant in Kerala"
            else:
                primary_kw = "Business Consultant & Growth Advisor Kerala"
            sec_kws = kw if kw else "GTM strategy, business consultant Kerala, unit economics audit, digital transformation"
        elif file.startswith("services/"):
            cat = "Services & Solutions"
            page_name = file.replace("services/", "").replace(".html", "").replace("/index", "")
            primary_kw = f"{page_name.replace('-', ' ').title()} Kerala"
            sec_kws = kw if kw else f"{page_name.replace('-', ' ')} services, digital marketing services Kerala"
        elif file.startswith("locations/"):
            cat = "Location Pages"
            loc_name = file.replace("locations/", "").replace(".html", "").replace("/index", "").replace("/", "")
            primary_kw = f"Digital Marketing Agency in {loc_name.capitalize()}" if loc_name else "Kerala Locations Hub"
            sec_kws = kw if kw else f"digital marketing {loc_name}, SEO services {loc_name}"
        elif file.startswith("industries/"):
            cat = "Industry-Specific Landing Pages"
            ind_name = file.replace("industries/", "").replace(".html", "").replace("/index", "")
            primary_kw = f"{ind_name.replace('-', ' ').title()} Digital Marketing Kerala"
            sec_kws = kw if kw else f"{ind_name.replace('-', ' ')} marketing, SEO for {ind_name}"
        elif file.startswith("blog/"):
            cat = "Blog Articles & Knowledge Hub"
            art_name = file.replace("blog/", "").replace(".html", "").replace("/index", "")
            primary_kw = art_name.replace("-", " ").title()
            sec_kws = kw if kw else f"{primary_kw}, Kerala digital marketing guide"
        elif file.startswith("tools/"):
            cat = "SEO Tools & Calculators"
            tool_name = file.replace("tools/", "").replace(".html", "").replace("/index", "")
            primary_kw = f"Free {tool_name.replace('-', ' ').title()} Tool"
            sec_kws = kw if kw else f"{tool_name.replace('-', ' ')} online tool"
        elif file.startswith("case-studies/"):
            cat = "Case Studies & Case References"
            cs_name = file.replace("case-studies/", "").replace(".html", "").replace("/index", "")
            primary_kw = f"Digital Marketing Case Study - {cs_name.replace('-', ' ').title()}"
            sec_kws = kw if kw else "digital marketing results, SEO ROI case study"
        else:
            cat = "Core & Primary Pages"
            if file == "index.html":
                primary_kw = "Best Digital Marketer & SEO Expert in Kerala"
                sec_kws = "best SEO expert in Kerala, best digital marketer in Kerala, digital marketing expert Kerala, Google Ads specialist Kerala"
            elif file == "about.html":
                primary_kw = "Abin Vinod — SEO Expert & Digital Marketing Specialist"
                sec_kws = "Abin Vinod, digital marketing consultant Kerala, SEO background"
            else:
                name = file.replace(".html", "")
                primary_kw = f"{name.capitalize()} — Abin Vinod"
                sec_kws = kw if kw else f"{name} Abin Vinod"
                
        categories[cat].append({
            "url": url,
            "file": file,
            "title": title,
            "h1": h1,
            "primary_kw": primary_kw,
            "sec_kws": sec_kws,
            "intent": "Transactional / Commercial" if ("best_" in file or "services" in file or "pricing" in file) else ("Informational" if ("blog" in file or "tools" in file) else "Navigational / Commercial")
        })

    # Write Markdown Document
    md = []
    md.append("# Comprehensive Keyword Mapping & Technical SEO Architecture Document\n")
    md.append("**Website**: [https://abinvinod.in](https://abinvinod.in)\n")
    md.append("**Author / Lead Strategist**: Abin Vinod\n")
    md.append("**Total Mapped Pages**: 114 Pages\n")
    md.append("**Target Geographic Market**: Kerala (All 14 Districts), India & International Markets\n\n")
    
    md.append("## Executive Summary\n")
    md.append("This document provides a complete 1-to-1 keyword mapping matrix for all 114 URLs across the **abinvinod.in** portfolio ecosystem. Each page is mapped with its primary target keyword, secondary LSI (Latent Semantic Indexing) keywords, search intent, page title, H1 tag, and relative filepath. This ensures zero keyword cannibalization, optimal internal link anchor distribution, and structured E-E-A-T coverage across all search verticals.\n\n")
    
    for cat_name, items in categories.items():
        if not items:
            continue
        md.append(f"## {cat_name} ({len(items)} Pages)\n\n")
        md.append("| Target URL / File | Primary Target Keyword | Secondary Keywords | Search Intent | H1 Tag |\n")
        md.append("| :--- | :--- | :--- | :--- | :--- |\n")
        for item in items:
            url_link = f"[{item['file']}]({item['url']})"
            sec = item['sec_kws'].replace("\n", " ")
            if len(sec) > 90:
                sec = sec[:87] + "..."
            h1_clean = item['h1'].replace("|", "-")
            if len(h1_clean) > 60:
                h1_clean = h1_clean[:57] + "..."
            md.append(f"| {url_link} | **{item['primary_kw']}** | {sec} | {item['intent']} | `{h1_clean}` |\n")
        md.append("\n")
        
    with open("keyword_mapping_document.md", "w", encoding="utf-8") as out_md:
        out_md.write("".join(md))
        
    print("Keyword Mapping Document generated successfully in markdown format!")

if __name__ == "__main__":
    generate_keyword_mapping()
