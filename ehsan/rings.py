from sys import stdin, stdout

def processInput(strList):
    grid = []
    for s in strList[1:]:
        grid.append([x for x in s])
    return grid

def ringSolution(strList):
    grid = processInput(strList)
    yBound = len(grid) - 1
    xBound = len(grid[0]) - 1
    currentRing = 0
    rings = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != 'T':
                continue

            directions = [
                (y + 1, x),
                (y - 1, x),
                (y, x + 1),
                (y, x - 1),
            ]

            for (newY, newX) in directions:
                if not (0 <= newY <= yBound and 0 <= newX <= xBound) or grid[newY][newX] == '.':
                    grid[y][x] = str(currentRing + 1)
                    if currentRing < len(rings):
                        rings[currentRing].append((y, x))
                    else:
                        rings.append([(y, x)]) 
                    break
    
    for r in rings:
        currentRing += 1
        for (y, x) in r:
            directions = [
                (y + 1, x),
                (y - 1, x),
                (y, x + 1),
                (y, x - 1),
            ]
            for (newY, newX) in directions:
                if not(0 <= newY <= yBound and 0 <= newX <= xBound and grid[newY][newX] == 'T'):
                    continue
                
                grid[newY][newX] = str(currentRing + 1)
                if currentRing < len(rings):
                    rings[currentRing].append((newY, newX))
                else:                         
                    rings.append([(newY, newX)])
    result = []
    for row in grid:
        newRow = []
        for c in row:
            if currentRing < 10:
                newRow.append(('.'*(2 - len(c)))+c)
            else:
                newRow.append(('.'*(3 - len(c)))+c)
        result.append(''.join(newRow))
    
    return '\n'.join(result)
 
raw = []
line = stdin.readline()
while line:
    raw.append(line.rstrip())
    line = stdin.readline()

stdout.write(str(ringSolution(raw)))