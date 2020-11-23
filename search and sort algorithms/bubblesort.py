#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:07:50 2020

@author: Reaz 

ascending or from lowest to highest 


Documentation: We are comparing each element to its left 
and swapping it. Therefore we are not targeting each element 
individually from the array in the outer for loop, but rather
targeting the indexes sequentially. Therefore, we may/will 
target the same element more than once, but that's okay because
the element to its left has already been taken care of when we 
swapped. 

    
    
""" 


array=[5,1,4,2,13,2,21,3]
a=array

for i in range (len(a)): 
    for i in range (len(a)-1): 
        if a[i]> a[i+1]: 
            temp=a[i] 
            a[i]=a[i+1] 
            a[i+1]=temp 
        
       
sorted_array=a  
print (f'the sorted array is {sorted_array}') 