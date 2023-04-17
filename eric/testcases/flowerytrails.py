import random

P_MAX = 10000 // 1000
T_MAX = 250000 // 10000
L_MAX = 1000 // 10 
# :)

P = random.randint(2, P_MAX)
T = random.randint(1, T_MAX)
L = random.randint(1, L_MAX)

def get_test_values(p1):
    p2 = random.randint(0, P - 2)
    length = random.randint(1, L)
    return str(f"{p1} {p2} {length}")

print(P, T)
print(get_test_values(0))
for i in range(T - 2):
    print(get_test_values(random.randint(0, P - 1)))
print(get_test_values(P - 1))
print()