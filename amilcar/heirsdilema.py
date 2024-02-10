# Heir's Dilema
# https://open.kattis.com/problems/heirsdilemma

combos = 0

# input session number range.
low, high = input('Enter range: ').strip().split()

for num in range(int(low), int(high) + 1):
    num_list = [int(ch) for ch in str(num)]

    # test for repeated digits and zeros in number
    if len(num_list) != len(set(num_list)) or 0 in num_list:
        continue

    # test if each digit is a factor of num
    is_factor = True
    for i in num_list:
        if num % i != 0:
            is_factor = False
            break
    if is_factor:
        combos += 1

print(combos)
