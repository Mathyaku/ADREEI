e f# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 22:07:12 2017

@author: Raissa
"""

#w, h = 3, 2;
#matrix_of_points = [[0 for x in range(h)] for y in range(w)]
#matrix_of_distance = [[0 for x in range(w)] for y in range(w)]
#
#matrix_of_points[0][0] = 1
#matrix_of_points[0][1] = 1
#
#matrix_of_points[1][0] = 2
#matrix_of_points[1][1] = 2
#
#matrix_of_points[2][0] = 3
#matrix_of_points[2][1] = 3

from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km

def distances(points):
    from scipy.spatial import distance
    import numpy as N
    matrix_of_distance = [[0 for x in range(N.shape(points)[0])] for y in range(N.shape(points)[0])]
    for i in range(0, N.shape(points)[0]):
        for j in range(0, N.shape(points)[0]):
            if i == j: 
                matrix_of_distance[i][j] =  float("inf")
            else:
                matrix_of_distance[i][j] = distance.euclidean(points[i][:],points[j][:])  
#                matrix_of_distance[i][j] = haversine(points[i][0], points[i][1],points[j][0], points[j][1])   
    return matrix_of_distance

#
#distances(matrix_of_points)