import sys
import os
from rgb import Rgb_Handler
from thermal import Thermal_Handler
import cv2
import select
# modules for button press
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

class Data_Collector():
    def __init__(self):
        GPIO.setwarnings(False) # Ignore warning for now
        GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
        self.take_pictures = False

    def _button_callback(self, channel):
        self.take_pictures = not (self.take_pictures)

    def begin_data_stream(self):
        GPIO.add_event_detect(10,GPIO.RISING, callback = self._button_callback)
        img_num = 0
        
        rgb_handler = Rgb_Handler(2, 60)
        thm_handler = Thermal_Handler(0,60)

        usb_path_rgb = "/media/pi/DCA5-2D88/rgb_images"
        usb_path_thm = "/media/pi/DCA5-2D88/thm_images"

        while True:
            if (self.take_pictures == True):
                rgb_frame = rgb_handler.get_frame()
                rgb_handler.print_fps()

                thm_frame = thm_handler.get_frame()

                # displays the image 
                #cv2.imshow("rgb frame", rgb_frame)
                #cv2.imshow("thm frame", thm_frame)
                
                filename_rgb = f"rgb{img_num}.jpg"
                filename_thm = f"thm{img_num}.jpg"
                
                save_path_rgb = os.path.join(usb_path_rgb, filename_rgb)
                save_path_thm = os.path.join(usb_path_thm, filename_thm)

                cv2.imwrite(save_path_rgb, rgb_frame)
                cv2.imwrite(save_path_thm, thm_frame)
                
                cv2.imshow('rgb', rgb_frame)
                cv2.imshow('thermal', thm_frame)
                cv2.waitKey(1)

                img_num += 1
            else:
                continue
            
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