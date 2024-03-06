#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
from collections import Counter
def lonelyinteger(a):
    # Write your code here
    #return a.count(1) #1의 occurence를 출력
    c = Counter(a)
    for k in c.keys():
        if c[k] ==1:
            return k
        
    #return Counter(a).most_common()[-1][0] ## 각각의 빈도수 세서 내림차순으로 정리
    

#다른 답

def lonelyinteger(a):
    
    return 





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
