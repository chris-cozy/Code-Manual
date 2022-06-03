#To define an object, use the class keyword. It's common practice to make the first letter of a class uppercase (camel case)
#The __init__ method allows you to create an instance of the object. It is called whenever you created an instance.
#__init__ is essentially a constructor.
    #'self' represents the instance of the object itself.
    # It is used before variables so that python understands you are referring to the variable that
    #is in the current instance, and not a global variable 
#Methods are functions in the objects
    #We also pass 'self' in the methods to connect them to the class
#An attribute is a characteristic of an object, they are variables.
    #The attributes don't need to have the same name as the parameters, but it is cleaner this way
    #Class Object Attributes, defined at the class/object level, are the same for every instance
    #Because of this, they don't need the 'self' keyword
        #You can also reference class level attribute like:
        #ClassName.attribute
class NameOfClass():

    species = 'human'
    
    def __init__(self, param1, param2 = 'Default'):
        self.param1 = param1
        self.param2 = param2
        self.random_attribute = 'this id s random attribute'

    def random_method(self):
        print("I'm a random {}, my species is {}".format(self.param1, self.species))
        print("My species is {}".format(NameOfClass.species))

#When creating an instance you must fill its initializing parameters, defined in __init__
#You can enter the parameters like a dictionary
test_obj = NameOfClass(param1 = 'test1', param2 = 'test2')
test_obj.random_method()