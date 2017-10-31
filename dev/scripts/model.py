# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.core import Dense, Flatten, Dropout
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import CSVLogger


import readImage

# Setup of train and Test
#readImage.removeImages()
#readImage.generateTrainAndTestImages()
 
width = 128
height = 128
 
# 7. Define model architecture
model = Sequential()

#model.add(Convolution2D(64, 3, 3, activation='relu', input_shape=(128, 128, 3)))
#model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Convolution2D(128, 3, 3, activation='relu'))
#model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Convolution2D(256, 3, 3, activation='relu'))
#model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Convolution2D(512, 3, 3, activation='relu'))
#model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Flatten())
#model.add(Dense(256, activation = 'relu'))
#model.add(BatchNormalization(momentum=0.75))
#model.add(Dropout(0.5))
#model.add(Dense(1, activation = 'sigmoid'))

model.add(Convolution2D(32, 3, 3, activation='relu', input_shape=(width, height, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Convolution2D(64, 3, 3, activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Convolution2D(128, 3, 3, activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Convolution2D(256, 3, 3, activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Convolution2D(512, 3, 3, activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(BatchNormalization(momentum=0.60))
model.add(Dropout(0.125))
model.add(Dense(512, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

adam_optimizer = Adam(lr=0.0001, decay=1e-6)

# 8. Compile model
model.compile(loss='binary_crossentropy',
              optimizer = adam_optimizer,
              metrics=['accuracy'])

train_data_gen = ImageDataGenerator(shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
train_gen = train_data_gen.flow_from_directory('train', target_size=(width, height), batch_size=32, class_mode='binary')

valid_data_gen = ImageDataGenerator()
valid_gen = valid_data_gen.flow_from_directory('test', target_size=(width, height), batch_size=32, class_mode='binary')

csv_logger = CSVLogger('modelOficial.log')

model.fit_generator(
    train_gen,
    steps_per_epoch = 1606 // 32, #50
    epochs = 20,
    validation_data = valid_gen,
    validation_steps = 689 // 34, #20
    callbacks = [csv_logger])

#scores = model.evaluate_generator(valid_gen,689)
# 9. Fit model on training data
#model.fit(X_train, y_train, 
#          batch_size=25, nb_epoch=30, verbose=1)
 
# 10. Evaluate model on test data
#score = model.evaluate(X_test, y_test, verbose=0)
#print("score -> loss: {:.4f} - acc: {:.4f} ".format(scores[0], scores[1]))

classification_json = model.to_json()
with open("cnn_model_modelOficial.json", "w") as json_file:
    json_file.write(classification_json)
model.save_weights("cnn_model_modelOficial.h5")