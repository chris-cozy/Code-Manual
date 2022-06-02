#When you create a variable name in Python it is stored in the 'namespace' and it has a scope. 
# The scope determines the visibility of that variable name in other parts of your code.
#LEGB rule format.
    #L - Local: Names assigned in any way within a function (def or lambda), and not declared global in that function
    #E - Enclosing function local: Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer
    #G - Global(module): Names assigned at the top-level of a module file, or declared global in a def within the file
    #B - Built-in(Python): Names preassigned in the built-in names module: open, range, SyntaxError, etc

#By declaring a variable using the global keyword inside a function, 
# you expand its scope globally and allow changes that happen to it within that function to be retained.
x = 0
def add():
    global x
    x = x + 2

add()
print(x)

#Because of the power of the global keyword, you should avoid using it unless necessary. 
# Instead, you should take in the global variable as a parameter, do the reassignment, and return the reassignment as an object.
#This method is much cleaner and safer. A lot easier to debug because there is a clear reassignment.

x = 0
def sub(x):
    x = x - 2
    return x

x = sub(x)

