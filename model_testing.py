from keras_preps import load_model, preprocess_drawing, analysis
from main import identify_picture
from PIL import Image
from globals import canvas_size

def testing():
    model = load_model()

    #add file names from test_data folder here
    images = [
        #"crab1",
        #"fish1"
    ]

    result = ""

    for image in images:
        prediction = testing_with(image, model)
        result += "\n" + image + "->" + prediction
    
    print(result)
    

def testing_with(image_name, model):
    img = Image.open("test_data/" + image_name + ".png")
    img = img.resize(size=(canvas_size,canvas_size))
    tensor_img = preprocess_drawing(img)
    return analysis(tensor_img, model)


testing()