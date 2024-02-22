#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:14:38 2023

@author: yeomss
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'bestInGenre' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING genre as parameter.
# Base URL: https://jsonmock.hackerrank.com/api/tvseries?page=
#

def bestInGenre(genre):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    genre = input()

    result = bestInGenre(genre)

    fptr.write(result + '\n')

    fptr.close()
