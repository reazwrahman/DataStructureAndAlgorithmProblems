e#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 23:13:54 2020

@author: Reaz
"""
''' tip: when doing recursion problem, 
always think about the stopping condition first''' 

global found 
global my_str  
my_str=''
found=[] 


def word_split(string,word_list):  
    
    global found 
    global my_str
   
    
    if len(my_str)==len(string): 
        print (f'all words found {found}')  
        print (word_list)
        return found    
        
        
    elif len(word_list)>0:   
        for i in range (len(word_list)):
            if word_list[i] in string:  
                my_str=my_str+word_list[i]
                found.append(word_list[i])  
                del (word_list[i])   
                word_split(string,word_list)   
    
word_split('ilovedogsJohn',['i','dogs','love','John'])
