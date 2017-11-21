# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:54:36 2017

@author: Raissa
"""



#from random import random 
import numpy as np
from kmeans import clusterization
from distances import distances
from pandas import DataFrame
import pandas as pd
from read_output import read_output 
import matplotlib.pyplot as plt
import random

def count_itens(df, unique_labels):
    count = [] 
    for i in unique_labels:
        count.append(len(df[df['labels'] == i]))
    return count
        
def unique(labels):
    output = []
    for x in labels:
        if x not in output:
            output.append(x)
    print(output)
    return output

#def gen_paths(index_threats_list): 
lista = random.sample(range(1, 3000), 200)
index_threats_list= lista    
#Definição de variaveis
peso_distancia = 1
peso_tempo = 0
vel_med_drone = 100 #km/h
max_flight_time = 1
num_pontos = 8; #locais a serem visitados
tempo_prep = 30; #min
num_drone = 5; 
num_cluster = 10;
max_carga_drone = 3000; #g
peso_inseticida = 10; #g por ponto
param_sec = 0.75;
#max_pontos = max_carga_drone/peso_inseticida
max_pontos = 20

if vel_med_drone != "" and max_flight_time != "": 
    distancia = vel_med_drone * max_flight_time
else:
    distancia = 100

#Get threat lat lon positions
df = pd.read_pickle("positions.pkl")
df = df.loc[index_threats_list,:]

matriz_pontos = np.asmatrix(df)

optimal = False
k = 4
drone_paths = []
#    colors = ['black', 'bo', 'co', 'go', 'yo', 'mo', 'ko']
while(not optimal):
    k = k + 1
    #Clusterização
    labels = clusterization (matriz_pontos, k)
    df['labels'] = labels
    
    color = ['r', 'b', 'c', 'g', 'y', 'm', 'k']
    
    unique_labels = unique(labels)
    plt.axis([-50, -75, 10, -15])
    for i in unique_labels:
            plt.plot(df[df['labels'] == i][0], df[df['labels'] == i][1], color[i%len(color)]+ 'o')
    plt.show()

     
    #Se tivermos mais que max_pontos
    if any([x > max_pontos for x in count_itens(df, unique_labels)]):
        continue
    
    #Calcula distancias entre os pontos
    matrix_distances = distances(matriz_pontos)
    
    #para cada cluster
    for i in unique_labels:
        matrix_distances = distances((df[df['labels'] == i]).as_matrix())
        #Se a distancia entre quaisquer dois pontos for maior que a maxima do drone, não continua
        if np.any([[(x > distancia and x != float('inf')) for x in y]  for y in matrix_distances]):
            continue
    
    #starter_point = [round(random()) for x in range(num_pontos)]
    #matriz_conexoes = [[random() for x in range(num_pontos)] for y in range(num_pontos)]
    
    from random import randint
    colors = []
    
    for i in range(10):
        colors.append('%06X' % randint(0, 0xFFFFFF))
    for label in unique_labels:
        base_distance = 1
        cluster_points = (df[df['labels'] == label]).as_matrix()
        matrix_distances = distances(cluster_points)
        file = open('testfile' + str(label) + '.lp', 'w') 
        
        #Função objetivo
        file.write('min: dist_total; \n\n\n') #+  str(peso_tempo) + 'tempo_total \n\n\n') 
        
        #minimizacao da distancia 
        file.write('//Implementa a funcao objetivo \n')
        str_lp ='dist_total >= ' + str(base_distance)
        for i in range(0, len(matrix_distances)):
            for j in range(0, len(matrix_distances)):
                if j != i:
#                if matrix_distances[i][j] == float('inf'):
#                    str_lp = str_lp + ' + ' + str(9999999999) + 'X[' + str(i) + '][' + str(j) + ']'
                    
#                else:
                    str_lp = str_lp + ' + ' + str(matrix_distances[i][j]) + 'X[' + str(i) + '][' + str(j) + ']'
        
        file.write(str_lp + ";\n")
        
        #Restrição de visitar cada coisa uma unica vez
        file.write('//Visitar cada ponto pelo menos uma vez \n')
        str_lp ='1 >='
        for i in range(0, len(matrix_distances)):
            str_lp_total_neg ='1 >= '
            str_lp_total_pos = ''
            for j in range(0, len(matrix_distances)):
                if j != i:
        #        str_lp = str_lp + ' + X[' + i + '][' + j + ']'
                    str_lp_total_pos = str(str_lp_total_pos) + ' + X[' + str(i) + '][' + str(j) + ']'
                    str_lp_total_neg = str(str_lp_total_neg) + ' + X[' + str(i) + '][' + str(j) + ']'
            str_lp_total_pos  = str_lp_total_pos + '>= 1'
            str_lp_total_neg  = str_lp_total_neg
            file.write(str_lp_total_pos  + ';\n')
            file.write(str_lp_total_neg + ";\n\n")
        file.write('\n')
        
        
        file.write('//Visitar cada ponto uma unica vez \n')
        str_lp =''
        for j in range(0, len(matrix_distances)):
            str_lp_total_neg ='1 >='
            str_lp_total_pos = ''
            for i in range(0, len(matrix_distances)):
                if j != i:
                    str_lp_total_pos = str(str_lp_total_pos) + ' + X[' + str(i) + '][' + str(j) + ']'
                    str_lp_total_neg = str(str_lp_total_neg) + ' + X[' + str(i) + '][' + str(j) + ']'
            str_lp_total_pos  = str_lp_total_pos + '>= 1'
            str_lp_total_neg  = str_lp_total_neg 
            file.write(str_lp_total_pos  + ';\n')
            file.write(str_lp_total_neg + ";\n\n")
        file.write(str_lp + '\n')
#        #str_lp_total_pos  = str_lp_total_pos + '>=' + str(num_pontos)
        #str_lp_total_neg  = str_lp_total_neg + '>= -' + str(num_pontos)
        
        file.write('//Visitar exatamente um ponto duas vezes \n')
    #    
    
        for j in range(0, len(matrix_distances)):
            for i in range(0, len(matrix_distances)):
                if j != i:
                    str_lp = '1 >= + X[' + str(j) + '][' + str(i) + '] + X[' + str(i) + '][' + str(j) + ']'
                    file.write(str_lp + ';\n')
    
        for j in range(0, len(matrix_distances)):
            for i in range(0, len(matrix_distances)):
                if j != i:
                    str_lp = 'X[' + str(i) + '][' + str(j) + '] >= 0'
                    file.write(str_lp + ';\n')
            
        file.write('//Subgrafos \n')
    #    
        for k in range(2, len(matrix_distances)):
            str_lp = str(k) + " -1 >="
            for j in range(0, k):
                for i in range(0, k):
                    if j != i:
                        str_lp = str_lp + ' + X[' + str(i) + '][' + str(j) + ']'
            file.write(str_lp + ';\n')
    
    
    #Restricoes da capacidade do drone
        str_lp =  str(1000) + '>= dist_total'
        file.write(str_lp + ';\n')
        
        for i in range(0, len(matrix_distances)):
            for j in range(0, len(matrix_distances)):
                if j != i:
                    file.write('int X[' + str(i) + '][' + str(j) + '];\n')
        
        
        file.close()
        tempo = 300000
        import os
        status = os.system("lp_solve -s -timeout " + str(tempo) + " testfile" + str(label) + ".lp > saida" + str(label) + ".txt")
    #    command = [];
    #[status,cmdout] = system(command)
        path_data = read_output("saida" + str(label) + ".txt")
        for i in range( len(  path_data ) ):
            drone_paths.append(
                dict(
                    type = 'scattergeo',
                    locationmode = 'ISO-3',
                    lon = [ cluster_points[i][0], cluster_points[path_data[i].index(1)][0] ],
                    lat = [ cluster_points[i][1], cluster_points[path_data[i].index(1)][1] ],
                    mode = 'lines',
                    line = dict(
                        width = 1,
                        color = colors[label%len(colors)],
                    ),
#                        opacity = float(cluster_points['cnt'][i])/float(df_flight_paths['cnt'].max()),
                )
            )
    
        optimal = 1
    layout = dict(
        title = 'Optimal path between threats',
        showlegend = False, 
        geo = dict(
            projection=dict( type='azimuthal equal area' ),
            showland = True,
            landcolor = 'rgb(243, 243, 243)',
            countrycolor = 'rgb(204, 204, 204)',
        ),
    )
    fig = dict( data=drone_paths , layout=layout )
#    import plotly
    plot( fig, filename='d3-path-brazil_1.html')
            
####### Cemiterio de codigo ###############
#    n = 200
#    #pontos aleatorios
#    mu_lat, sigma_lat = -4.17, 3
#    mu_long, sigma_long = -62, 4 # mean and standard deviation
#    s_lat = np.random.normal(mu_lat, sigma_lat, n)#, np.random.normal(mu_long, sigma_long, 222)]
#    s_long = np.random.normal(mu_long, sigma_long, n)
    
    #Restrição de numero de pontos
    #numpontos  <= max_carga_drone/peso_inseticida
    #matriz_pontos = [[random() for x in range(2)] for y in range(num_pontos)]
#    matriz_pontos = [[0 for x in range(2)] for y in range(len(s_long))]
#    for i in range(len(s_long)):
#        matriz_pontos[i] = [s_long[i], s_lat[i]]
            
            
    #    plt.plot([1,2,3,4], [1,4,9,16], 'ro')
    #    plt.axis([55, 70, 0, 10])
    #    plt.show()
    #    from numpy import array
    #    for i in range(k):
    #        plt.plot(df[df['labels'] == k][0], df[df['labels'] == k][1], color[k])
    #    plt.show()
    #                