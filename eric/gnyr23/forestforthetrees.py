from collections import deque, defaultdict

# all possible directions
directions = [(-1, -1), (1, -1), (-1, 1), (1, 1)]

def solve():
    N_TREES, N_SENSORS, R_MAX = map(int, input().strip().split())
    trees = []
    for _ in range(N_TREES):
        x, y = map(int, input().strip().split())
        trees.append(x, y) 
    sensors = []
    for _ in range(N_SENSORS):
        x, y = map(int, input().strip().split())
        sensors.append((x, y)) # sensor positons
    
    found = None # valid positions go here

    def check(x: int, y: int, visited_trees: set, visited_sensors: set):
        if len(current_trees) == len(sensors):
            # base case, a tree has been found for each sensor, valid position found
            if found: # We already found a position
                return "Ambigious"
            found = (x, y) 
            return 
        for sensor in sensors: # loop over sensors 
            if sensor in current_sensors: # ignore sensors mapped to a tree
                continue
            for tree in trees: # loop over trees
                if tree in current_trees: # ignore trees mapped to a sensor
                    continue
                # check if position maps to the tree
                current_trees.add(tree)
                current_sensors.add(sensor)
                if check(x, y, current_trees, current_sensors):
                    return True
                current_trees.remove(tree)
                current_sensors.remove(sensor)
        return False

            
        
    for tree in trees:
        (treeX, treeY) = tree
        current_trees = set()
        current_trees.add(tree)
        for sensor in sensors:
            (sensorX, sensorY) = sensor
            current_sensors = set()
            current_sensors.add(sensor)
            for xDirection, yDirection in directions:
                x = treeX + (sensorX * xDirection) # calculate position
                y = treeY + (sensorY * yDirection) 
                check(x, y) # recursively check these trees
    
    for tree in trees:
        current_trees.add(tree)

    if len(found) > 0: # 1 or more positions found
        if len(found) == 1: # exactly 1 found
            return " ".join(found[0])
        return "Ambiguous"
    return "Impossible"

print(solve())


    