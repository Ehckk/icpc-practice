from sys import stdin, stdout
from collections import deque

def processInput(strList):
    first = strList[0].split(' ')
    n, m = int(first[0]), int(first[1])

    grid = []
    for row in strList[1:]:
        grid.append([int(x) for x in row])
    
    return grid, n, m

def gridSolution(strList):
    grid, n, m = processInput(strList)
    yBound = len(grid) - 1
    xBound = len(grid[0]) - 1
    
    # bfs
    queue = deque([(0, 0, 0)])
    visited = set()
    moves = 0
    while queue:
        (y, x, moves) = queue.popleft()

        if (y, x) == (n - 1, m - 1):
            return moves
        
        jump = grid[y][x]

        directions = [
            (y + jump, x),
            (y - jump, x),
            (y, x + jump),
            (y, x - jump),
        ]
   
        for (newY, newX) in directions:
            if 0 <= newY <= yBound and 0 <= newX <= xBound and (newY, newX) not in visited:
                visited.add((newY, newX))
                queue.append((newY, newX, moves + 1))

    return -1 

raw = []
line = stdin.readline()
while line:
    raw.append(line.rstrip())
    line = stdin.readline()

stdout.write(str(gridSolution(raw)))
