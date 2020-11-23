#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:52:15 2020

@author: Reaz
largest_continuous sum
"""



def largest_continuous_sum(a):
    
    global il 
    global il_dict 
    
    i=0 
    j=i+1 
    ls=a[0]
    il_dict={} 
    il=[]
    while i<len(a)-1:  
        ls=a[i] 
        current_sum=a[i]
        while j<len(a): 
            #print (f'checking if {current_sum}+{a[j]} is larger than {ls}') 
            if(current_sum+a[j]>ls): 
                ls=current_sum+a[j]  
                current_sum=ls
                #print (f'ls now is {ls}')
                se=(i,j)
                j+=1
            else:
                current_sum=ls+a[j] 
                j+=1 
        il.append(ls)
        il_dict[ls]=se
        i+=1 
        j=i+1
    print(f'largest sum is {max(il)}, start and end index are {il_dict[max(il)]}')  
    
    
largest_continuous_sum([1,2,-1,3,4,10,10,-10,-1]) 
largest_continuous_sum([1,2,-1,3,4,-1])