# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:30:56 2017

@author: Matheus
"""
from keras.models import model_from_json
from keras.optimizers import Adam
import numpy as np

import readImage

# load json and create model
json_file = open('cnn_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("cnn_model.h5")
print("Loaded model from file")

adam_optimizer = Adam(lr=0.0001, decay=1e-6) 

# evaluate loaded
loaded_model.compile(loss='binary_crossentropy',
              optimizer=adam_optimizer,
              metrics=['accuracy'])

#set the image size
width = 128
height = 128

#load the test data
xData = readImage.xTrain(width, height)

iTrain = round(len(xData)*0.7)
iTest = len(xData) - iTrain

X_train = xData[0:iTrain]
X_test = xData[iTrain:len(xData)]
del xData

yData = readImage.yTrain()

y_train = yData[0:iTrain]
y_test = yData[iTrain:len(yData)]
del yData 

score = loaded_model.evaluate(X_train, y_train, verbose=0)
print("score -> loss: {:.4f} - acc: {:.4f} ".format(score[0], score[1]))