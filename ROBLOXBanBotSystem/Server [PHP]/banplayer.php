<?php
$number = NULL;
if (isset($_GET["userid"]))
{
    $number = $_GET["userid"];
}
else
{
    die("You need to supply a user id with the request!");
}
$fp = fopen('bannedplayers.txt', 'a'); //opens file in append mode
fwrite($fp, ' ' . $number . '');
fclose($fp);

echo "Banned Player.";
?>
