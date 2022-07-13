# Lists are essentially arrays
# The last element can also be accessed with index -1.
# Lists support indexing, slicing, concatenation and reassingment
test = [1,2,3,4,5]

# Built-in list functions.
# sort() - sorts in alphabetical or numerical order. Changes list
# reverse() - reverses list. Changes list
# append(x) - adds x to end of list
# pop() -  removes from end of list, or a specified index, and returns removed item
# extend() - takes in a list, and appends it to the end of the current list
# count(x) - returns the number of times entry x occurs in a list
test.sort()
test.reverse()
test.append(6)
test.pop()
test.extend(new_list= [1,2,3])
test.count(1)

# insert(index, object) - Places the object at the index
# remove(x) - removes first occurence of value x
test.insert(3, 'test')

# List comprehensions are a unique way of creating a list in python.
# Saves space but takes same amount of computational time
# When compared to the regular for loop append method, 
# you're basically taking the action after the for loop and placing it before the for loop
# You can also perform operations of the variable
# This creates a list with the letters in the string
test_string = 'hello'
test = [letter for letter in test_string]

test_2 = [x for x in 'word']

test_3 = [x for x in range(0,11) if x%2 == 0]

celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]

test_4 = [x if x%2 == 0 else 'ODD' for x in range(0,11)]

test_5 = [x*y for x in [2,4,6] for y in [1,10,1000]]
