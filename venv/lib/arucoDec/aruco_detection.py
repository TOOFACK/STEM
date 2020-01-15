import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
marker_size = 8

calib_path = ''
camera_matrix = np.loadtxt('/home/pavel/Рабочий стол/CameraMatrix.txt', delimiter=',')
camera_distorion = np.loadtxt('/home/pavel/Рабочий стол/CameraDistortion.txt', delimiter=',')



aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_ARUCO_ORIGINAL)
parameters = aruco.DetectorParameters_create()



cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    corners, ids, rejected = aruco.detectMarkers(image=gray, dictionary=aruco_dict, parameters=parameters)
    if ids != None:
        aruco.drawDetectedMarkers(frame, corners)
        print(ids)
        ids = None


    cv2.imshow('frame', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
