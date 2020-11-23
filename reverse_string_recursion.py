#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:30:07 2020

@author: Reaz
"""
rev=[]
def reverse_string(string,start,end): 
    
   
    string=list(string)
    if start==end:   
        result=''
        for i in range(len(string)):  
            result=result+string[i]
        print (result)
        return result
    
    else: 
        temp=string[start] 
        string[start]=string[end] 
        string[end]=temp 
        start+=1 
        end-=1 
        reverse_string(string,start,end) 

reverse_string('anagram',0,len('anagram')-1)