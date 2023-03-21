# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 06:26:08 2020

@author: Ravi Varma Injeti
"""


def valid_paranthesis(char):
    brackets = []
    for brac in char:
        if brac in ["(","{","["]:
            brackets.append(brac)
            
        else:
            if brac in [")","}","]"]:
                #return False
                ####storing in  a temporary variable####
                current_char = brackets.pop()
                if current_char == '(':
                    if brac != ")":
                        return False
                if current_char == '[':
                    if brac != ']':
                        return False
                if current_char == '{':
                    if brac != "}":
                        return False   
                
    if brackets:
         return False 
    
    return True
    
    
char = '{(lfjhbdg)}'#"{()}["
k = valid_paranthesis(char)
if k:
    print("True")
else:
    print("False")
    
    

            
                
            
            