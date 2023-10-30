import sys

# test = [ '6 4', '1 2', '2 3', '3 4', '5 6' ]
# test = [ '2 1', '2 1' ]
# test = [ '4 3', '2 3', '4 2', '3 4' ]

first_line = False

graph = {}
visited = [] # will be a list of booleans, all are set to false initially

def internet(graph):
	queue = [1]
	while len(queue) > 0:
		house = queue.pop()

		idx = house - 1
		if visited[idx]: continue # House was visited, don't check it again
		visited[idx] = True

		for other_house in graph[house]:
			queue.append(other_house)

# for line in test:
for line in sys.stdin: # this is for kattis
	num_1, num_2 = [int(i) for i in line.split()]

	if not first_line: # parse the first line differently to initialize graph + visited list
		for i in range(1, num_1 + 1):
			graph[i] = []
			visited.append(False)
		first_line = True
	else: # two way connections
		graph[num_1].append(num_2)
		graph[num_2].append(num_1)

internet(graph)
visited_count = 0
for i, house in enumerate(visited):
	if not house:
		print(f'{i + 1}')
		visited_count += 1

if visited_count == 0:
	print('Connected', file=sys.stdout)
