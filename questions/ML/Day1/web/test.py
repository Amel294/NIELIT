#!/usr/bin/env python
from bs4 import BeautifulSoup
from urllib import urlopen

# if has Chinese, apply decode()
#html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
html = urlopen("http://beta.nielit.gov.in/calicut/calicut/content/research-leading-phd").read().decode('utf-16')


soup = BeautifulSoup(html, ‘html.parser’)

print(soup)
