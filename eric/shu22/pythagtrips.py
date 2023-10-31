"""
a^2 + b^2 = c^2
c = sqrt(a^2 + b^2)
"""
import math

LIMIT = 10000000

def gcf(num1, num2):
    if num2 == 0: return num1
    return gcf(num2, num1 % num2)

def solve():
    C = int(input())
    counts = [0] * 4
    b = 1
    for a in range(C - 1, 0, -1): # PTs smaller than C
        if a <= b: break
        b = math.sqrt(pow(C, 2) - pow(a, 2))
        if not b == b // 1: continue # use flooring to avoid round off bs
        # We have found a pythag triple
        print(b, a, C) 
        if gcf(C, gcf(b, a)) == 1:
            # GCF of all factors is 1, we have found a PPT
            counts[0] += 1
        else:
            # Non-PPT count
            counts[1] += 1
    a = LIMIT
    for b in range(C + 1, LIMIT + 1): # PTs smaller than B up to 2500
        a = math.sqrt(pow(C, 2) + pow(b, 2))
        if not a == a // 1: continue 
        print(b, a, C) 
        if gcf(C, gcf(a, b)) == 1:
            counts[2] += 1
        else:
            counts[3] += 1
    print(counts[0], counts[1], counts[2], counts[3])

solve()
# bruh 🗿