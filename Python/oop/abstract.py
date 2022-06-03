#Abstract classes are those that aren't intended to be instantiated.
#They are designed to only serve as a base class
#They can have skeleton methods that can run an error if called from the abstract class
#A derivation of polymorphism
#Abstract class
class Animal():

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

#New Classes
class Dog(Animal):

    def speak(self):
        return self.name + ' says woof'

class Cat(Animal):

    def speak(self):
        return self.name + ' says meow'

fido = Dog('fido')
isis = Cat('isis')
print(fido.speak())
print(isis.speak())

#A more realistic example of abstract class use is opening different file types, 
#using one method name