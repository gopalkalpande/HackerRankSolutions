''' I got this code in the following youtube video. Watch the full video for better understanding of the problem 
    and how it is optimized.
  https://youtu.be/46V6tnxy_Vs  
  
  Thank you.  '''


#!/bin/python3

import math
import os
import random
import re
import sys

# Used to get the median
def get_median(counting_sort_list, trailing_days, median_position):
    counter, left = 0, 0
    # Find number where we pass through the median
    while counter < median_position:
        counter += counting_sort_list[left]
        left += 1
        
    # Step back one time
    right = left
    left -= 1
    
    # If odd or both left and right of even are same number
    if counter > median_position or trailing_days % 2 != 0:
        return left
    else:
        # Find right value for even
        while counting_sort_list[right] == 0:
            right += 1
        return ((left + right) / 2)
    
    
    
    

 # Complete the activityNotifications function below.
def activityNotifications(expenditure, trailing_days):
    # Initialize the counting sort array
    counting_sort_list = [0]*201
    end = trailing_days
    
    # Perform counting sort
    for i in range(0, end):
        counting_sort_list[expenditure[i]] += 1
    current = 0
    total_notification = 0
    
    # Determine odd or even median position
    if trailing_days % 2 == 0:
        median_position = int(trailing_days / 2)
    else:
        median_position = int(trailing_days / 2) + 1
        
    total_expenditure_length = len(expenditure)
    
    # Start and move along expenditures list
    while end < total_expenditure_length:
        median = get_median(counting_sort_list, trailing_days, median_position)
        if expenditure[end] >= median * 2:
            total_notification += 1
            
        # Modify the queue, first in first out
        counting_sort_list[expenditure[current]] -= 1
        counting_sort_list[expenditure[end]] += 1
        current += 1
        end += 1
        
    return total_notification




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
