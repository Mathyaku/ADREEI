# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:05:32 2017

@author: Raissa
"""
plt.axis([-50, -75, 10, -12])
for i in range(5):
        plt.plot(df[df['labels'] == i][0], df[df['labels'] == i][1], color[i])
plt.show()
