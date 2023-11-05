# all possible directions, U L D R
directions = {
	"R": (lambda x, y: (x, y)),
	"U": (lambda x, y: (y, -x)),
	"L": (lambda x, y: (-x, -y)),
	"D": ((lambda x, y: (-y, x)))
}

def solve():
	N_TREES, N_SENSORS, R_MAX = map(int, input().strip().split())
	trees = set()
	for _ in range(N_TREES):
		x, y = map(int, input().strip().split())
		trees.add((x, y))
	sensors = []
	for _ in range(N_SENSORS):
		sX, sY = map(int, input().strip().split())
		sensors.append((sX, sY)) # sensor positons
	
	found = None # valid positions go here

	def check(x: int, y: int, key: str, tree: tuple[int, int]):
		# validate position
		mapped_trees = set({tree})
		for tree in set(trees - {tree}): # set difference 
			direction = directions[key]
			for sensor in sensors[1:]:
				sX, sY = sensor
				adjX, adjY = direction(sX, sY)
				tX = x + adjX
				tY = y + adjY 
				target_tree = (tX, tY)
				# is there a tree at this sensors position
				if not target_tree in trees:
					return False
				mapped_trees.add(target_tree)
	
			if not len(mapped_trees) == N_SENSORS:  # Unable to map all trees
				return False

			# ensure any unmapped trees are not within R_MAX
			for tree in set(trees - mapped_trees):
				tX, tY = tree
				m_dist = abs(tX - x) + abs(tY - y)
				if m_dist > R_MAX: # tree outside robot's range, does not need to be mapped
					continue
				return False # "detectable" tree within robots range, invalid position
		return True
			
	for key, direction in directions.items():
		for tree in trees:
			(tX, tY) = tree
			sX, sY = sensors[0] # all sensors will have to be mapped
			adjX, adjY = direction(sX, sY)
			x = tX - adjX
			y = tY - adjY
			pos = (x, y) 
			if pos in trees:
				continue
			if not check(x, y, key, tree): # check if the robot is possibly at this position
				continue
			if found: # Location already found, we just found another 
				return "Ambiguous" 
			found = (x, y)
	if not found: # no valid positions found
		return "Impossible"
	return " ".join(map(str, found))


print(solve())