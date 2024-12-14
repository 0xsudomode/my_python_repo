import re

def search_for_word(word, text):
    """Search for a specific word in the given text."""
    match = re.search(word, text)
    if match:
        print(f'[+] Result: {match.group()}')
        print(f'[+] Start index: {match.start()}')
        print(f'[+] End index: {match.end()}')
        print(f'[+] Span is a tuple: {match.span()}')
    else:
        print(f'[+] No match found for "{word}".')

def find_numbers_in_text(text):
    """Find all numbers in the given text."""
    numbers = re.findall(r'\d+', text)
    if numbers:
        print('[+] Found numbers:')
        for num in numbers:
            print(f'  {num}')
    else:
        print('[+] No numbers found.')

def find_email_in_text(text):
    """Find an email in the given text."""
    email_re = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    email_match = re.search(email_re, text)
    if email_match:
        print(f'[+] Found email: {email_match.group()}')
    else:
        print('[+] No email found.')

def find_all_except_numbers_and_emails(text):
    """Find everything except numbers and emails in the given text."""
    # Define the email and number regex patterns
    email_re = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    number_re = r'\d+'

    # Step 1: Find all non-space words
    words = re.findall(r'\S+', text)
    
    # Step 2: Filter out numbers and emails
    filtered_words = [word for word in words if not re.match(number_re, word) and not re.match(email_re, word)]
    
    if filtered_words:
        print('[+] Found everything except numbers and emails:')
        print(' '.join(filtered_words))
    else:
        print('[+] No matches found excluding numbers and emails.')

def main():
    greeting = 'hello world , test@gmail.com just a simple example of using regular expression module.\n regex these numbers 1333 56 45 2322'
    print(greeting)
    # Search for the word "hello"
    search_for_word('hello', greeting)
    
    # Find all numbers in the text
    find_numbers_in_text(greeting)
    
    # Find email in the text
    find_email_in_text(greeting)
    
    # Find everything except numbers and emails
    find_all_except_numbers_and_emails(greeting)

if __name__ == '__main__':
    main()
