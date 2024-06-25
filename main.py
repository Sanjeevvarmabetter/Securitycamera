import cv2
import datetime
import time
import ipfshttpclient
import requests


ipfs_client = 

#first thing is we need to code how to access our webcam and view video from it

video = cv2.VideoCapture(0)
# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
#for full body use full_body file

#now we need to read the image

detection = False

detection_stopped_time = None
timer_start = False
x = 2

frame_size = (int(video.get(3)),int(video.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
#now we need output stream

while(True):
    #capture the vidoes frame by frame
    r,frame = video.read()
    #convert the image to grayscale
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #for detecting faces in the image           scale factor 
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(30,30))
    
    #recording will start only when a face is detected
    #now we need to write the code for checking faces
    
    if len(faces) > 0:
        if detection:
            timer_start = False
        else:
            detection = True                                  
            currenttime = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S") #day month year hour second
            out = cv2.VideoWriter(f"{currenttime}.mp4",fourcc,20,frame_size) #file name will be current time
            print("Started recording!!")


    elif detection: #if we did not dectect a body or face but we detected something
        #start our timer
        if timer_start:
            if time.time() - detection_stopped_time >= x:
                detection = False
                timer_start = False
                out.release()
                print("Stopped recording")
        else:
            timer_start = True
            detection_stopped_time = time.time() #this will give you current time

       
        if detection:
             out.write(frame)


    for (x,y,width,height) in faces:
        cv2.rectangle(frame,(x,y),(x+width,y+height),(255,0,0),3) #this is bgr not rgb
    #for displaying the resulting frame
    cv2.imshow('frame',frame)


    #for turning off the cam 
    # we are using keyboard key x see the py doc for accessing the keys in program
    if cv2.waitKey(1) & 0xFF == ord('x'):  #you can change this
        break

video.release

cv2.destroyAllWindows()

