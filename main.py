import cv2
import numpy as np
from pupil import Pupil
from eye import getEyeArray

cap = cv2.VideoCapture(0);
while True:
    # underscore is throw-away
    #frame is image array vector
    _, frame = cap.read();
    try:
        arr = getEyeArray(frame)
        pupil = Pupil(arr[0], arr[1], frame) #pass in the eye objects into pupil
        #cv2.drawKeypoints(frame, pupil.keyPointLeft, frame, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        #cv2.imshow('Video', frame)
    except: #if no faces detected
        print("no face")
        cv2.imshow('Video', frame)
    """print(p.x)
    cv2.circle(frame, (p.x, p.y), 2, (0,0,225), 2)
    cv2.imshow('Video', frame)"""


    #waits for a key to be pressed
    #waits for 1 milliseconds for key pressed
    key = cv2.waitKey(1);
    if key == 27: # esc key
        break

cap.release()
cv2.destroyAllWindows()
