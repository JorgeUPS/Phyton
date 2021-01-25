# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:27:16 2021

@author: Bryan
"""

dict1={'R1':'10.0.0.1',
       1:'AP',
       2:2.5,3:True,
       'R2':'172.17.0.1'}
print(dict1)
print(len(dict1))
print(type(dict1))
print(dict1[1])
print(dict1[2])
print(dict1[3])
print(dict1['R1'])
dict1['R3']='10.0.0.3'
print('R3'in dict1)
