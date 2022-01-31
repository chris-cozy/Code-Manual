
x = 5
y = 10

#IF-STATEMENT
    #you can have as many elifs as you want
    #Control flow syntax makes use of colons and indentations (whitespace)
if x < y:
    print(x)
    x = x + 1
elif y < x:
    print(y)
    y = y - 1
else:
    print(x + y)




#FOR-LOOP
    #For loops allow for iterables (cycling through each letter in a string, 
    #going through each variable in a list, etc.)
my_iterable = [1,2,3]
for item_name in my_iterable:
    print('Hello')

    #Common syntax if you don't intend to use the variable name is to replace it with an _ instead.
for _ in 'Hello World':
    print('Cool')



#WHILE_LOOP
while x < y:
    print('Oh no!')

#another version
while x < y:
    print('Oh no!')
else:
    print('Oh yes!')



#KEYWORDS
    #break - Breaks out of the current enclosing loop
    #continue - Goes to the top of the closest enclosing loop
    #pass - Does nothing at all



#USEFUL OPERATORS
    #To check the parameters of a built-in function, use Shift + Tab

    #range() - a generator that measures a range of values 
    # or creates a range of values based on (start, end, skip) values

    #enumerate() - takes an innumerable object and returns an index counter 
    # then the element at that iteration

    #zip() - zips together lists. 
    # If you just apply it (zip(list1, list2) it will return the location in memory where the zip is located. 
    # If you iterate through it (for item in zip(list1, list2) it will return a tuple with the zipped lists. 
    # You can cast the zip as a list to see the pairings as well.

    #in (operator) - can use it to quickly check if an object is in a list, string, dict, tuple, etc.

    #random - a built-in library in python.

    #input() - Displays text then asks user for input. Typically saved under a variable for later callback. 
    # Anything passed into it by the user is taken as a string. 
    # Have to cast as int or float if you want the return variable as one of those types.

    #min()
    #max()

#LIST COMPREHENSIONS 
    # A unique way of quickly creating a list in Python
ex_list = [element for element in "string"]
    # You can even perform operations on the first variable name
mylist = [num**2 for num in range(0,11)]
    # You can also add if-statements
mylist = [x for x in range(0,11) if x%2 == 0]