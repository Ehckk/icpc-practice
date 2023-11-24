'''
Jacob Stephens, ICPC
October 3, 2023
Kingpin Escape Kattis https://open.kattis.com/problems/kingpinescape
'''
n, h = map(int, input().split()) # where n <= 10,000

# build two way graph (O(n))
graph = {}
for _ in range(n-1):
    node, neighbor = map(int, input().split())
    if node not in graph:
        graph[node] = []
    
    if neighbor not in graph:
        graph[neighbor] = []
    
    graph[node].append(neighbor)
    graph[neighbor].append(node)

# find leaves in graph
leaves = [node for node in graph if len(graph.get(node)) == 1]

retiredLeaf = leaves[0] # used later if odd number of leaves
tunnels = [] # solution array

def buildTunnel(leaf, tunnelCount):
    visited = {leaf: 0}
    stack = [[leaf, 0]]
    count = 0
    
    # BFS to find two leaves furthest apart
    while stack:
        node, count = stack.pop(0)
        count += 1
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append([neighbor, count])
                visited[neighbor] = count

    reverse = {visited[i]: i for i in visited if i in leaves} 
    
    # establish connection between located leaves
    endLeaf1 = reverse.get(max(reverse))
    endLeaf2 = reverse.get(min(reverse))
    graph[endLeaf1].append(endLeaf2)
    graph[endLeaf2].append(endLeaf1)
    
    # remove from leaves array
    leaves.remove(endLeaf1)
    leaves.remove(endLeaf2)

    # append this connection to answer
    tunnels.append([endLeaf1, endLeaf2])

    # if odd number of leaves
    if len(leaves) == 1:
        tunnels.append([leaves[0], retiredLeaf])
    
for leaf in leaves: #calling this function for every leaf is causing O(n^2)
    buildTunnel(leaf, 0)

# output 
print(len(tunnels))
for tunnel in tunnels:
    print(f'{tunnel[0]} {tunnel[1]}')
