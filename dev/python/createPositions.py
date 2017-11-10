# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 20:04:57 2017

@author: Raissa
"""
from pandas import DataFrame
import numpy as np
#import pandas
#pontos aleatorios
n= 3000
mu_lat, sigma_lat = -4.17, 3
mu_long, sigma_long = -62, 4 # mean and standard deviation
s_lat = np.random.normal(mu_lat, sigma_lat, n)#, np.random.normal(mu_long, sigma_long, 222)]
s_long = np.random.normal(mu_long, sigma_long, n)

matriz_pontos = [[0 for x in range(2)] for y in range(len(s_long))]
for i in range(len(s_long)):
    matriz_pontos[i] = [s_long[i], s_lat[i]]
df = DataFrame(matriz_pontos)
df.to_pickle("positions.pkl")

