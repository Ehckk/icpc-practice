file = open("./inputs/a.in.txt") 
P = int(file.readline())
def solve():
    solutions = []
    for _ in range(P):
        (K, N) = map(int, file.readline().split())
        total = 0
        for i in range(N + 1):
            total += i
        total_odd = 0
        for i in range(1, 2 * N + 1, 2):
            total_odd += i
        total_even = 0
        for i in range(0, 2 * N + 1, 2):
            total_even += i
        solutions.append(" ".join(map(str, [K, total, total_odd, total_even])))
    return "\n".join(solutions)

solutions = solve()
file.close()

with open("./inputs/a.test.txt", "w") as file:
    file.write(solutions)

with open("./inputs/a.test.txt") as test, open("./inputs/a.out.txt") as actual:
    test_passed = True
    for test_line in test.readlines():
        actual_line = actual.readline()
        if not actual_line.strip() == test_line.strip():
            print(f"YOU FAILED 💀 - Expected {actual_line}, Got {test_line}")
            test_passed = False
            break
    if test_passed: print(f"Passed")
    
"""
3
1 1
2 10
3 1001
"""

