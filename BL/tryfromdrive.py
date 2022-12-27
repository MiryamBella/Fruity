import os
#from pydrive.auth import GoogleAuth
#from pydrive.drive import GoogleDrive
#from google.colab import auth
#from oauth2client.client import GoogleCredentials


import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import to_categorical
import keras.utils as image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from tqdm import tqdm
import csv



def makeDataset(dirs_images, fruitFolder=None):
    imageNames=[]
    categories = []
    indexFruite=0
    for dir_images in dirs_images:
        filenames = os.listdir(dir_images)
        for filename in filenames:
            categories.append(indexFruite)
        if(fruitFolder!=None):
            for i in range(len(filenames)):
                filenames[i] = fruitFolder[indexFruite] + filenames[i]
        imageNames+= filenames
        indexFruite+=1
    df = pd.DataFrame({
        'id': imageNames,
        'label': categories
    })
    return df


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

test=makeDataset([dir_train_banana], ["banana/"])

'''
test=makeDataset([dir_train_banana, dir_train_kiwi, dir_train_Apple, dir_train_avocado, dir_train_cherry, dir_train_mango,
                  dir_train_orange, dir_train_pinenapple, dir_train_strawberries, dir_train_watermelon],
                  ["banana/", "kiwi/", "apple/", "avocado/", "cherry/", "mango/", "orange/", "pinenapple/", "stawberries/",
                   "watermelon/"])
print(test)
'''
# We have grayscale images, so while loading the images we will keep grayscale=True, if you have RGB images, you should set grayscale as False
train_image = []
for i in tqdm(range(train.shape[0])):
    img = image.load_img(dir_train +train['id'][i], target_size=(28,28,1), grayscale=True)
    img = image.img_to_array(img)
    img = img/255
    train_image.append(img)
X = np.array(train_image)

y=train['label'].values


y = to_categorical(y)
#זה הטרגט בעיקרון


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)



#ניצור את המודל:
#במודל שלנו יהיו 2 שכבות רגילות- אחת נסתרת צפופה ושכבת פלטת
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),activation='relu',input_shape=(28,28,1)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))


#נקמפל את המודל שלנו
model.compile(loss='categorical_crossentropy',optimizer='Adam',metrics=['accuracy'])


model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))



#לשים בתוך מערך את התמונות של הטסט
test_image = []
for i in tqdm(range(test.shape[0])):
    img = image.load_img(dir_test +test['id'][i], target_size=(28,28,1), grayscale=True)
    img = image.img_to_array(img)
    img = img/255
    test_image.append(img)
test = np.array(test_image)


# making predictions
predict_x=model.predict(test)
prediction=np.argmax(predict_x,axis=1)

# creating submission file
sample = pd.read_csv('test.csv')
sample['label'] = prediction
sample.to_csv('sample_cnn.csv', header=True, index=False)
#סוג של קובץ שיש בו את השמות של התמונות והם ממופות סתם לאפס, ואז לאחר הריצה זה ישתנה לתוצאות האמיתיות


count=0
countAll=0
for i in range(len(sample["label"])):
  countAll+=1
  if(sample["label"][i]==0):
    count+= 1

print(count)
print(countAll)








