from collections import deque

# all possible directions
DIRECTIONS = [(-1, -1), (1, -1), (-1, 1), (1, 1)]

def solve():
    N_T, N_S, R_MAX = map(int, input().strip().split())

    visited = {}
    for _ in range(N_T):
        tX, tY = map(int, input().strip().split())
        visited[(tX, tY)] = [None for _ in range(DIRECTIONS)]
    sensors = {}
    for _ in range(N_S):
        sX, sY = map(int, input().strip().split())
        sensors[(sX, sY)] = False
        
    found = []
    trees = set()
    sensors = set()

    def search(x, y, direction, current_sensors: set):
        if len(sensors) == N_S:
            return (x, y)
        for sensor in sensors:
            if sensor in current_sensors:
                continue
            (sX, sY) = sensor
            (dX, dY) = direction

            tX = x + (sX * dX)
            tY = y + (sY * dY)
            tree = visited.get((tX, tY), None)

            if tree is None: 
                continue
            current_sensors.add(sensor)
            search()
            current_sensors.remove(sensor)         
        return None



    for tX, tY in trees:
        for i in DIRECTIONS:
            if search(tX, tY, i, set()):
                print(found)
                # if found: # We already found a position
                #     return "Ambigious"
                # found = x, y

print(solve())