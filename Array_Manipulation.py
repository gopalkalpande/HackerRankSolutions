#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    rows = len(queries)
    for i in range(rows):
        a = queries[i][0]
        b = queries[i][1]
        k = queries[i][2]
        arr[a - 1]  += k
        arr[b] -= k
            
    temp = 0
    max_value = 0
    for i in range(n):
        max_value += arr[i]
        if(temp < max_value):
            temp = max_value
    return temp
    
    
#********* Example Solution of how code is operating**********
    # 5 3
    # 1 2 100
    # 2 5 100
    # 3 4 100
    # index_position       0     1     2     3     4     5
    # arr                  0     0     0     0     0     0
    # 1st pass            100   0     -100  0     0     0
    # 2nd pass            100   100   -100  0     0     -100
    # 3rd pass            100   100   0     0     -100  -100
    
    # do cummulative sum  100   200   200   200   100

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
