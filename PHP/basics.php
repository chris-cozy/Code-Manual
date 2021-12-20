<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Doc Title</title>
    </head>
    <body>
        <!--to use php must include the php tag-->
        <!-- Everything in these tags will be php code-->
        <!-- BASIC VARIABLES/OUTPUT AND GETTING INFO FROM USER IN HTML -->
        <?php
            //echo outputs to the screen
            echo "This is a test.\n";
            //print does the same as echo, though echo loads faster
            print "This is another test >:)\n";
            //don't need quotations when dealing with numbers, unless you want it to be viewed as a string
            echo 12;
            //You can also write equations within echo
            echo 10 + 5;
        ?>

        <!--Grabbing input from the user to fill in a php variable using HTML-->
        <!--Using the get method in the form allows you to link it to php-->
        <form method="GET">
            <input type="text" name="person">
            <button>SUBMIT</button>
        </form>
        <?php
             //Variables are defined by $
             $name = "KAMORI";
             echo $name;
             //When wanting to combine php code with a string, need to include a separator (.)
             echo $name." is a crackhead, according to Kirsten\n";

             //To use the name we grabbed with the html form
             //However this code will show an error until the variable person is defined by the user (submitted by the form)
             //There is code to avoid this which will be learned later
             $name = $_GET['person'];
             echo $name." is a crackhead!\n";
        ?>
    </body>
</html>