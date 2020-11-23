#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:57:28 2020

@author: Reaz 

return the nth index of fibonacci sequence 
""" 

import time  
from functools import lru_cache

@lru_cache(maxsize=5000)
def fibonacci(n):
    
    if type(n) != int: 
        raise (TypeError)
    
    if n==0:  
        return 1 
    if n==1:  
        return 1 
    
    else:  
        fibo=fibonacci(n-1)+fibonacci(n-2)  
        return fibo
    
start=time.time()    
for n in range (1,350): 
    print (n,":",fibonacci(n+1)/fibonacci(n)) 
end=time.time() 

print (f'total time taken {end-start} seconds')