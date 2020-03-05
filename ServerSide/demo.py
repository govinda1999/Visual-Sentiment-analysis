from imutils import face_utils
from subprocess import call
import numpy as np
import argparse
import imutils
import dlib
import cv2
import pandas as pd
import os




data={"inner_mouth":[],"mouth":[],"left_eyebrow":[],"right_eyebrow":[],"left_eye":[],"right_eye":[],"jaw":[],'nose':[],'output':[]}
# construct the argument parser and parse the arguments

#to get width and heigth of each parameter pass image and shape_predictor as argument


ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())




# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

# load the input image, resize it, and convert it to grayscale
images=[]


#image = cv2.imread(file)
image = cv2.imread(args["image"])
#image = imutils.resize(image, width=500)
gray=image
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in the grayscale image
rects = detector(gray, 1)

# loop over the face detections
for (i, rect) in enumerate(rects):
	# determine the facial landmarks for the face region, then
	# convert the landmark (x, y)-coordinates to a NumPy array
	shape = predictor(gray, rect)
	shape = face_utils.shape_to_np(shape)

	# loop over the face parts individually
	
	for (name, (i, j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
		# clone the original image so we can draw on it, then
		# display the name of the face part on the image
		clone = image.copy()
		cv2.putText(clone, name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
			0.7, (0, 0, 255), 2)

		# loop over the subset of facial landmarks, drawing the
		# specific face part
		tempx=[]
		tempy=[]
		for (x, y) in shape[i:j]:
			tempx.append(x)
			tempy.append(y)
			cv2.circle(clone, (x, y), 1, (0, 0, 255), -1)

		# extract the ROI of the face region as a separate image
		(x, y, w, h) = cv2.boundingRect(np.array([shape[i:j]]))
		roi = image[y:y + h, x:x + w]
		roi = imutils.resize(roi, width=250, inter=cv2.INTER_CUBIC)

		# show the particular face part
		#cv2.imshow("ROI", roi)
		#cv2.imshow("Image", clone)
		#cv2.waitKey(0)
		left=min(tempx)
		right=max(tempx)
		top=min(tempy)
		down=max(tempy)
		#print(left,right,top,down)
		#print(5/6)
		flag=False
		try:
			data[name].append(float((abs(left-right)))/(abs(top-down)))
		except Exception as e:
			flag=True


	if "happy" in args['image']:
		data['output'].append(1)
	elif "sadness" in args['image']:
		data['output'].append(2)
	elif "fear" in args['image']:
		data['output'].append(3)
	elif "contempt" in args['image']:
		data['output'].append(4)
	elif "disgust" in args['image']:
		data['output'].append(5)
	elif "surprise" in args['image']:
		data['output'].append(6)
	elif "anger" in args['image']:
		data['output'].append(7)
	else:
		data['output'].append(100)
		
	#print(data)
	# visualize all facial landmarks with a transparent overlay
	#output = face_utils.visualize_facial_landmarks(image, shape)
	#cv2.imshow("Image", output)
	#cv2.waitKey(0)
#print(data)
if not flag:
	t1=pd.DataFrame.from_dict(data)

	t1.to_csv("final11.csv",mode='a',header=False)

print(data)
