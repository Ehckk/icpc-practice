import sys
from collections import defaultdict

graph = defaultdict(list)

a, b, e, p = map(lambda x: int(x), sys.stdin.readline().split())
visited = [False for _ in range(e)]
depths = [-1 for _ in range(e)]

def dfs(node, depth):
	if not depths[node] == -1:
		depths[node] = max(depths[node], depth)
		return 
	visited[node] = True
	depths[node] = depth
	for adj in graph[node]:
		dfs(adj, depth + 1)

for _ in range(p):
	x, y = map(lambda x: int(x), sys.stdin.readline().split())
	graph[x].append(y) 
for node in list(graph.keys()):
	if visited[node]: continue
	dfs(node, 0)
levels = [0 for _ in range(e)]
for node in depths:
	levels[node] += 1

aPromotions = -1 
bPromotions = -1
nPromotions = 0
current = 0
for employees in levels:
	current += employees
	if aPromotions == -1:
		if a - current >= 0: continue
		aPromotions = current - employees
	if bPromotions == -1:
		if b - current >= 0: continue 
		bPromotions = current - employees
	nPromotions += employees
print(aPromotions)
print(bPromotions)
print(nPromotions)