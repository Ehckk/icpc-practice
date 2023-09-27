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
    # cannot lay brick size j + 1 at position i if
    #   i + j + 1 not in set and i + j + 1 < total
"""
def solve():    
    (N, MAX_1, MAX_2, MAX_3) = map(int, input().strip().split())

    crease_total = 0
    creases = set()
    for i, brick in enumerate(map(int, input().strip().split())):
        crease_total += brick
        if i + 1 < N: creases.add(crease_total)

    visited = [[False for _ in range(max(MAX_1, MAX_2, MAX_3))] for _ in range(3)]

    def brickwall(total, c1, c2, c3):
        if total == crease_total: return True # Sum is target
        if total > crease_total: return False # Sum is above target
        if total in creases: return False # Sum is on crease

        # This combination has already been checked
        if visited[0][c1] and visited[1][c2] and visited[2][c3]: return False 
        
        visited[0][c1] = True
        visited[1][c2] = True
        visited[2][c3] = True

        # place down a 1-brick
        if c1 < MAX_1: return brickwall(total + 1, c1 + 1, c2, c3)
        # place down a 2-brick
        if c2 < MAX_2: return brickwall(total + 2, c1, c2  + 1, c3)
        # place down a 3-brick
        if c3 < MAX_3: return brickwall(total + 3, c1, c2, c3 + 1)

        return False

    return "YES" if brickwall(0, 0, 0, 0) else "NO"

print(solve())

# Result: 