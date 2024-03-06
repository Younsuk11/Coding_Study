#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

#nxm 행렬(square)을 받아서 오른쪽, 왼쪽 대각선 성분 합의 차이를 구해라

def diagonalDifference(arr):
    # Write your code here
    n = len(arr) #3
    right_sum = 0
    left_sum = 0
    for i in range(n):
        right_sum += arr[i][i]
        left_sum +=arr[i][n-i-1]
    return abs(right_sum - left_sum)

    #n = len(arr) - 1
    #return abs(sum([arr[i][i] - arr[i][n-i] for i in range(n+1)]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
