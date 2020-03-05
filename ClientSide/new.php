<?php 
$response = file_get_contents("http://127.0.0.1:5000/api/image?source=/opt/lampp/htdocs/demo/upload/mycanvas.png");
     $json = json_decode($response);
     //echo "<scrip>console.log(".$json.")</script>";
     //echo $json;
    // header("location:test_image.php?sucsess");
     $string = file_get_contents("/home/govinda/Desktop/test/api.json");
     $json_temp = json_decode($string,true);
     //echo $json_temp;
     echo '<img src="upload/mycanvas.png"></img>';
     echo "Anger ".$json_temp['anger']."\n";
     echo "Fear ".$json_temp['fear']."\n";
     echo "Sadness ".$json_temp['sadness']."\n";
     echo "Happy ".$json_temp['happy']."\n";

?>