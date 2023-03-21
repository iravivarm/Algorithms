# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 05:55:23 2020

@author: Ravi Varma Injeti
"""


def last_word(word):
    words = word.split()
    if len(words) == 0:
        return 0
    return len((words[-1]))
        
word = "Ravi Varma Injeti"
print(last_word(word))