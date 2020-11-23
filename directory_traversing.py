#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:47:36 2020

@author: Reaz
"""

''' DOCUMENTATION:  
its a recursive algorithm, we walk into a path 
ask whether its a directory or a file
    -if its a file, 
        -stop and return the depth  
        
    -if its a directory 
        -get all the files in it 
        -create path with the files names  
        -increment the depth level 
        -call the function recursively to do the same thing 
    
    
    '''

import os 
import sys 
import re 
import glob  
import functools 
import time



starting_path='/Users/Reaz'
#starting_path='/Users/Reaz/Documents/python_codes/directory_test'  
depth=0  
directory_dict={}

@functools.lru_cache(maxsize=1000)
def directory_traverse(path,depth): 

    if os.path.isdir(path)== False: 
#        print (depth) 
#        print ('-----------')
#        print ('END OF THE ROAD') 
#        print ('\n') 
        
        return depth 

    else:   
        try: # to skip permission error for certain folders
            #print ('its a directory alright')
            os.chdir(path) 
            files=glob.glob('*')  
            depth+=1 
            #print (depth) 
            directory_dict[path]=(depth,files)
            for file in files: 
                current_path=os.path.join(path,file)  
                directory_traverse(current_path,depth) 
        except: 
            pass
        
start=time.time()        
directory_traverse(starting_path,depth)  
end=time.time() 
print (f'------- {end-start} seconds taken -------')        
        
        
        
        
        
        