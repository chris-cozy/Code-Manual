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
        ?>
    </body>
</html>