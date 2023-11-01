# parse input
connections = []
for i in range(int(input('Enter: '))):
    connections.append(input())
    
testCity1 = input()
testCity2 = input()
testCity3 = input()

# build graph
graph = {}
for connection in connections:
    connList = connection.split()
    if connList[0] not in graph:
        graph[connList[0]] = []

    graph.get(connList[0]).append(connList[1])


# traverse graph
toVisit = [testCity1]
visited = [testCity1]

while toVisit:
    current = toVisit.pop()

    for neighbor in graph[current]:
        if neighbor not in visited:
            toVisit.append(neighbor)
            visited.append(neighbor)
           