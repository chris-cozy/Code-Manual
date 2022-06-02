#To define an object, use the class keyword. It's common practice to make the first letter of a class uppercase (camel case)
#The __init__ method allows you to create an instance of the object. It is called whenever you created an instance.
#__init__ is essentially a constructor.
    #'self' represents the instance of the object itself.
    # It is used before variables so that python understands you are referring to the variable that
    #is in the current instance, and not a global variable 
#We also pass 'self' in the methods to connect them to the class
#The attributes don't need to have the same name as the parameters, but it is cleaner this way
class NameOfClass():

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def random_method(self):
        print("I'm random")

#An attribute is a characteristic of an object, they are variables.
#When creating an instance you must fill its initializing parameters, defined in __init__
#You can enter the parameters like a dictionary
test_obj = NameOfClass(param1 = 'test1', param2 = 'test2')
test_obj.random_method()