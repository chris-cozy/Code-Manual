#Strings use either single or double quotes
test1 = 'Example string'
test2 = "Example 'String'"

#String indexing begins at 0
letter0 = test1[0]

#String slicing [start:stop:step], step is size of the jumps you take from start to stop. the stop index is not inclusive
slice1 = test1[0::2]

#Quick way to reverse a string
test1_r = test1[::-1]

#Built-in string functions for upper and lower case. Have to reassign if want to use the return
test1.upper()
test2.lower()

#Built-in string function for splitting string into a list based on a character. Reassign if you want to use return
' '.split(test1)

#Strings are immutable and don't allow item assignment
#Two methods of inserting a variable into string: f-strings, and .format()
name = 'Chris'
print(f'Hello, my name is {name}')

print('This is a {} string'.format('test'))

#Another example of format()
index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1

#String concatenation is easy
test3 = 'Hello'
test4 = 'World'
test5 = test3 + test4