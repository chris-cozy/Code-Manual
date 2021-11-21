<?php
    include_once 'connect.php';
?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Doc Title</title>
    </head>
    <body>
       <?php
            //---Connecting the database to php---//
            //You want to have the database connection file separate. In this directory it is called connect.php. Then include it at the top
            
            //---Showing database data on a website---//
            $sql = "SELECT * FROM users;";
            //Have to query the code to run it in the database
            $result = mysqli_query($conn, $sql);
            //check if there are any results (optional but recommended)
            $resultCheck = mysqli_num_rows($result);
            
            if ($resultCheck > 0){
                //this inserts each row of appropriate data into $row as an array
                while ($row = mysqli_fetch_assoc($result)){
                    //To fetch the data from $row, write the name of the column you want to access
                    //This outputs all of the user ids
                    echo $row['user_uid']."<br>";
                }

            }
        ?>
        <!--The action sets a path to a file to run after submit is clicked -->
        <form action="db/prepared_statements.php" method="POST">
            <input type="text" name="first" placeholder="Firstname">
            <br>
            <input type="text" name="last" placeholder="Lastname">
            <br>
            <input type="text" name="email" placeholder="E-mail">
            <br>
            <input type="text" name="uid" placeholder="Username">
            <br>
            <input type="password" name="pwd" placeholder="Password">
            <br>
            <button type="submit" name="submit">Sign up</button>
        </form>
    </body>
</html>