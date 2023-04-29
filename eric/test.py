from collections import deque
import sys

graph = {}

line_count = 0
file_count = 0
start = ""

for line in sys.stdin.readlines():
	if line_count == 0:
		file_count = int(line)
	elif line_count <= file_count:
		file, keys = line.split(':')
		if file not in graph.keys():
			graph[file] = []
		for item in keys.strip().split():
			if item not in graph.keys():
				graph[item] = []
			graph[item].append(file)
	else:
		start = line
	line_count += 1

visited = set()
queue = deque()
queue.append(start)

output = ""
while len(queue) > 0:
	file = queue.popleft()
	if file in visited: continue
	visited.add(file)

	output += f"{file}\n"
	for item in graph[file]:
		if item in visited: continue
		queue.append(item)

print(output)
