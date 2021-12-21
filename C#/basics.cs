//The basic layout of a C# file
//Comments are formatted the same as in C
/*
    Namespaces are the same as #include statements in C
    - For example, "using System;"
    - This namespace contains the random class
*/
using System;

namespace practice
{
    class basics
    {
        static void Main(string[] args)
        {
             /*
            Methods are functions. 
            For example, Constant.Writeline 
             is a method implemented somewhere in the C# codebase 
            that outputs to the terminal
            Math.Abs is another example.
            */
            Console.Writeline("Hello World");

            //using the keyword const makes a variable a constant
            const int num = -150;
            int absnum  = Math.Abs(num);
            Console.WriteLine(absnum);

            /*
            ARRAYS - same as C
            except the new keyword is needed because C# is an OOP language
            This array can hold 5 ints
            When you create a new int array, the positions are initialized to 0
            */
            int[] numArray = new int[5];
            numArray[0] = 8;
            numArray[1] = 16;
            Console.WriteLine(numArray[1]);

            int[] num2Array = {0,1,2,3,4,5};

            /*
            LOOPS - same as C
            */
            //While
            int whileEx = 0;
            while(whileEx < 10)
            {
                whileEx++;
            }

            int forEx = 10;
            for(int i = 0; i < 10; i++)
            {
                forEx--;
            }
           
        }
    }
}