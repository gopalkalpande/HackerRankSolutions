#!/bin/python3

import math
import os
import random
import re
import sys
import statistics


# Python program for counting sort 
  
# The main function that sort the given string arr[] in  
# alphabetical order 
def countSort(arr): 
  
    # The output character array that will have sorted arr 
    output = [0 for i in range(256)] 
  
    # Create a count array to store count of inidividul 
    # characters and initialize count array as 0 
    count = [0 for i in range(256)] 
  
    # For storing the resulting answer since the  
    # string is immutable 
    ans = ["" for _ in arr] 
  
    # Store count of each character 
    for i in arr: 
        count[i] += 1
  
    # Change count[i] so that count[i] now contains actual 
    # position of this character in output array 
    for i in range(256): 
        count[i] += count[i-1] 
  
    # Build the output character array 
    for i in range(len(arr)): 
        output[count[arr[i]]-1] = arr[i] 
        count[arr[i]] -= 1
  
    # Copy the output array to arr, so that arr now 
    # contains sorted characters 
    for i in range(len(arr)): 
        ans[i] = output[i] 
    return ans 


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    count = 0
    n = len(expenditure)
    for i in range(n - d):
        median_of_bucket = 0.0
        #print(expenditure[i : i + d])
        temp = countSort(expenditure[i : i + d])
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
