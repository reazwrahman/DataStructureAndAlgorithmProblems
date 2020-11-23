#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:41:20 2020

@author: Reaz 

solution 1, 2 only works for positive integers, unfortunately! :(
""" 
from mergesort_practice import mergesort 


def three_slot_bubblesort(a):
    for i in range (0,3):  
        #print (f'taking care of {a[i]} now')
        for j in range (i+1,4): 
            #print (f'i is {i}')
            if a[j]<a[i]: 
                temp=a[i] 
                a[i]=a[j] 
                a[j]=temp  
                #print (a)   
    return a  

#' solution 1: time complexity of O(n log n)' 
def mergesorted_lp(a):
    b=mergesort(a)
    print (f'mergesorted {b}')
    last=len(b)-1
    largest_product=b[last]*b[last-1]*b[last-2] 
    print (f'mergesorted largest product {largest_product}') 

#'solution 2: time complexity threeslotbbosrt=O(3*3)+ one_pass:O(n-3) 
# total time complexity ~ O(n), better than nlogn' 
    
def three_slot_bbsorted_lp(a):
    a=three_slot_bubblesort(a)  
    print (f'three slot bubble sorted {a}') 
    highest=a[2] 
    higher=a[1] 
    high=a[0] 
    
    i=3
    while i>2 and i<len(a): 
     
        if a[i]>highest:              
            highest=a[i]  
            i+=1
        
        if a[i]>higher:              
            higher=a[i]  
            i+=1
            
        if a[i]>high:  
            high=a[i] 
            i+=1  
        
        else: 
            i+=1 
        
       
    
    largest_product=highest*higher*high 
    print (f'three slot bubblesorted largest product {largest_product}')

x=[3,2,1,2,1,81,0,21,23,5]
print (x)            
#mergesorted_lp(x) 
three_slot_bbsorted_lp(x)