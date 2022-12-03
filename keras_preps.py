from PIL import Image
from tensorflow.keras.utils import img_to_array
import tensorflow as tf
import numpy as np
import labels
from globals import input_size, image_size, __uuid__
from contour_finding import find_contours, bounding_box
import uuid
import os

def load_model():
    model = tf.keras.models.load_model('./model/')
    model.predict(tf.zeros([1, input_size, input_size , 1]))
    print("model ready")
    return model

def preprocess_drawing(img):
    global __uuid__
    __uuid__ = str(uuid.uuid1())
    if not os.path.exists("temp"):
        os.makedirs("temp")

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
    classes = np.argmax(predictions[0])
    result = labels.labels[classes]
    return(result)


