def solve():
    line = list(map(int, input().strip().split()))
    T = line[0]
    values = []
    for i in range(T):
        values.append(line[i + 1])
    sorted = [value for value in values]
    sorted.sort()
    is_pivot = [True for _ in range(T)]
    for i in range(T):
        is_pivot[i] = values[i] == sorted[i]
    count = len(list(filter(lambda x: x == True, is_pivot)))
    solution = [count]
    for i in range(T):
        if is_pivot[i]: solution.append(values[i])
    return " ".join(map(str, solution))

print(solve(), end="")