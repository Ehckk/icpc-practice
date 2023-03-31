graph = {
    1: [4, 2],
    4: [7, 1],
    2: [1, 5, 3],
    5: [6, 2],
    6: [6],
    3: [2],
    7: [4]
}


rest = [1] 
visited = set([1])
while rest:
    r = rest.pop(0)
    print(r)
    for n in graph.get(r, []):
        if n not in visited:
            rest.append(n)
            visited.add(n)
