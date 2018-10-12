#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    counts = 0
    for i in range(len(q)-1,-1,-1):     # starts from last index till first index of array
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2),i):     # as a person can move only two positions forward check between (element - 2)_th index to i_th index
            if q[j] > q[i]:                     # if the number is greater increase the count by one
                counts+=1
    print(counts)
    

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
