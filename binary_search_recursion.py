#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 23:03:45 2020

@author: Reaz 

binary search with recursion
"""


def binary_search(a,k): 
    
    mid=len(a)//2  
    
    if len(a)==1 and a[0]!=k :  
        print (a)
        print ('sorry element not found') 
        return False 
    
    if k==a[mid]:    
        print (a)
        print ('Found! element found')
        return True 

    elif k<a[mid]: 
        a=a[:mid]  
        #print(a)
        binary_search(a,k)
    
    elif k>a[mid]: 
        a=a[mid:]  
        #print(a)
        binary_search(a,k) 
    


a=[1,2,3,4,5,6,7,8,10,11,12,13,14,15] 
k= 2
binary_search(a,k)