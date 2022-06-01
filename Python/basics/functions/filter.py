#The filter function also takes in a function and an iterable. 
# The difference is the function must return True or False. 
# The filter function applied the function to the iterables and returns the ones that are True. 
# Like map, filter will return a memory location, so you must use the list function or iterate through with a for loop.
def checkEven(num):
    return num%2 == 0

mynums = [1,2,3,4,5,6]
list(filter(checkEven, mynums))

#Another example
list(filter(lambda num:num%2 == 0, mynums))