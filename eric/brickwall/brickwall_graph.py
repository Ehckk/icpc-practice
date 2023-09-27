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

- If the problem bricks contain 3 ones in a row -> NO
- If the problem bricks contain 2 ones in a row -> NO
- If the problem bricks contain a 1 -> ONLY 3 CAN BE USED
"""

from collections import defaultdict


def solve():    
    (N, c1, c2, c3) = map(int, input().strip().split())
    
    # cannot lay brick size j + 1 at position i if
    #   i + j + 1 not in set and i + j + 1 < total

    brick_counts = [c1, c2, c3]
    crease_total = 0
    creases = set()
    for i, brick in enumerate(map(int, input().strip().split())):
        crease_total += brick
        if i + 1 < N: creases.add(crease_total)

    graph = defaultdict(list)
    for i in range(crease_total):
        if i in creases: continue
        for j in range(3):
            value = i + j + 1
            if not value in creases and value <= crease_total:
                graph[i].append(j + 1)

    def brickwall(total):
        if total == crease_total: return True # Sum is target
        if total > crease_total: return False # Sum is above target
        if total in creases: return False # Sum is on crease

        for adj in graph[total]:
            if brick_counts[adj - 1] == 0: continue # not enough of each brick
            brick_counts[adj - 1] -= 1 # use the brick
            if brickwall(total + adj): return True # yay it works
            brick_counts[adj - 1] += 1 # not found, backtrack
        return False

    return "YES" if brickwall(0) else "NO"

print(solve())

# Result: 