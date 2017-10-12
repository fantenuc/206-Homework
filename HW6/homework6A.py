from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl

f = open('actualdata.html', 'r')
html_doc = f.read()
f.close()

number_count = []
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

soup = BeautifulSoup(html_doc, 'html.parser')
for tag in soup.find_all('span'):
    tag = str(tag)
    new_tag = tag.split('>')[1]
    tag2 = new_tag.split('<')
    number_count.append(int(tag2[0]))

print('Sum: ', sum(number_count))