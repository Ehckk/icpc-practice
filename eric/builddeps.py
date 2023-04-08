from collections import defaultdict, deque
import sys

graph = defaultdict(list)
start = int(sys.stdin.readline())
for line in range(0, start):
	file, keys = sys.stdin.readline().split(':')
	for item in keys.strip().split():
		graph[item].append(file)
key = sys.stdin.readline().strip()

# print(graph)
visited = defaultdict(lambda: -1) # Stores visited files and their depth in key-value pairs
queue = deque([key])
current_depth = 0

while queue:
	file = queue.popleft()
	visited[file] = current_depth

	for item in graph[file]:
		if visited[item] == -1:  # Not visited
			visited[item] = current_depth + 1
			queue.extend(graph[item])
		else:
			visited[item] = max(visited[item], current_depth + 1)

	current_depth += 1 # Visit the files that depend on this file

# print(visited)
output = list(visited.items()) # Get list of key-value pairs from the visited dict
output.sort(key=lambda x: x[1]) # Sort it in ascending order by the depth
output = map(lambda x: x[0], output) # Use map function to get a list of just the file names
print("\n".join(output))
