#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:00:22 2020

@author: Reaz 

leetcode: stock price question 2
"""

a=[1, 7, 2, 3, 6, 7, 6, 7]
min_price=a[0] 
max_profit=0
for i in range (1,len(a)):   
    if a[i]>a[i-1]: 
        max_profit=max_profit+(a[i]-a[i-1]) 
print (max_profit)
        