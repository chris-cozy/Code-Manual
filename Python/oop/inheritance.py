#Inheritance is a way to form new classes using already-defined classes
#To allow a class to inherit methods from another class, 
# pass the base class in as an argument to the new class.
# Then call the base class's __init__ method within the new class's __init__
#You can overwrite methods in the base class simply by redefining them in tne new class
#BASE CLASS
class Animal():
    def __init__(self):
        print("Animal Created")
    
    def who_am_i(self):
        print("I am an animal")
    
    def eat(self):
        print("I am eating")

#NEW CLASS
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    
    def who_am_i(self):
        print("I am a dog")

#Now the new class can use all of the methods of the base class
my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()

