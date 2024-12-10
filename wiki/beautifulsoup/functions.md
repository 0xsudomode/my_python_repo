1. Basic Operations

BeautifulSoup(markup, parser):
- Parse the HTML or XML content (markup) and return a BeautifulSoup object.
- markup: The content to parse (can be a string or a file).
- parser: The parser to use, typically 'html.parser', 'lxml', or 'html5lib'.
2. Tag Searching

find(name, attrs, recursive, string, **kwargs):
- Find the first tag that matches the given criteria.
- name: The name of the tag to search for (e.g., 'div', 'a').
- attrs: A dictionary of attributes to filter by (e.g., {'class': 'link'}).
- string: A string or regular expression to match inside the tag.
- Returns the first matching tag or None if no match is found.

find_all(name, attrs, recursive, string, limit, **kwargs):
- Find all tags that match the given criteria.
- limit: Limits the number of results returned.
- Returns a list of all matching tags.

select(selector):
- Find tags using CSS selectors.
- selector: A string containing the CSS selector (e.g., '.class', '#id').
- Returns a list of matching tags.
3. Text and Attributes

get_text(separator='', strip=False):
- Extract all text from the tag and its descendants.
- separator: String to insert between the text parts (default is '').
- strip: If True, strips leading/trailing whitespaces from the text.

get(name, default=None):
- Retrieve the value of a tag's attribute.
- name: The attribute name (e.g., 'href', 'src').
- default: The value to return if the attribute is not found (default is None).

attrs:
- A dictionary of the tag's attributes.
- For example, tag.attrs returns a dictionary like {'class': ['some-class'], 'id': 'element-id'}.
4. Navigating the Parse Tree

parent:
- Retrieve the parent tag of the current tag.
- Returns the parent tag or None if there is no parent.

children:
- Iterates over all child tags of the current tag.
- Returns a list of child tags as a generator.

next_sibling:
- Retrieve the next sibling tag of the current tag.
- Returns the next sibling or None if there is no next sibling.

previous_sibling:
- Retrieve the previous sibling tag of the current tag.
- Returns the previous sibling or None if there is no previous sibling.
5. Tag Modifications

decompose():
- Remove the tag from the parse tree and destroy it.
- After calling this method, the tag is no longer part of the document.

extract():
- Remove the tag from the parse tree but keep it in memory.
- After calling this method, the tag is removed from the document but still accessible.

insert(position, tag):
- Insert a tag as a child of the current tag at the specified position.
- position: The index where the tag should be inserted.
- tag: The tag to insert.

replace_with(tag):
- Replace the current tag with another tag or string.
- tag: The tag or string that will replace the current tag.

unwrap():
- Remove the tag but keep its contents.
- This removes the tag while leaving its child elements in place in the document.
6. String Operations

string:
- Retrieve the string inside a tag.
- If the tag contains nested tags, string will return the concatenated text of those nested tags, or None if there’s no string inside.
7. Cloning and Copying

clone():
- Create a copy of a tag.
- The cloned tag is independent of the original and can be modified without affecting the original tag.
- This is useful when you need a duplicate of a tag to manipulate separately.

This format should provide a detailed understanding of each function, similar to how the os module functions were presented.
