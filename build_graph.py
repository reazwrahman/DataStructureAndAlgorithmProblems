#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 05:00:20 2020

@author: Reaz
"""

graph={} 

graph['a']=['c'] 
graph['b']=['c','e']  
graph['c']=['a','b','d','e']  
graph['d']=['c']  
graph['e']=['c','b']  
graph['f']=[]  

connections=[]
for key in graph:  
    for val in graph[key]: 
        connections.append((key,val)) 

print (connections)