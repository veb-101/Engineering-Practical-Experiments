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
if (isset($_POST['submit'])) {
				$user = $age = $gender = $email = ''; //to clear data whenever alert occurs
				if ($_POST['user'] == '' || $_POST['age'] == '' || $_POST['gender'] == '' || $_POST['mail'] == '') {
								echo "<script>
					alert('Please fill all the fields');
				 </script>";
				} else {
								//storing entered data into variables
								$user   = $_POST['user'];
								$age    = $_POST['age'];
								$gender = $_POST['gender'];
								$email  = $_POST['mail'];
				}
}
?>
	<form action="" method="post">
	<div>
	<table>
	 <tr>
		<td>Name :</td> 
        <td><input type="text" name="user" placeholder="Enter name"></td>
	 </tr>
	<tr>	 
		<td>Age :  </td>
        <td><input type="text" name="age"></td>
	</tr>
	<tr>
		<td>Gender : </td>
        <td>
            <input type="radio" name="gender" value="male">Male 
            <input type="radio" name="gender" value="female">Female
        </td>
	</tr>
	<tr>
		<td>Email : </td>
        <td>
            <input type="mail" name="mail" placeholder="eg: you@gmail.com" required>
        </td>
	</tr>
	<tr>
		<td></td>
        <td>
            <input type="submit" name="submit">
        </td>
	</tr>
	
	</table>
	</div>
	<footer>
	<h2>Your data:</h2><br>
		<?php
echo $user . "<br>";
echo $age . "<br>";
echo $gender . "<br>";
echo $email . "<br>";
?>
	</footer>
	</form>
</body>
</html>