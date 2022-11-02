import string
from fastapi import FastAPI
import schemas
from PIL import Image
from keras_preps import *

app = FastAPI()
model = load_model()

@app.get("/identify_drawing/")
def identify_drawing(drawing_coordinates: schemas.Drawing):
    img = drawing_tool.draw_image_from_coordinates(drawing_coordinates)
    tensor_img = preprocess_drawing(img)
    return analysis(tensor_img, model)


#debug route to load any image from the dataset
@app.get("/training_data/{animal}/{image_name}")
def identify_picture(animal, image_name):
    img = Image.open("dataset/" + animal + "/" + image_name + ".png").convert('L')
    tensor_img = preprocess_drawing(img)
    return analysis(tensor_img, model)


@app.get("/test_data/{image_name}")
def identify_picture(image_name):
    img = Image.open("test_data/" + image_name + ".png").convert('L')
    tensor_img = preprocess_drawing(img)
    return analysis(tensor_img, model)


@app.post("/file_path/")
def image_from_file_path(file_path: schemas.File_path):
    img = Image.open(file_path.imageLocation).convert('L')
    tensor_img = preprocess_drawing(img)
    return analysis(tensor_img, model)
