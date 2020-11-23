#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 00:50:07 2020

@author: Reaz 

udemy ecommerce question 2
"""
def conditional_product(a): 
    
    a=[4,3,2,1] 
    b=[]
    for i in range (len(a)):  
        right=1 
        left=1 
        result=1
        for j in range (i+1,len(a)):  
            right=right*a[j] 
        for k in range (i-1,-1,-1): 
            left=left*a[k] 
        result=right*left 
        b.append(result) 
    
    print (b) 
    return b

a=[4,3,2,1,2]  
conditional_product(a)