<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link rel="stylesheet" href="src.css">

<title>link-scraper</title>

<?php
 $flag = 1;
 date_default_timezone_set("Asia/Tehran");
 //
 $ip = $_SERVER['REMOTE_ADDR'];
 $str1 =
 "[".date("Y/m/d")."__".date("h:i:sa")."]".
 "[".htmlspecialchars($_POST["url"])."]".
 "[".$ip."]"."\n";
 @fwrite($fh, $str1);
 $fh = @fopen("LOG.txt", "a");
 @fwrite($fh, $str1);
 @fclose($fh);
 //
 system("/home/dyane/q/list-builder \"".htmlspecialchars($_POST["url"])."\"");
?>

<div id="footer" align="center">
 <p>DONE.</p>
 <a href="src.htm" >&larr;BACK</a>
</div>

<script src="src.js"></script>
