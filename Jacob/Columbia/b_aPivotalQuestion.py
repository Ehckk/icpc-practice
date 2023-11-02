# Jacob Stephens, October 31, 2023
# Problem B: A Pivotal Question (GNYR ICPC 2023)

A = [int(i) for i in input().split()[1:]]

maxval = -float('inf')
minval = float('inf')
mins = []
maxes = []

# traverse forward and backward through list,
# updating running max and min values
for i in range(len(A)):
    if A[i] > maxval:
        maxes.append(A[i])
        maxval = A[i]

    x = A[len(A)-1-i]
    if x < minval:
        mins.append(x)
        minval = x

# calc pivots, and output
pivots = [str(n) for n in maxes if n in mins]
print(" ".join(pivots))