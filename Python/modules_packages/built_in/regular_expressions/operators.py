import re

# OR operator (|) - used when searching for multiple terms
text = "My phone number is 408-555-1234"
pattern = r'phone|is'
phone = re.search(pattern, text)
print(phone.group())

# Wildcard operator (.) - used to denote any value
text = "The cat in the hat sat there"
pattern = r'.at'
matches = re.findall(pattern, text)
print(matches)

# Starts with (^) - Indicates what the pattern starts with. Only searchs for if the entire text begins with that pattern
text = "1This is an example string"
pattern = r'^\d'
matches = re.findall(pattern, text)
print(matches)

# Ends with ($) - Indicates what the pattern ends with. Only searchs for if the entire text ends with that pattern
text = "This is an example string2"
pattern = r'\d$'
matches = re.findall(pattern, text)
print(matches)

# Exclusion operator (^ When used in conjunction with a set of brackets) - Used to exclude pattern types
# Example - this returns every character that isn't a number
    # Can use the + operator to put the sentence back together
text = "There are 3 numbers in 45 this 23 entire sentence 67"
pattern = r'[^\d]'
matches = re.findall(pattern, text)
print(matches)

# This is a common way to remove punctuation from a sentence, to 'clean' the text data
text = "This is a string! But it has punctuation. How can we remove it?"
pattern = r'[^!.? ]+'
matches = re.findall(pattern, text)
clean = ' '.join(matches)
print(clean)

# Inclusion ([]) - Used to group patterns
# They indicate a group, for easy code readability
text = "Only find the hyphen-words in this sentence. But you don't know how long-ish they are."
pattern = r'[\w]+-[\w]+'
matches = re.findall(pattern, text)
print(matches)

# Options (()) - Used for multiple options for matching
    # For example if you want to find a group of words with the same prefix
text = "Hey, would you like some catfish?"
text2 = "Hey, would you like to take a catnap?"
text3 = "Hey, would you like this caterpillar"
pattern = r'cat(fish|nap|pillar)'
matches = re.search(pattern, text)
print(matches)

