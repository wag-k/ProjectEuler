# -*- coding: utf-8 -*-
"""
Created on Tue May  1 15:38:39 2018

Project Euler 
Problem 8

@author: Owner
"""
import numpy as np

def txt2onearray(filename = "sample.txt"):
    f = open(filename)
    line = list(map(int, f.readline().replace("\n", "")))
    array = np.array(line)
    
    while line:        
        line = list(map(int, f.readline().replace("\n", "")))
        array = np.append(array, line)
    f.close()
    return array

def solveP8(array = txt2onearray()):

    return True

print(txt2onearray())


