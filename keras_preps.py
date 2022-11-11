from PIL import Image
from tensorflow.keras.utils import img_to_array
import tensorflow as tf
import numpy as np
import labels
from globals import input_size, image_size
import cv2
import uuid
import os
__uuid__ = ""

def load_model():
    f = open('./models/current_version.txt')
    model_used = f.read()
    model = tf.keras.models.load_model('./models/' + model_used )
    model.predict(tf.zeros([1, input_size, input_size , 1]))
    print("model ready")
    return model

def preprocess_drawing(img):
    global __uuid__
    __uuid__ = str(uuid.uuid1())
    os.mkdir("temp/" + __uuid__)
    img_path = "temp/" + __uuid__ + "/original.png"
    img.save(img_path)
    contours = find_contours(img_path)
    x,y,w = bounding_box(contours)
    img = img.crop((x, y, w, img.height))
    img = img.resize(size = image_size)
    img = img.convert('L')
    img.save("temp/" + __uuid__ + "/processed.png")
    tensor_img = img_to_array(img)
    tensor_img = tf.expand_dims(tensor_img, 0)
    return tensor_img

def analysis(tensor_img, model):
    predictions = model.predict(tensor_img)
    #print(predictions)
    classes = np.argmax(predictions[0])
    #print(classes)
    result = labels.labels[classes]
    return(result)

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
    #print("x: " + str(min_x) + " y: " + str(min_y) + " w: " + str(max_w))
    return min_x , min_y, max_w

