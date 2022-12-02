import cv2
import numpy as np
from keras_preps import __uuid__

def find_contours(img_path):
    
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(img_grey, 127, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    img_contours = np.zeros(img.shape)
    cv2.drawContours(img_contours, contours, -1, (0,255,0), 2)
    cv2.imwrite("temp/" + __uuid__ + "/contours.png", img_contours)
    return contours


def bounding_box(contours):
    img_contours = cv2.imread("temp/" + __uuid__ + "/contours.png")
    height, width, *_ = img_contours.shape
    
    min_x = width
    min_y = height
    max_w = 0
    max_h = 0
    
    for contour in contours:
        x,y,w,h = cv2.boundingRect(contour)

        if x < min_x: min_x = x
        if (x+w) > 0: max_w = (x+w)
        if y < min_y: min_y = y
        if (y+h) > 0: max_h= (y+h)
        
    cv2.rectangle(img_contours, (min_x, min_y), (max_w, max_h), (0,255,0), 2)
        
    cv2.imwrite("temp/" + __uuid__ + "/contours.png", img_contours)
    return min_x , min_y, max_w