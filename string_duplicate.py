#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:33:29 2020

@author: Reaz
"""
def string_duplicate(a):
    
    print (a)  
    cp=0
    i=0 
    j=i+1
    while i<(len(a)-1):
        while j<len(a):  
            #print (f'checking if {a[i]} = {a[j]}')
            if a[i]==a[j]:  
                print (f'found duplicate {a[j]}')  
                cp=1
                #break  
                return False
                
            else: 
                j+=1
        
        if cp==0:
            i+=1 
            j=i+1
        else: 
            break
    if i==len(a)-1: 
        print ('no duplicates found') 
        return True

string_duplicate('goog')