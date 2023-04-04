
stringInp = []
inp1 = input().split()
nHouse = int(inp1[0])
nRows = int(inp1[1])


for _ in range(nRows):
    stringInp.append(input().split())

inp = []
for i in stringInp:
    inp.append(list(map(int, i)))

inp.sort()