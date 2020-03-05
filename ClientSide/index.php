<!DOCTYPE html>
<html>
<head>
    <title>Visual Sentiment Analysis</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"/>
    <link rel="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"></link>
    <style type="text/css">
        .align-body{
            margin-top: 25vh;
        }
        .bg-img {
        background-image: url("img1.jpg");
        min-height: 500px;
        background-position: center;
        margin: 0px 0px 0px 0px;
        background-repeat: no-repeat;
        background-size: cover;
        }
    </style>
</head>
<body class="bg-img">
<div class="container align-body">
    <div class="row justify-content-center">
    <div class="col-lg-4">
        <div class="card" style="width: 18rem;">
            <img src="upload.png" class="card-img-top w-100 " alt="upload image">
            <div class="card-body">
            <h5 class="card-title">Select File</h5>
            <form action="test_image.php" enctype="multipart/form-data" method="POST">
                <input type="file" name='file' id='file'/> 
                <input type="submit" name="uploadbutton btn-outline-primary btn" value="Upload">            
            </form>
        </div>
        </div>
    </div>
    <div class="col-lg-4">
        <div class="card" style="width: 18rem;">
            <img src="img2.png" class="card-img-top" alt="webcam image">
            <div class="card-body">
            <h5 class="card-title">Take Image from Webcam</h5>
            <a href="webcam.html" class="btn btn-outline-primary">Open Webcam</a>
        </div>
        </div>
    </div>
    </div>
</div>
</body>
</html>