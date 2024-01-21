<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="src.css">

<title>result</title>

<div align='center'><table><tr><th>submitted!</th></tr></div>

<?php
#upload-file
$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["up_file"]["name"]);

$file_tmp = $_FILES['up_file']['tmp_name'];
$total = count($_FILES['up_file']['name']);

for ($i=0; $i<$total; $i++) {
	$tmpFilePath = $_FILES['up_file']['tmp_name'][$i];
	if ($tmpFilePath != "") {
		$newFilePath = "uploads/" . $_FILES['up_file']['name'][$i];
		move_uploaded_file($tmpFilePath, $newFilePath);
	}
}
?>
