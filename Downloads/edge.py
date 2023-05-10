import cv2
import numpy as np

cam = cv2.VideoCapture(2)

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    
    edges = cv2.Canny(image=blur, threshold1=50, threshold2=100)
    
    cv2.imshow('test', edges)
    cv2.waitKey(1)
    
