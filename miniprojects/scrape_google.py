#!/usr/bin/python3


# a basic script to showcase google scraping (first page only)
# feel free to modify it and extend it's functionality

import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) == 1:
	print(f'usage : python {sys.argv[0]} "query"')
	sys.exit()

url = f"https://www.google.com/search?q={sys.argv[1]}"

# to avoid bot-like behaviour
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

resp = requests.get(url,headers=headers)

soup = BeautifulSoup(resp.text,'lxml')

# jsname attribute added to identify g00gle's stuff
links = soup.find_all('a', href=True, jsname="UWckNb")

for link in links:
	print(link['href'])
