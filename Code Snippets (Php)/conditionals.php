<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Conditionals</title>
    </head>
    <body>
        <?php
            //If else
            $x = 1;
            if ($x == 1){
                echo "Kamori is better";
            }else{
                echo "Kamori is cracked";
            }
            //Example of use: checking if someone is logged in, then echo out their profile pictures and info, etc
            $y == 0;
            if ($y > $X){
                echo "Kurse is better";
            }elseif ($y < $x){
                echo "Kamori is better";
            }

            //Switch - default is called if none of the cases are true
            $x ==1;
            switch (){
                case 1:
                    echo "X is 1";
                    break;
                case 2:
                    echo "X is 2";
                    break;
                case 3:
                    echo "X is 3";
                    break;
                case "number":
                    echo "X is 'number'";
                    break;
                default:
                    echo "X is undefined";
            }
            //While loop
            $x = 1;
            while ($x <= 5){
                echo "hi there<br>";
                $x++;
            }

            //Do-While Loop
            //different from a while loop because it will always execute at least once
            $x = 1;
            do {
                echo "hi there<br>";
                $x++;
            }
            while ($x <= 5);

            //For loop
            for($i = 0; $i < 10; $i++){
                echo "hello<br>";
            }

            //For-Each Loop
            //Deals with arrays
            //Sets each individual value in the array to the defined variable in the ()
            $array = array(1,2,3,4,5);
            foreach ($array as $num){
                echo "This num is ".$num;
            }
            //NEXT VIDEO IS 21
        ?>
    </body>
</html>