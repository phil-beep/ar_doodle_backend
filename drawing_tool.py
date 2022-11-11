import schemas
from PIL import Image, ImageDraw
from globals import canvas_size

def draw_image_from_coordinates(drawing_container: schemas.Drawing):
    canvas = Image.new("RGB", (canvas_size, canvas_size), "white")
    coords = (zip(stroke[0], stroke[1]) for stroke in drawing_container.drawing)
    img = render_unity_pixels(coords, canvas)
    return img

#debug only, will be removed, use unity coordinates
def render_quickdraw_strokes(coords, canvas):
    x = ImageDraw.Draw(canvas)

    for outer_container in coords:
        extracted_coordinates = []
        for inner_container in outer_container:
            extracted_coordinates += inner_container
            x.line(extracted_coordinates, fill="black", width = 2)
    
    return canvas


def render_unity_pixels(coords, canvas):
    
    extracted_coordinates = []
    for outer_container in coords:
        for inner_container in outer_container:
            extracted_coordinates += inner_container
            canvas.putpixel((inner_container), (0,0,0))
    
    return canvas
    

