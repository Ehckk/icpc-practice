import fileinput

def bread(inputList, targetList):
    indexMap = {}

    for i in range(len(targetList)):
        indexMap[targetList[i]] = i

    swapCount = 0
    j = 0

    while j < len(inputList):
        targetIndex = indexMap[inputList[j]]
        if j == targetIndex:
            j += 1
        else:
            inputList[j], inputList[targetIndex] = inputList[targetIndex], inputList[j]
            swapCount += 1

    return "Possible" if swapCount % 2 == 0 else "Impossible"

firstLine = True
lists = []
for line in fileinput.input():
    line = line.rstrip()
    if not firstLine:
        lists.append(list(map(int, line.split(' '))))

    if len(lists) == 2:
        print(bread(lists[0], lists[1]))

    if firstLine:
        firstLine = False
    
