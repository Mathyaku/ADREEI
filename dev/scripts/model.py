# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
np.random.seed(123)
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.datasets import mnist

import readImage
 
# Load pre-shuffled MNIST data into train and test sets
X_train = readImage.xTrain()

y_train = readImage.yTrain()

#X_test = readImage.xTest()


from matplotlib import pyplot as plt
plt.imshow(X_train[0])


# print (X_train.shape)
# (60000, 28, 28, 1)

# Convert 1-dimensional class arrays to 10-dimensional class matrices
Y_train = np_utils.to_categorical(y_train, 2)
#Y_test = np_utils.to_categorical(y_test, 2)

print(Y_train.shape)
# (60000, 10)

# 6. Preprocess class labels
Y_train = np_utils.to_categorical(y_train, 2)
#Y_test = np_utils.to_categorical(y_test, 2)
 
# 7. Define model architecture
model = Sequential()
 
model.add(Convolution2D(32, [3, 3], activation='relu', input_shape=(240,320,3)))
model.add(Convolution2D(32, [3, 3], activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
 
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax'))
 
# 8. Compile model
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
 
# 9. Fit model on training data
model.fit(X_train, Y_train, 
          batch_size=32, nb_epoch=5, verbose=1)
 
# 10. Evaluate model on test data
#score = model.evaluate(X_test, Y_test, verbose=0)