<?php
$number = NULL;
if (isset($_GET["userid"])) {
    $number = $_GET["userid"];
} else {
    die("Please add a User ID.");
}
$a = 'bannedplayers.txt';
   
$b = file_get_contents('bannedplayers.txt');
  
$c = preg_replace('/'.$number.'/', '', $b);
echo $c;
  
file_put_contents($a, $c); 
?>