//---DESCRIPTION---//
/*
A toString() is an in-built method in Java that returns the value given to it in string format. 
Hence, any object that this method is applied on, will then be returned as a string object.

If you print any object, Java compiler internally invokes the toString() method on the object. 
So overriding the toString() method, returns the desired output, 
it can be the state of an object etc. depending on your implementation.

By overriding the toString() method of the Object class, we can return values of the object, so we don't need to write much code.

Without overriding the toString() function, trying to print an object will return its hashcode values.

*/

//---EXAMPLE---//
class Student{  
    int rollno;  
    String name;  
    String city;  
     
    Student(int rollno, String name, String city){  
    this.rollno=rollno;  
    this.name=name;  
    this.city=city;  
    }  
    
    @Override
    public String toString(){//overriding the toString() method  
     return rollno+" "+name+" "+city;  
    }  
    public static void main(String args[]){  
      Student s1=new Student(101,"Raj","lucknow");  
      Student s2=new Student(102,"Vijay","ghaziabad");  
        
      System.out.println(s1);//compiler writes here s1.toString()  
      System.out.println(s2);//compiler writes here s2.toString()  
    }  
   }  

   //---OUTPUT---//
   // 101 Raj lucknow
   // 102 Vijay ghazibad
