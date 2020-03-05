from subprocess import call
import os 
import csv

tt=1
#to generate csv file
for file in os.listdir("/home/govinda/Desktop/test/ck/happy"):
	print("happy")
	#print(file)
	tt+=1
	call("python demo.py --shape-predictor shape_predictor_68_face_landmarks.dat --image /home/govinda/Desktop/test/ck/happy/"+file,shell=True)
	if tt==5:
		exit()

'''	
v=open("/home/govinda/Desktop/test/final3.csv")
r=csv.reader(v)
count=1
for item in r:
	item.append(count)
v.close()
'''
for file in os.listdir("/home/govinda/Desktop/test/ck/fear"):
	print("fear")
	print(file)
	call("python demo.py --shape-predictor shape_predictor_68_face_landmarks.dat --image /home/govinda/Desktop/test/ck/fear/"+file,shell=True)
'''
v=open("/home/govinda/Desktop/test/final3.csv")
r=csv.reader(v)
count=2
for item in r:
	item.append(count)
v.close()
'''

for file in os.listdir("/home/govinda/Desktop/test/ck/disgust"):
	print("disgust")
	print(file)
	call("python demo.py --shape-predictor shape_predictor_68_face_landmarks.dat --image /home/govinda/Desktop/test/ck/disgust/"+file,shell=True)
'''
v=open("/home/govinda/Desktop/test/final3.csv")
r=csv.reader(v)
count=3
for item in r:
	item.append(count)
v.close()
'''

for file in os.listdir("/home/govinda/Desktop/test/ck/anger"):
	print("anger")
	print(file)
	call("python demo.py --shape-predictor shape_predictor_68_face_landmarks.dat --image /home/govinda/Desktop/test/ck/anger/"+file,shell=True)
'''
v=open("/home/govinda/Desktop/test/final3.csv")
r=csv.reader(v)
count=4
for item in r:
	item.append(count)
v.close()
'''

for file in os.listdir("/home/govinda/Desktop/test/ck/sadness"):
	print("sadness")
	print(file)
	call("python demo.py --shape-predictor shape_predictor_68_face_landmarks.dat --image /home/govinda/Desktop/test/ck/sadness/"+file,shell=True)

'''
v=open("/home/govinda/Desktop/test/final3.csv")
r=csv.reader(v)
count=5
for item in r:
	item.append(count)
v.close()
'''

for file in os.listdir("/home/govinda/Desktop/test/ck/surprise"):
	print("surprice")
	print(file)
	call("python demo.py --shape-predictor shape_predictor_68_face_landmarks.dat --image /home/govinda/Desktop/test/ck/surprise/"+file,shell=True)
'''
v=open("/home/govinda/Desktop/test/final3.csv")
r=csv.reader(v)
count=6
for item in r:
	item.append(count)
v.close()
'''

for file in os.listdir("/home/govinda/Desktop/test/ck/contempt"):
	print("contempt")
	print(file)
	call("python demo.py --shape-predictor shape_predictor_68_face_landmarks.dat --image /home/govinda/Desktop/test/ck/contempt/"+file,shell=True)
'''
v=open("/home/govinda/Desktop/test/final3.csv")
r=csv.reader(v)
count=7
for item in r:
	item.append(count)
v.close()
'''
