<?php
    include_once '../connect.php';

    //Uses values from form in databases.php
    $first = $_POST['first'];
    $last = $_POST['last'];
    $email = $_POST['email'];
    $uid = $_POST['uid'];
    $pwd = $_POST['pwd'];

    /*
    SQL Injection - People writing code as an input to get into your database and create or destroy something
    Two methods to protect against this
        -Prepared statements
        -Escaping the data to make sure it is only seen as text, rather than code
            -Using mysqli_real_escape_string

    Prepared statements
    - Adds placeholders for the variables then sends code to database to parse it into the actual data, then send it to the database, which will read it as characters
    */


    //--Inserting data into database--//
    //Want to include this in a separate php file, which will be linked to using the action tag inside the form tag
    $sql = "INSERT INTO users (user_first, user_last, user_email, user_uid, user_pwd) VALUES ('$first', '$last', '$email', '$uid', '$pwd');";
    mysqli_query($conn, $sql);
    //The header function simply takes you to another file
    header("Location: ../databases.php?signup=success");
?>