#Lambda Expressions are a quick way to create anonymous functions, 
# which are one-time use functions that are unnamed
#Lambda expressions can be used for a variety of things, for example grabbing the first character of every string in a list
#You should only use lambda expression if you can still easily read it when you come back to it later.
#Syntax - lambda [var name]: [simple expression with var]
lambda num:(num % 2) == 0

#You can set a variable equal to a lambda expression and call the variable like a function
square = lambda num: num**2
square(5)

#Often times lambda will be used in conjunction with other functions such as map and filter. 
# For example, passing a lambda expression into a map or filter rather than defining a function for it.
mynums = [1,2,3,4,5,6]
list(map(lambda num:num**2, mynums))