<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link rel="stylesheet" href="src.css">

<title>Z-TEST</title>

<?php
$host = '94.183.164.196';
$port = 80;
$waitTimeoutInSeconds = 1;
if ($fp = fsockopen($host, $port, $errCode, $errStr, $waitTimeoutInSeconds)) {
	echo $host." is available.";
} else {
	echo $host." is NOT available.";
}
fclose($fp);
?>
