<link rel="stylesheet" href="src.css">

<body bgcolor="lightgrey">
<form action="src.php" method="post" enctype="multipart/form-data">
<?php
$usr = "foo";

$fh = fopen("stk.DAT", "r");
$str1 = "";
$str1 = fread($fh, filesize("stk.DAT"));
fclose($fh);

echo(
"<textarea id=\"id1\">".$str1."</textarea>
<p>".$usr.":</p>
<textarea id=\"id2\" name=\"msg\"></textarea>"
);

$fh = fopen("stk.DAT", "a");
$str2 = "";
$str2 = $usr.": ".htmlspecialchars($_POST["msg"])."\n";
fwrite($fh, $str2);
fclose($fh);

$fh = fopen($usr.".MSG", "w");
$str3 = "";
$str3 = $usr.": ".htmlspecialchars($_POST["msg"])."\n";
fwrite($fh, $str3);
fclose($fh);

echo("<input type=\"submit\" value=\"send\" />");

//echo(
//"<script>
//document.getElementById(\"id1\").value = "";
//</script>"
//);
//sleep(2);
//header("Location: src.php");
?>
</form></body>

<!--
setInterval(function() {location.reload();}, 2000);
document.getElementById("id1").value = "";
-->
