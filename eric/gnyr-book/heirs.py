L, H = input().strip().split()

good_count = 0 

for num in range(int(L), int(H) + 1):
    num_list = []
    for ch in str(num):
        num_list.append(int(ch))
    num_set = set(num_list)
    if not len(num_set) == len(num_list):
        continue
    
    if 0 in num_set:
        continue
    
    is_divisible = True
    for i in num_list:
        if num % i == 0:
            continue
        is_divisible = False
        break
    if not is_divisible:
        continue
    
    good_count += 1
    
print(good_count)
    