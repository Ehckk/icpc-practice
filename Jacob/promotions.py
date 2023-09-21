from collections import defaultdict

A, B, E, P = map(int, input().split())

# create adj list
graph = {}
for _ in range(P):
    x, y = map(int, input().split())

    if x not in graph:
        graph[x] = []
    
    graph[x].append(y)

# determine dependent nodes using adj list
v = set()
for node in graph:
    for n in graph.get(node):
        v.add(n)

# determine roots using dependent nodes
roots = []
for key in list(graph):
    if key not in v:
        roots.append(key)

# determine dependency level of each node using roots

dist_graph = defaultdict(lambda: -1)
def dfs(root, graph):
    stack = [(root, 0)]

    while stack:
        node, depth = stack.pop()
        
        if depth > dist_graph[node]:
            dist_graph[node] = depth

        for neighbor in graph.get(node, []):
            stack.append((neighbor, depth + 1))
    
    return dist_graph


for root in roots:
    dfs(root, graph)


print('x')
'''
for root in roots:
    empToDep[root] = {0}

count = 0
visited = roots[:]


visited = set()
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)


for root in roots:
    dfs(visited, graph, roots)


for i, root in enumerate(roots):
    for neighbor in graph.get(root):
        if neighbor not in visited:
            visited.append(neighbor)
            roots.append(neighbor)

            if root not in empToDep:
                empToDep[root] = set()

            empToDep[root].add(i)

    

print(visited, roots)
#print(f'Unvisited: {set(v - list(graph))}')

# make dict where key = employee and value = longest path to get there
# make dict where key = path number from 0 to longest and value = employees in that group

# 4 - 2 = 2 example find solution using graph
# 2 - 2 = 0
'''