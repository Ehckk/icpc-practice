import fileinput

def tower(boxes):
    if (len(boxes) != 8):
        return ""
    
    tower1Sum = boxes[6];
    t1Indexes = []

    def findTowerIndexes(currentSum, idx, indexes, found):
        if currentSum > tower1Sum or len(indexes) > 3 or found:
            return
        if currentSum == tower1Sum and len(indexes) == 3:   
            found = True
            t1Indexes.extend(indexes)
            return
        
        while idx < len(boxes) - 2 and not found:
            indexes.append(idx)
            findTowerIndexes(currentSum + boxes[idx], idx + 1, indexes, found)
            indexes.pop()
            idx += 1
    
    findTowerIndexes(0, 0, [], False)

    # python moment
    t2Result = [boxes[i] for i in range(len(boxes) - 2) if i not in t1Indexes]
    t1Result = [boxes[i] for i in t1Indexes]

    t1Result.sort(reverse=True)
    t2Result.sort(reverse=True)

    return " ".join([str(x) for x in (t1Result + t2Result)])

for line in fileinput.input():
    line = line.rstrip()
    boxes = [int(x) for x in line.split()]
    print(tower(boxes))