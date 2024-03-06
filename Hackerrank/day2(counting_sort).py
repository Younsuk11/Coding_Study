#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
#counting sort
# Instead, you create an integer array whose index range covers the entire range of values in your array to sort. 
# Each time a value occurs in the original array, you increment the counter at that index. 
# At the end, run through your counting array, printing the value of each non-zero valued index that number of times.
#array 전체 숫자를 아우를 수 있는 index array -> 각 index에 맞는 숫자들이 각각 얼만큼 있는지 세는 알고리즘
#센 것을 기반으로 array을 형성
#constraints : array 성분은 0~100사이 값이다.

def countingSort(arr):
    # Write your code here
    result = [0] * 100 #초기 0으로 채워진 array들
    for i in arr:
        result[i] += 1
    return result

# from collections import Counter, defaultdict

# def countingSort(arr):
#     counts = defaultdict(lambda: 0, dict(Counter(arr)))

#     return [counts[x] for x in range(100)]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
