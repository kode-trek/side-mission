<?php
$fh = fopen("stk.dat", "w") or die("error -- unable to open file!");

$str=htmlspecialchars($_POST["in"])."\n";	fwrite($fh, $str);

exec('lab51 python hist.py');
?>
