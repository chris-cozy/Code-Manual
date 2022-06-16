# Character Identifiers - used as placeholders for the information you are searching for
    # \d    a digit
    # \w    alphanumeric (includes uderscores)
    # \s    white space
    # \D    non digit
    # \W    non alphanumeric
    # \S    non whitespace
# Add an 'r' in front of the pattern string to signify that it is a pattern
# This will return any phone number in this format
import re
text = "My phone number is 408-555-1234"
pattern = r'\d\d\d-\d\d\d-\d\d\d\d'
phone = re.search(pattern, text)
print(phone.group())

# You can use quantifiers to indicate repitition of the same character
# These come after the character identifier
    # +         Occurs 1 or more times
    # {3}       Occurs exactly 3 time
    # {2, 4}    Occurs 2 to 4 times
    # {3,}      Occurs 3 or more times
    # *         Occurs 0 or more times
    # ?         Occurs once or none
text = "My phone number is 408-555-1234"
pattern = r'\d{3}-\d{3}-\d{4}'
phone = re.search(pattern, text)
print(phone.group())

# You can use groups for any general task that involves grouping together regular expressions
# Compile - compiles different regular expression pattern codes
    # Insert each pattern in parenthesis
    # You can call the individual patterns later by calling group. Indexing begins at 1
# Example - finding a number and extracting the area code (first 3 digits)
text = "My phone number is 408-555-1234"
pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
phone = re.search(pattern, text)
print(phone.group(1))