import cv2

#get the cv2 cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#Defining a function to do detection
#It takes gray scale img to detect and original img to draw the rectangle
def detect(gray, frame):
    #first detect all the faces in the img 1.3=> scaling of img 5=>min no. of factors surrounding to confirm it is an img
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #(x,y) upper left corner coordinate
    for (x, y, w, h) in faces:
        #it takes upper left ant bottom right coordinate to draw then color and size
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        #now for each face we detect eye 
        #we do this logically to reduce time 
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    return frame

#Now detection part is over
#as the function takes images, we have to convert the video ongoing to images and pass it

#Extracting img from web cam
video_capture = cv2.VideoCapture(0)# 0 for device web cam and 1 for external
#this returns the last frame of the video

while True :
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    #show result
    cv2.imshow('Video', canvas)
    #Trick to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()


