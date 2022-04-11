//--DESCRIPTION--//
/*
Default methods are implicitly public, and declared with the default keyword at the beginning of the method signature
They also provide and implementation.
Interfaces can have multiple implementations, and default methods allow us to add new methods to an interface that
are automatically available in all of the implementations.
This preserves backwards compatability without refactoring

When you write an implementing class, then declare an instance of that class somewhere, the default methods are
readily available.

The most common use of interface default methods is to incrementally provide additional functionality to a given type without
breaking the implementing classes.
We can also use them to provide additioal functionality around an existing abstract method.

If a class implements several interfaces that define the same default methods, the code will not compile due to the conflict.
To fix this:
    Explicitly provide an implementation for the conflicting method(s) by using @Override
    You can also have the class use the default methods of one of the interfaces, by returning like:
        return  Vehicle(chosen interface).super.turnAlarmOn();


you can also define static methods within an interface. To call them by the implementing classes, the interface must be referenced
preceeding the method name, like:
    MyInterface.staticMethod();

The idea behind static interface methods is to provide a simple mechanism that allows us to increase 
the degree of cohesion of a design by putting together related methods in one single place without having to create an object.
The same can pretty much be done with abstract classes. 
The main difference is that abstract classes can have constructors, state, and behavior.
Furthermore, static methods in interfaces make it possible to group related utility methods, without 
having to create artificial utility classes that are simply placeholders for static methods.
*/

//--EXAMPLE--//
public interface MyInterface{
    //regular interface methods

    default String defaultMethod(){
        return "this is a default method for all implementations";
    }

    static int staticMethod(){
        return 0;
    }
}