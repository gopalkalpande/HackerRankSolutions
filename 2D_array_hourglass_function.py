#!/bin/python3

import math
import os
import random
import re
import sys

# hourglass function
#a b c
#  d
#e f g



# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = -9 * 7      # total 7 elements in hourglass function and minimum value each element can have is -9. 
                          # So to compare the minimum sum is -63.
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            a = arr[i][j]
            b = arr[i][j+1]
            c = arr[i][j+2]
            d = arr[i+1][j+1]
            e = arr[i+2][j]
            f = arr[i+2][j+1]
            g = arr[i+2][j+2]
            hgs = a+b+c+d+e+f+g
            max_sum = max(max_sum,hgs)
            
    return max_sum
    


    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for i in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
