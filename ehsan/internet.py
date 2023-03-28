from sys import stdin, stdout

def createAdjacencyMap(strList):
    adj = {}

    for s in strList:
        s = s.split(' ')
        h1 = s[0]
        h2 = s[1]

        if h1 in adj:
            adj[h1].append(h2)
        else:
            adj[h1] = [h2]
        if h2 in adj:
            adj[h2].append(h1)
        else:
            adj[h2] = [h1]
    
    return adj

def internet(rawStrList):
    N = int(rawStrList[0].split(' ')[0])
    adj = createAdjacencyMap(rawStrList[:1])
    visited = set(['1'])

    def dfs(current):
        rest = [current]
        while rest:
            r = rest.pop()
            for h in adj.get(r, []):  
                if h not in visited:
                    visited.add(h)
                    rest.append(h) 

    if '1' in adj:
        dfs('1')
    
    result = [str(h) for h in range(2, N + 1) if str(h) not in visited]
    return "\n".join(result) if len(result) > 0 else "Connected"

raw = []
line = stdin.readline()
while line:
    raw.append(line.rstrip())
    line = stdin.readline()

stdout.write(internet(raw))
