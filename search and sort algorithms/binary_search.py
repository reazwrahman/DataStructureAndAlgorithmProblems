#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:44:43 2020

@author: Reaz 


binary search while loop

"""

original=[1,2,3,4,5,6,7,8] 
original_length=len(original)
   
array=[1,2,3,4,5,6,7,8]    
l=len(array)


item=7 
iteration=0
while True:  
    
    if type(item)!=int: 
        print ('invalid item, not an integer type')  
        break
    
    iteration+=1
    print (f'loop number = {iteration}') 
    if item == array[int(l/2)]: 
        index=int(l/2) 
        print (f'item found') 
        break 
    
    elif item < array[int(l/2)] and (item >= original[0]): 
        array=array[0:int(l/2)]   
        l=len(array)
        #print ('less')
        #print (array)
    
    elif item > array[int(l/2)] and (item <= original[original_length-1]): 
        array=array[int(l/2):l]   
        l=len(array)
        #print('more')
        #print (array)
    
    else: 
        print ('item not found')
        break
        
        
        
        
        