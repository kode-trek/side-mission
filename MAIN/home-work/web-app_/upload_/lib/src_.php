<?php
$target_file = basename($_FILES["fileToUpload"]["name"]);
$file_tmp = $_FILES['fileToUpload']['tmp_name'];
// file-exist
if (file_exists($target_file)) exit("File already EXISTs!");
// actual-upload
if (file_put_contents($target_file, fopen($file_tmp, 'r'))) echo "DONE.";
else echo "ERROR!";
?>
