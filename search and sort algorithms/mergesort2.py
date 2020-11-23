#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:52:40 2020

@author: Reaz
"""

a=[90,1,0,4,25,12,3,11,1,3,2,1,5,7,8] 

#a=[4,3,2,1]
print (a)

def mergesort(a): 
    
    if len(a)>1:
        mid=len(a)//2  
        left=a[:mid] 
        right=a[mid:]  
        mergesort(right) 
        mergesort(left) 
        merge(left,right,a) 
    
    
    return a
    
    


def merge (a1,a2,a):
    
    i=j=k=0
    while i<len(a1): 
        while j<len(a2):  
            if a1[i]<a2[j]: 
                a[k]=a1[i] 
                k+=1 
                i+=1  
               
            elif a2[j]<=a1[i]:  
                a[k]=a2[j] 
                k+=1 
                j+=1   
                
            
            if i==len(a1) and j!=len(a2):
                while j<len(a2): 
                    a[k]=a2[j] 
                    k+=1 
                    j+=1
            if j==len(a2) and i!=len(a1): 
                while i<len(a1): 
                    a[k]=a1[i] 
                    k+=1 
                    i+=1
   
            
            
            
print(mergesort(a))        

#merge([3,4],[1,2],[4,3,2,1])    
    
    