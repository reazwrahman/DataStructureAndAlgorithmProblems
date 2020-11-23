#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:33:05 2020

@author: Reaz
"""

a=[23,29,15,19,31,7,9,5,20,1,13]
print (a)
gap=int (len(a)/2)   
while gap>0:
    for i in range (gap,len(a),1):   
        current_element=a[i]
        for j in range(i-gap,-1,-gap):   
            if current_element<a[j]: 
                temp=a[j] 
                a[j]=current_element 
                a[j+gap]=temp 
    
    gap=int(gap/2) 
print (f'sorted {a}')




    
## documentation: Think of this algorithm 
# as an insertion algorithm but instead of incrementing by 1, 
# we increment it using a gap
# take an example set and look at 3 numbers separated by the gap 
# now mentally perform an insertion algorithm onto those 3 numbers 
# and thats it!  Needless to say u need to understand insertion algo very well 
# to understand this one