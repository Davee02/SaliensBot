import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui

pyautogui.PAUSE = 0.001

last_time = time.time()
start_time = time.time()
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))
lower_range = np.array([90,100,50], np.uint8)
upper_range = np.array([100,250,250], np.uint8)

while(time.time() - start_time < 119):
    print(time.time() - start_time)
    screen = np.array(ImageGrab.grab(bbox=(637,380,1590,860)))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)

    print("FPS: {}".format(1/(time.time() - last_time)))
    last_time = time.time()

    mask = cv2.inRange(screen, lower_range, upper_range)
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

    _, conts,h=cv2.findContours(maskClose.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(screen,conts,-1,(255,0,0),3)
    
    for i in range(len(conts)):
            x,y,w,h=cv2.boundingRect(conts[i])
            pyautogui.click(x + 637, y + 405, clicks=5)
            pyautogui.press('1')
time.sleep(5)
pyautogui.click(970, 580)