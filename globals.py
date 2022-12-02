from labels import labels

input_size = 128
image_size = (input_size, input_size)
batch_size = 64
input_shape = (input_size, input_size, 1)
n_classes = len(labels)
epochs = 20
max_drawings = 50000
validation_split = 0.2
canvas_size = 128
__uuid__ = ""