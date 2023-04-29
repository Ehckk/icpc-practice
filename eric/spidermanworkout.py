import sys

for _ in range(int(sys.stdin.readline().strip())):
    count = int(sys.stdin.readline().strip())
    
    dist = [int(i) for i in sys.stdin.readline().strip().split()]

    bestPath = str("IMPOSSIBLE")
    bestHeight = float('inf')
    path = [dist[1]]

    def spiderman(current, maxHeight):
        index = len(path)
        if len(path) == len(dist):
            bestPath = "".join(['U' if i == 1 else 'D' for i in path])
            bestHeight = maxHeight
            return
        next = current - dist[index] # next height if we go down
        if next > 0: # then we can go down
            path.append(-1)
            spiderman(next, maxHeight, path)
            path.pop()
        next = current + dist[index] # next height if we go up
        if next < maxHeight: # then we can go up and (potentially) find a shorter path
            path.append(1)
            spiderman(next, max(maxHeight, next), path)
            path.pop()
        
    spiderman(dist[1], dist[1])
    print(bestPath)

