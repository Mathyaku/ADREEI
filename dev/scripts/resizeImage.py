# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 19:48:20 2017

@author: Matheus
"""
from PIL import Image
from scipy import misc
import numpy as np
import os
from matplotlib import pyplot as plt

def storeImages():
   
    # importing all name of imgs
    pictureNames = os.listdir("../train")
    
    # creating the directory
    os.makedirs('../vba/train')
    
    for imgName in pictureNames:
        
        # read img
        img = Image.open("../train/" + imgName)
    
        # setting dimensions
        width = 320 #640
        height = 240 #480
        
        # resizing the img
        imgResized = img.resize((width, height), Image.NEAREST)
        
        #converting img to array
        imgRGB = np.array(imgResized)
        
        # save resized image 
        misc.imsave("../vba/train/" + imgName, imgRGB)
        
        # visualization
        #plt.imshow(imgRGB)
        
    return