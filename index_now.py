import xml.etree.ElementTree as ET
import urllib.request
import json
import ssl

def main():
    sitemap_path = "sitemap.xml"
    host = "abinvinod.in"
    key = "8f7b76722d3b4b568393c597db2a11b6"
    key_location = f"https://{host}/{key}.txt"
    
    try:
        # Parse sitemap to extract URLs
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        
        # XML namespace
        ns = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        
        urls = []
        for url_node in root.findall("ns:url", ns):
            loc_node = url_node.find("ns:loc", ns)
            if loc_node is not None:
                urls.append(loc_node.text)
                
        print(f"Parsed {len(urls)} URLs from sitemap.")
        
        if not urls:
            print("No URLs found to index.")
            return

        # Prepare request payload
        payload = {
            "host": host,
            "key": key,
            "keyLocation": key_location,
            "urlList": urls
        }
        
        data = json.dumps(payload).encode("utf-8")
        
        # Send POST request to IndexNow endpoint
        # endpoints: https://api.indexnow.org/indexnow or https://www.bing.com/indexnow
        url = "https://api.indexnow.org/indexnow"
        req = urllib.request.Request(
            url, 
            data=data, 
            headers={"Content-Type": "application/json; charset=utf-8"}
        )
        
        # Disable SSL verification issues if any on local environments
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        
        print(f"Submitting URLs to {url}...")
        with urllib.request.urlopen(req, context=ctx) as response:
            status_code = response.getcode()
            print(f"IndexNow Response Status Code: {status_code}")
            if status_code in (200, 202):
                print("URLs successfully submitted to IndexNow!")
            else:
                print(f"Failed to submit. Response code: {status_code}")
                
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
