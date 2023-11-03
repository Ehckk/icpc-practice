from collections import deque

# all possible directions
DIRECTIONS = [(-1, -1), (1, -1), (-1, 1), (1, 1)]

def solve():
    N_T, N_S, R_MAX = map(int, input().strip().split())

    visited = { s:{ t:[None for _ in range(DIRECTIONS)] for t in range(N_T) } for s in range(N_S) }
    queue = deque()

    trees = {}
    for i in range(N_T):
        tX, tY = map(int, input().strip().split())
        trees[i] = (tX, tY)
        
    sensors = {}
    for _ in range(N_S):
        sX, sY = map(int, input().strip().split())
        sensors[i] = (sX, sY)
    
    # nodes = locations the robot could be at
    # edges = positions that "map" to each other by way of sensor readings
    
    found = None

    while queue:
        t, current_sensors = queue.pop()
        remaining = current_sensors - set(sensors) # i learned this is databases class
        if not remaining: # each sensor has mapped a tree -> position found
            if found: # We already found a position
                return "Ambigious"
            found = 

        if visited[t, s]:

    if len(found) > 0: # 1 or more positions found
        if len(found) == 1: # exactly 1 found
            return " ".join(found[0])
        return "Ambiguous"
    return "Impossible"

print(solve())


    