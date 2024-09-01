import os
import matplotlib.pyplot as plt
import numpy as np
# from tensorflow.keras.utils import load_img,img_to_array
import keras.utils as Image
from keras.src.utils import img_to_array
# from tensorflow.keras.models import load_model
import tensorflow as tf



class Identify:
    def __init__(self, instance_path=""):
        self.pathModel = os.path.join(instance_path, "../services/identifyFruits/model/keras3/fruitsModel_keras3_seperet.keras")
        self.basicPath_train = os.path.join(instance_path, "../../DAL/dataset/all_data/train/")
        self.basicPath_test = os.path.join(instance_path, "../../DAL/dataset/all_data/test/")
        self.clientsImagePath = os.path.join(instance_path, "../DAL/dataset/clientsImage/")
        self.model = tf.keras.models.load_model(self.pathModel)
        self.categorys = {0: "apple",
                          2: "avocado",
                          1: "banana",
                          3: "cherry",
                          4: "kiwi",
                          5: "mango",
                          6: "orange",
                          7: "pinenapple",
                          8: "strawberries",
                          9: "watermelon"
                          }


    def __str__(self):
        returnstr= "the model path: " +self.pathModel + '\n'+ self.model.summary()
        return returnstr

    def identifyObject(self, name_image):
        img_width, img_height = 200, 200
        channels = 3
        img = Image.load_img(self.clientsImagePath + name_image, target_size=(img_width, img_height))
        img = img_to_array(img)
        img = img.reshape(1, img_width, img_height, channels).astype('float32')
        img = img / 255.0  # Normalization

        preds = self.model.predict(img)
        print("the result: ", self.categorys[np.argmax(preds)])
        print("predictions:{}\ncategory:{}".format(preds, np.argmax(preds)))  # argmax - returns indices of the max element of the array in a particular axis.

        return self.categorys[np.argmax(preds)]





