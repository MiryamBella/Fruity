'''
# Import dependencies
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.image as mpimg

dir_train_fruit= '../DAL/dataset/fruits/train/'

dir_train_apple = '../DAL/dataset/apple/train'
dir_test_apple = '../DAL/dataset/apple/test'
dir_train_banana = '../DAL/dataset/fruits/train/banana'
dir_train_kiwi = '../DAL/dataset/fruits/train/kiwi'
dir_test_banana  = '../DAL/dataset/fruits/test/banana'
dir_test_kiwi  = '../DAL/dataset/fruits/test/kiwi'


# explore the dataset - how many images in the training set?
path, dirs, files = next(os.walk(dir_train_banana))
file_count_train = len(files)
print("count train images banana:")
print(file_count_train)
# explore the dataset - how many images in the training set?
path, dirs, files = next(os.walk(dir_train_kiwi))
file_count_train += len(files)
print("count train images kiwi:")
print(file_count_train)

# and how many in the test set?
path, dirs, files = next(os.walk(dir_test_banana))
file_count_test = len(files)
print("count test images:")
print(file_count_test)
# and how many in the test set?
path, dirs, files = next(os.walk(dir_test_kiwi))
file_count_test = len(files)
print("count test images:")
print(file_count_test)

# make a dataset out of the images in the training dir
filenames_banana = os.listdir(dir_train_banana)
filenames_kiwi = os.listdir(dir_train_kiwi)
categories = []
for filename in filenames_banana:
    categories.append(1)
for i in range(len(filenames_banana)):
    filenames_banana[i]= 'banana/'+filenames_banana[i]
print(filenames_banana)
for filename in filenames_kiwi:
    filename= 'kiwi/'+filename
    categories.append(0)
for i in range(len(filenames_kiwi)):
    filenames_kiwi[i]= 'kiwi/'+filenames_kiwi[i]

df = pd.DataFrame({
    'filename': filenames_banana + filenames_kiwi,
    'category': categories
})
# how many dogs and cats?
print('number of banana: %d' % len(df[df.category==1]))
print('number of kiwi: %d' % len(df[df.category==0]))

# visualize the images



# Create figure with a specified number of subplots
def plot_images(images, labels, sp=3):
    fig, axes = plt.subplots(sp, sp)
    fig.subplots_adjust(hspace=1, wspace=0.3)

    for i, ax in enumerate(axes.flat):
        # Plot image
        ax.imshow(mpimg.imread(images[i]))

        # Plot label
        ax.set_xlabel('Label : %s' % labels[i])

    plt.show()

# visualize random images in the ori_dir
img_paths = []
img_labels = []

for i in range(9):
  # pick 9 random ids from the dataset
  rand_id = np.random.randint(0, file_count_train)

  # get the img path from the id
  filename = df.loc[rand_id, 'filename']
  path = os.path.join(dir_train_fruit, filename)
  img_paths.append(path)

  # get the img label from the id
  img_label = df.loc[rand_id, 'category']
  if img_label == 1:
    img_labels.append('banana')
  else:
    img_labels.append('kiwi')

plot_images(img_paths, img_labels)






from PIL import Image


# resize with white background instead of missing pixels
def resize_with_white_background(path_ori, path_dest):
    img = Image.open(path_ori)

    # resize and keep the aspect ratio
    img.thumbnail((224, 224), Image.LANCZOS)

    # add the white background
    img_w, img_h = img.size
    background = Image.new('RGB', (224, 224), (255, 255, 255))
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(img, offset)
    background.save('resizedTrain/' + path_dest)

from tqdm import tqdm

# run the function to resize all the images in the 'ori_dir'
for item in tqdm(df['filename']):
  file = dir_train_fruit + '/' + item
  resize_with_white_background(file, item)
'''





'''
import numpy
from tensorflow import keras
from keras.constraints import maxnorm
from keras.utils import np_utils

seed = 21

from keras.datasets import cifar10

# Loading in the data
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
print(X_train)

print("a")
# Normalize the inputs from 0-255 to between 0 and 1 by dividing by 255
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train = X_train / 255.0
X_test = X_test / 255.0
print("b")

# One-hot encode outputs
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
class_num = y_test.shape[1]

model = keras.Sequential()
model.add(keras.layers.layer1)
model.add(keras.layers.layer2)
model.add(keras.layers.layer3)


model = keras.Sequential([
    keras.layers.layer1,
    keras.layers.layer2,
    keras.layers.layer3
])


model = keras.Sequential()
model.add(keras.layers.Conv2D(32, (3, 3), input_shape=X_train.shape[1:], padding='same'))
model.add(keras.layers.Activation('relu'))


model.add(keras.layers.Conv2D(32, 3, input_shape=(32, 32, 3), activation='relu', padding='same'))


model.add(keras.layers.Dropout(0.2))


model.add(keras.layers.BatchNormalization())

model.add(keras.layers.Conv2D(64, 3, activation='relu', padding='same'))
model.add(keras.layers.MaxPooling2D(2))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.BatchNormalization())







#עעעעעעעעעעעעעעעע


model.add(keras.layers.Conv2D(64, 3, activation='relu', padding='same'))
model.add(keras.layers.MaxPooling2D(2))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.BatchNormalization())

model.add(keras.layers.Conv2D(128, 3, activation='relu', padding='same'))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.BatchNormalization())



model.add(keras.layers.Flatten())
model.add(keras.layers.Dropout(0.2))





model.add(keras.layers.Dense(32, activation='relu'))
model.add(keras.layers.Dropout(0.3))
model.add(keras.layers.BatchNormalization())


model.add(keras.layers.Dense(class_num, activation='softmax'))


model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy', 'val_accuracy'])


print(model.summary())



numpy.random.seed(seed)
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=25, batch_size=64)


# Model evaluation
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))



'''



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
    model = None
    model = load_model("model/"+Pmodel)
    basic_path= "../DAL/dataset/clientsImage/"
    img_width, img_height = 150, 150
    a=0
    countCorect=0
    channels =3
    l=[]
    path = basic_path #"gdrive/MyDrive/data_sets/cats_dogs/PetImages/test/"+category
    miniA = 0
    miniC = 0
    print(Pmodel)
    for i in os.listdir(path):
      img = load_img(path+i, grayscale=False,target_size=(img_width, img_height)) # grayscale-black or white
      img = img_to_array(img)
      img = img.reshape(1, img_width, img_height, channels).astype('float32')
      img = img / 255.0 # Normalization

      preds = model.predict(img)

      print("the result: ", categorys[np.argmax(preds)])
      #print("predictions:{} category:{}".format(preds,np.argmax(preds))) # argmax - returns indices of the max element of the array in a particular axis.
      #a += 1
      #miniA+=1
      #if(categorys[np.argmax(preds)] in category):
      #  countCorect+=1
      #  miniC+=1
    #l.append(category +': '+ str(miniA)+", "+ str(miniC) + ", "+ str(round(miniC/miniA, 3)) )
    #resultPrint+="model name: "+ Pmodel+'\n'
    #for h in l:
        #resultPrint+=str(h) +"\n"
    #resultPrint+= a +' ' +countCorect+"\n"
    #resultPrint+= str(round(countCorect/a, 3))+'\n'
    #resultPrint+= "------------------------------------------------------"+ '\n'

print(resultPrint)




