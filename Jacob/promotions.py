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

# obtain length of every level
levels = [0 for _ in range(E)]
for level in dist_graph.values():
    levels[level] += 1

# find outputs
for currP in [A,B]: 
    promoted = 0
    for i in range(len(levels)):
        r = currP - levels[i]
        

        if r == 0:
            lastLevel = i+1
            promoted += levels[i] 
            currP = r
            break

        elif r < 0:
            lastLevel = i+1
            break

        promoted += levels[i] 
        currP = r  

    print(promoted)


never = sum(levels[lastLevel:])
print(never)from collections import defaultdict

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

# obtain length of every level
levels = [0 for _ in range(E)]
for level in dist_graph.values():
    levels[level] += 1

# find outputs
for currP in [A,B]: 
    promoted = 0
    for i in range(len(levels)):
        r = currP - levels[i]
        

        if r == 0:
            lastLevel = i+1
            promoted += levels[i] 
            currP = r
            break

        elif r < 0:
            lastLevel = i+1
            break

        promoted += levels[i] 
        currP = r  

    print(promoted)


never = sum(levels[lastLevel:])
print(never)
