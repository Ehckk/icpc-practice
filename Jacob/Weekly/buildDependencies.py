
graph = {
    "gmp": ["set", "map"],
    "solution": [],
    "base": ["queue", "map"],
    "set": ["solution"],
    "map": ["solution"],
    "queue": ["solution"]

}

dependancies = {
    "gmp" : [],
    "base": [],
    "solution": ["set", "map", "queue"],
    "set": ["gmp", "base"],
    "map": ["gmp", "base"],
    "queue": ["base"]

}

# depth-first search

stack = ["gmp"]
visited = ["gmp"]

while stack:
    file = stack.pop(0)
    
    for dependent in graph.get(file):
        if dependent not in visited:
            stack.append(dependent)
            visited.append(dependent)
            for dependency in dependancies.get(dependent):
                print(dependency)

    
print(f'stack: {stack}, visited: {visited}')

for i in visited:
    print(visited)
