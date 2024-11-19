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
	sensors = []
	for _ in range(N_SENSORS):
		s_x, s_y = map(int, input().strip().split())
		sensors.append((s_x, s_y))  # sensor positions

	found = None  # valid positions go here

	def check(p_x: int, p_y: int, key: str, tree: tuple[int, int]):
		# validate position
		mapped_trees = {tree}
		adj = directions[key]
		for sensor in sensors[1:]:
			s_x, s_y = sensor
			adj_x, adj_y = adj(s_x, s_y)
			t_x = p_x + adj_x
			t_y = p_y + adj_y
			target_tree = (t_x, t_y)
			# is there a tree at this sensors position
			if not target_tree in trees:
				return False
			mapped_trees.add(target_tree)

		if not len(mapped_trees) == N_SENSORS:  # Unable to map one tree to each sensor
			return False

		# ensure any unmapped trees are not within R_MAX
		for t in set(trees - mapped_trees):
			t_x, t_y = t
			m_dist = abs(t_x - p_x) + abs(t_y - p_y)
			if m_dist > R_MAX:  # tree outside robot's range, does not need to be mapped
				continue
			return False  # "detectable" tree within robots range, invalid position
		return True

	for k, direction in directions.items():
		for t in trees:
			t_x, t_y = t
			s_x, s_y = sensors[0]  # all sensors will have to be mapped
			adj_x, adj_y = direction(s_x, s_y)
			x = t_x - adj_x
			y = t_y - adj_y
			pos = (x, y)  # calculate possible position using any tree, sensor, and direction
			if pos in trees:  # robot cannot be on a tree
				continue
			if not check(x, y, k, t):  # check if the robot is possibly at this position
				continue
			if found:  # Location already found, we just found another
				return "Ambiguous"
			found = (x, y)
	if not found:  # no valid positions found
		return "Impossible"
	return " ".join(map(str, found))


print(solve())
