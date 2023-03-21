# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 06:41:27 2020

@author: Ravi Varma Injeti
"""


def two_sum(arr, x):
    for i in range(len(arr)):
        left = i + 1
        right = len(arr) - 1
        temp = x - arr[i]
        while left <= right:
            mid = left + (right -left) // 2
            
            if arr[mid] == temp:
                return[left, mid + 1]
            elif arr[mid] < temp:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1
                
                
arr = [2,7,11,15]

x = 10            
print(two_sum(arr, x))