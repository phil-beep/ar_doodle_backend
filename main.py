from fastapi import FastAPI
import schemas
import tensorflow as tf
import drawing_tool

app = FastAPI()

@app.get("/identify_drawing/")
def identify_drawing(drawing: schemas.Drawing):
    drawing_tool.draw_image(drawing)
    return tf_analysis(drawing);

def tf_analysis(drawing: schemas.Drawing):

    #todo: connect with tensorflow api
    return(tf.__version__)

