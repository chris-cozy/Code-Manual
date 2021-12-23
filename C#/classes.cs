using System;

/*
Classes are similar to data types, but much more expansive and versatile
They can provide properties and methods
They are more similar to structs, but still more expansive

To create a new class in VS2019, right click on your project in the right hand window
    -> Add -> new item -> class

INSTANCES
    To make an instance of a class, use the syntax
        *class name* *instance name* = new *class name*(*include any needed args here*);
    This creates an object. A class is a set of instructions on how data is stored, like a blueprint.
    An object is what is created based on those instructions. Like a house built off of the blueprint.
    You can create multiple objects based off of a class.
*/
namespace practice
{
    class Person
    {
        /*
        CLASS VARIABLES
        Variables that are part of a class are called fields
        My default, fields are made private and unaccessible outside a member of the class itself
        We can change that by using the public keyword
            - Then the variables can be adjusted and displayed by anything
        In most cases you'll want fields to be private
        */
        public string name = "NULL";
        public int weight = 150;

        //Using static fields means it belongs to the class itself rather than the object
        //It cannot be changed, and must be accessed from the class itself
        //  -Person.species
        //A useful use of the static field is a counter that counts the number of objects made from that class
        public static string species = "Human";
        public static int personCount = 0;

        /*
        CONSTRUCTORS
        Classes are called like methods to create objects, this is their constructor
        Classes have constructors with no params by default, but we can define our own
        Generally placed at the start of the class body

        What we place in the constructor will be run for each object
        The parameters must be satisfied when creating a new object
        Unless we have mulitple constructors
            This is called overloading
            Can be done for any method, not just constructors

        When we call the constuctor to create an object, what parameters were entered will be checked,
        and the appropriate constructor will be used
        */
        public Person(string new_Name, int new_Weight){
            name = new_Name;
            weight = new_Weight;
            personCount++;
        }

        public Person(string new_Name){
            name = new_Name;
            personCount++;
        }
        

        /*
        METHODS
        Similar to functions in C
        Can have class-specific methods
        Use the return statement to return values;

        Every time we call this method on an object, that specific object's weight field will increase
        */
        public void Eat(int val){
            weight += val;
        }

        public char FirstInitial(){
            return name[0];
        }
  
    }
}