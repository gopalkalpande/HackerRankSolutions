# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 12:25:38 2018

@author: CMBLAB
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#********This code works fine but it's not time bounded for some input cases.*********
#           I'have used Selection sort algorithm for this problem.[start at ###1 and ends at ###2]


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
###1
    for i in range(0, len(arr) - 1):
        min_index = i
        for j in range(i+1 , len(arr)):
            if(arr[j] < arr[min_index]):
                min_index = j
        
        if(arr[min_index] < arr[i]):
            count = count + 1    
        arr[min_index], arr[i] = arr[i], arr[min_index]
###2        
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
