from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urllst = []
url = input('Enter - ')
link = 0

while link < 7:
    taglst = []
    #html = urllib.request.urlopen(url).read()
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    for i in range(8):
        for tag in tags:
            taglst.append(tag)

    url = taglst[17].get('href', None)
    urllst.append(url)

    link += 1

answer = re.findall('by_([^ ]*).html', url)
print (answer[0])
