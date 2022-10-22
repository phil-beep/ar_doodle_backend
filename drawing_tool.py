import schemas
from PIL import Image, ImageDraw

canvas_size = 256
img = Image.new("RGB", (canvas_size, canvas_size), "white")
draw = ImageDraw.Draw(img)

def draw_image(drawing_container: schemas.Drawing):

    # zip x,y coordinates
    strokes = (zip(stroke[0], stroke[1]) for stroke in drawing_container.drawing)

    #change function later depending on how drawing works in frontend
    render_stop_while_drawing(strokes)
    #img.show()
    resized = img.resize(size=(28, 28))
    return resized;

def render_stop_while_drawing(strokes):

    for outer_container in strokes:
        extracted_coordinates = []
        for inner_container in outer_container:
            extracted_coordinates += inner_container
            draw.line(extracted_coordinates, fill="black", width = 2)


def render_dont_stop_while_drawing(strokes):
    
    extracted_coordinates = []
    for outer_container in strokes:
        for inner_container in outer_container:
            extracted_coordinates += inner_container
            draw.line(extracted_coordinates, fill="black", width = 2)
    

