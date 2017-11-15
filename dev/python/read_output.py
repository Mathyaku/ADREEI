# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 21:10:14 2017

@author: Raissa
"""
import re
#import time
def read_output(fname):
#    fname = "saida0.txt" 
    with open(fname) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
#    print(content)
    try:
#        print(content[len(content)-1])
        num_pontos = int(re.match('X\[(\d+)+\]\[(\d+)+\] * (\d+)+', content[len(content)-1]).group(1))
    except: 
        try:
            num_pontos = int(re.match('X\[(\d+)+\]\[(\d+)+\] * (-)*(\d+(?:\.\d*)?(?:[eE][+\-]?\d+))+', content[len(content)-1]).group(1))
        except:
           print ('Line ' + content[len(content)-1] + " doesn't follow the pattern") 
    matriz_pontos = [[0 for x in range(num_pontos+1)] for y in range(num_pontos+1)]
    for line in content[6:len(content)-1]:
        print(line)
    #    time.sleep(5)
        try: 
            data = re.match('X\[(\d+)+\]\[(\d+)+\] * (-)*(\d+(?:\.\d*)?(?:[eE][+\-]?\d+))+', line)
            matriz_pontos[int(data.group(1))][int(data.group(2))] = round(float(data.group(3)))
        except:
            try:
                data = re.match('X\[(\d+)+\]\[(\d+)+\] * (\d+)+', line)
                matriz_pontos[int(data.group(1))][int(data.group(2))] = round(int(data.group(3)))
            except: 
                print ('Line ' + line + " doesn't follow the pattern")
    return matriz_pontos
    

