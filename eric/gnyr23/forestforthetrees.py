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
	
	trees_used = set() # used trees go here
	sensors_used = set() # used sensors go here
	found = None # valid positions go here

	def check(x: int, y: int, key: str): # this is where the robot (possibly) is
		# validate position
		unused_sensors = set(sensors - sensors_used)
		if len(unused_sensors) == 0:
			return True
		unused_trees = set(trees - trees_used)
		direction = directions[key]
		for sensor in unused_sensors:
			sX, sY = sensor
			adjX, adjY = direction(sX, sY)
			tX = x + adjX
			tY = y + adjY # is there a tree at this sensors position
			target_tree = (tX, tY)
			# print((x, y), (sensor), target_tree, len(unused_trees))

			if not target_tree in unused_trees:
				continue # tree does not exist or already used

			trees_used.add(target_tree)
			sensors_used.add(sensor)
			result = check(x, y, key) # check position
			trees_used.remove(target_tree) # backtrack
			sensors_used.remove(sensor)
			if result:
				return True
		return False

	# TODO: what happen to state?? use positions + direction?
	for tree in trees:
		(tX, tY) = tree
		trees_used.add(tree)
		for sensor in sensors:
			sX, sY = sensor
			sensors_used.add(sensor)
			# start with a tree and sensor pair
			# facing up
			# facing right
			# facing left
			# facing down
			for key, value in directions.items():
				(adjX, adjY) = value(sX,sY) 
				x = tX - adjX
				y = tY - adjY
				if check(x, y, key):
					print(tree, sensor, key, (x, y))
					if found: # 1 position already found, but we found another
						return "Ambiguous"
					found = (x, y)
			sensors_used.remove(sensor)
		trees_used.remove(tree)

	if not found: # 1 or more positions found
		return "Impossible"
	return " ".join(found)

print(solve())	