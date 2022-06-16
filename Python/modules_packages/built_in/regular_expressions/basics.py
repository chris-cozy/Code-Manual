# Regular expressions (regex) allow us to search for general patterns structures in text data.
# For example, if you are looking for an email address but don't know the exact email, you can look for the pattern: 
    # 'text' + '@' + 'text' + '.com'. 
# You can use regex to construct a generalized pattern string to search for text information in that format
# To understand regex, you must understand the special syntax for these pattern strings
# The regular expression library is called 're'
import re

# Searching for patterns within text
    # Search (pattern, text to search through) - this function searches through the text to find the specified pattern
    # It returns a match object, with the strating and ending index of the match
    # Will return None if there is no match
# If there are multiple instances of the match it will only return the first 
text = "The special agent's contact number is 505-457-6078"
pattern = 'contact'
match = re.search(pattern, text)

# There are methods available to match objects
    # Span - return indeces of the match
    # Start - return starting index
    # End - return ending index
    # Group - returns the matched string
match.span()
match.start()
match.end()
match.group()

# Findall (pattern, text to search through) - this returns all matches of the pattern
    # Returns a list of the matched strings
text = "The special agent's contact number is 505-457-6078. contact him immediately before it is too late to contact"
matches = re.findall(pattern, text)

# Finditer (pattern, text to search through) - this is used to iterate through individual match objects when there are multiple matches
    # Returns a match object for each instance
for match in re.finditer(pattern, text):
    print(match)