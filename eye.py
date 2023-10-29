import cv2
import numpy as np
import dlib
cap = cv2.VideoCapture(0);
#library for facial detection
detector = dlib.get_frontal_face_detector();
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
"""
The eye class contains the original frame passed in, the frame of the eye
and the (x,y) coordinates of top left of frame and bottom right of frame. 
"""
class Eye:
    def __init__(self, frame, xL, yL, xR, yR):
        self.yL = yL
        self.yR= yR
        self.xR = xR
        self.xL = xL
        self.frame = frame
        self.eyeFrame = self.getEyeFrame()

    """
    will return the eye frame
    """
    def getEyeFrame(self):
        cropped_frame = self.frame[self.yL:self.yR, self.xL:self.xR]
        return cropped_frame;

"""
helper method to return an array of eyes. If a face is detected then it will 
create two new eyes and return in array. Otherwise it will throw and exception
"""
def getEyeArray(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);

    faces = detector(gray);  # array of all faces
    try:
        face = faces[0]
        landmarks = predictor(gray, face)
        leftEye = Eye(frame, landmarks.part(17).x, landmarks.part(19).y,
                      landmarks.part(27).x, landmarks.part(28).y)
        rightEye = Eye(frame, landmarks.part(27).x, landmarks.part(22).y,
                      landmarks.part(15).x, landmarks.part(28).y)

        eyeArray = [leftEye, rightEye];
        return eyeArray
    except:
        raise Exception("no face")


