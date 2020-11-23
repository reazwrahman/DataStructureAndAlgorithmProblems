#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:28:54 2020

@author: Reaz
""" 

from collections import defaultdict

a=[3,1,2,4,4,2,3,1,5]
 
def hashmap_solution(a):
    track=defaultdict(int)
    for x in a:
        track[x]+=1 
    
    for y in track: 
        if track[y]==1: 
            print (f'the non repeated number is {y}') 
            

def set_solution(a):     
    solution=2*sum(set(a))-sum(a)    
    print (f'the non repeated number is {solution}') 

def exclusive_or_solution(a): 
    solution=0 
    for x in a: 
        solution=solution^+x #exclusive or operation 
    print (f'the non repeated number is {solution}')  

hashmap_solution(a) 
set_solution(a) 
exclusive_or_solution(a)
    
        