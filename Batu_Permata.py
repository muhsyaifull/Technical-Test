#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'batuPermata' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def batuPermata(arr):

    elemen_batu = set('abcdefghijklmnopqrstuvwxyz')

    for batu in arr:
        elemen_batu &= set(batu)
        
    return len(elemen_batu)

if __name__ == '__main__':
    import os

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input().strip()
        arr.append(arr_item)

    result = batuPermata(arr)

    fptr.write(str(result) + '\n')
    fptr.close()
