# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:30:56 2017

@author: Matheus
"""
from keras.models import model_from_json
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
import numpy as np

def predict():
    # load json and create model
    json_file = open('cnn_model_modelOficial.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("cnn_model_modelOficial.h5")
    print("Loaded model from file")
    
    adam_optimizer = Adam(lr=0.0001, decay=1e-6) 
    
    # evaluate loaded
    loaded_model.compile(loss='binary_crossentropy',
                  optimizer=adam_optimizer,
                  metrics=['accuracy'])
    
    width = 128
    height = 128
    
    test_data_gen = ImageDataGenerator()
    test_gen = test_data_gen.flow_from_directory('test', target_size=(width, height), batch_size=1, class_mode='binary',shuffle=False,seed=0)
    
    predictions = loaded_model.predict_generator(test_gen,689) #loaded_model.evaluate_generator(test_gen,689)
    
    predicted_classes = [];
    for n in predictions:
        predicted_classes.append(round(n[0]))
        
    score = sum(1*(test_gen.classes == predicted_classes))/len(predicted_classes)
    
    print(score)

    return predicted_classes


   # print("score -> loss: {:.4f} - acc: {:.4f} ".format(score[0], score[1]))
    
   # return score
    
    