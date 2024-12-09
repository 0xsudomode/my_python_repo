#!/usr/bin/python3

#######################################
# Tool   : Libgen parser              #
# Author : sudomode                   #
# This tool is very basic             #
# Feel free to add more functionality #
#######################################

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import textwrap

def wrap_text(text, width=50):
    return "\n".join(textwrap.wrap(text, width))

site = "http://libgen.is"

book = input('Please enter the name of the book you\'re looking for: ')
resp = requests.get(f'{site}/search.php?req={book}')


soup = BeautifulSoup(resp.content,'html.parser')
table = soup.find('table', {'class': 'c'})
rows = table.find_all('tr')[1:]


# Prepare data to be displayed
book_data = []
for row in rows:
    columns = row.find_all('td')
    title = wrap_text(columns[2].text.strip(), width=50)
    author = wrap_text(columns[1].text.strip(), width=20)
    year = columns[4].text.strip()
    link_1 = columns[9].find('a')['href'] if columns[9].find('a') else "N/A"
    link_2 = columns[10].find('a')['href'] if columns[10].find('a') else "N/A"
    download_links = f"{link_1}\n{link_2}"
    book_data.append([title, author, year,download_links])

# Use tabulate to print the table
print(tabulate(book_data, headers=["Title", "Author", "Year","Download"], tablefmt="grid"))
