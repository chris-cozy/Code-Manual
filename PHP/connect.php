<?php
/*
Video 36
Don't need closing tags in a pure php file
4 parameters we need: server name, user name, password, database name
Can save this doc in an 'includes' subdir if you want
*/
$dbServername= "";
$dbUsername = "";
$dbPassword = "";
$dbName= "";

$conn = mysqli_connect($dbServername, $dbUsername, $dbPassword, $dbName); //conn stands for connection
