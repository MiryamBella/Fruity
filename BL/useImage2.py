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
           8: "strawberries",
           9: "watermelon"
          }
resultPrint=""
for Pmodel in os.listdir("model/"):
    model = load_model("model/"+Pmodel)
    basic_path= "../DAL/dataset/clientsImage/"
    img_width, img_height = 150, 150
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
          img = img_to_array(img)
          img = img.reshape(1, img_width, img_height, channels).astype('float32')
          img = img / 255.0 # Normalization

          preds = model.predict(img)
          #print(i)
          #print("the result: ", categorys[np.argmax(preds)])
          #print("predictions:{} category:{}".format(preds,np.argmax(preds))) # argmax - returns indices of the max element of the array in a particular axis.
          a += 1
          miniA+=1
          if(categorys[np.argmax(preds)] in category):
            countCorect+=1
            miniC+=1
        l.append(category +': '+ str(miniA)+", "+ str(miniC) + ", "+ str(round(miniC/miniA, 3)) )
    resultPrint+="model name: "+ Pmodel+'\n'
    for h in l:
        resultPrint+=str(h) +"\n"
    resultPrint+= a +' ' +countCorect+"\n"
    resultPrint+= str(round(countCorect/a, 3))+'\n'
    resultPrint+= "------------------------------------------------------"+ '\n'

print(resultPrint)




