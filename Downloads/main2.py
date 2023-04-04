import sys
import os
# from seg import h_seg
from rgb import Rgb_Handler
from thermal import Thermal_Handler
import cv2
import select
import time
from tkinter import *
from PIL import Image, ImageTk

# modules for button press
# TODO Uncomment for prod
# import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

class Data_Collector():
    def __init__(self):
        # TODO Uncomment for prod
        # GPIO.setwarnings(False) # Ignore warning for now
        # GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
        # GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
        self.take_pictures = False

        self.rgb_handler = Rgb_Handler(0, 60)

        # GUI member variables
        self.window = Tk()
        self.window.title("Camera GUI")

        # Create a label for displaying the video feed
        self.label = Label(self.window)
        self.label.pack(padx=10, pady=10)

    def _button_callback(self, channel):
        self.take_pictures = not (self.take_pictures)

    def _render (self):
        rgb_frame = self.rgb_handler.get_frame()

        img = Image.fromarray(rgb_frame)
        imgtk = ImageTk.PhotoImage(image=img)

        # update the label with the new image
        self.label.imgtk = imgtk
        self.label.config(image=imgtk)

        self.window.after(10, self._render)

    def begin_data_stream(self):
        # GPIO.add_event_detect(10,GPIO.RISING, callback = self._button_callback)
     
        window = Tk()
        window.title("Camera GUI")

        # Create a label for displaying the video feed
        label = Label(window)
        label.pack(padx=10, pady=10)
        
        # rgb_handler = Rgb_Handler(2, 60)
        # thm_handler = Thermal_Handler(0,60)

        usb_path_rgb = "/media/pi/DCA5-2D88/rgb_images"
        usb_path_thm = "/media/pi/DCA5-2D88/thm_images"

        self._render()

        self.window.mainloop()
        # TODO Uncomment for prod
        # GPIO.cleanup()

Data_Collector().begin_data_stream()

'''
foo():
    self.GO = !(self.GO)
add_event(foo)
while True:
    if (self.GO):
        # do stuff

    else:
        continue


'''

'''
foo():
    self.GO = !(self.GO)
add_event(foo)
while True:
    if (self.GO):
        # do stuff
    else:
        continue
'''