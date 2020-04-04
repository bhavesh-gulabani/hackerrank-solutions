# Problem Link => https://www.hackerrank.com/challenges/diagonal-difference/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr, n):
    i = 0
    j = 0
    sum1 = 0
    sum2 = 0

    while i < n and j < n:
        sum1 += arr[i][j]
        i += 1
        j += 1

    i = n-1
    j = 0
    sum2 = 0

    while i >= 0 and j < n:
        sum2 += arr[j][i]
        i -= 1
        j += 1

    return abs(sum1 - sum2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()
