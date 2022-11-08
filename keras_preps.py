from PIL import Image
from tensorflow.keras.utils import img_to_array
import tensorflow as tf
import numpy as np
import labels
from globals import input_size, image_size
import cv2

def load_model():
    f = open('./models/current_version.txt')
    model_used = f.read()
    model = tf.keras.models.load_model('./models/' + model_used )
    model.predict(tf.zeros([1, input_size, input_size , 1]))
    print("model ready")
    return model

def preprocess_drawing(img):
    img_path = "temp/temp.png"
    img.save(img_path)
    contours = find_contours(img_path)
    x,y,w,h = bounding_box(contours)
    img = img.crop((y, x, x + w, img.height))
    img = img.resize(size = image_size)
    img = img.convert('L')
    tensor_img = img_to_array(img)
    tensor_img = tf.expand_dims(tensor_img, 0)
    return tensor_img

def analysis(tensor_img, model):
    predictions = model.predict(tensor_img)
    print(predictions)
    classes = np.argmax(predictions[0])
    print(classes)
    result = labels.labels[classes]
    return(result)

def find_contours(img_path):
    
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(img_grey, 100, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    img_contours = np.zeros(img.shape)
    cv2.drawContours(img_contours, contours, -1, (0,255,0), 3)
    cv2.imwrite('temp/contours.jpg', img_contours)
    return contours


def bounding_box(contours):
    img_contours = cv2.imread('temp/contours.jpg')
    for contour in contours: 
        x,y,w,h = cv2.boundingRect(contour)
        cv2.rectangle(img_contours, (x, y), (x+w, y+h), (0,255,0), 3)
        
    cv2.imwrite('temp/contours.jpg', img_contours)
    return x,y,w,h

