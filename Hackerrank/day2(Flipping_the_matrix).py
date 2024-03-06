#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#
#sort(reverse = True) :  내림차순 정리 
#reverse() : 단순 순서 바꾸기
#2nx2n matrix(nxn 총 4개) -> upper left의 총합이 최대가 될 수 있도록 reverse
#2차원 -> 1차원 : sum(list, []) | 혹은 : list(itertools.chain(*list1)) | list(itertools.chain.from_iterable(list1))
# 굳이 최대를 "찾을" 필요는 없을 수도 있다. 만드는 경우도 생각하자. 


def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix)
    s = 0 #making max sum
    for i in range(n//2):
        for j in range(n//2):
            s += max(matrix[i][j], matrix[n -1-i][j], matrix[i][n-1-j], matrix[n-1-i][n-1-j])
            #checking which element is bigger when you do row or column reversing

    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
