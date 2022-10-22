from fastapi import FastAPI
import schemas
import drawing_tool
from PIL import Image
from keras_preps import analysis

app = FastAPI()

@app.get("/identify_drawing/")
def identify_drawing(drawing: schemas.Drawing):
    img = drawing_tool.draw_image(drawing)
    return analysis(img)

