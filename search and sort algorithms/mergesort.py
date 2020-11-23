#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:39:34 2020

@author: Reaz 

Mergesort algorithm: watch jenny's lecture for concept 
followed geekforgeek for the code implementation
uncomment the print statements for a better understanding
"""


def mergesort(a): 
  
    #print (a)  
    if len(a)>1: 
        mid=(len(a))//2
        left=a[:mid] 
        right=a[mid:]    
        print (f' the midpoint right now is {a[mid]}')
        print (f'left array is {left}') 
        print (f'right array is {right}') 
        print (f'executing left mergesort({left})')
        mergesort(left)   
        print (f'EXECUTING RIGHT mergesort({right})')
        mergesort(right) 
        #print (left) 
        #print (right)
        merge(left,right,a) 
    
    print (f'function is completed and returning {a}')
    return a
        
    
        
def merge(a1,a2,a): 
    
    print (f' now we are gonna merge {a1} and {a2}')
    #print (f'a1 is {a1}') 
    #print (f'a2 is {a2}')
    
    i=j=k=0
    while i<len(a1):  
        while j<len(a2):  
            #print (f' checking if {a1[i]} is less than {a2[j]}')
            if a1[i]<a2[j]:   
                #print ('yes')
                a[k]=a1[i]  
                i+=1 
                k+=1
            elif a2[j]<a1[i]: 
                #print ('no')
                a[k]=a2[j] 
                k+=1
                j+=1   
                
            if j==len(a2):    
                #print ('i has reached max')
                while i<len(a1): 
                    a[k]=a1[i] 
                    k+=1 
                    i+=1
                
                
            elif i==len(a1):  
                #print ('i has reached max')
                while j<len(a2): 
                    a[k]=a2[j] 
                    k+=1 
                    j+=1 
            #print (a)
    print (f'sorted array is {a}')
    return a
        
#merge([3,4],[1,2],a)   
a=[4,3,2,1]
print (a)
s=mergesort(a)  
print (f'sorted array is {s}')