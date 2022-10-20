from fastapi import FastAPI
import schemas
import tensorflow as tf

app = FastAPI()

@app.get("/identify_drawing/")
def identify_drawing(drawing: schemas.Drawing):
    return tf_analysis(drawing);

def tf_analysis(drawing: schemas.Drawing):

    #todo: connect with tensorflow api
    return(tf.__version__)

