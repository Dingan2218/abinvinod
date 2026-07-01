import os
import re

GA4_SCRIPT = """<!-- Google Analytics (GA4) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-Y586J4M1L8"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    def gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-Y586J4M1L8');
  </script>"""

def clean_file(filepath):
    print(f"Cleaning: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject GA4 script if not present
    if 'gtag' not in content:
        # Find </head> and insert GA4 script right before it
        if '</head>' in content:
            content = content.replace('</head>', f'  {GA4_SCRIPT}\n</head>')
        else:
            print(f"WARNING: </head> tag not found in {filepath}")

    # 2. Clean links: replace href="... .html" with clean urls
    # E.g., href="something.html" -> href="something"
    # Negative lookahead/behind to avoid replacing non-local/non-html stuff
    # Pattern matches href="some-page.html" or href="../blog/page.html"
    def link_replacer(match):
        link = match.group(1)
        # Skip external/anchor/js/email links
        if link.startswith(('http://', 'https://', '#', 'mailto:', 'tel:', 'javascript:')):
            return match.group(0)
        # Replace index.html with appropriate home path
        if link == 'index.html' or link == '/index.html':
            return 'href="/"'
        if link.endswith('.html'):
            clean_link = link[:-5]  # Strip .html
            return f'href="{clean_link}"'
        return match.group(0)

    content = re.sub(r'href="([^"]+)"', link_replacer, content)

    # Clean any trailing slashes in specific relative nav-links if they exist
    # E.g. href="blog/" -> href="blog"
    content = re.sub(r'href="blog/"', 'href="blog"', content)
    content = re.sub(r'href="/blog/"', 'href="/blog"', content)

    # 3. Add width & height to the main project image if this is index.html
    if os.path.basename(filepath) == 'index.html' and filepath.count('/') == 0 and filepath.count('\\') == 0:
        content = re.sub(
            r'<img src="assets/project1.png"\s+alt="([^"]+)"\s+class="project-image"\s+loading="lazy">',
            r'<img src="assets/project1.png" alt="\1" class="project-image" loading="lazy" width="800" height="500">',
            content
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    # Clean root files
    root_files = ['index.html', '404.html']
    for rf in root_files:
        if os.path.exists(rf):
            clean_file(rf)
            
    # Clean blog files
    blog_dir = 'blog'
    if os.path.exists(blog_dir):
        for f in os.listdir(blog_dir):
            if f.endswith('.html'):
                clean_file(os.path.join(blog_dir, f))

if __name__ == '__main__':
    main()
