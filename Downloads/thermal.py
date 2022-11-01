import cv2
import time

import sys
import select
import tty
import termios

cap = cv2.VideoCapture(2)
cap.set(5, 60)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

framecount = 0
prevMillis = 0

print(cap.get(5))

def fpsCount():
    global prevMillis
    global framecount
    millis = int(round(time.time() * 1000))
    framecount += 1
    if millis - prevMillis > 1000:
        print(framecount)
        prevMillis = millis 
        framecount = 0

def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def loopCamera(camera):
    img_num = 0
    tty.setcbreak(sys.stdin.fileno())

    while True:

        ret, frame = camera.read()
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #blur = cv2.blur(frame, (5, 5))
        #ret, thresh = cv2.threshold(blur, 170, 255, 0)
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        cv2.imshow("frame", frame)

        # fpsCount()    
        # k = cv2.waitKey(1) & 0xff
        # if k == 27:
        #     print("hererererere")
        #     break

        if isData():
            c = sys.stdin.read(1)
            if c == 'a': 
                cv2.imwrite("thermal{}.jpg".format(img_num), frame)
                img_num += 1
    


loopCamera(cap)

cap.release()
cv2.destroyAllWindows()