import sys

scatter = [['A', 'B', 'C', 'D'],
           ['E', 'F', 'G', 'H'],
           ['I', 'J', 'K', 'L'],
           ['M', 'N', 'O']]

position = {}

for y in range(len(scatter)):
    for x in range(len(scatter[y])):
        position[scatter[y][x]] = [y, x]


def scatter_puzzle(scatter_in):
    total = 0
    for k in range(len(scatter_in)):
        for p in range(len(scatter_in[k])):
            if scatter_in[k][p] == '.':
                continue

            input_y, input_x = [k, p]
            desire_y, desire_x = position[scatter_in[k][p]]

            sub_total = abs(input_y - desire_y) + abs(input_x - desire_x)
            total += sub_total
    return total


arr = []

brk = 0
for values in sys.stdin:
    value = [val for val in values.strip()]
    letters = "".join(value)
    arr.append(letters)
    if brk == 3:
        break
    brk += 1

scatter_puzzle(arr)
