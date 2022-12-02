import schemas
from PIL import Image, ImageDraw
from globals import canvas_size

def draw_image_from_coordinates(drawing_container: schemas.Drawing):
    canvas = Image.new("RGB", (canvas_size, canvas_size), "white")
    coords = (zip(stroke[0], stroke[1]) for stroke in drawing_container.drawing)
    img = render_unity_pixels(coords, canvas)
    return img

def render_unity_pixels(coords, canvas):
    extracted_coordinates = []
    for outer_container in coords:
        for inner_container in outer_container:
            extracted_coordinates += inner_container
            canvas.putpixel((inner_container), (0,0,0))
    return canvas
    

