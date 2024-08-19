import tensorflow as tf
from tensorflow import keras
# import keras.api._v2.keras as keras
print("tensortlow", tf.version.VERSION)
# print("keras", keras.version.VERSION)




img_width, img_height = 200, 200

nb_train_samples = 7300
nb_validation_samples = 1025  # choose number of samples
train_data_dir = '../DAL/MY_data/train/'
validation_data_dir = '../DAL/MY_data/test/'

BATCH_SIZE = 16 # divid the data to small group for every iteration
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import random
import numpy as np

#
train_image_generator      = ImageDataGenerator(rescale=1./255)  # Generator for our training data #rescale the pixel to range 0-1
validation_image_generator = ImageDataGenerator(rescale=1./255)  # Generator for our validation data


train_data_gen = train_image_generator.flow_from_directory(batch_size=BATCH_SIZE,
                                                           directory=train_data_dir, # path
                                                           shuffle=True, # random
                                                           target_size=(img_width,img_height), #(150,150)
                                                           class_mode='binary') # or catagorially
val_data_gen = validation_image_generator.flow_from_directory(batch_size=BATCH_SIZE,
                                                              directory=validation_data_dir,
                                                              shuffle=False,
                                                              target_size=(img_width,img_height), #(150,150)
                                                              class_mode='binary')



def create_model():
    model = tf.keras.Sequential([
        keras.layers.Dense(3, activation='relu', input_shape=(img_width, img_height, 3)),
        keras.layers.GlobalAveragePooling2D(),
        keras.layers.Dense(5),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(10)
    ])

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])

    return model

# Create a basic model instance
model = create_model()

# Display the model's architecture
print("model")
print(model.summary())
#
# checkpoint_path = "training_1/cp.ckpt"
# checkpoint_dir = os.path.dirname(checkpoint_path)

# Create a callback that saves the model's weights
# cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
#                                                  save_weights_only=True,
#                                                  verbose=1)

# Train the model with the new callback
model.fit(train_data_gen, epochs=2)  # Pass callback to training
print("after fit")

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


import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.utils import load_img,img_to_array
from tensorflow.keras.models import load_model
channels =3
#model2 = load_model("fruitsModel.h5")
counter = 15
a=0
countCorect=0
# for category in ["apple/","avocado/", "banana/","cherry/", "kiwi/","mango/", "orange/","pinenapple/", "stawberries/","watermelon/"]:
#
#   path = validation_data_dir + category#"gdrive/MyDrive/data_sets/cats_dogs/PetImages/test/"+category
#   for i in os.listdir(path)[0:15]:
#       img = load_img(path+i, grayscale=False,target_size=(img_width, img_height)) # grayscale-black or white
#
#       plt.matshow(img) # func - take the array and show as a matrix
#       plt.show()
#       img = img_to_array(img)
#       img = img.reshape(1, img_width, img_height, channels).astype('float32')
#       img = img / 255.0 # Normalization
#
#       preds = model.predict(img)
#       print("predictions:{} category:{}".format(preds,np.argmax(preds))) # argmax - returns indices of the max element of the array in a particular axis.
#       print("The friute is", categorys[np.argmax(preds)])
#       a += 1
#       if(categorys[np.argmax(preds)] in category ):
#         countCorect+=1
# print("all:",a)
# print("countCorect:", countCorect)
# print(countCorect/a)
# This may generate warnings related to saving the state of the optimizer.
# These warnings (and similar warnings throughout this notebook)
# are in place to discourage outdated usage, and can be ignored.

#
#
model.save('saved_model/my_model')
# Save the weights
model.save_weights('checkpoints/my_checkpoint.weights.h5')



# Create a new model instance
model = create_model()
# Restore the weights
model.load_weights('checkpoints/my_checkpoint.weights.h5')
print("model sumery")
print(model.summary())
# new_model = tf.keras.models.load_model('saved_model/my_model')
#
# # Check its architecture
# print("new model")
# print(new_model.summary())
#
# # Create and train a new model instance.
# model2 = create_model()
# model2.fit(train_images, train_labels, epochs=5)
#
# # Save the entire model to a HDF5 file.
# # The '.h5' extension indicates that the model should be saved to HDF5.
# model2 .save('my_model.h5')
#
# # Recreate the exact same model, including its weights and the optimizer
# new_model2 = tf.keras.models.load_model('my_model.h5')
#
# # Show the model architecture
# print("new model2")
# print(new_model2.summary())



