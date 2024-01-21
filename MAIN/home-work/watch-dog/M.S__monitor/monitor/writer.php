<?php
$fh = fopen("stk.dat", "a") or die("error -- unable to open file!");
$str="data=".htmlspecialchars($_GET["data"])."\n";	fwrite($fh, $str);
fclose($fh);
echo "<script>window.location='default.htm'</script>";
?>
