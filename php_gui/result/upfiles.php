<?php
$target_dir = "../images/";
$target_path = $target_dir . basename($_FILES['bitmap']['name']);
if(move_uploaded_file($_FILES['bitmap']['tmp_name'], $target_path)){
  echo "The file " . basename($_FILES['f1']['name']) . "has been uploaded";
}else{
  echo "error";
}
?>
