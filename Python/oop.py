#when creating classes, it's common practice to make the first letter uppercase
class NameOfClass():

    #When creating an instance of this object you must fill these parameters
    #Self is used so that python understands you are referring to the variable that
    #is in the current instance of the class, and not a global variable 
    def _init_(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    #We use 'self' to connect these methods to the class
    def random_method(self):
        print("I'm random")