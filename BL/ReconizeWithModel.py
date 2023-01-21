import os
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.utils import load_img,img_to_array
from tensorflow.keras.models import load_model


categorys={0: 'apple', 1: 'banana', 2: 'beetroot', 3: 'bell pepper', 4: 'cabbage', 5: 'capsicum', 6: 'carrot',
          7: 'cauliflower', 8: 'chilli pepper', 9: 'corn', 10: 'cucumber', 11: 'eggplant', 12: 'garlic', 13: 'ginger',
          14: 'grapes', 15: 'jalepeno', 16: 'kiwi', 17: 'lemon', 18: 'lettuce',
          19: 'mango', 20: 'onion', 21: 'orange', 22: 'paprika', 23: 'pear', 24: 'peas', 25: 'pineapple',
          26: 'pomegranate', 27: 'potato', 28: 'raddish', 29: 'soy beans', 30: 'spinach', 31: 'sweetcorn',
          32: 'sweetpotato', 33: 'tomato', 34: 'turnip', 35: 'watermelon'}
'''
    {0: "apple",
           2: "avocado",
           1: "banana",
           3: "cherry",
           4: "kiwi",
           5:"mango",
           6: "orange",
           7: "pinenapple",
           8: "strawberries",
           9: "watermelon"
          }'''
model = load_model("model/FV.h5")
basic_path= "../DAL/dataset/all_data/test/"

img_width, img_height = 224, 224
a=0
countCorect=0
channels =3
l=[]
for category in ["apple/","avocado/", "banana/","cherry/", "kiwi/","mango/", "orange/","pinenapple/", "strawberries/","watermelon/"]:
    path = basic_path + category#"gdrive/MyDrive/data_sets/cats_dogs/PetImages/test/"+category
    miniA = 0
    miniC = 0
    for i in os.listdir(path):
      img = load_img(path+i, grayscale=False,target_size=(img_width, img_height)) # grayscale-black or white

      #plt.matshow(img) # func - take the array and show as a matrix
      #plt.show()
      img = img_to_array(img)
      img = img.reshape(1, img_width, img_height, channels).astype('float32')
      img = img / 255.0 # Normalization

      preds = model.predict(img)
      print(i)
      print("the result: ", categorys[np.argmax(preds)])
      print("predictions:{} category:{}".format(preds,np.argmax(preds))) # argmax - returns indices of the max element of the array in a particular axis.
      a += 1
      miniA+=1
      if(categorys[np.argmax(preds)] in category):
        countCorect+=1
        miniC+=1
    l.append(category +': '+ str(miniA)+", "+ str(miniC) +", "+ str(miniC/miniA))
for h in l:
    print(h)
print(a, countCorect)
print(countCorect/a)