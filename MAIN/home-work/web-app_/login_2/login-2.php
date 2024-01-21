<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link rel="stylesheet" href="src.css">

<title>cred-check</title>

<div id="footer" align="center">
<?php

$flg = "false";
if ((htmlspecialchars($_POST["uname"]) == "adham") and (htmlspecialchars($_POST["upass"]) == "admin")) $flg = "true";
if ((htmlspecialchars($_POST["uname"]) == "safar") and (htmlspecialchars($_POST["upass"]) == "clock")) $flg = "true";

if ($flg == "false") {
	echo(
	"access-denied!<br>
	<div align=\"center\"><a href=\"login-1.htm\">Back</a></div>"
	);
} else {header("Location: src.php");}
?>
</div>
