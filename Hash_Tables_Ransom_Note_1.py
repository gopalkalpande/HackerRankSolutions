#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    for word in note:
        if word in magazine:
            magazine.remove(word)
        else:
            return False
    return True

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    flag = checkMagazine(magazine, note)
    
    if(flag):
        print("Yes")
    else:
        print("No")
