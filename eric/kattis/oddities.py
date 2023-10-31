def solve():
    N = int(input())
    for _ in range(N):
        X = int(input())
        result = "even" if X % 2 == 0 else "odd"
        print(f"{X} is {result}")
solve()