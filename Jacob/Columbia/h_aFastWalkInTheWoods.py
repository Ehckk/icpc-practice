'''
    Jacob Stephens / November 2, 2023
    Problem H: A (Fast) Walk in the Woods -- GNYR ICPC 2023
'''
n, m = map(int, input().split())
xys = [int(i) for i in input().split()]

# key = node, value = [x,y]
coords = {}
for i in range(n):
    coords[i+1] = [xys[i*2], xys[i*2+1]]

''' create graph '''
graph = {}
for i in range(m):
    node, conn, weight = map(int, input().split())
   
    if node not in graph:
        graph[node] = {}
    
    if conn not in graph:
        graph[conn] = {}

    # if x values are equal
    if coords[node][0] == coords[conn][0]:
        # if node is above connection
        if coords[node][1] > coords[conn][1]:
            nodeToConn = 'S'
            connToNode = 'N'
        # if node is below connection
        else:
            nodeToConn = 'N'
            connToNode = 'S'
    # if y values are equal
    elif coords[node][1] == coords[conn][1]:
        # if node is right of connection
        if coords[node][0] > coords[conn][0]:
            nodeToConn = 'W'
            connToNode = 'E'
        # if node is left of connection
        else:
            nodeToConn = 'E'
            connToNode = 'W'
   
    graph[node][nodeToConn] = [conn, weight]
    graph[conn][connToNode] = [node, weight]
''' create graph end '''

# get initial instruction
target, d = input().split()
target = int(target)

# initialize variables
axis = ['N', 'E', 'S', 'W', 'N', 'E']
justDeleted = 1

# traverse through path until you have no more options
while len(graph[target]) + justDeleted > 1:
    # update current node
    curr = target
    target = graph[target][d][0]

    # subtract weights
    forwardConn = graph[curr][d]
    forwardConn[1] -= 1

    oppositeIndex = axis.index(d)+2
    backwardConn = graph[target][axis[oppositeIndex]]
    backwardConn[1] -= 1

    # delect edge if weight = 0
    if forwardConn[1] <= 0:
        del graph[curr][d]
        del graph[target][axis[oppositeIndex]]
        justDeleted = 1

    else:
        justDeleted = 0

    # no choice
    if len(graph[target]) + justDeleted == 2:
        for e in ['N', 'E', 'S', 'W']:
            
            if (e != axis[oppositeIndex]) and (e in graph[target]):
                d = e
                break

    # go left
    elif len(graph[target]) + justDeleted == 3:
        if d == 'N':
            d = 'W' if 'W' in graph[target] else 'N'

        elif d == 'E':
            d = 'N' if 'N' in graph[target] else 'E'
        
        elif d == 'S':
            d = 'E' if 'E' in graph[target] else 'S'
        
        elif d == 'W':
            d = 'S' if 'S' in graph[target] else 'W'

    # if you go straight, d doesn't change

# output
print(" ".join([str(i) for i in coords[target]]))
