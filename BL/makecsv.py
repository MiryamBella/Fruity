import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.utils import load_img,img_to_array
from tensorflow.keras.models import load_model
'''
dir_train='dataset/all_data/train/'
dir_test='dataset/all_data/test/'


dir_train_banana = 'dataset/all_data/train/banana'
dir_train_kiwi = 'dataset/all_data/train/kiwi'
dir_train_Apple = 'dataset/all_data/train/Apple'
dir_train_avocado = 'dataset/all_data/train/avocado'
dir_train_cherry     = 'dataset/all_data/train/cherry'
dir_train_mango = 'dataset/all_data/train/mango'
dir_train_orange = 'dataset/all_data/train/orange'
dir_train_pinenapple = 'dataset/all_data/train/pinenapple'
dir_train_strawberries = 'dataset/all_data/train/strawberries'
dir_train_watermelon = 'dataset/all_data/train/watermelon'

train=makeDataset([dir_train_banana, dir_train_kiwi, dir_train_Apple, dir_train_avocado, dir_train_cherry, dir_train_mango, dir_train_orange, dir_train_pinenapple, dir_train_strawberries, dir_train_watermelon],
                  ["banana/", "kiwi/", "Apple/", "avocado/", "cherry/", "mango/", "orange/", "pinenapple/", "strawberries/","watermelon/"])
print(train)
train.to_csv("train.csv")


dir_train_banana = 'dataset/all_data/test/banana'
dir_train_kiwi = 'dataset/all_data/test/kiwi'
dir_train_Apple = 'dataset/all_data/test/Apple'
dir_train_avocado = 'dataset/all_data/test/avocado'
dir_train_cherry = 'dataset/all_data/test/cherry'
dir_train_mango = 'dataset/all_data/test/mango'
dir_train_orange = 'dataset/all_data/test/orange'
dir_train_pinenapple = 'dataset/all_data/test/pinenapple'
dir_train_strawberries = 'dataset/all_data/test/stawberries'
dir_train_watermelon = 'dataset/all_data/test/watermelon'



test=makeDataset([dir_train_banana, dir_train_kiwi, dir_train_Apple, dir_train_avocado, dir_train_cherry, dir_train_mango, dir_train_orange, dir_train_pinenapple, dir_train_strawberries, dir_train_watermelon],
                  ["banana/", "kiwi/", "apple/", "avocado/", "cherry/", "mango/", "orange/", "pinenapple/", "stawberries/","watermelon/"])
print(test)

test.to_csv("test.csv")'''

categorys={0: "apple",
           2: "avocado",
           1: "banana",
           3: "cherry",
           4: "kiwi",
           5:"mango",
           6: "orange",
           7: "pinenapple",
           8: "stawberries",
           9: "watermelon"
          }
model = load_model("fruitsModel.h5")
path= "dataset/apple/test/"

img_width, img_height = 150, 150
a=0
countCorect=0
channels =3
for i in os.listdir(path):
  img = load_img(path+i, grayscale=False,target_size=(img_width, img_height)) # grayscale-black or white

  #plt.matshow(img) # func - take the array and show as a matrix
  #plt.show()
  img = img_to_array(img)
  img = img.reshape(1, img_width, img_height, channels).astype('float32')
  img = img / 255.0 # Normalization

  preds = model.predict(img)
  print("the result: ", categorys[np.argmax(preds)])
  print("predictions:{} category:{}".format(preds,np.argmax(preds))) # argmax - returns indices of the max element of the array in a particular axis.
  a += 1
  if(categorys[np.argmax(preds)] in "apple" ):
    countCorect+=1
print(a, countCorect)
print(countCorect/a)
