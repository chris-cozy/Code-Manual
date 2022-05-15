// We are logging this message on the console
console.log('Hello World');

//---VARIABLES---//
//Use the 'let' keyword to declare a variable
let name;
name = 'Chris';
console.log(name);
//Variabes cant be a reserved keyword
//Should have meaningful names
//Cannot start with a number

//You can declare multiple variables on one line, but best practice is to separate

//---CONSTANTS---//
//Value cannot be reasssigned
const interestRate = 0.3;
//Constant should be the default choice if you don't need to redefine

//---PRIMITIVE TYPES---//
/*
    Strings
    Number - all numbers are of this type, including floats
    Boolean
    undefined - uninitialized declared types are this by default. A type and value
    null - used in situations where you want to clear a variable's value. type = object
*/
let name2 = 'Chris'; //String
let age = 30; //Number
let isApproved = false; //Boolean
let firstName = undefined;
let selectedColor = null;

//---DYNAMIC TYPING---//
//JS is a dynamic language like Python, meaning the variable type can change at runtime
console.log(typeof name2);
//Changing name2 from a string to a number
name2  = 2;
console.log(typeof name2);

//---REFERENCE TYPES---//
/* 
    Object
    Arrays
    Function
*/

//---OBJECTS---//
//The brackets are called an object literal
//Can enter 'key: value' pairs for properties
let person = {
    name: 'Cozy',
    age: 21
};
console.log(person);

//Accessing a property
    //Dot notation - more concise
    person.name = "Kurse";

    //Bracket notation - useful when the user is selecting the property, for changes at runtime
    //Allows for dynamic accessing
    person['name'] = 'Frogboy';

console.log(person.name);

//---ARRAYS---//
//Square brackets called the array literal
let selectedColors = ['red', 'blue'];
console.log(selectedColors);
console.log(selectedColors[1]);
//The length of arrays and the object types stored within are also dynamic
selectedColors[2] = 1;
console.log(selectedColors);
//Technically an array is an object
//The dot notation can be used to view the properties of the array


//---FUNCTIONS---//
function greet(){
    console.log('Hello World');
}

greet();

//Define a parameter
function personalGreet(name){
    console.log('Hello ' + name);
}
//En ter the argument when calling
personalGreet('Kirsten');
//If you don't pass in a value for a parameter, it will be undefined
personalGreet();

//---FUNCTION TYPES---//
//Performing a task
greet();

//Calculating a value, etc
//Use the return keyword to return a value
function square(number) {
    return number * number;
}

let newNum = square(2);
console.log(square(5));