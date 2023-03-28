N, M = map(int, input().split(" "))

conn = {}

for l in range(M):
    #print(l)
    a, b = map(int, input().split(" "))
    conn[a] = conn.get(a, []) + [b]
    conn[b] = conn.get(b, []) + [a] 

visited = [1]
visited_set = {1}
for v in visited:
    # add all neighbors to visited if they are not in there already.
    for n in conn.get(v, []):
        if n not in visited_set:
            visited_set.add(n)
            visited.append(n)

if len(visited) == N:
    print("Connected")
else:
    for n in range(1, N+1):
        if n not in visited_set:
            print(n)