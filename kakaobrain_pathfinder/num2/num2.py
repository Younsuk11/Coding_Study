#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 14:25:39 2023

@author: yeomss
"""

#%%








#%%
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMinimumTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. UNWEIGHTED_INTEGER_GRAPH centre
#  2. INTEGER_ARRAY status
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#
#

def findMinimumTime(centre_nodes, centre_from, centre_to, status):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    centre_nodes, centre_edges = map(int, input().rstrip().split())

    centre_from = [0] * centre_edges
    centre_to = [0] * centre_edges

    for i in range(centre_edges):
        centre_from[i], centre_to[i] = map(int, input().rstrip().split())

    status_count = int(input().strip())

    status = []

    for _ in range(status_count):
        status_item = int(input().strip())
        status.append(status_item)

    result = findMinimumTime(centre_nodes, centre_from, centre_to, status)

    fptr.write(str(result) + '\n')

    fptr.close()
