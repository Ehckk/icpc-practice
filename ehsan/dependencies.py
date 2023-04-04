from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict
setrecursionlimit(10**6)

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
    topVisited = set()
    def traverse(node):
        topVisited.add(node)

        for n in fileToDeps.get(node, []):
            if n in topVisited:
                continue
            traverse(n)

        order.append(node)
    
    for node in fileToDeps:
        if node not in topVisited:
            traverse(node)
        
    visited = set([file])
    stack = [file]
    while len(stack) > 0:
        r = stack.pop()
        for n in depToFiles.get(r, []):
            if n not in visited:
                visited.add(n)
                stack.append(n)

    result = list(filter(lambda n: n in visited, order))
    result = '\n'.join(result)
    return result if len(result) > 0 else file

raw = []
line = stdin.readline()
while line:
    raw.append(line.rstrip())
    line = stdin.readline()

stdout.write(makeFile(raw))
