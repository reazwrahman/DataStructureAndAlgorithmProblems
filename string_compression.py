#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:34:55 2020

@author: Reaz 

first algorithm has O(2n) time complexity 
second algorithm O(n) 
but second algorithm only works for consecutive 
duplicates, whereas first algorithm is not  
restricted like that. 
"""

def string_compression(a): 
    
    
    i=0
    counter=0 
    sample={}
    for i in range(len(a)): 
        if a[i] not in sample:  
            counter=1
            sample[a[i]]=counter 
        else: 
            counter=sample[a[i]]+1 
            sample[a[i]]=counter 
    
    keys=list(sample.keys())  
    result=''
    for i in range(len(sample)): 
        result=result+keys[i]+str(sample[keys[i]]) 
    
    print (result) 
    return result
        
    



def string_compression2(a): 
    
    counter=1 
    i=0 
    result=''
    while i <len(a)-1: 
        if a[i+1]==a[i]:  
            #print ('found similar')
            counter+=1 
            i+=1  
            
        else:  
            #print (a[i]+str(counter))  
            result=result+a[i]+str(counter)
            counter=1
            i+=1  
    # to take care of the very last letter, 
# since i stops at lena(a)-1        
    result=result+a[i]+str(counter) 
    print (result) 
    return result

a='AAAABBBBCCCCvvDDEEEEf'
print(string_compression(a)==string_compression2(a))   
   
  