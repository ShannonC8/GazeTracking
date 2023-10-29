import cv2
import numpy as np
import dlib
cap = cv2.VideoCapture(0);
#library for facial detection
detector = dlib.get_frontal_face_detector();
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

class Pupil:
    def __init__(self, leftEye, rightEye, frame):
        self.yR, self.xR = self.setPupil(leftEye.eyeFrame)
        self.yL, self.xL = self.setPupil(rightEye.eyeFrame)
        self.frame = frame
        self.rightEye = rightEye
        self.leftEye = leftEye

    def setPupil(self, pic):
        detector_params = cv2.SimpleBlobDetector_Params()
        detector_params.filterByArea = True
        detector = cv2.SimpleBlobDetector_create(detector_params)
        gray_frame = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
        _, img = cv2.threshold(gray_frame, 80, 255, cv2.THRESH_BINARY)
        img = cv2.erode(img, None, iterations=2)  # 1
        img = cv2.dilate(img, None, iterations=4)  # 2
        img = cv2.medianBlur(img, 5)  # 3
        keypoints = detector.detect(img)
        try:
            print(keypoints[0].pt)
            eye = cv2.drawKeypoints(pic, keypoints, pic, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            #
            cv2.imshow("pi", pic)
            return keypoints[0].pt[0], keypoints[0].pt[1]
        except:
            raise Exception("no pupil")



