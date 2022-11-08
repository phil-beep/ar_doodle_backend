from globals import *
import datetime, os
from matplotlib import pyplot as plt
import random

from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.models import Sequential
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.keras.metrics import sparse_categorical_accuracy
from tensorflow.keras.layers.experimental.preprocessing import Rescaling, RandomFlip, RandomRotation, RandomWidth, RandomHeight
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout, BatchNormalization
from tensorflow.keras.callbacks import TensorBoard, EarlyStopping


train_ds = image_dataset_from_directory(
    "dataset",
    validation_split=validation_split,
    subset="training",
    seed=123,
    color_mode="grayscale",
    image_size=image_size,
    batch_size=batch_size
)

val_ds = image_dataset_from_directory(
    "dataset",
    validation_split=validation_split,
    subset="validation",
    seed=123,
    color_mode="grayscale",
    image_size=image_size,
    batch_size=batch_size
)

#configuring the network
model = Sequential([
    Rescaling(1. / 255, input_shape=input_shape),
    BatchNormalization(),

    Conv2D(6, kernel_size=(3, 3), padding="same", activation="relu"),
    Conv2D(8, kernel_size=(3, 3), padding="same", activation="relu"),
    Conv2D(10, kernel_size=(3, 3), padding="same", activation="relu"),
    BatchNormalization(),
    MaxPooling2D(pool_size=(2, 2)),

    Flatten(),

    Dense(700, activation='relu'),
    BatchNormalization(),
    Dropout(0.2),

    Dense(500, activation='relu'),
    BatchNormalization(),
    Dropout(0.2),

    Dense(400, activation='relu'),
    Dropout(0.2),

    Dense(n_classes, activation='softmax')
])

model.compile(
    optimizer="adam",
    loss=SparseCategoricalCrossentropy(),
    metrics=["accuracy"]
)

model.summary()

version = str(epochs) + "_" + str(max_drawings) + "_" + str(validation_split) + "_" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
logdir = os.path.join("logs",version)
tensorboard = TensorBoard(logdir,  histogram_freq=1)
callbacks = EarlyStopping(restore_best_weights=True)

#training the model
model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs,
    verbose=1,
    callbacks = [tensorboard, callbacks]
)

def save_model():
    increment_version()
    model.save('./models/model_' + version)


def increment_version():
    f = open("./models/current_version.txt", "w")
    v = 'model_' + version
    f.write(v)
    f.close()

save_model()