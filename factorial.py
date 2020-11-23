#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 00:40:38 2020

@author: Reaz
"""

def factorial(n): 
    
    print (f'first attempt at calculating {n}')
    if n>0:
        fact=n*factorial(n-1)  
        print (f'calculating {n} times {n-1} now')
        print (fact)  
        return fact
    
    else:  
        print (1)
        return 1 

 


factorial (5)