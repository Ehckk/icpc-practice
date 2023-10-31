input = ['.TT...', 'TTTT..', 'TTTTT.', 'TTTTT.', 'TTTTTT', '..T...']
tree = []
output = []
for i, line in enumerate(input):
    tree.append([])
    output.append([])
    for char in line:
        tree[i].append(char)
        output[i].append('.')
print(tree)

graph = {}
for i in range(0, len(tree)):
    for j in range(0, len(tree[i])):
        if tree[i][j] == '.':
            output[i][j] += '.'
        else:
            checkNeighbors(i, j, 1)

def checkNeighbors(row, col, layer):
    if col == len(tree[row]) - 1 or col == 0 or col == len(tree[row]) - 1 or row == 0:
        output[row][col] =


print(output)
