#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:49:15 2020

@author: Reaz
"""

def string_permutation(string): 
    
    b=string
    a=list(b) 
    c=list(b)
    pm=[]
    for each_letter in c: 
        i=0 
        word=''
        while i<len(a)-1:   
            start=a[i]  
            end=a[i+1]
            a[i]=end
            a[i+1]=start  
            i+=1 
            word='' 
            for each in a: 
                word=word+each  
            if word not in pm:
                pm.append(word) 
    
    print (f'{len(pm)} distinct combinations found')
    print (pm) 
    return pm 


string_permutation('abc')
             
    
        
        
        
        
        