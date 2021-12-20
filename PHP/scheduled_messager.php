<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Scheduled Messager</title>
    </head>
    <body>
        <?php
            //Whenever you want to write html code inside php code, you must use quotes and echo it out.
            //Treat it like a string
            $dayofweek = date("w");
            switch($dayofweek){
                case 0:
                    echo "<p>It is Sunday.</p>";
                    break;
                case 1:
                    echo "<p>It is Monday.</p>";
                    break;
                case 2:
                    echo "<p>It is Tuesday.</p>";
                    break;
                case 3:
                    echo "<p>It is Wednesday.</p>";
                    break;
                case 4:
                    echo "<p>It is Thursday.</p>";
                    break;
                case 5:
                    echo "<p>It is Friday.</p>";
                    break;
                case 6:
                    echo "<p>It is Saturday.</p>";
                    break;
            }



        ?>
    </body>
</html>