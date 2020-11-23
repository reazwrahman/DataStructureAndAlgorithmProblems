#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:04:56 2020

@author: Reaz
selection sort algorithm 

Documentation: We start by assuming that the first element 
is the smallest one. Then we look for something smaller in the  
list. If we find a smaller number we swap it with our assumed 
value. And we do this sequentially thru the whole list. 

Again, like bubble sort it's not important that we have hit 
each element individually. The ordering will take care of itself 
automatically as long as we move sequentially thru the indexes
"""

a=[96,5,1,4,2,84,13,2,21,3]


for i in range (len(a)):  
    for j in range (i+1,len(a)): 
        if a[j]<a[i]: 
            temp=a[i] 
            a[i]=a[j] 
            a[j]=temp

print (a)


''' this algorithm also works, this was my first try
#for i in range (len(a)):  
#    smallest=a[i] 
#    for j in range (i,len(a)):  
#        if a[j]<smallest: 
#            smallest=a[j] 
#            a[j]=a[i]
#            a[i]=smallest 
#    print (a)
#            
#            
#print (a) 
'''