# Problem Link => https://www.hackerrank.com/challenges/fibonacci-modified/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
    cache = [t1, t2]
    
    for i in range(2, n):
        num = cache[i-2] + (cache[i-1]*cache[i-1])
        cache.append(num)

    return cache[n-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
