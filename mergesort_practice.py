#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 02:51:34 2020

@author: Reaz
mergersort_practice 
"""







def mergesort(s): 
    
    if len(s)>1: 
        mid=len(s)//2 
        left=s[0:mid] 
        right=s[mid:] 
        mergesort(left) 
        mergesort(right) 
        s=merge(left,right,s)  
        return s
    
    else: 
        #print (s)
        return s


def merge(a,b,s):
    
    i=j=k=0  
        
    
    while i < len(a):
        while j< len(b):  
                #print (f' if {a[i]} <= {b[j]}')
                if a[i]<=b[j]: 
                    s[k]=a[i] 
                    k+=1 
                    i+=1 
                    
                    if i==len(a): 
                        while j<len(b): 
                            s[k]=b[j] 
                            k+=1 
                            j+=1 
    
    
                elif b[j]<a[i]:  
                    #print (f' if {b[j]} <= {a[i]}')
                    s[k]=b[j] 
                    k+=1 
                    j+=1  
                    if j==len(b): 
                        while i<len(a): 
                            s[k]=a[i] 
                            k+=1 
                            i+=1 
    
                
    #print (s) 
    return s
            
       
def main():   
    s=[14,1,2,13,9,6,0,55,66]
    s=mergesort(s)  
    print (s)
    
if __name__=="__main__": 
    main()
    
