r, k = map(int, input().split())

flips = k // r
if k % r > r/2:
    flips += 1

if flips % 2 == 0:
    print('up')
else:
    print('down')