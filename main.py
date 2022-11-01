import string
from fastapi import FastAPI
import schemas
from PIL import Image
from keras_preps import *

app = FastAPI()

@app.get("/identify_drawing/")
def identify_drawing(drawing_coordinates: schemas.Drawing):
    model = load_model()
    img = preprocess_drawing(drawing_coordinates)
    return analysis(img, model)


#debug route to load any image from the dataset
@app.get("/{animal}/{image_name}")
def identify_picture(animal, image_name):
    model = load_model()
    
    img = Image.open("dataset/" + animal + "/" + image_name + ".png").convert('L')
    img.show()
    tensor_img = img_to_array(img)
    tensor_img = tf.expand_dims(tensor_img, 0)
    tensor_img /= 255
    return analysis(tensor_img, model)

@app.post("/file_path/")
def image_from_file_path(file_path: schemas.File_path):
    
    img = Image.open(file_path.imageLocation)
    model = load_model()
    return analysis(img, model)
