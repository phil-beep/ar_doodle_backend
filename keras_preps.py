from PIL import Image
from tensorflow.keras.utils import img_to_array
import tensorflow as tf
import numpy as np
import labels
from globals import input_size, image_size

def load_model():
    f = open('./models/current_version.txt')
    model_used = f.read()
    model = tf.keras.models.load_model('./models/' + model_used )
    model.predict(tf.zeros([1, input_size, input_size , 1]))
    print("model ready")
    return model

def preprocess_drawing(img):
    img = img.resize(size = image_size)
    img.show()
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


