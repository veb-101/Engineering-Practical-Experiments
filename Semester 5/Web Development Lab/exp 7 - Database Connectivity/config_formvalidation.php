<?php
	$localhost = 'localhost';	// localhost or 127.0.0.1
	$username = "root";			//user name of phpmyadmin
	$password = "";				//password
	$database = "employee";		//database name in phpmyadmin
	
	//creating connection with this parameters
	$conn = mysqli_connect($localhost, $username, $password, $database);
	
	//checking connection established or not
	if($conn){
		echo "Connection successfull";

	// $sql = "create table emp(name varchar(30) not null, age int not null, gender varchar(3), email)"
	
	}else{
		echo "Access denied";
	}
?>