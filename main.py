from fastapi import Depends, FastAPI
import schemas
from PIL import Image
from keras_preps import load_model, preprocess_drawing, analysis
from drawing_tool import draw_image_from_coordinates
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from validation import validate

app = FastAPI(openapi_url=None)
security = HTTPBasic()
model = load_model()

@app.post("/identify_drawing/")
def identify_drawing(drawing_coordinates: schemas.Drawing, creds : HTTPBasicCredentials = Depends(security)):
    
    validate(creds);
    
    img = draw_image_from_coordinates(drawing_coordinates)
    tensor_img = preprocess_drawing(img)
    return analysis(tensor_img, model)

    

