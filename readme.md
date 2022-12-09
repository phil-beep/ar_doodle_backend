# Readme
## How to set up the project

This installation requires a Python version 3.9 or higher!

#### 1. Get pip

https://pip.pypa.io/en/stable/installation/

---

#### 2. Install and activate a virtual environment

Create the environment:

`$ python3 -m venv venv`

Start the environment and make sure it stays active while developing!

`$ source venv/bin/activate`

---

#### 3. Install Tensorflow

Next, install the latest version of Tensorflow (Version 2.x required !)

`$ pip install tensorflow`

For Apple users:

`$ pip install tensorflow-macos`

`$ pip install tensorflow-metal`

---

#### 4. Installing the dependencies

To run the project, you will need to install all the additional dependencies using pip:

`$ pip install -r requirements.txt`

---

#### 5. Preparing the Model

For this step you will need to write the quickdraw objects (fish, car, etc.) you want to train into the **labels.py** file. Make sure you put the objects in the same (alphabetical) order they appear in the official list.

Make sure you adjust the **n_classes** variable to the total number of model classes used in the in the **globals.py** file. You can also adjust parameters as epochs and image resolution.

Download the models:

`$ python get_dataset.py`


Train and save the model:

`$ python model_training.py`

---

#### 6. Select the best model

Our current best model is already placed inside the **/model**-folder. If you perform further training that exceeds the accuracry, simply replace the Keras files with the ones from the folder mentioned inside **models/current_version.txt**.

---

#### 7. Launch the server!
`$ uvicorn main:app --reload`