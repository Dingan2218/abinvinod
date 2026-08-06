import os
import datetime

def get_url_info(rel_path):
    """
    Given a relative path to an HTML file, return (loc, priority, changefreq)
    """
    # Normalize path separators
    clean_path = rel_path.replace('\\', '/')
    
    # Root index.html
    if clean_path == 'index.html':
        return 'https://abinvinod.in/', '1.0', 'weekly'
    
    # Remove .html extension
    if clean_path.endswith('.html'):
        clean_path = clean_path[:-5]
        
    # If path ends with /index, remove /index
    if clean_path.endswith('/index'):
        clean_path = clean_path[:-6]
        
    loc = f"https://abinvinod.in/{clean_path}"
    
    # Main top-level directory index or main pages get 0.9 priority
    top_level_hubs = {
        'about', 'services', 'portfolio', 'case-studies', 'pricing', 
        'contact', 'faq', 'blog', 'locations', 'tools', 'industries', 
        'testimonials', 'best_digital_marketer_kerala', 
        'best_seo-expert-kerala', 'business-consultant'
    }
    
    parts = clean_path.split('/')
    if len(parts) == 1 and parts[0] in top_level_hubs:
        priority = '0.9'
        changefreq = 'weekly'
    elif len(parts) == 2 and parts[0] in top_level_hubs and parts[1] == '':
        priority = '0.9'
        changefreq = 'weekly'
    else:
        priority = '0.8'
        changefreq = 'monthly'
        
    return loc, priority, changefreq

def generate_sitemap():
    base_dir = '.'
    urls = []
    
    # Exclude directories
    excluded_dirs = {'.git', '.vscode', '.gemini', 'node_modules', 'assets'}
    
    for root, dirs, files in os.walk(base_dir):
        # Filter out excluded directories in-place
        dirs[:] = [d for d in dirs if d not in excluded_dirs and not d.startswith('.')]
        
        for file in files:
            if not file.endswith('.html'):
                continue
                
            # Skip 404 page
            if file == '404.html' and root == base_dir:
                continue
                
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base_dir)
            
            loc, priority, changefreq = get_url_info(rel_path)
            
            mtime = os.path.getmtime(full_path)
            lastmod = datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
            
            # Avoid duplicates
            if not any(u['loc'] == loc for u in urls):
                urls.append({
                    'loc': loc,
                    'lastmod': lastmod,
                    'changefreq': changefreq,
                    'priority': priority
                })
                
    # Sort urls: higher priority first, then alphabetically by location
    urls.sort(key=lambda x: (-float(x['priority']), x['loc']))
    
    sitemap_content = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    
    for url in urls:
        sitemap_content.append("  <url>")
        sitemap_content.append(f"    <loc>{url['loc']}</loc>")
        sitemap_content.append(f"    <lastmod>{url['lastmod']}</lastmod>")
        sitemap_content.append(f"    <changefreq>{url['changefreq']}</changefreq>")
        sitemap_content.append(f"    <priority>{url['priority']}</priority>")
        sitemap_content.append("  </url>")
        
    sitemap_content.append("</urlset>")
    
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap_content) + "\n")
        
    print(f"Sitemap generated successfully with {len(urls)} clean URLs!")

if __name__ == "__main__":
    generate_sitemap()

