#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:15:52 2023

@author: yeomss
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'predictAnswer' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY stockData
#  2. INTEGER_ARRAY queries
#

def predictAnswer(stockData, queries):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stockData_count = int(input().strip())

    stockData = []

    for _ in range(stockData_count):
        stockData_item = int(input().strip())
        stockData.append(stockData_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = predictAnswer(stockData, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
