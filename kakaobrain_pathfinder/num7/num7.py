#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:18:57 2023

@author: yeomss
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'bioHazard' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY allergic
#  3. INTEGER_ARRAY poisonous
#

def bioHazard(n, allergic, poisonous):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    allergic_count = int(input().strip())

    allergic = []

    for _ in range(allergic_count):
        allergic_item = int(input().strip())
        allergic.append(allergic_item)

    poisonous_count = int(input().strip())

    poisonous = []

    for _ in range(poisonous_count):
        poisonous_item = int(input().strip())
        poisonous.append(poisonous_item)

    result = bioHazard(n, allergic, poisonous)

    fptr.write(str(result) + '\n')

    fptr.close()
