# Visual Sentiment analysis 
Sentiment analysis based on human face image.

program.py is based on MLPClassifier and ne.py is based on SVC.

ServerSide/ck/ is dataset folder.

Library Required

      1.dlib
      2.sklearn
      3.pandas
      4.numpy
      5.flask
      6.cv2
      7.tensorflow

# Changes in files

    1.ServerSide/api/api.py provide path to call function.
    2.ClientSide/test_image.php provide path to upload folder.
    3.Replace path in ne.py,video.py,demo2.py with proper path according to your condition.
    
# Run

    1. Start Xampp Server (for Ubuntu sudo /opt/lampp/lampp start)
    2. Start Api ( cd ServerSide/api && python api.py)
    3. Copy CLientSide in htdocs folder
    4. Goto localhost/ClientSide/index.php
   
    




