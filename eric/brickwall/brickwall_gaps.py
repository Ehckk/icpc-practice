"""
ignore this slop 

5 2 1 3
2 3 1 3 2
YES

5 1 2 3
2 3 1 3 2
NO

5 6 1 1
2 3 1 2 3
NO

- If gap == 1 then: 
    - 2 brick or 3 brick is needed 
- If gap == 2 then:
    -  1 (creates a 1 gap) brick or 3 brick is needed 
- If gap == 3 then (only possible at beginning):
    # 1 (creates a 2 gap) brick or 2 (creates 1-gap) brick is required

"""
def print_bricks(bricks):
    for i in range(3, 0, -1):
        for j in range(len(bricks)):
            print(bricks[j][i - 1], end=" ")
        print()

# what bricks can we use at each gap?

def solve():    
    (N, c1, c2, c3) = map(int, input().strip().split())
    brick_counts = [c1, c2, c3] # amount of each size brick 
    bottom_bricks = input().strip().split()

    total = 0 
    creases = set()
    for i in range(N):
        total += int(bottom_bricks[i])
        if i + 1 < N: creases.add(total) # Find creases between bricks

    # if brick lengths = total 
    # then number of spots for creases = total + 1 (start and end)
    bricks = [[pos in creases for _ in range(3)] for pos in range(total + 1)]
    # print_bricks(bricks)

    pos = 0
    while pos < len(bricks):
        if all(bricks[pos]): continue
        i, j = pos
        while not all(bricks[pos]) and len(bricks) < total + 1:
            j += 1 # Find the next gap
        pos = j + 1
        if j - pos == 3: return False # three consecutive gaps
        while pos < j:
            for size in range(3, 0, -1): # 3, 2, 1
                bricks[pos][size - 1] = bricks[pos][size - 1] 
            pos += 1 

        while not all(bricks[j]) != 0 and j < len(gaps):
            j += 1
        for i in range():
        while i < j:
            for size in range(3):
                value = -1 if size + 1 == j - i else i + size + 1
                graph[i].append(value)
            i += 1
        j += 1
        i += 1 

    def brickwall(current):
        if current == total: return True
        if current > total: return False
         
        for i in range(len(graph[current])):
            if graph[current][i] == -1: continue 
            if brick_counts[i] == 0: continue # cannot use brick

            brick_counts[i] -= 1 # use brick
            if brickwall(graph[current][i]): return True
            brick_counts[i] += 1 # un-use brick
        return False
    
    return "YES" if brickwall(0) else "NO"

print(solve())

# Result: 