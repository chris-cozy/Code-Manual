using System;

namespace practiceCode
{
    class Cat
    {
        //private fields
        private string name;
        private int age;

        public Cat(string newName, int newAge)
        {
            name = newName;
            age = newAge;
        }

        //getter
        public string getName(){
            return name;
        }

        //setter
        public void setName(string newName){
            name = newName;
        }

        //Property
        public int Age {
            get { return age;}
            set { age = value; }
        }

    }
}
