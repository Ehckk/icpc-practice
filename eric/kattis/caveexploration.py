from collections import defaultdict

graph = defaultdict(set) # Adjacency list for graph
discoveryTime = [] # Track the time each node is "discovered" in the DFS traversal 
minTime = [] # Shortest possible time the node can be discovered
bridges = [] # Track bridges
visited = []

def readInput():
	line = input().strip().split()
	nodes = int(line[0]) # Number of nodes
	edges = int(line[1]) # Number of edges
	
	for _ in range(nodes):
		discoveryTime.append(-1)
		minTime.append(-1)
		visited.append(False)
	
	for _ in range(edges):
		line = input().strip().split()
		node1 = int(line[0])
		node2 = int(line[1])
		graph[node1].add(node2)
		graph[node2].add(node1)

def findBridges(current, parent, time=0):
	discoveryTime[current] = time; # Set discovery time
	minTime[current] = time; # Assume the minimum possible discovery time is the current discovery time 

	for next in graph[current]: # Loop over adjacent nodes
		if next == parent: continue # Avoid child-parent connection
		
		if discoveryTime[next] == -1: # Node has not yet been discovered
			time += 1 # Increment time 
			findBridges(next, current, time) # Recurse on the child node
			# After DFS from next node, discovery times for relevant nodes should be set
			if discoveryTime[current] < minTime[next]: # Next node cannot possibly be discovered before current node
				bridges.append((current, next)) # We have found a bridge 
			minTime[current] = min(minTime[current], minTime[next]) # Next node 
		else: # Next node already discovered, so next node has anscestor that is NOT current node 
			minTime[current] = min(minTime[current], discoveryTime[next]) # Update min time accordingly

def exploreCave():
	for (node1, node2) in bridges:
		graph[node1].remove(node2)
		graph[node2].remove(node1) # Remove the bridge from the graph

	safeNodeCount = 0
	stack = [0]

	while len(stack) > 0: # Normal DFS
		current = stack.pop()
		
		if visited[current]: continue
		visited[current] = True

		safeNodeCount += 1
		for next in graph[current]: 
			stack.append(next)
	return safeNodeCount

readInput()
findBridges(0, -1) # Track the order of discovery (first visit) through DFS
print(exploreCave())