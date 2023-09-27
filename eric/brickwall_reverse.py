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

"""
Strategy 1: Brute Force (TLE at 108)
Strategy 2: Big ass DP array 
"""

def solve():    
    (N, c1, c2, c3) = map(int, input().strip().split())
    brick_counts = [c1, c2, c3] # amount of each size brick 
    bricks = list(map(int, input().strip().split()))
    creases = set()
    crease_total = 0 # store target value
    for i in range(len(bricks)):
        crease_total += bricks[i]
        if i + 1 < N: # ignore last (target) position
            creases.add(crease_total) # ignore creases

    def brickwall(current):
        if current == 0: return True
        if current < 0: return False
        if current in creases: return False

        for brick_size in range(3, 0, -1): # 3, 2, 1
            if brick_counts[brick_size - 1] == 0: continue # cannot use brick

            brick_counts[brick_size - 1] -= 1 # use brick
            if brickwall(current - brick_size): return True
            brick_counts[brick_size - 1] += 1 # un-use brick
        return False
    
    return "YES" if brickwall(crease_total) else "NO"

print(solve())

# Result: 