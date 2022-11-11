from fastapi import FastAPI
import schemas
from PIL import Image
from keras_preps import load_model, preprocess_drawing, analysis
from drawing_tool import draw_image_from_coordinates

app = FastAPI()
model = load_model()

@app.post("/identify_drawing/")
def identify_drawing(drawing_coordinates: schemas.Drawing):
    img = draw_image_from_coordinates(drawing_coordinates)
    tensor_img = preprocess_drawing(img)
    return analysis(tensor_img, model)


#debug route to load any image from the dataset
@app.post("/training_data/{animal}/{image_name}")
def identify_picture(animal, image_name):
    img = Image.open("dataset/" + animal + "/" + image_name + ".png")
    tensor_img = preprocess_drawing(img)
    return analysis(tensor_img, model)


@app.post("/test_data/{image_name}")
def identify_picture(image_name):
    img = Image.open("test_data/" + image_name + ".png")
    background = Image.new('RGBA', img.size, (255,255,255))
    img = Image.alpha_composite(background, img)
    tensor_img = preprocess_drawing(img)
    return analysis(tensor_img, model)


@app.post("/file_path/")
def image_from_file_path(file_path: schemas.File_path):
    img = Image.open(file_path.imageLocation)
    tensor_img = preprocess_drawing(img)
    return analysis(tensor_img, model)
