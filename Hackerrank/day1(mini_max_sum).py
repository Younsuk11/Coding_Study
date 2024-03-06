import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
# array의 5개 중 4개의 합 중에서 최소, 최대 출력

def miniMaxSum(arr):
    # Write your code here

    arr.sort() #ascending sort , desencding sort : sort(reverse = True)
    print(sum(arr[:-1]), sum(arr[1:]))
    #print(f"{sum(arr) - max(arr)} {sum(arr) - min(arr)}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)