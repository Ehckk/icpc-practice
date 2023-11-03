from collections import defaultdict, deque

# all possible directions, U L D R
directions = {
	"R": (lambda x, y: (x, y)),
	"U": (lambda x, y: (y, -x)),
	"L": (lambda x, y: (-x, -y)),
	"D": (lambda x, y: (-y, x))
}

def solve():
	N_TREES, N_SENSORS, R_MAX = map(int, input().strip().split())
	trees = set()
	for _ in range(N_TREES):
		x, y = map(int, input().strip().split())
		trees.add((x, y))
	sensors = set()
	for _ in range(N_SENSORS):
		sX, sY = map(int, input().strip().split())
		sensors.add((sX, sY)) # sensor positons
	
	# visited combinations go here
	visited: dict[str, dict[tuple[int, int], set[tuple[int, int]]]] = {
		key:{} for key in directions.keys() 
	} 
	# { direction: { (x, y): { (treeX, treeY) }}}
	queue = deque() # for modified bfs

	found = None # valid positions go here

	# add possible robot positions (based on trees, sensors, direction) to queue
	for tree in trees:
		tX, tY = tree
		for sensor in sensors:
			sX, sY = sensor
			for key, value in directions.items():
				adjX, adjY = value(sX,sY) 
				x = tX - adjX
				y = tY - adjY
				if visited[key].get((x, y), None) is not None: 
					continue
				visited[key][(x, y)] = set([tree])
				queue.append(((x, y), key, set([tree]), set([sensor])))
	while queue:
		(x, y), key, trees_used, sensors_used = queue.popleft()
		unused_sensors = set(sensors - sensors_used) # set diff for fast lookups

		if len(unused_sensors) == 0:
			print(x, y, key, trees_used, sensors_used)
			if found: # we have already found a position
				return "Ambiguous"
			found = (x, y)
			continue
		
		unused_trees = set(trees - trees_used)
		direction = directions[key]

		for sensor in unused_sensors:
			sX, sY = sensor
			adjX, adjY = direction(sX, sY)
			tX = x + adjX
			tY = y + adjY # is there a tree at this sensors position
			target_tree = (tX, tY)

			if not target_tree in unused_trees:
				continue # tree does not exist or already used

			# target tree + direction visited from this starting position
			print(visited[key][(x, y)], target_tree)
			if target_tree in visited[key][(x, y)]:
				continue
			visited[key][(x, y)].add(target_tree)
			trees_used.add(target_tree)
			sensors_used.add(sensor)
			print(((x, y), key, trees_used, sensors_used))
			queue.append(((x, y), key, trees_used, sensors_used))

	if not found: # 1 or more positions found
		return "Impossible"
	return " ".join(found)

print(solve())	