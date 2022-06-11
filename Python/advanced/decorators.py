# Decorators allow you to add extra functionality to an existing function
# Commonly used in web frameworks such as Jango or Flask
#To break down decorators, here is an example of passing in a function as an argument.
def hello():
    return 'Hello World!'

def func(another_func):
    print('Other code runs here')
    print(another_func())


#Decorator Example
#This takes in a function, wraps it with extra code, then returns the wrapped function
def decorator(func):
    def wrapper():
        print('This is wrapper code')
        func()
        print('More wrapper code')
    
    return wrapper

#Decorators use a special syntax '@' to simplify the creation process
#By using the name of the decorator function with this syntax, you automatically pass the
#original function into it. Now you can call the original function and it will be decorated.
@decorator
def test_func():
    print('I want to be ravaged and decorated!')

test_func()