#!/bin/python3

import math
import os
import random
import re
import sys

def merge(prices, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = prices[l + i] 
  
    for j in range(0 , n2): 
        R[j] = prices[m + 1 + j] 
  
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            prices[k] = L[i] 
            i += 1
        else: 
            prices[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        prices[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        prices[k] = R[j] 
        j += 1
        k += 1
  
# l is for left index and r is right index of the 
# sub-array of arr to be sorted 
def mergeSort(prices,l,r): 
    if l < r: 
  
        # Same as (l+r)/2, but avoids overflow for 
        # large l and h 
        m = int((l+(r-1))/2)
  
        # Sort first and second halves 
        mergeSort(prices, l, m) 
        mergeSort(prices, m+1, r) 
        merge(prices, l, m, r)
        return prices



# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    count = 0
    n = len(expenditure)
    for i in range(n - d):
        median_of_bucket = 0.0
        #print(expenditure[i : i + d])
        temp = mergeSort(expenditure[i : i + d],0,len(expenditure[i : i + d])-1)
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
