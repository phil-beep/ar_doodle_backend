from pathlib import Path
from quickdraw import QuickDrawDataGroup, QuickDrawData
from PIL import Image
from globals import *
import labels


def generate_class_images(name, max_drawings, recognized):
    directory = Path("dataset/" + name)

    if not directory.exists():
        directory.mkdir(parents=True)

    images = QuickDrawDataGroup(name, max_drawings=max_drawings, recognized=recognized)
    for img in images.drawings:
        filename = directory.as_posix() + "/" + str(img.key_id) + ".png"
        img.get_image(stroke_width=3).resize(image_size).save(filename)


for label in labels.labels:
    generate_class_images(label, max_drawings, recognized=True)
