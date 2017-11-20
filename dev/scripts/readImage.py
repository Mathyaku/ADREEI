# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 19:48:20 2017

@author: Matheus
"""
from PIL import Image
import numpy as np
import os
import csv
import glob
import shutil

def xTrain(width, height):
   
    # importing all name of imgs
    pictureNames = os.listdir("../vba/train")
    
    #list of imgs
    
    x_train = np.zeros( (len(pictureNames),height,width,3), dtype="float32" )
    
    
    for i,imgName in enumerate(pictureNames):
        
        # read img
        img = Image.open("../vba/train/" + imgName)
    
        #converting img to array
        imgRGB = np.asarray(img, dtype="float32") #/255
        
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
        y_train.append( int(row[1]) )
    
    myarray = np.asarray(y_train, dtype="int")
    return myarray

def generateTrainAndTestImages():
 
    ifile = open('../train_labels.csv', "rt")
    reader = csv.reader(ifile)
    y_train = []
    y_names = []
    next(reader)
    
    for row in reader:
        y_train.append( int(row[1]) )
        y_names.append( (row[0])+'.jpg' )
    
    myarray = np.asarray(y_train, dtype="int")
    
    indexes = np.random.permutation(myarray.shape[0])
    iTraining, iTesting = indexes[:round(len(myarray)*0.7)], indexes[round(len(myarray)*0.7):]

    
    for i in iTraining:
        if(myarray[i] == 1):
            shutil.copy("../train/" + y_names[i], "train/1")
        else:
            shutil.copy("../train/" + y_names[i], "train/0")
    
    for i in iTesting:
        if(myarray[i] == 1):
            shutil.copy("../train/" + y_names[i], "test/1")
        else:
            shutil.copy("../train/" + y_names[i], "test/0")
    

def removeDir():
    shutil.rmtree('train/0/')
    shutil.rmtree('train/1/')
    shutil.rmtree('test/0/')
    shutil.rmtree('test/1/')
    
def createDir():
    os.makedirs('train/0')
    os.makedirs('train/1')
    os.makedirs('test/0')
    os.makedirs('test/1')