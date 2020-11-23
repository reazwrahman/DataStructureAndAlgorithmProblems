im#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 19:58:30 2020

@author: Reaz 
INSERTION SORT ALGORITHM
"""

a=[4,2,3,1]
print (a)


for i in range (1,len(a)):  
    current_element=a[i]  
    print (f'now checking {current_element}')
    
    for j in range (i-1,-1,-1):  
        
    
        if current_element<a[j]:  
            temp=a[j] 
            print (f' replacing {a[j]} with {current_element}')
            a[j]=current_element 
            a[j+1]=temp  
            print (a)  
    print ('end of line') 
    print ('------')
    
            
            







#for i in range (1,len(a)):            
#    x=a[i]
#    
#    for j in range (i-1,-1,-1):  
#        
#        if x>a[j]:   
#          
#            tempj=a[j]  
#            a[j+1]=tempj   
#            a[j]=x 
#           
#         
#print (f'sorted array is {a}')