from sys import stdin, stdout
from collections import defaultdict, deque

def processInput(strList):
    strList = [list(filter(str.rstrip, x.split(' '))) for x in strList]
    fileToDeps, depToFiles = defaultdict(list), defaultdict(list)
    
    for line in strList[1:len(strList) - 1]:
        val = line[0].strip(':')
        deps = line[1:]
        for file in deps:
            depToFiles[file].append(val)
            fileToDeps[val].append(file)
        if not deps:
            fileToDeps[val] = []
    
    return depToFiles, fileToDeps, strList[-1][0]

def makeFile(strList):
    depToFiles, fileToDeps, file = processInput(strList)

    order = []
    ind = defaultdict(int)
    for node in fileToDeps:
        ind[node] += len(fileToDeps[node])
    
    # enqueue the nodes with indegree of 0
    queue = deque([])
    for i in ind:
        if ind[i] == 0:
            queue.append(i)
            order.append(i)
    
    # Remove nodes with indegree of 0 from the graph
    # Continually subtract the indegree of a node when one of its dependencies is removed
    # the order list holds the topological ordering
    while queue:
        node = queue.popleft()
        for n in depToFiles.get(node, []):
            ind[n] -= 1
            if ind[n] == 0:
                queue.append(n)
                order.append(n)

    # dfs from the file and track all the visited nodes
    visited = set([file])
    stack = [file]
    while stack:
        node = stack.pop()
        for n in depToFiles.get(node, []):
            if n not in visited:
                stack.append(n)
                visited.add(n)
    
    # output the visited nodes in topological order, using the order list we created earlier
    result = '\n'.join(list(filter(lambda n: n in visited, order)))
    return result if len(result) > 0 else file

raw = []
line = stdin.readline()
while line:
    raw.append(line.rstrip())
    line = stdin.readline()

stdout.write(makeFile(raw))