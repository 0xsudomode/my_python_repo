# Regular Expressions in Python (`re` Module)

The `re` module in Python is a powerful tool for performing pattern matching and text processing using regular expressions. Below is a comprehensive guide and examples to help you use it effectively.

---

## **Basics of the `re` Module**

The `re` module provides various methods for searching, replacing, and manipulating text using patterns:

### **Common Functions**

| Function               | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `re.match()`           | Matches a pattern at the beginning of a string.                            |
| `re.search()`          | Searches for a pattern anywhere in the string.                             |
| `re.findall()`         | Returns a list of all matches of a pattern in the string.                  |
| `re.finditer()`        | Returns an iterator yielding match objects for all matches in the string.  |
| `re.sub()`             | Replaces matches with a replacement string.                               |
| `re.split()`           | Splits a string based on a pattern.                                        |

---

## **Special Characters in Regular Expressions**

| Character | Description                                              |
|-----------|----------------------------------------------------------|
| `.`       | Matches any character except a newline.                  |
| `^`       | Matches the start of a string or line.                   |
| `$`       | Matches the end of a string or line.                     |
| `*`       | Matches 0 or more repetitions of the preceding character.|
| `+`       | Matches 1 or more repetitions of the preceding character.|
| `?`       | Matches 0 or 1 repetition of the preceding character.    |
| `{n}`     | Matches exactly `n` repetitions.                         |
| `{n,}`    | Matches `n` or more repetitions.                         |
| `{n,m}`   | Matches between `n` and `m` repetitions.                 |
| `[]`      | Matches any character inside the brackets.               |
| `|`       | Acts as an OR operator (e.g., `cat|dog`).                |
| `()`      | Groups expressions and captures matched text.            |
| `\\`     | Escapes special characters (e.g., `\\.` matches a literal dot). |

---

## **Character Classes and Escapes**

| Pattern    | Description                                               |
|------------|-----------------------------------------------------------|
| `\w`      | Matches any word character (alphanumeric + underscore).   |
| `\W`      | Matches any non-word character.                           |
| `\d`      | Matches any digit.                                        |
| `\D`      | Matches any non-digit character.                          |
| `\s`      | Matches any whitespace character.                         |
| `\S`      | Matches any non-whitespace character.                     |
| `\b`      | Matches a word boundary.                                  |
| `\B`      | Matches a non-word boundary.                              |

---

## **Examples**

### **Basic Matching**

```python
import re

text = "The price is $5.00."
match = re.search(r'\$\d+\.\d+', text)  # Match a price pattern
if match:
    print(match.group())  # Output: $5.00
```

### **Finding All Matches**

```python
text = "I have 2 cats, 3 dogs, and 5 birds."
matches = re.findall(r'\d+', text)  # Find all numbers
print(matches)  # Output: ['2', '3', '5']
```

### **Replacing Text**

```python
text = "My phone number is 123-456-7890."
result = re.sub(r'\d', 'X', text)  # Replace all digits with 'X'
print(result)  # Output: My phone number is XXX-XXX-XXXX.
```

### **Splitting Text**

```python
text = "apple, orange; banana|grape"
result = re.split(r'[;|,]', text)  # Split on semicolons, pipes, or commas
print(result)  # Output: ['apple', ' orange', ' banana', 'grape']
```

---

## **Lookahead and Lookbehind Assertions**

| Type                     | Description                                      |
|--------------------------|--------------------------------------------------|
| **Lookahead** (`?=...`)  | Matches a pattern only if it's followed by another pattern. |
| **Negative Lookahead** (`?!...`) | Matches a pattern only if it's NOT followed by another pattern. |
| **Lookbehind** (`?<=...`) | Matches a pattern only if it's preceded by another pattern. |
| **Negative Lookbehind** (`?<!...`) | Matches a pattern only if it's NOT preceded by another pattern. |

### **Examples**

```python
# Lookahead
text = "Python2, Python3, and Python"
print(re.findall(r'Python(?=3)', text))  # ['Python']

# Negative Lookahead
print(re.findall(r'Python(?!3)', text))  # ['Python2', 'Python']

# Lookbehind
text = "ID:123, Code:456, ID:789"
print(re.findall(r'(?<=ID:)\d+', text))  # ['123', '789']

# Negative Lookbehind
print(re.findall(r'(?<!ID:)\d+', text))  # ['456']
```

---

## **Flags in the `re` Module**

| Flag                 | Description                                             |
|----------------------|---------------------------------------------------------|
| `re.IGNORECASE` (`re.I`) | Makes the match case-insensitive.                      |
| `re.MULTILINE` (`re.M`)  | Allows `^` and `$` to match at the start and end of each line. |
| `re.DOTALL` (`re.S`)     | Makes the `.` special character match newlines as well. |
| `re.VERBOSE` (`re.X`)    | Allows you to write regular expressions with comments and whitespace for better readability. |

### **Examples**

```python
# Case-insensitive match
text = "Python is FUN"
print(re.findall(r'fun', text, re.IGNORECASE))  # ['FUN']

# Multiline match
text = "First Line\nSecond Line"
print(re.findall(r'^Second', text, re.MULTILINE))  # ['Second']

# Dotall match
text = "First Line\nSecond Line"
print(re.findall(r'First.*Second', text, re.DOTALL))  # ['First Line\nSecond']
```

---

## **Greedy vs. Non-Greedy Matching**

- **Greedy**: Quantifiers like `*` and `+` match as much as possible.
- **Non-Greedy**: Add `?` to make the quantifier match as little as possible.

### **Examples**

```python
text = "<tag>content</tag>"

# Greedy match
print(re.findall(r'<.*>', text))  # ['<tag>content</tag>']

# Non-greedy match
print(re.findall(r'<.*?>', text))  # ['<tag>', '</tag>']
```

---

## **Tips and Best Practices**

1. **Escape Special Characters**:
   Use `\\` to match special characters like `.`, `*`, or `?`.
   ```python
   text = "Price is $5.00"
   print(re.findall(r'\\$', text))  # ['$']
   ```

2. **Use Raw Strings**:
   Always use raw strings (`r'...'`) for regular expressions to avoid issues with escape sequences in Python.

3. **Test Patterns**:
   Use tools like [regex101](https://regex101.com/) or [Pythex](https://pythex.org/) to debug and visualize matches.

---

## **Summary**

The `re` module is a versatile tool for text processing, offering a wide range of features like pattern matching, replacements, splitting, and advanced assertions (lookahead/lookbehind). Understanding these features can help you tackle complex text-processing tasks efficiently.

Let me know if you need further clarification or examples!

