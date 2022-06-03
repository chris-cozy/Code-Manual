#Polymorphism refers to the way that different object classes can share the same method name.
#Both of the classes below have a speak method
#With polymorphism you can call both object's speak method, with disregard to which class it is an instance of
class Dog():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + ' says woof!'

class Cat():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + ' says meow!'

#An example of utilizing polymorphism
niko = Dog('niko')
felix = Cat('felix')

for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))

#Another example (more common)
def pet_speak(pet):
    print(pet.speak())