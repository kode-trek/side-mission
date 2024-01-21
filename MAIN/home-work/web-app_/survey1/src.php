<link rel="stylesheet" href="src.css">

<title>title</title>

<div style="overflow-x:auto;"><table style="width:100%"><tr><th>submitted!</th></tr>

<?php

$fh = fopen("stk.dat", "w") or die("error -- unable to open file!");

$str="name=".htmlspecialchars($_POST["name"])."\n";	fwrite($fh, $str);
$str="gender=".htmlspecialchars($_POST["gender"])."\n";	fwrite($fh, $str);

fclose($fh);

if(isset($_FILES['image'])) {

	$flag=1;

	$file_name=$_FILES['image']['name'];
	$file_size=$_FILES['image']['size'];
	$file_tmp=$_FILES['image']['tmp_name'];
	$file_type=$_FILES['image']['type'];

#	check extension
	$file_ext=strtolower(end(explode('.',$_FILES['image']['name'])));
	$extensions=array("jpeg","jpg","png");
	if(in_array($file_ext,$extensions)===false) {
		$errors[]="extension not allowed, please choose a JPEG or PNG file.";
		$flag=0;
	}

#	check size
	if($file_size > 2097152) {
		$errors[]='File size must be excately 2 MB';
		$flag=0;
	}

	if($flag!==0) {
		file_put_contents($file_name, fopen($file_tmp, 'r'));
		echo "<div align='center'><img src=$file_name height='320' width='240' /></div>";
	}else {echo $errors[0];}
}

?>
