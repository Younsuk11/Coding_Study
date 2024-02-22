import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    p, n, z = 0,0,0
    a = len(arr)

    ### list는 바로 boolean 계산이 없어서 하나씩 계산해야한다. (numpy는 가능한 기능이니 혼동하지 말것)
    for i in arr: 
        if i > 0: p +=1
        elif i<0 : n+=1
        else: z +=1

    p_r = float(p/a)
    n_r = float(n/a)
    z_r = float(z/a)
    print(f"{p_r:.6f}") ## 실수형 변수 float 자리수 지정
    print(f"{n_r:.6f}")
    print(f"{z_r:.6f}")
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


