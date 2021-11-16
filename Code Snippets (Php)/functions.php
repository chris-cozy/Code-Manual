<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Doc Title</title>
    </head>
    <body>
        <!--Variable scope:
            Global scope: defined outside of the function
            Local scope: defined inside the function -->
         <?php
            //There are predefined and user defined functions, like in C
            //Example of predefined function use
            $name = "KAMORI";
            $length = strlen($name);
            echo $length;

            $full_name = "KAMORI TENAME";
            $word_c = str_word_count($full_name);
            echo $word_c;

            $pos = strpos($full_name, $name);
            echo pos;

            $full_name = str_replace($name, "CHRIS", $full_name);

            //USER DEFINED FUNCTIONS - keep them reusable
            //basic setup - use the function tag to define as a function
            //It's typical to include a separate document defining all of your php functions for the program
            $y = 100;
            function practice($x) 
            {
                $new_num = $x * 0.75;
                echo "here is 75% of what you wrote ".$new_num;
            }
            practice($y);

        ?>
    </body>
</html>