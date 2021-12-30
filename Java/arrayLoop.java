/*
    Java has additional type of loop  that can be helpful for arrays
	- Two parts
		○ Declaration
			§ Declare new variable that will only be used in this loop, with the same data type as the items in the array to be looped through
		○ Expression
			§ Evaluates as an array. It can be an array, or a function call that returns an array
		○ Syntax for (<Declaration of variable> : <Expression/array>){}
			§ It is helpful to think of it as "foreach variable in array"
*/
class Basic{
    public static void main(String args[]){
        Integer numbers[] = {10,20,30,40,50,60,70,80,90,100};

        //prints out every number in the array
        For(Integer x : numbers){
            System.out.println(x);
        }
    }
}