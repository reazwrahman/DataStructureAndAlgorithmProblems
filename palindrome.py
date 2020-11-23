#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:47:48 2020

@author: Reaz 
2 algorithms are implemented
"""


def palindrome(word): 
    
    b=[]
    for i in range(len(word)-1,-1,-1):  
        b.append(word[i])
    print (f'original= {word}')
    print (f'reversed= {b}') 
    i=0
    while i<len(word): 
        if word[i]!=b[i]: 
            print ('not an anagram')  
            return False
            break
        else: 
            i+=1
    if i==len(word):
        print ('its an anagram')  
        return True

def palindrome2(a): 
    i=0  
    cp=0
    j=len(a)-1
    while i<=len(a)//2 and cp==0: 
        while j>=len(a)//2:   
            print (f'checking if {a[i]} = {a[j]}') 
            if a[i]!=a[j]: 
                print ('not a palindrome')  
                cp=1 
                return False
                break   
                
            elif a[i]==a[j] and cp==0: 
                i+=1 
                j-=1  
            
    if i>=len(a)//2 or j<=len(a)//2: 
        print ('its a palindrome') 
        return True 
    
word=a="kayak" 
print(palindrome(word)==palindrome2(a))