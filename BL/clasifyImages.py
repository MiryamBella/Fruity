#this file are not use in project, but for testing the model.

'''import os
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.utils import load_img,img_to_array
from tensorflow.keras.models import load_model
import matplotlib.image as mpimg



def plot_images(images, labels, sp=3):
    fig, axes = plt.subplots(sp, sp)
    fig.subplots_adjust(hspace=1, wspace=0.3)

    for i, ax in enumerate(axes.flat):
        # Plot image
        ax.imshow(mpimg.imread(images[i]))

        # Plot label
        ax.set_xlabel('Label : %s' % labels[i])

    plt.show()



categorys= {0: "apple",
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
model = load_model("model/FV.h5")
basic_path= "../DAL/dataset/clientsImage/"

img_width, img_height = 224,224 #150, 150
a=0
countCorect=0
channels =3
l=[]
path = basic_path# + category#"gdrive/MyDrive/data_sets/cats_dogs/PetImages/test/"+category
miniA = 0
miniC = 0
listImage=[]
labels=[]
for i in os.listdir(path):
    img = load_img(path+i, grayscale=False,target_size=(img_width, img_height)) # grayscale-black or white

    #plt.matshow(img) # func - take the array and show as a matrix
    #plt.show()
    img = img_to_array(img)
    img = img.reshape(1, img_width, img_height, channels).astype('float32')
    img = img / 255.0 # Normalization

    preds = model.predict(img)
    #listImage.append(path+i)
    #labels.append(categorys[np.argmax(preds)])
    print(i)
    print("the result: ", categorys[np.argmax(preds)])
    #print("predictions:{} category:{}".format(preds,np.argmax(preds))) # argmax - returns indices of the max element of the array in a particular axis.
    #a+=1
#plot_images(listImage, labels, 5)
#print(a, countCorect)
#print(countCorect/a)



'''