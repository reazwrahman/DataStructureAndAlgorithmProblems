#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:11:45 2020

@author: Reaz 
amazon stock profit_algorithm from UDEMY 
"""
# brute force method: 

def amzn_stock(a): 
    
    lp=0
    for i in range(len(a)-1): 
        for j in range(i+1,len(a)): 
            if a[j]-a[i]>lp: 
                lp=a[j]-a[i] 
    print (f'largest profit= ${lp}') 
    return lp 
  

### O(n) method with just one pass 

def amzn_stock2(a): 
    
    min_price=a[0] 
    max_profit=a[1]-a[0] 
    
    for price in a: 
        if price<min_price: 
            min_price=price 
        current_profit=price-min_price 
        if current_profit>max_profit: 
            max_profit=current_profit 

    print (f' maximum profit is ${max_profit}') 
    return max_profit 

a=[12,11,15,3,10] 
amzn_stock2(a)  