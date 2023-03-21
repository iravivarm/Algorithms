# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 05:54:07 2020

@author: Ravi Varma Injeti
"""


def remove_duplicates(num):
    index = 1
    
    while index < len(num):
        if  num[index] == num[index - 1]:
            num.pop(index)
        else:
            index = index + 1
    return len(num)



num = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates((num)))