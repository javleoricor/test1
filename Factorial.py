# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 18:46:15 2020

@author: Leandro
"""

num = int(input('Digite número'))
fact = 1
if(num == 0):
    print('El factorial es 1')
else:
    for n in range(1,num+1):
        fact = fact*n
    print('El factorial es ', fact)
