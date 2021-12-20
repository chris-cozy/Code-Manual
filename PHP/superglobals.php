<!-- Code to start a session. This goes at the top of all the webpages that you want to be able to use the session variables -->
<?php
    session_start();
?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Doc Title</title>
    </head>
    <body>
        <!--Using this for post and get -->
        <!--If you use post instead of get the information won't be visible in the url -->
        <form method="GET">
            <input type="hidden" name="name" value="value">
            <button type="submit">Press this</button>
        </form>
        <!-- A superglobal is a variable that has already been created for us inside the php code itself -->
        <?php
            /* SUPERGLOBALS
            $GLOBALS
            $_POST
            $_GET
            $_COOKIE
            $_SESSION
            */

            //$GLOBALS
            $x = 5;
            function something(){
                $y = 10;
                //Globals - can use this to access global variables without passing them in. 
                //It's not used for this purpose, only use in special cases
                $GLOBALS['x'];
            }
            //$_POST and $_GET
            //passing information into the url to use on another page
            echo $_GET['name'];

            //$_COOKIE and $_SESSION
            //The basic idea behind this is to save information on the user
            //cookie is for the browser, session is for the server
            //sessions are used to make the website constantly remember who is currently logged in
            //sessions are much more secure than cookies, when it comes to being hacked
            //cookies can be used for harmless information, but for users and passwords sessions are used
            //sessions are wiped once the browser is closed down, unlike cookies

            //to make a cookie variable
            setcookie("name","value");
            //to make it expire after a time (in this case a day)
            setcookie("name","value", time()+86400);
            //to force destroy a cookie set the time to negative

            //make a session variable
            $_SESSION['name'] = "value";

            //To use session variables on multiple pages of your webpage, must have a session running. The top of this document holds an example

            //example of a login check. Can expand this to much larger changes
            if (!isset($_SESSION['username']))
            {
                echo "You are not logged in"
            }else
            {
                echo "You are logged in"
            }
        ?>
   </body>
</html>   