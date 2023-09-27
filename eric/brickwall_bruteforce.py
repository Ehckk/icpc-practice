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

def solve():    
    (N, c1, c2, c3) = map(int, input().strip().split())

    brick_counts = [c1, c2, c3]
    crease_bricks = list(map(int, input().strip().split()))

    creases = set()
    crease_total = 0

    for i in range(len(crease_bricks)):
        crease_total += crease_bricks[i]
        if i + 1 < N: creases.add(crease_total)
    
    def brickwall(total):
        if total == crease_total: return True # Sum is target
        if total > crease_total: return False # Sum is above target
        if total in creases: return False # Sum is on crease

        for i in range(3, 0, -1): # 3, 2, 1: Each brick width
            if brick_counts[i - 1] == 0: continue # not enough of each brick
            brick_counts[i - 1] -= 1 # use the brick
            if brickwall(total + i): return True # yay it works
            brick_counts[i - 1] += 1 # not found, backtrack
        return False

    return "YES" if brickwall(0) else "NO"

print(solve())

# Result: TLE after 108 testcases