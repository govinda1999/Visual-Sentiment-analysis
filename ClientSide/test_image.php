<?php 
if(isset($_POST["uploadbutton"]))
{

     $filename=$_FILES["file"]["name"];

     $fileTmpname=$_FILES['file']['tmp_name'];
     $filesize=$_FILES["file"]["size"];
     $fileerror=$_FILES["file"]["error"];
     $filetype=$_FILES["file"]["type"];
     $filenamearray=explode('.',$filename);
     $fileExt=strtolower(end($filenamearray));
     $allowed=array('jpg','jpeg','png');
     if(in_array($fileExt,$allowed))
     {
         if($fileerror==0)
         {
           if($filesize<1000000)
           {
                 $filenewname=date('d-m-Y-H-i-s')."-".$_FILES["file"]["name"];
                 $destination='upload/'.$filenewname;
                 move_uploaded_file($fileTmpname,$destination);
                 $response = file_get_contents("http://127.0.0.1:5000/api/image?source=/opt/lampp/htdocs/demo/".$destination);
                 $json = json_decode($response);
                 $string = file_get_contents("/home/govinda/Desktop/test/api.json");
                 $json_temp = json_decode($string,true);
                 echo '<img src="'.$destination.'"></img>';
                 echo "Anger ".$json_temp['anger']."\n";
                 echo "Fear ".$json_temp['fear']."\n";
                 echo "Sadness ".$json_temp['sadness']."\n";
                 echo "Happy ".$json_temp['happy']."\n";
           }
           else
           {
            echo "file size too large";
           }
         }
         else
         {
             echo "error in uploadin";
         }

     }
     else
     {
         echo "you cant upload this file type";
     }
}
?>
