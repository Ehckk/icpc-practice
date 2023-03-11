import fileinput

def npuzzle(squares):
    positions = {
        "A": [0, 0],
        "B": [0, 1],
        "C": [0, 2],
        "D": [0, 3],
        
        "E": [1, 0],
        "F": [1, 1],
        "G": [1, 2],
        "H": [1, 3],

        "I": [2, 0],
        "J": [2, 1],
        "K": [2, 2],
        "L": [2, 3],

        "M": [3, 0],
        "N": [3, 1],
        "O": [3, 2]
    }

    scatter = 0
    for y in range(len(squares)):
        for x in range(len(squares[y])):
            if squares[y][x] == ".":
                continue
            
            [desiredY, desiredX] = positions[squares[y][x]]
            
            scatter += abs(desiredX - x) + abs(desiredY - y)
    
    return scatter

lines = []
for line in fileinput.input():
    line = line.rstrip()
    lines.append(line)
    if len(lines) == 4:
        print(npuzzle(lines))
        lines = []