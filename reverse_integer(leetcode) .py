#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:02:37 2020

@author: Reaz 

time complexity= O(n/2)+O(n)~O(n)
""" 

def reverse_integer(a):
    
    negative=0  
    if a<0: 
        negative=1   
        a=a*-1
    a=list(str(a))  
    i=0 
    while i<=(len(a)//2)-1: 
        start=a[i] 
        end=a[len(a)-1-i] 
        a[i]=end 
        a[len(a)-1-i]=start 
        #print (a) 
        i+=1   
    number=''
    for i in range(len(a)): 
      number=number+a[i]    
    number=int(number) 
    if negative==1:  
        number=number*-1
        
    print(number)  

a=-41200
reverse_integer(a)