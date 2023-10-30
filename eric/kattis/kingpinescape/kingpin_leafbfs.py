from collections import defaultdict, deque

def solve():
	graph = defaultdict(list)
	(N, H) = map(int, input().split())
	for _ in range(N - 1):
		(a, b) = map(int, input().split())
		graph[a].append(b)

	visited = [False] * N
	leaves = []
	# BFS will find leaves in order of depth in tree
	queue = deque()
	queue.append(H)
	while queue:
		node = queue.popleft()
		is_leaf = True
		if visited[node]: continue
		visited[node] = True
		for adj in graph.get(node, []):
			is_leaf = False
			queue.append(adj)
		if is_leaf: leaves.append(node)
	added_edges = [] # two pointers to get leaf pairs
	i = 0
	j = len(leaves) - 1
	while i < j:
		added_edges.append([leaves[i], leaves[j]])
		i += 1
		j -= 1
	if i == j: # odd number of leaves:
		added_edges.append([leaves[i], H])
	print(len(added_edges))
	for (a, b) in added_edges:
		print(a, b)
solve()

# Result WA after 2