from sys import stdin


def grid_setup(matrix):
    # N X M grid, N is the number of rows (x_axis)
    n, m = (int)(matrix[0]), (int)(matrix[1])

    grid = []
    for row in matrix[2:]:
        grid.append([int(x) for x in row])

    return grid, n, m


def find_path(matrix):
    start = (0, 0)
    grid, _, _ = grid_setup(matrix)
    end = (len(grid) - 1, len(grid[0]) - 1)
    y_max, x_max = end

    visited = set([start])
    current_node = [(start, 0)]

    while current_node:
        node, num_moves = current_node.pop(0)
        if node == end:
            return num_moves

        max_jump = grid[node[0]][node[1]]

        delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        next_node = [(node[0] + dy*max_jump, node[1] + dx*max_jump)
                     for dy, dx in delta]

        for next_node_y, next_node_x in next_node:
            if (0 <= next_node_y <= y_max
                and 0 <= next_node_x <= x_max
                and (next_node_y, next_node_x)
                    not in visited):

                visited.add((next_node_y, next_node_x))
                current_node.append(
                    ((next_node_y, next_node_x), num_moves + 1))
    return -1


arr = []
for item in stdin:
    arr += item.split()

print(find_path(arr))
