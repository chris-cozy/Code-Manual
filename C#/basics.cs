//The basic layout of a C# file
using System;

namespace practice
{
    class basics
    {
        static void Main(string[] args)
        {
            //Methods are functions. For example, this is 
            //a method implemented somewhere in the C# codebase 
            //that outputs to the terminal
            Console.Writeline("Hello World");
            //another example:
            int num = -150;
            int absnum  = Math.Abs(num);
            Console.WriteLine(absnum);
        }
    }
}