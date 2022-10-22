# Readme
## How to set up the project

This installation requires a Python version 3.9 or higher!

#### 1. Get pip

https://pip.pypa.io/en/stable/installation/

---

#### 2. Install and activate a virtual environment

We will use Anaconda for this installation.

Select and download the latest Miniforge3 installer for your OS:

https://github.com/conda-forge/miniforge/releases/tag/4.14.0-0

Create the environment:

`$ conda create --name tf`

Start the environment and make sure it stays active while developing!

`$ conda activate tf`

---

#### 3. Install Tensorflow

Next, install the latest version of Tensorflow (Version 2.x required !)

`$ pip install tensorflow`

For Apple users:

`$ pip install tensorflow-macos`

`$ pip install tensorflow-metal`

---

#### 4. Install and launch Docker

Download Docker:

https://docs.docker.com/get-docker/

`$ docker pull tensorflow/tensorflow:latest`

`$ docker run -it -p 8888:8888 tensorflow/tensorflow:latest-jupyter`

---

#### 5. Install Poetry

First,  you will need to install the dependency manager Poetry:

`$ pip install poetry`

After the installation has finished, let Poetry automatically install all the required dependencies of the project:

`$ poetry install`

---

#### 6. Preparing the Model

For this step you will need to write the quickdraw objects (fish, car, etc.) you want to train into the **labels.py** file. Make sure you put the objects in the same (alphabetical) order they appear in the official list.

Make sure you adjust the **n_classes** variable to the total number of model classes used in the in the **globals.py** file. You can also adjust parameters as epochs and image resolution.

Download the models:

`$ python get_models.py`


Train and save the model:

`$ python model_training.py`

---

#### 7. Launch the server!
`$ uvicorn main:app --reload`
