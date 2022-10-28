import schemas
from PIL import Image, ImageDraw
from globals import image_size
canvas_size = 256


def draw_image_from_coordinates(drawing_container: schemas.Drawing):
    img = Image.new("RGB", (canvas_size, canvas_size), "white")
    draw = ImageDraw.Draw(img)

    # zip x,y coordinates
    strokes = (zip(stroke[0], stroke[1]) for stroke in drawing_container.drawing)

    #change function later depending on how drawing works in frontend
    render_stop_while_drawing(strokes, draw)
    #img.show()
    img = img.resize(size=image_size)
    img.show()
    return img

def render_stop_while_drawing(strokes, draw):

    for outer_container in strokes:
        extracted_coordinates = []
        for inner_container in outer_container:
            extracted_coordinates += inner_container
            draw.line(extracted_coordinates, fill="black", width = 2)


def render_dont_stop_while_drawing(strokes, draw):
    
    extracted_coordinates = []
    for outer_container in strokes:
        for inner_container in outer_container:
            extracted_coordinates += inner_container
            draw.line(extracted_coordinates, fill="black", width = 2)
    

