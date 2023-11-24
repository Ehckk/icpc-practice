import sys

for i in sys.stdin:
    # i is the line ('12 17 36')
    numList = i.split(' ')
    # splitting puts them into a list of strings ['12', '17', '36', ...]
    inputs = []
    for num in numList:
        inputs.append(int(num))
       
    # inputs = [12, 17, 36, 37, 51, 63, 92, 124]
    tower2 = inputs.pop(-1)
    tower1 = inputs.pop(-1)

    towerSolution1 = []
    towerSolution2 = []

    for i in inputs:
        for j in inputs:
            for k in inputs:
                if i + j + k == tower1 and (i != j) and (j != k) and (i != k):
                    towerSolution1.append(i)
                    towerSolution1.append(j)
                    towerSolution1.append(k)
                    inputs.remove(i)
                    inputs.remove(j)
                    inputs.remove(k)
                    towerSolution2.append(inputs[0])
                    towerSolution2.append(inputs[1])
                    towerSolution2.append(inputs[2])
    
    towerSolution1.sort(reverse = True)
    towerSolution2.sort(reverse = True)

    output = towerSolution1 + towerSolution2  #list 

    output = " ".join([str(c) for c in output])
    print(output)

