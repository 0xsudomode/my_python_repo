#!/usr/bin/python3

# using beautiful soup module

# Common Use Cases
# 1. Web scraping: Extracting data like titles, links, or text.
# 2. Data cleaning: Removing unwanted HTML tags.
# 3. Web automation: Pre-processing data for further analysis.


from bs4 import BeautifulSoup


html_doc = """
<!DOCTYPE html>
<html>
<head>
    <title>Sample Page</title>
</head>
<body>
    <h1>Main Heading</h1>
    <p class="intro">This is a sample introduction paragraph.</p>
    <p class="content">This is some sample content.</p>
    <a href="https://example.com" id="link1">Example Link</a>
</body>
</html>
"""

# parsing html

soup = BeautifulSoup(html_doc,'lxml') # lxml is a parser

# pretty print the html
print(soup.prettify())

# access elements by tags
print(soup.h1)
print(soup.title.string)

# accessing attributes
link = soup.a
print(link['href'])
print(link['id'])

# finding elements
print(soup.find('p'))
#find all elements
print(soup.find_all('p'))


# find by attribute
print(soup.find('p',class_='intro'))
print(soup.find_all('a',href=True))

# changing text
soup.h1.string = "New Heading"
print(soup.h1)  # <h1>New Heading</h1>


# adding or removing elements
new_tag = soup.new_tag('h2')
new_tag.string = "Subheading"
soup.body.append(new_tag)
print(soup.body)

# to remove a tag
soup.h1.decompose()  # Removes the h1 tag
print(soup.body)

# searching with CSS selectors

# Select by tag
print(soup.select('p'))  # Returns all <p> tags

# Select by class
print(soup.select('.intro'))  # Returns elements with class="intro"

# Select by id
print(soup.select('#link1'))  # Returns element with id="link1"

# Nested selectors
print(soup.select('body h1'))  # Returns all <h1> tags inside <body>


# extracting data
links = soup.find_all('a')
for link in links:
    print(link['href'])

# print page content without html
print(soup.get_text())
