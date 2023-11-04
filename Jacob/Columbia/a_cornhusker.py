'''
    Jacob Stephens / November 3, 2023
    Problem A: Cornhusker -- GNYR ICPC 2023
'''
husks = list(map(int, input().split()))
N, KWF = map(int, input().split())

sum = 0
for i in range(5):
    sum += husks[i*2] * husks[i*2+1]

print(sum // 5 * N // KWF)
