from collections import defaultdict

def solve():
	graph = defaultdict(list)
	(N, H) = map(int, input().split())
	for _ in range(N - 1):
		(a, b) = map(int, input().split())
		graph[a].append(b)

	visited = [False] * N
	stack = []
	
	return 
solve()