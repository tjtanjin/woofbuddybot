from PIL import Image, ImageOps
from io import BytesIO
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import json

def classify_breed(chat_id, input_type):
    """
    This function loads the trained model to classify dogs
    Args:
        chat_id: id used to identify the sent media file
        input_type: format of file sent by user
    """
    #open image to classify
    img = Image.open('./input_media/{}.{}'.format(chat_id, input_type))

    #convert to jpg
    if input_type != "JPG" or input_type != "JPEG":
        img = img.convert('RGB')

    #process image
    img = img_processor(img)

    #load model
    model = load_model("./models/model.hdf5")

    #return classification
    class_number = np.argmax(model.predict(img), axis=-1)
    breed = map_to_class(class_number).replace("_", " ").title()
    return breed

def img_processor(img):
    """
    This function processes the image sent by the user to be fed to the trained model.
    Args:
        img: image sent by user
    """
    img = ImageOps.fit(img, (400, 400), Image.ANTIALIAS)
    # convert to numpy array
    img = img_to_array(img)
    img = img/255.
    img = np.expand_dims(img, axis=0)
    return img

def map_to_class(class_number):
    """
    This function maps the numerical class number to actual breed name of the dog.
    Args:
        class_number: identified class number of the dog
    """
    with open("./config/mapping.json", "r") as file:
        file = json.load(file)

    for key, value in file.items():
        if value == str(class_number.flat[0]):
            breed = key
            break
    return breed