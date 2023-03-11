import sys
in_lines = ".BCD\nEAGH\nIJFL\nMNOK"


def dist(x1, y1, x2, y2):
    xdist = x2 - x1
    ydist = y2 - y1
    mDist = abs(xdist) + abs(ydist)
    return mDist


def solve_it(problem):
    coords = {
        "A": (0, 0),
        "B": (1, 0),
        "C": (2, 0),
        "D": (3, 0),
        "E": (0, 1),
        "F": (1, 1),
        "G": (2, 1),
        "H": (3, 1),
        "I": (0, 2),
        "J": (1, 2),
        "K": (2, 2),
        "L": (3, 2),
        "M": (0, 3),
        "N": (1, 3),
        "O": (2, 3),
    }
    x = 0
    y = 0
    scatter = 0
    for i in problem:
        if i == "\n":
            continue

        if i != ".":
            desired = coords[i]
            scatter += dist(x, y, desired[0], desired[1])


        x = x + 1
        if x > 3:
            x = 0
            y += 1

    return scatter

i = 0
input = []
for s in sys.stdin.readlines():
    input.append(s)
    
    i += 1
    if i == 4:
        break


print(solve_it("".join(input)))
