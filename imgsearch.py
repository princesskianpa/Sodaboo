###This here is from drov0 found it by accident while googling python stuff.
import cv2
import numpy as np
import pyautogui
import random
import time

def region_grabber(region):
    x1 = region[0]
    y1 = region[1]
    width = region[2]-x1
    height = region[3]-y1

    return pyautogui.screenshot(region=(x1,y1,width,height))

def imagesearcharea(image, x1,y1,x2,y2, precision=0.8, im=None) :
    if im is None :
        im = region_grabber(region=(x1, y1, x2, y2))
        #im.save('test.png')

    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc
