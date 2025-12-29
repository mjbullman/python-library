from io import BytesIO
from lxml import etree

import requests

url = 'https://google.com'
r = requests.get(url)
content = r.content

parser = etree.HTMLParser()
content = etree.parse(BytesIO(content), parser=parser)

for link in content.findall('.//a'):
    print(f'{link.get("href")} -> {link.text}')

#url = 'https://www.martinbullman.xyz'
#response = requests.get(url)
#print(response.status_code)
#print(response.text)

