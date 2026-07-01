import os
import datetime

def generate_sitemap():
    base_url = "https://abinvinod.in"
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    urls = []
    
    # Add home page
    urls.append({
        "loc": f"{base_url}/",
        "lastmod": current_date,
        "changefreq": "weekly",
        "priority": "1.0"
    })
    
    # Folders to scan
    scan_dirs = {
        ".": 1.0,
        "blog": 0.8,
        "best_digital_marketer_kerala": 0.9,
        "best_seo-expert-kerala": 0.9
    }
    
    for dir_path, default_priority in scan_dirs.items():
        if not os.path.exists(dir_path):
            continue
            
        for file in os.listdir(dir_path):
            if not file.endswith('.html'):
                continue
                
            # Skip templates/system files or index files we treat specially
            if file == 'index.html':
                if dir_path == '.':
                    continue  # already added home page
                else:
                    # e.g., /blog/index.html -> /blog
                    clean_path = dir_path.replace('\\', '/')
                    loc = f"{base_url}/{clean_path}"
                    priority = "0.9"
                    changefreq = "weekly"
            elif file == '404.html':
                continue
            else:
                # Normal html file
                # Remove .html extension for clean URL
                clean_name = file[:-5]
                if dir_path == '.':
                    loc = f"{base_url}/{clean_name}"
                else:
                    clean_dir = dir_path.replace('\\', '/')
                    loc = f"{base_url}/{clean_dir}/{clean_name}"
                priority = "0.8"
                changefreq = "monthly"
                
            # Get last modified time of the file
            full_path = os.path.join(dir_path, file)
            mtime = os.path.getmtime(full_path)
            lastmod = datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
            
            # Avoid duplicate urls
            if not any(u["loc"] == loc for u in urls):
                urls.append({
                    "loc": loc,
                    "lastmod": lastmod,
                    "changefreq": changefreq,
                    "priority": priority
                })
                
    # Sort urls for clean sitemap presentation
    urls.sort(key=lambda x: (x["priority"], x["loc"]), reverse=True)
    
    # Write to sitemap.xml
    sitemap_content = ['<?xml version="1.0" encoding="UTF-8"?>',
                       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
                       
    for url in urls:
        sitemap_content.append("  <url>")
        sitemap_content.append(f"    <loc>{url['loc']}</loc>")
        sitemap_content.append(f"    <lastmod>{url['lastmod']}</lastmod>")
        sitemap_content.append(f"    <changefreq>{url['changefreq']}</changefreq>")
        sitemap_content.append(f"    <priority>{url['priority']}</priority>")
        sitemap_content.append("  </url>")
        
    sitemap_content.append("</urlset>")
    
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap_content))
        
    print(f"Sitemap generated successfully with {len(urls)} clean URLs!")

if __name__ == "__main__":
    generate_sitemap()
