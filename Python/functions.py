#To view what methods are available for an object, use: objectname.(Press Tab)
#You can also use: help(Method Call)

#The 'def' keyword is needed to create a function in Python
    # def name_of_function()
    # '''
    # Docstring explains function (optional)
    # '''
    # code to be executed

#To call the function:
    #>>name_of_function()

def name_of_function(name):
    print("Hello" + name)

name_of_function("Jose")

#With functions, generally use return rather than print

def add(num1, num2):
    return num1 + num2

result  = add(3,7)
print(result)

# You can set a variable equal to an initial value when creating a function to include a default if no parameters are stated when there should be one

def say_hello(name = "Default"):
    print(name)

# ARGS
    # *args - arguments; *kwargs - key word arguments
    # *args allows a function to take in an arbitrary number of arguments
        # puts the parameters into a tuple-based format

def myfunc(*args):
    return sum(args)

    # *args can be any other word (the 'args' is arbitrary)

def myotherfunc(*spam):
    return sum(spam)

#KWARGS
    # **kwargs is used for key words, it creates a dictionary of key-value pairs
    # Similar usage to args
    # It will return back a dictinary, similar to how args returns a tuple
    # format - def myfunc(fruits = 'apple', veggie = 'lettuce')

# You can use both *args and **kwargs in the same function
    # def myfunc(*args, **kwargs)
    # The order must stay consistent to what was defined in the base parameter:
        # (*args, **kwargs) -> (10, 20, food = 'grape')