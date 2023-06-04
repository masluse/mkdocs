import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

def generate_sitemap(base_url, output_file='site/sitemap.xml'):
    with open(output_file, 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        
        for root, dirs, files in os.walk('site'):
            for file in files:
                if file.endswith('.html'):
                    filepath = os.path.join(root, file)
                    url_path = filepath.replace('site', '')
                    url = urljoin(base_url, url_path)
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text, 'html.parser')
                    lastmod = soup.time['datetime'] if soup.time else ''

                    f.write('<url>\n')
                    f.write('<loc>{}</loc>\n'.format(url))
                    if lastmod:
                        f.write('<lastmod>{}</lastmod>\n'.format(lastmod))
                    f.write('</url>\n')

        f.write('</urlset>\n')

# Update with your base url
generate_sitemap('https://mkdocs.mregli.com')
