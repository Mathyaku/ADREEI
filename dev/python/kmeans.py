# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 21:07:40 2017

@author: Raissa
"""

def clusterization (X, k):
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from sklearn.cluster import KMeans
    from sklearn import datasets

#    np.random.seed(5)
#    iris = datasets.load_iris()
    estimators = [('k_means_iris_', KMeans(n_clusters=k))] #,
    #              ('k_means_iris_3', KMeans(n_clusters=3)),
    #              ('k_means_iris_bad_init', KMeans(n_clusters=3, n_init=1,
    #                                               init='random'))]
    
#    fignum = 1
#    titles = [str(k) + ' clusters']
    for name, est in estimators:
#        fig = plt.figure(fignum, figsize=(4, 3))
#        ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
        est.fit(X)
        labels = est.labels_
    import matplotlib.pyplot as plt
#    plt.plot([1,2,3,4], [1,4,9,16], 'ro')
    plt.axis([55, 70, 0, 10])
    plt.show()
    from numpy import array
    color = ['ro', 'bo', 'co', 'go', 'yo']
    for i in range(k):
        plt.plot(df[df['labels'] == 0][k], df[df['labels'] == 0][k], color[0])
    plt.show()
        
    
    return labels


#   
#    ax.scatter(X[:, 3], X[:, 0], X[:, 2],
#               c=labels.astype(np.float), edgecolor='k')
##
#    ax.w_xaxis.set_ticklabels([])
#    ax.w_yaxis.set_ticklabels([])
#    ax.w_zaxis.set_ticklabels([])
#    ax.set_xlabel('Petal width')
#    ax.set_ylabel('Sepal length')
#    ax.set_zlabel('Petal length')
#    ax.set_title(titles[fignum - 1])
#    ax.dist = 12
#    fignum = fignum + 1
#
## Plot the ground truth
#    fig = plt.figure(fignum, figsize=(4, 3))
#    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
#    
#    for name, label in [('Setosa', 0),
#                        ('Versicolour', 1),
#                        ('Virginica', 2)]:
#        ax.text3D(X[y == label, 3].mean(),
#                  X[y == label, 0].mean(),
#                  X[y == label, 2].mean() + 2, name,
#                  horizontalalignment='center',
#                  bbox=dict(alpha=.2, edgecolor='w', facecolor='w'))
# Reorder the labels to have colors matching the cluster results
#y = np.choose(y, [1, 2, 0]).astype(np.float)
#    ax.scatter(X[:, 3], X[:, 0], X[:, 2], edgecolor='k')
##
#    ax.w_xaxis.set_ticklabels([])
#    ax.w_yaxis.set_ticklabels([])
#    ax.w_zaxis.set_ticklabels([])
#ax.set_xlabel('Petal width')
#ax.set_ylabel('Sepal length')
#ax.set_zlabel('Petal length')
#ax.set_title('Ground Truth')
#    ax.dist = 12
#
#    fig.show()