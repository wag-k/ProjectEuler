# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:24:36 2018

Project Euler 
Problem 7

@author: Owner
"""

import numpy as np

a = []
a.append(2)
a.append(3)
n_p = 10001
 
n = 3
flag_append = False

print(np.size(a))

while np.size(a) < n_p:
    flag_append = False
    n += 1
    for i in range(0,np.size(a)-1):
        if n % a[i] == 0:
            flag_append = False
            break
        else:
            flag_append = True

    print(str(flag_append))
    if flag_append == True:
        a.append(n)
    else:
        pass
    print("n = " + str(n))
    print("Size of a is ... " + str(np.size(a)))

print(a)
print("n = " + str(n))
print("Prime number of "+ str(n) + " times is ... " + str(a[n_p]))