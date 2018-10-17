#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

def bucket_sort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i]/size)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])
 
    for i in range(length):
        insertion_sort(buckets[i])
 
    result = []
    for i in range(length):
        result = result + buckets[i]
 
    return result
 
def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp
 

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    count = 0
    n = len(expenditure)
    for i in range(n - d):
        median_of_bucket = 0.0
        #print(expenditure[i : i + d])
        temp = bucket_sort(expenditure[i : i + d])
        if (d % 2) == 1:
            k = int(d / 2) 
         #   print("k : {}".format(k))
            median_of_bucket = temp[k]
  
        else:
            k = int(d / 2)
          #  print("k : {}".format(k))
            median_of_bucket = (temp[k] + temp[k + 1]) / 2
        
        #print(median_of_bucket)
        #print(expenditure[i + d])
        if (median_of_bucket*2) <= (expenditure[i + d]):
            count += 1
            
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
