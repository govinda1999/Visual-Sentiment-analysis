var capture;
var video;

function setup() {
  createCanvas(320,240);
  video = createCapture(VIDEO);
  video.position(0,0);
  video.size(320, 240);
  //capture.hide();
  background(50);
}

function draw() {
     video.show();
    filter('THRESHOLD');
    image(video,0,0);
}

function mousePressed(){
  save('myCanvas.png');
  window.location.href = "new.php";
  return false;
}