#You can set a variable equal to a function, then call it later.
#The variable will be a pointer to the function object.
def hello():
    return "hello"

greet = hello

greet()