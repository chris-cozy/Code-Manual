<?php
    include_once '../connect.php';

    //Uses values from form in databases.php
    $first = mysqli_real_escape_string($conn, $_POST['first']);
    $last = mysqli_real_escape_string($conn, $_POST['last']);
    $email = mysqli_real_escape_string($conn, $_POST['email']);
    $uid = mysqli_real_escape_string($conn, $_POST['uid']);
    $pwd = mysqli_real_escape_string($conn, $_POST['pwd']);

    /*
    SQL Injection - People/hackers writing code as an input to get into your database and create or destroy something
    Two methods to protect against this
        -Prepared statements
            -The best way
        -Escaping the data to make sure it is only seen as text, rather than code
            -Using mysqli_real_escape_string
    */


    //--Inserting data into database--//
    //Want to include this in a separate php file, which will be linked to using the action tag inside the form tag
    $sql = "INSERT INTO users (user_first, user_last, user_email, user_uid, user_pwd) VALUES ('$first', '$last', '$email', '$uid', '$pwd');";
    mysqli_query($conn, $sql);
    //The header function simply takes you to another file
    header("Location: ../databases.php?signup=success");
?>