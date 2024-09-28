def solve():
    line = list(map(int, input().strip().split()))
    T = line[0]

    values = line[1:]
    sorted = line[1:]
    sorted.sort()

    is_pivot = [True for _ in range(T)]
    for i in range(T):
        is_pivot[i] = values[i] == sorted[i]

    if T % 2 == 1: # odd number of values
        i = 0
        midpoint = T // 2 # do the partition check, but only for the midpoint
        while is_pivot[midpoint] and i < T:
            if i < midpoint:
                is_pivot[midpoint] = values[i] < values[midpoint]
            if i > midpoint:
                is_pivot[midpoint] = values[i] > values[midpoint]
            i += 1

    count = is_pivot.count(True)
    solution = [count]
    i = 0
    while i < T and len(solution) < 101: # only return the first 100 pivots 
        if is_pivot[i]: 
            solution.append(values[i])
        i += 1
    return " ".join(map(str, solution))

print(solve())