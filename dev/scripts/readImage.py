# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 19:48:20 2017

@author: Matheus
"""
from PIL import Image
import numpy as np
import os

def read():
   
    # importing all name of imgs
    pictureNames = os.listdir("../vba")
    
    #list of imgs
    data = []
    
    for imgName in pictureNames:
        
        # read img
        img = Image.open("../vba/" + imgName)
    
        #converting img to array
        imgRGB = np.array(img)
        
        # save resized image 
        data.append(imgRGB)    
        
    return data