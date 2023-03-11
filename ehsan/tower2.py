import fileinput
import math

def binarySearch(nums, target, l):
    r = len(nums) - 1

    while l < r:
        mid = math.floor((l + r) / 2)

        if nums[mid] >= target:
            r = mid
        if nums[mid] < target:
            l = mid + 1
    
    return l if nums[l] == target else -1

def tower(rawInput):
    t1Sum = rawInput[6]
    boxes = rawInput[0:6]
    boxes.sort()

    def findTowerIndexes():
        for i in range(len(boxes)):
            for j in range(i+1, len(boxes) - 1):
                target = t1Sum - boxes[i] - boxes[j]
                k = binarySearch(boxes, target, j + 1)
                if k > -1:
                    return [i, j, k]
    
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