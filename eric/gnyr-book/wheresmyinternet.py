def solve():
    N, M = map(int, input().strip().split())
    houses = {(i + 1):[] for i in range(N)}
    for _ in range(M):
        a, b = map(int, input().strip().split())
        houses[a].append(b)
        houses[b].append(a)

    visited = [False for _ in range(N)]

    stack = [1]
    while stack:
        node = stack.pop()
        if visited[node - 1]: # n - 1 because the first node is 1 and not 0 :( 
            continue
        visited[node - 1] = True
        for adj in houses[node]:
            stack.append(adj)
    not_connected = []
    for i in range(N):
        if visited[i]:
            continue
        not_connected.append(i + 1)

    if not not_connected:
        return "Connected"
    return "\n".join(map(str, not_connected))

print(solve())