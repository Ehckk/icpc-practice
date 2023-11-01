# Jacob Stephens, October 31, 2023

line = [int(i) for i in input().split()[1:]]
p = []
sortedLine = sorted(line)
for i in range(len(line)):
    if line[i] == sortedLine[i]:
        p.append(line[i])

# output
print(len(p), end= ' ')
print("".join(int(i) for i in p))
