H, W = [int(x) for x in input().split(" ")]

# read in the tree.
tree = []
for _ in range(H):
    l = input()
    r = []
    for c in l:
        r.append(c == "T")
    tree.append(r)

out = []
for y in range(H):
    row = []
    for x in range(W):
        row.append(".")
    out.append(row)

# add all "first" layers to the starting point
rest = []

for y in range(H):
    for x in range(W):
        first = False
        if tree[y][x]:
            for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx = x + dx
                ny = y + dy
                if nx < W and nx >= 0 and ny < H and ny >= 0:
                    first |= (not tree[ny][nx])
                else:
                    first = True
            if first:
                rest.append((x, y, 1))

visited = set([(x, y) for (x, y, _) in rest])

for (rx, ry, rl) in rest:
    out[ry][rx] = rl
    for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = rx + dx
        ny = ry + dy
        if nx < W and nx >= 0 and ny < H and ny >= 0:
            if not (nx, ny) in visited and tree[ny][nx]:
                visited.add((nx, ny))
                rest.append((nx, ny, rl+1))

biggest = max(r[2] for r in rest)
squares = 2 if biggest < 10 else 3

            
for y in range(H):
    for x in range(W):
        print(str(out[y][x]).rjust(squares, "."), end = "")
    print("")