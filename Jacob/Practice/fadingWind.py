import math
h, v, k, s = map(int, input().split())

while h > 0:
    s = s + v
    v = v - max(1, math.floor(v/10))
    if v >= k:
        h = h - 1
        if h == 0:
            v = 0
    if v <= 0:
        h = 0
        v = 0
    
    if s > 0:
        s = s - 1
