import sys
import tty
from rgb import Rgb_Handler
from thermal import Thermal_Handler
import cv2
import select

def key_is_pressed(a_key):
    if (True == select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])):
        c = sys.stdin.read(1)
        if c == a_key: 
            return True
        else:
            return False
    return False

def begin_data_stream():
    rgb_img_num = 0
    thermal_img_num = 0
    tty.setcbreak(sys.stdin.fileno())
    
    rgb_handler = Rgb_Handler(0, 60)
    # thermal_handler = Thermal_Handler(60)

    while True:
        # print("flag AAA")
        rgb_frame = rgb_handler.get_frame()
        rgb_handler.print_fps()
        # thermal_frame = thermal_handler.get_frame()
        # print("flag A")
        cv2.imshow("rgb frame", rgb_frame)
        # cv2.imshow("thermal frame", thermal_frame)
        # print("flag B")
        if (key_is_pressed("a") == True):
            cv2.imwrite("rgb{}.jpg".format(rgb_img_num), rgb_frame)
            rgb_img_num += 1
        # print("flag C")
        if (key_is_pressed("b") == True):
            # cv2.imwrite("thermal{}.jpg".format(thermal_img_num), thermal_frame)
            thermal_img_num += 1
        # print("flag D")
        if (key_is_pressed("q") == True):
            rgb_handler.release()
            # thermal_handler.release()
            cv2.destroyAllWindows()
        # print("flag E")
begin_data_stream()