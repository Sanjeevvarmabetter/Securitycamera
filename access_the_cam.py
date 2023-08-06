import cv2

#first thing is we need to code how to access our webcam and view video from it

video = cv2.VideoCapture(0)

while(True):
    #capture the vidoes frame by frame
    r,frame = video.read()

    #for displaying the resulting frame

    cv2.imshow('frame',frame)


    #for turning off the cam 
    # we are using keyboard key x see the py doc for accessing the keys in program
    if cv2.waitKey(1) & 0xFF == ord('x'):  #you can change this
        break

video.release

cv2.distroyAllWindows()

