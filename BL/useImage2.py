# Import dependencies
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.image as mpimg

from sklearn.model_selection import train_test_split

dir_train_fruit='dataset/fruits/train/'

dir_train_apple = 'dataset/apple/train'
dir_test_apple = 'dataset/apple/test'
dir_train_banana = 'dataset/fruits/train/banana'
dir_train_kiwi = 'dataset/fruits/train/kiwi'
dir_test_banana  = 'dataset/fruits/test/banana'
dir_test_kiwi  = 'dataset/fruits/test/kiwi'


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


'''
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

'''


#                                          make a dataset out of the images in the training dir
def makeDataset(indexFruite, dir_images, fruitFolder=None):
    filenames = os.listdir(dir_images)
    filenames_kiwi = os.listdir(dir_train_kiwi)
    categories = []
    for filename in filenames:
        categories.append(indexFruite)
    if(fruitFolder!=None):
        for i in range(len(filenames)):
            filenames[i] = fruitFolder + filenames[i]
    df = pd.DataFrame({
        'filename': filenames,
        'category': categories
    })
    return df
df= makeDataset(1, dir_train_banana, 'banana/')
df.apply()
# how many dogs and cats?
print('number of banana: %d' % len(df[df.category == 1]))
print('number of kiwi: %d' % len(df[df.category == 0]))


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




kiwi_train_valid=df[df.category == 0]
'''
to split one dataset
#                                         separate the kiwi from the banana in the dataframe
filtered_kiwi = df[df.category == 0]
filtered_banana = df[df.category == 1]


#                                    split to train, validate and test folders with the help of sklearn
# each split is to 2 groups
# so we need 2 splits in order to split to 3 groups


# the first split is to cats_test and the rest of the images
kiwi_train_valid, kiwi_test = train_test_split(filtered_kiwi, test_size=0.1, random_state=1)

# the second split on the cats_train_valid folder separates to 2 folders: train and valid
kiwi_train, kiwi_valid = train_test_split(kiwi_train_valid, test_size=0.2, random_state=1)

# how many cats in the train and valid?
print(kiwi_train.shape[0])
print(kiwi_valid.shape[0])

# split the dogs dataset to the same ratio
banana_train_valid, banana_test = train_test_split(filtered_banana, test_size=0.1, random_state=1)

banana_train, banana_valid = train_test_split(banana_train_valid, test_size=0.2, random_state=1)
'''

# importing tensorflow and Keras for doing ML
from tensorflow.python.keras.models import Model, Sequential
from tensorflow.python.keras.layers import Dense, Flatten, Dropout
from tensorflow.python.keras.applications import VGG16
from tensorflow.python.keras.applications.vgg16 import preprocess_input, decode_predictions
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.optimizers import Adam, RMSprop









#dog= banana=1
#cat= kiwi=0


