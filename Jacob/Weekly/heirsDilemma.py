L, H = map(int, input().split())
validCombos = 0

# iterate through combos
for num in range(L, H+1):
    isValid = True
    strNum = str(num)

    # check if 0
    if '0' in strNum:
        continue

    # check uniqueness
    if len(set(strNum)) != len(strNum):
        continue

    # check divisible
    for digit in strNum:
        if num % int(digit) != 0:
            isValid = False
            break

    if isValid:
        validCombos += 1

print(validCombos)
