import fileinput

def tower(rawInput):
    t1Sum = rawInput[6]
    boxes = rawInput[0:6]
    boxes.sort()

    def findTowerIndexes():
        for i in range(len(boxes)):
            l = i + 1
            r = len(boxes) - 1

            while l < r:
                currentSum = boxes[i] + boxes[l] + boxes[r]

                if currentSum < t1Sum:
                    l += 1
                if currentSum > t1Sum:
                    r -= 1
                if currentSum == t1Sum:
                    return [i, l, r]
            
    t1Indexes = findTowerIndexes()

    t2Result = [boxes[i] for i in range(len(boxes)) if i not in t1Indexes]
    t1Result = [boxes[i] for i in t1Indexes]

    t1Result.sort(reverse=True)
    t2Result.sort(reverse=True)

    return " ".join([str(x) for x in (t1Result + t2Result)])

for line in fileinput.input():
    line = line.rstrip()
    rawInput = [int(x) for x in line.split()]
    print(tower(rawInput))