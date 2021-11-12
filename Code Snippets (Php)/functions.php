<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Doc Title</title>
    </head>
    <body>
        
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
        ?>
    </body>
</html>