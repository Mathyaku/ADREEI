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
xData = readImage.xTrain()

iTrain = round(len(xData)*0.7)
iTest = len(xData) - iTrain

X_train = xData[0:iTrain]
X_test = xData[iTrain:len(xData)]
del xData

yData = readImage.yTrain()

y_train = yData[0:iTrain]
y_test = yData[iTrain:len(yData)]
del yData 

from matplotlib import pyplot as plt
plt.imshow(X_train[0])

nClass = 2

# Convert 1-dimensional class arrays to 10-dimensional class matrices
Y_train = np_utils.to_categorical(y_train, nClass)
Y_test = np_utils.to_categorical(y_test, nClass)

# 6. Preprocess class labels
Y_train = np_utils.to_categorical(y_train, nClass)
Y_test = np_utils.to_categorical(y_test, nClass)
 
# 7. Define model architecture
model = Sequential()
 
model.add(Convolution2D(32, [5, 5], activation='relu', input_shape=(120,160,3)))
model.add(Convolution2D(32, [5, 5], activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
 
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(nClass, activation='softmax'))
 
# 8. Compile model
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
 
# 9. Fit model on training data
model.fit(X_train, Y_train, 
          batch_size=32, nb_epoch=1, verbose=1)
 
# 10. Evaluate model on test data
score = model.evaluate(X_test, Y_test, verbose=0)