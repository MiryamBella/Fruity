import os
import numpy as np
import pandas as pd

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

test.to_csv("test.csv")