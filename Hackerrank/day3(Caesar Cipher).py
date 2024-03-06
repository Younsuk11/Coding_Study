#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
#shift by k in alphabet letters, and maping original string to shifted alphabet letters.
#from string import ascii_lowercase, ascii_uppercase

#if 문 잘못짜면 runtime error : 최대한 효율적으로 짜라


def caesarCipher(s, k):
    
    from string import ascii_lowercase, ascii_uppercase # string alphabets
  
    result = ""
    for  v in s:
        if v in ascii_uppercase:
            i = (ascii_uppercase.index(v) +k) %26
            result += ascii_uppercase[i]
        elif v in ascii_lowercase:
            i =(ascii_lowercase.index(v) +k) %26 
            result += ascii_lowercase[i] 
        else:
            result += v
    
    return result




# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     s = input()

#     k = int(input().strip())

#     result = caesarCipher(s, k)

#     fptr.write(result + '\n')

#     fptr.close()

s = input()

k = int(input().strip())

result = caesarCipher(s, k)

