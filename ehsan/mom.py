from sys import stdin, stdout
from collections import defaultdict

def processInput(rawInput):
    graph = defaultdict(list)
    n = int(rawInput[0])
    strList = [x.split(' ') for x in rawInput[1: 1 + n]]
    toVisit = rawInput[1 + n:]

    for [c1, c2] in strList:
        graph[c1].append(c2)

    return graph, toVisit

def mom(rawInput):
    graph, toVisit = processInput(rawInput)
    safenodes = set() # for memoization
    visited = set() 
    visiting = set() # detecting cycles

    def dfs(node):
        if node in visiting or node in safenodes:
            return True
        if node in visited:
            return False
            
        visited.add(node)
        visiting.add(node)

        for n in graph.get(node, []):
            if dfs(n):
                safenodes.add(n)
                safenodes.add(node)
            
        visiting.remove(node)
        return node in safenodes
    
    result = []
    for node in toVisit:
        result.append(node + (" safe" if dfs(node) else " trapped"))
        visited.clear()

    return "\n".join(result)

raw = []
line = stdin.readline()
while line:
    raw.append(line.rstrip())
    line = stdin.readline()
stdout.write(mom(raw))