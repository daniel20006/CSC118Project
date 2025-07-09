import cv2

capture = cv2.VideoCapture(0)
face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret, frame = capture.read()  # Added ret, frame for reading video frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Changed capture to frame
    faces = face_haar_cascade.detectMultiScale(gray, 1.1, 4) # Changed face_haar_cascade() to face_haar_cascade.detectMultiScale() and removed image

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2) # Changed capture to frame
    cv2.imshow('Face', frame) # Changed face_haar_cascade to frame and removed winname

    if cv2.waitKey(30) & 0xFF == 27: # Corrected waitKey usage
        break

cv2.release()