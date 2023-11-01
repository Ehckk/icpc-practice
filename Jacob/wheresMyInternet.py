
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

total = set()
for i in inp:
    for j in i:
        int(j)
        total.add(j)

if 1 not in total:
    for i in total:
        print(i)
else:
    powered = {1}
    # create graph of two-way connections
    # key = node, value = empty list
    d = {}
    for ction in inp:
        for house in ction:    
            d[house] = list()

    # fill each value (empty list) with each node's connection(s)
    for ction in inp:
        (d.get(ction[0])).append(ction[1])
        (d.get(ction[1])).append(ction[0])

    count = 2
    
    for node in d:
        for neighbor in d.get(node):
            if (neighbor - node == 1) and (neighbor - max(powered) == 1):
                powered.add(neighbor)
                powered.add(node)

    outp = list(total - powered)
    # not all connected
    if len(outp) >= 1:
        for i in outp:
            print(i)
    # all connected
    else:
        print('Connected')
