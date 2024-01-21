<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="src.css">

<title>User Check</title>

<div align='center' id='footer'>
<?php
exec('python chk_usr_reg.py "' . htmlspecialchars($_POST["uname"]) . '"');

$myfile = fopen("stage.txt", "r") or die("Unable to open file!");
$flag = fread($myfile,filesize("stage.txt"));
fclose($myfile);
if ($flag == 'True') {
	$fh = fopen("stage.txt", "w") or die("error -- unable to open file!");
	#u-name
	$str = htmlspecialchars($_POST["uname"]) . "\n";	fwrite($fh, $str);
	#u-pass
	$str = htmlspecialchars($_POST["upass"]) . "\n";	fwrite($fh, $str);
	#e-mail
	$str = htmlspecialchars($_POST["e_mail"]) . "\n";	fwrite($fh, $str);
	#date
	date_default_timezone_set("Asia/Tehran");
	$str = date("Y/m/d") . '_' . date("h:i:sa") . "\n";	fwrite($fh, $str);
	fclose($fh);
	exec('python add_usr.py');

	$myfile2 = fopen("stage.txt", "r") or die("Unable to open file!");
	$acc = '<pre>' . fread($myfile2,256) . '</pre>';
	fclose($myfile2);

	echo 'Your account has been successfully created.';
#	echo '<br>';
#	echo $acc;
	echo '<br>';
	echo "<div align='center'><a href='index.php'>Login</a></div>";
} else {
	echo 'The username already exists.';
	echo '<br>';
	echo "<div align='center'><a href='reg.php'>Back</a></div>";
}
?>
</div>
