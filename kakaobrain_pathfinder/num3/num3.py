#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 14:26:53 2023

@author: yeomss
"""

#%%








#%%

#!/bin/python3

import math
import os
import random
import re
import sys



#%%
text = "ab"
p = "AB"
s = "DE"


p_list = [ text[:i+1] for i in range(len(text))]
s_list = [ text[i:] for i in range(len(text))]
# print(text.find(p))
# print(s[::-1])}

l = []
for i in range(len(text)):
    for j in range(i+1, len(text)+1):
               
               l.append(text[i:j])

#
#reverse로 찾던, 그냥 찾던 항상 0이 나와야한다.-> 0이 나올 경우, 


#%%
#
# Complete the 'calculateScore' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING text
#  2. STRING prefixString
#  3. STRING suffixString
#

def calculateScore(text, prefixString, suffixString):
    # Write your code here
    
    #all substrings
    p = []
    s = []

    
    for i in range(len(prefixString)):
        for j in range(i+1, len(prefixString)+1):
            p.append(prefixString[i:j])
            
    for i in range(len(suffixString)):
        for j in range(i+1, len(suffixString)+1):
            s.append(suffixString[i:j])
    
    p = list(set(p))
    s =list(set(s))
                                   
    check = []
    #checking
    for i in range(len(text)):
        for j in range(i+1, len(text)+1):
            
            
            for pre in p:
                for suf in s:
                    
                    if text.startswith(pre, i, j): text.endswith(suf, i, j):
                        score = len(pre) + len(suf)
                        check.append(text[i:j])
    
    check.sort()
    temp = list(map(len, check))
    return p, s,check, check[temp.index(max(temp))]
    

#%%

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    text = input()

    prefixString = input()

    suffixString = input()

    result = calculateScore(text, prefixString, suffixString)

    fptr.write(result + '\n')

    fptr.close()
