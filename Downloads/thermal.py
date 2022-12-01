import cv2
import time
import sys
import select
import tty
import termios
import numpy as np
import cv2
from flirpy.camera.boson import Boson
from datetime import datetime as dt
import csv
import os
import sys
# import matplotlib.pyplot as plt
import winsound
from win32com.client import Dispatch
import shutil

class Thermal_Handler:

    def __init__(self, fps_cap = 60):
        device_index = Boson.find_video_device()
        self.cap = cv2.VideoCapture(device_index)
        self.cap.set(5, fps_cap)

        if not self.cap.isOpened():
            print("Cannot open camera")
            exit()

        self.framecount = 0
        self.prevMillis = 0

        print(self.cap.get(5))

    def print_fps(self):
        global prevMillis
        global framecount
        millis = int(round(time.time() * 1000))
        framecount += 1
        if millis - prevMillis > 1000:
            print(framecount)
            prevMillis = millis 
            framecount = 0
    
    def get_frame(self):
        ret, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if not ret:
            print("Can't receive frame (stream end?).")
            sys.exit(1)

        # cv2.imshow("frame", frame)
        return frame
    
    def release (self):
        self.cap.release()