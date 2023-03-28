import sys


def connected(house):
    graph = {}

    (num_houses, c) = house[0]
    num_houses = int(num_houses)

    for k, v in house[1:]:
        (k, v) = int(k), int(v)
        if k not in graph:
            graph[k] = [v]
        else:
            graph[k].append(v)
        if v not in graph:
            graph[v] = [k]
        else:
            graph[v].append(k)

    to_visite = []
    visited = set()

    """
    num_houses = 6
    1, 2, 3, 4, 5, 6
    visited = (1, 2, 3, 4)
    houses = [1, 2, 3, 4, 5, 6, 7, 8]
    vis = [1, 2, 3, 4]
    """

    if 1 in graph:
        visited.add(1)
        to_visite.append(1)

    while to_visite:
        node = to_visite.pop(0)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                to_visite.append(neighbor)
                visited.add(neighbor)

    if num_houses == len(visited):
        print('Connected')
        return

    not_visited = (list(set(range(1, num_houses + 1)) - visited))
    for i in sorted(not_visited):
        if i != 1:
            print(i)


list_tup = []
for n in sys.stdin:
    list_tup.append(tuple(n.split()))

connected(list_tup)
