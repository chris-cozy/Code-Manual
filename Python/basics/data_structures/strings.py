# Strings use either single or double quotes
test_0 = 'example string'
test_1 = 'Example string'
test_2 = "Example 'String'"

# String indexing begins at 0
letter_0 = test_1[0]

# String slicing [start:stop:step], step is size of the jumps you take from start to stop. the stop index is not inclusive
slice_1 = test_1[0::2]

# Quick way to reverse a string
test_reverse = test_1[::-1]

# Built-in string functions for upper and lower case. Have to reassign if want to use the return
# capitalize() - capitalizes the first letter of the first word
test_1.upper()
test_2.lower()
test_0.capitalize()


# Built-in string function for splitting string into a list based on a character. Reassign if you want to use return
    # Returns a list
    # Can be formatted in either of these ways
# partition(x) - Searches for substring y, and returns the part before and after, as well as the substring
    # (head, sep, tail)
    # Only separates at the first instance
' '.split(test_1)
test_1.split(' ')
test_1.partition(' ')

# Built in string function for joining strings together with a connector string
# Useful for turning words into a sentence
'--'.join(['a','b','c'])

#Strings are immutable and don't allow item assignment
#Two methods of inserting a variable into string: f-strings, and .format()
name = 'Chris'
print(f'Hello, my name is {name}')

print('This is a {} string'.format('test'))

# Another example of format()
index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1

#String concatenation is easy
test_3 = 'Hello'
test_4 = 'World'
test_5 = test_3 + test_4

# You can count the number of a certain substring
# count(x) - Counts the number of substring x
# find(x) - Returns the index of substring x
# endswith(x) - Checks if string ends with the substring
test_6 = 'This string contains multiple i'
test_6.count('i')
test_6.endswith('i')

# isalnum() - Checks if all characters in the string are alphanumeric
# isalpha() - Checks if all characters in the string are alphabetic
test_6.isalnum()
test_6.isalpha()

# islower() - Checks if all of the chars are lowercase
# isupper() - Checks if all chars are uppercase
# isspace() - Checks of all of the characters are whitespace
# istitle() - Returns true if the string is a title-case strings
