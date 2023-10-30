import random

P_MAX = 10000 // 1000
T_MAX = 250000 // 10000
L_MAX = 1000 // 10 
# :)

# P = random.randint(2, P_MAX)
# T = random.randint(1, T_MAX)
# L = random.randint(1, L_MAX)
P = 10
L = 1000
T = 2500

def get_test_values(p1):
    p2 = random.randint(0, P - 1)
    length = random.randint(1, L)
    return str(f"{p1} {p2} {length}\n")

with open('./testcases/flowertrails.txt', 'w', encoding='utf-8') as file:
    file.write(f"{P} {T}\n")
    file.write(get_test_values(0))
    for i in range(T - 2):
        file.write(get_test_values(random.randint(0, P - 1)))
    file.write(get_test_values(P - 1))
    file.close()
print('done')