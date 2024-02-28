from collections import defaultdict, deque

def solve():
    V, E = list(map(int, input().strip().split()))
    graph = defaultdict(list)
    
    for _ in range(E):
        a, b = list(map(int, input().strip().split()))
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [None for _ in range(V)]  # Label them as more than just visted/not visited

    queue = deque()
    queue.append((1, 'A'))  # Label the first node 
    

    while queue:
        node, label = queue.popleft()

        if visited[node - 1]:
            #print(node - 1, visited[node - 1], label)
            if visited[node - 1] == label: # Is this node labeled with the expected label?
                continue
            return "not bipartite"
        
        visited[node - 1] = label
        next_label = 'B' if label == 'A' else 'A'  # Set the next label
        
        for adj in graph[node]:
            queue.append((adj, next_label))

    # label_1 = []
    # label_2 = []
    # for i in range(len(visited)):
    #     if visited[i] == "A":
    #         label_1.append(i + 1)
    #     else: 
    #         label_2.append(i + 1)
    # print(label_1)
    # print(label_2)

    return "bipartite" 

print(solve())