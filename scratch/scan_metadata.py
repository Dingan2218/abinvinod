import os
import re
import json

def scan_html_files():
    base_dir = "."
    excluded = {".git", "node_modules", ".gemini", "assets"}
    results = []
    
    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in excluded and not d.startswith('.')]
        for f in files:
            if not f.endswith(".html"):
                continue
            filepath = os.path.join(root, f).replace("\\", "/")
            relpath = filepath[2:] if filepath.startswith("./") else filepath
            
            with open(filepath, "r", encoding="utf-8", errors="ignore") as file_obj:
                content = file_obj.read()
                
            title_m = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            title = title_m.group(1).strip() if title_m else ""
            
            desc_m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE | re.DOTALL)
            if not desc_m:
                desc_m = re.search(r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']', content, re.IGNORECASE | re.DOTALL)
            desc = desc_m.group(1).strip() if desc_m else ""
            
            kw_m = re.search(r'<meta\s+name=["\']keywords["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE | re.DOTALL)
            if not kw_m:
                kw_m = re.search(r'<meta\s+content=["\'](.*?)["\']\s+name=["\']keywords["\']', content, re.IGNORECASE | re.DOTALL)
            keywords = kw_m.group(1).strip() if kw_m else ""
            
            h1_m = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
            h1_raw = h1_m.group(1).strip() if h1_m else ""
            h1 = re.sub(r'<[^>]+>', ' ', h1_raw)
            h1 = " ".join(h1.split())
            
            url_slug = relpath[:-5] if relpath.endswith(".html") else relpath
            if url_slug == "index":
                url_path = "/"
            elif url_slug.endswith("/index"):
                url_path = "/" + url_slug[:-6]
            else:
                url_path = "/" + url_slug
                
            results.append({
                "file": relpath,
                "url": f"https://abinvinod.in{url_path}",
                "title": title,
                "h1": h1,
                "keywords": keywords,
                "desc": desc
            })
            
    with open("page_inventory.json", "w", encoding="utf-8") as out:
        json.dump(results, out, indent=2)
        
    print(f"Scanned {len(results)} pages successfully!")

if __name__ == "__main__":
    scan_html_files()
