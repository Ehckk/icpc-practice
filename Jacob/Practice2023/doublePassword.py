p1 = input()
p2 = input()

n = 4
for i in range(4):
    if p1[i] == p2[i]:
        n -= 1

print(2**n)