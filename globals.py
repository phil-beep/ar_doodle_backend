from labels import labels

input_size = 28
image_size = (input_size, input_size)
batch_size = 32
input_shape = (input_size, input_size, 1)
n_classes = len(labels)
epochs = 5
max_drawings = 1000
validation_split = 0.2