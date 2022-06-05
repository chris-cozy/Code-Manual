#Lists are essentially arrays
#With python lists, the last element can also be accessed with index -1
test_list = [1,2,3,4,5]

#Built-in list functions. These have no return, they change the actual list
#sort - sorts in alphabetical or numerical order
#reverse - reverses list
test_list.sort()
test_list.reverse()

#Lists support indexing, slicing, concatenation and reassingment
#Built-in list functions.
#append adds to end of list, pop removes from end of list and returns removed item
test_list.append(6)
test_list.pop()

#List comprehensions are a unique way of creating a list in python.
#Saves space but takes same amount of computational time
#When compared to the regular for loop append method, 
# you're basically taking the action after the for loop and placing it before the for loop
#You can also perform operations of the variable

#This creates a list with the letters in the string
test_string = 'hello'
test_list = [letter for letter in test_string]

test_list2 = [x for x in 'word']

test_list3 = [x for x in range(0,11) if x%2 == 0]

celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]

test_list4 = [x if x%2 == 0 else 'ODD' for x in range(0,11)]

test_list5 = [x*y for x in [2,4,6] for y in [1,10,1000]]
