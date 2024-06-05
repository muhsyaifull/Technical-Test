#!/bin/python3

import os
import sys

#
# Complete the 'kuadrat' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def kuadrat(a, b):
    
    def akar_kuadrat(x):
        if x == 0 or x == 1:
            return x
        start = 1
        end = x
        while start <= end:
            mid = (start + end) // 2
            mid_sq = mid * mid
            if mid_sq == x:
                return mid
            elif mid_sq < x:
                start = mid + 1
            else:
                end = mid - 1
        return end
    
    akar_a = akar_kuadrat(a)
    akar_b = akar_kuadrat(b)
    
    batas_bawah = akar_a if akar_a * akar_a >= a else akar_a + 1
    batas_atas = akar_b if akar_b * akar_b <= b else akar_b - 1
    
    if batas_bawah > batas_atas:
        return 0
    else:
        return (batas_atas - batas_bawah + 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])
        b = int(first_multiple_input[1])

        result = kuadrat(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
