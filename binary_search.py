# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 05:37:21 2020

@author: Ravi Varma Injeti
"""

def binary_search(arr, x): 
    low = 0
    high = len(arr) - 1
    mid = 0
  
    while low <= high: 
  
        mid = (high + low) // 2
  
        
        if arr[mid] < x: 
            low = mid + 1
  
        
        elif arr[mid] > x: 
            high = mid - 1
  
        
        else: 
            return mid 
  
    
    return -1
  
  
arr = [1,2,3,4,5,6,7,8]
searching = binary_search(arr, 9)
print(searching)