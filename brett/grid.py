N, M = map(int, input().split(" "))
t_x = N - 1
t_y = M - 1

grid = []
for _ in range(N):
    l = input()
    new_line = []
    for c in l:
        new_line.append(int(c))
    grid.append(new_line)

visited_set = {(0, 0)}
visited = [(0, 0, None)]

for (x, y, parent) in visited:
    # generate all the moves
    if x == t_x and y == t_y:
        break
    d = grid[x][y]
    
    neighbors = [
        (x + d, y),
        (x - d, y),
        (x, y + d),
        (x, y - d)
    ]

    for (nx, ny) in neighbors:
        if (nx, ny) not in visited_set and nx < N and nx >= 0 and ny < M and ny >= 0:
            visited_set.add((nx, ny))
            visited.append((nx, ny, (x, y)))

if x == t_x and y == t_y:
    count = 0
    #curr_x = x
    #curr_y = y
    curr_parent = parent
    # the last value is the end
    for (x, y, parent) in reversed(visited):
        if curr_parent is None:
            break
        if curr_parent == (x, y):
            count += 1
            curr_parent = parent
    print(count)
else:
    print(-1)
        # we are done. unwind it. next.