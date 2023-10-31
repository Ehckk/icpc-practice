def solve():
    h1, b1 = map(int, input().split())
    h2, b2 = map(int, input().split())
    p1 = h1 * 3 + b1
    p2 = h2 * 3 + b2
    diff = p1 - p2
    if diff == 0:
        return "NO SCORE"
    return f"{1 if diff > 0 else 2} {abs(diff)}"


print(solve())
