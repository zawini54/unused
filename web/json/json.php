<?php
$user = 'root';
$pass = '01234';
$host = 'localhost';
$db = 'json';

$connect = mysqli_connect($host, $user, $pass, $db);

if (mysqli_connect_errno()){
  echo 'Failed to connect';
}
?>
