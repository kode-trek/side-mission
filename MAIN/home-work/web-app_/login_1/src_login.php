<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="src.css">

<title>User Check</title>
<div align='center' id='footer'>
<?php
$fh = fopen("logs.txt", "a") or die("error -- unable to open file!");
#u-name
$str = htmlspecialchars($_POST["uname"]) . "\t";	fwrite($fh, $str);
#u-pass
$str = htmlspecialchars($_POST["upass"]) . "\t";	fwrite($fh, $str);
#date
date_default_timezone_set("Asia/Tehran");
$str = date("Y/m/d") . '_' . date("h:i:sa") . "\t";	fwrite($fh, $str);

exec('python chk_login.py "' . htmlspecialchars($_POST["uname"]) . '"' . ' "' . htmlspecialchars($_POST["upass"]) . '"');

$myfile = fopen("stage.txt", "r") or die("Unable to open file!");
$flag = fread($myfile,filesize("stage.txt"));
fclose($myfile);

if ($flag == 'True') {
	$str = '[FAILED]' . "\n";	fwrite($fh, $str);
	echo 'Access Denied!';
	echo '<br>';
	echo "<div align='center'><a href='index.php'>Back</a></div>";
} else {
	$str = '[OK]' . "\n";	fwrite($fh, $str);
	echo 'Access Granted.' . '<br>';
	if (htmlspecialchars($_POST["uname"]) == 'uname') {
		echo 'Greetings, Admin!';
	}
	else {
		echo 'Hello, ' . htmlspecialchars($_POST["uname"]) . '!';
	}
	echo '<br>';
	echo "<div align='center'><a href='index.php'>Logout</a></div>";
}

fclose($fh);
?>
</div>
