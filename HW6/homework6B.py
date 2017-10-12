from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl

f = open('actualdatab.html', 'r')
html_doc = f.read()
f.close()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

soup = BeautifulSoup(html_doc, 'html.parser')

urls = soup.find_all('a')
url_list = []
for x in range(7):
    for url in urls:
        if url == urls[17]:
            url = url.get('href')
            new_url = urlopen(url)
            print(urls.text)
    

