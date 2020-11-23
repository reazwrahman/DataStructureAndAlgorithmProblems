#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 14:34:54 2020

@author: Reaz
"""

a=[-1, 0, 1, 2, -1, -4] 
sol=[]
i=0 
j=0 
k=0 
while i<len(a):  
    while j<len(a) and j!=i: 
        while k<len(a) and k!=j and k!=i: 
            if i+j+k==0: 
                sol.append((i,j,k))  
                print (i,j,k) 
                i+=1 
                j+=1  
                k+=1 
            else: 
                i+=1 
                j+=1  
                k+=1 