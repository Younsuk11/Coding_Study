#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:17:01 2023

@author: yeomss
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'closestStraightCity' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY c
#  2. INTEGER_ARRAY x
#  3. INTEGER_ARRAY y
#  4. STRING_ARRAY q
#

def closestStraightCity(c, x, y, q):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    c_count = int(input().strip())

    c = []

    for _ in range(c_count):
        c_item = input()
        c.append(c_item)

    x_count = int(input().strip())

    x = []

    for _ in range(x_count):
        x_item = int(input().strip())
        x.append(x_item)

    y_count = int(input().strip())

    y = []

    for _ in range(y_count):
        y_item = int(input().strip())
        y.append(y_item)

    q_count = int(input().strip())

    q = []

    for _ in range(q_count):
        q_item = input()
        q.append(q_item)

    result = closestStraightCity(c, x, y, q)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
