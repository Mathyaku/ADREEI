# -*- coding: utf-8 -*-
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
    return matrix_of_distance

#
#distances(matrix_of_points)