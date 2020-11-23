#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:48:49 2020

@author: Reaz
"""

def missing_element(a,b): 
    i=0
    while i<len(a): 
        if a[i] not in b: 
            print (f'missing {a[i]}') 
            break 
        else: 
            i+=1
    if i==len(a): 
        print ('two arrays are same') 

missing_element([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1])