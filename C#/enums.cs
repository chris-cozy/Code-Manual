//STRUCTS and ENUMS
using System;

namespace practice
{
    /*
    Using an enum is a way to create a new datatype
    With predefined list of possible options for the data it will contain
    Enums use integers to keep track of which value is which, like indicing
    */
    enum Meal{
        Breakfast,
        Lunch,
        Dinner
    }
    class basics
    {
        static void Main(string[] args)
        {
            Meal mostImportant = Meal.Breakfast;

            if(mostImportant == Meal.Breakfast){
                Console.WriteLine("eggs and bacon");
            }
            //We can typecast the value to its int form (index)
            //Vice versa works as well
           Console.WriteLine((int)Meal.Lunch);
           Console.WriteLine((Meal)2);
        }
    }
}