import os
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.utils import load_img,img_to_array
from tensorflow.keras.models import load_model

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