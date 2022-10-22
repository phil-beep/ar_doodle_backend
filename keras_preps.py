from PIL import Image
from tensorflow.keras.utils import img_to_array
import tensorflow as tf
import numpy as np
import labels

def analysis(img: Image):
    f = open('./models/current_version.txt')
    model_used = f.read()
    model = tf.keras.models.load_model('./models/' + model_used )
    model.predict(tf.zeros([1, 28, 28, 1]))
    
    tensor_img = img_to_array(img)
    tensor_img = tf.expand_dims(tensor_img, 0)
    tensor_img /= 255.

    predictions = model.predict(tensor_img)
    classes = np.argmax(predictions, axis=1)

    result = labels.labels[classes[0]]

    return(result)