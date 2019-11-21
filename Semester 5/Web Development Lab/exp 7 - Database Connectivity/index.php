<?php
	include("config_formvalidation.php");	//including database connectivity file
?>
<html>
<head>
	<style>
		div{
			padding: 15px;
			background-color: red;
			font-size: 20px;
		}
		footer{
			background-color: green;
			font-size: 22px;
			color: white;
		}
	</style>
</head>
<body>
<?php
	if(isset($_POST['submit'])){
		$user = $age = $gender = $email ='';  //to clear data whenever alert occurs
		if($_POST['user'] == '' || $_POST['age'] == '' || $_POST['gender'] == '' || $_POST['mail'] == ''){
			echo "<script>
					alert('Please fill all the fields');
				 </script>";
		}else{
			//storing entered data into variables
			$user = $_POST['user'];
			$age = $_POST['age'];
			$gender = $_POST['gender'];
			$email = $_POST['mail'];
			
			//fetching name from database
			$query = "SELECT * FROM emp WHERE Name = '$user' ";
			
			// $query and $conn(connection made in config_formvalidation.php file) parameter passed
			$data = mysqli_query($conn,$query);
		
			//mysqli_num_rows is used to check whether that row is present or not
			$result = mysqli_num_rows($data);
			
			//if 0 then not present and goes in else part and if 1 it means it is present
			if( $result > 0 ){
				//If username is there in table then print msg this or else part
				$text = "You are already there!";
			}else{
				$text = "You are new. Welcome!";
			}
			
		}
	}
?>
	<form action="" method="post">
	<div>
	<table>
	 <tr>
		<td>Name :</td> <td><input type="text" name="user" placeholder="Enter name"></td>
	 </tr>
	<tr>	 
		<td>Age :  </td><td><input type="text" name="age"></td>
	</tr>
	<tr>
		<td>Gender : </td><td><input type="radio" name="gender" value="male">Male <input type="radio" name="gender" value="female">Female</td>
	</tr>
	<tr>
		<td>Email : </td><td><input type="mail" name="mail" placeholder="eg: you@gmail.com" required></td>
	</tr>
	<tr>
		<td></td><td><input type="submit" name="submit"></td>
	</tr>
	
	</table>
	</div>
	<footer>
	<h2>Your data:</h2><br>
		<?php
			echo $text."<br>";
			echo "Name:".$user."<br>";
			echo "Age: ".$age.'<br>';
			echo "Gender: ".$gender.'<br>';
			echo "Email: ".$email;
		?>
	</footer>
	</form>
</body>
</html>