from PIL import Image
from tensorflow.keras.utils import img_to_array
import tensorflow as tf
import numpy as np
import labels
import drawing_tool
from globals import input_size

def load_model():
    f = open('./models/current_version.txt')
    model_used = f.read()
    model = tf.keras.models.load_model('./models/' + model_used )
    model.predict(tf.zeros([1, input_size, input_size , 1]))
    return model

def preprocess_drawing(coordinates):
    img = drawing_tool.draw_image_from_coordinates(coordinates)
    tensor_img = img_to_array(img)
    tensor_img = tf.expand_dims(tensor_img, 0)
    tensor_img /= 255
    return tensor_img

def analysis(tensor_img, model):
    predictions = model.predict(tensor_img)
    print(predictions)
    classes = np.argmax(predictions[0])
    print(classes)
    result = labels.labels[classes]
    print(result)
    return(result)


