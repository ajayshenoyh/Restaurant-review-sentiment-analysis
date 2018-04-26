<?php
$c=mysql_connect("localhost","root","");
if(!$c)
{
echo "Not connected";
}
else
{
echo "Connected";
}
?>