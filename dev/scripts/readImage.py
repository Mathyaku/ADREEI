# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 19:48:20 2017

@author: Matheus
"""
from PIL import Image
import numpy as np
import os
import csv

def xTrain():
   
    # importing all name of imgs
    pictureNames = os.listdir("../vba/train")
    
    #list of imgs
    x_train = np.zeros( (len(pictureNames),240,320,3), dtype="float32" )
    
    
    for i,imgName in enumerate(pictureNames):
        
        # read img
        img = Image.open("../vba/train/" + imgName)
    
        #converting img to array
        imgRGB = np.asarray( img, dtype="float32" )/255
        
        # save resized image 
        x_train[i] = (imgRGB)
        
    return x_train

def xTest():
   
    # importing all name of imgs
    pictureNames = os.listdir("../vba/test")
    
    #list of imgs
    x_test = []
    
    for imgName in pictureNames:
        
        # read img
        img = Image.open("../vba/test/" + imgName)
    
        #converting img to array
        imgRGB = np.asarray( img, dtype="float32")
        
        # save resized image 
        x_test.append(imgRGB)    
        
    return x_test

def yTrain():
 
    ifile = open('train_labels.csv', "rt")
    reader = csv.reader(ifile)
    y_train = []
    next(reader)
    for row in reader:
        y_train.append(int(row[1]))
        
    return y_train