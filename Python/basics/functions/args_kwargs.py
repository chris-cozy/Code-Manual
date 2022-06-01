# ARGS
    # *args - arguments; *kwargs - key word arguments
    # *args allows a function to take in an arbitrary number of arguments
        # puts the parameters into a tuple-based format
def myfunc1(*args):
    return sum(args)

    # *args can be any other word (the 'args' is arbitrary)
def myfunc2(*spam):
    return sum(spam)

#KWARGS
    # **kwargs is used for key words, it creates a dictionary of key-value pairs
    # Similar usage to args
    # It will return back a dictinary, similar to how args returns a tuple
    # format - def myfunc(fruits = 'apple', veggie = 'lettuce')
def myfunc3(**kwargs):
    print(kwargs)

# You can use both *args and **kwargs in the same function
    # def myfunc(*args, **kwargs)
    # The order must stay consistent to what was defined in the base parameter:
        # (*args, **kwargs) -> (10, 20, food = 'grape')
def myfunc4(*args, **kwargs):
    total = sum(args)
    print(total + ' ' + kwargs)

myfunc4(10, 20, food = 'grape')

