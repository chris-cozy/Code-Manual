#The def keyword is needed to create a function in python
    # def name_of_function()
    # '''
    # Docstring explains function (optional)
    # '''
    # code to be executed
#To call the function:
    # >>name_of_function()
def name_of_function(name):
    print("Hello" + name)

name_of_function("Jose")

#With functions, generally use 'return' rather than 'print'
#Example
def add(num1, num2):
    '''
    Adds two numbers and returns the value
    '''
    return num1 + num2

result  = add(3,7)

#Example
def even_list(num_list):
    '''
    Returns true if any number inside a list is even
    '''
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers


# You can set a variable equal to an initial value when creating a function to 
# include a default if no parameters are stated when there should be one
def say_hello(name = "Default"):
    print(name)
