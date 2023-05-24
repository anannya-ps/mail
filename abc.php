<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $name = $_POST["name"];
  $branch = $_POST["branch"];
  $course = $_POST["course"];
  $activity = $_POST["activity"];
  $faculty_email = $_POST["faculty_email"];
// $name="manjuprasad32@gmail.com";
// $dept="AIML";
// $b="GSSSIETW";

$id="$faculty_email \x20\x20\x20 $name \x20\x20\x20 $branch \x20\x20\x20 $course \x20\x20\x20 $activity \x20\x20\x20 $faculty_email \x20\x20\x20 $faculty_email";
$command = 'C:\Users\Anannya\AppData\Local\Programs\Python\Python311\python.exe mail.py ' . $id ;//change path

#echo $command;
$python = `$command`;
echo $python;


}
?>

