<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Doc Title</title>
    </head>
    <body>
       <!--DATA TYPES-->
         <?php
            //String
            $name = "Coding is fun";
            $name = 'Coding is fun';

            //Integer
            $name = 20;

            //Float
            $name = 20.5784;

            //Boolean
            //true = 1;
            //false = 0;

            //Array
            $names = array("Kirsten","Canlas","Azarraga");
            //Inside the single quotes is where you put the desired array index
            echo $names['0'];
        ?>
        <!-- Operators: similar to C-->
        <?php
            //Arithmetic: Addtion, sub, divide, multiply, modulus are the same as C
            //Exponentiation: 2 to the power of 5
            echo 2**5
            
            //Assignment operators: same as C. =, +=, -=
        
            //Comparison Ops
            //==, !=, >, <, >=, <= the same as c. == does not check for data type
            //===, true if both variables are the same value and data type
            //!== is the false version of ===
            $x = 5;
            $y = 10;

            if($x > $y){
                echo $x." is greater than ".$y;
            }else{
                echo $y." is greater than ".$x
            }

            //Increment and Decrement ops
            $x = 10;
            //If you put the operator before it will add before the echo. If you put the operator after it will echo before the add
            echo ++$x;
            echo $x++;
            echo --$x;
            echo $x--;

            //Logical operators
            $x = 10;
            $y = 20;
            //Can use 'or' or ||, the same as in c
            if($x == $y or 1 == 1){
                echo "True";
            }
            //Can use 'and' or &&, the same as in c
            if($x == $y and 1 == 1){
                echo "True";
            }else{
                echo "False";
            }
            //Can use xor, one of them has to be true but not both
            if($x == $y xor 1 == 1){
                echo "Only one is True";
            }else{
                echo "False";
            }
        ?>
    </body>
</html>
  