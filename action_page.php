<?php
    $Username = $_POST['Username'];
    $password = $_POST['password'];
    // Making Connection with database

    $con = new mysqli('localhost','root','','phpdata');
    if ($con -> connect_error) {
    die('Connection failed :'.$conn -> connect_error);
    }
    else{
    $stmt = $con->query("INSERT INTO signup(Username,password)
        values(?,?)");
    $stmt->bind_param("ssssiss",$Username, $password);
    $stmt->execute();
    echo "Sign up successful";
    $stmt->close();
    $con->close();
     }?>