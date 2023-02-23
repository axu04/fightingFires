import sys
import os
from rgb import Rgb_Handler
from thermal import Thermal_Handler
import cv2
import select
# send help

def key_is_pressed(a_key):
    if (True == select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])):
        c = sys.stdin.read(1)
        if c == a_key: 
            return True
        else:
            return False
    else:
        return False

def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def begin_data_stream():
    img_num = 0
    
    rgb_handler = Rgb_Handler(2, 60)
    thm_handler = Thermal_Handler(0,60)

    usb_path_rgb = "D:/rgb_images"
    usb_path_thm = "D:/thm_images"

    while True:
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

        img_num += 1

begin_data_stream()