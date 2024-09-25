def combos():
    l, h = input().split()
    answer = 0
    for i in range(int(l),int(h)):
        duplicate_checker = set()
        for ch in str(i):
            duplicate_checker.add(ch)
        if len(duplicate_checker) != len(str(i)):
            continue
        i_as_a_string = str(i)
        if "0" in i_as_a_string:
            continue
        is_valid = True
        for character in i_as_a_string:
            number = int(character)
            if i % number != 0:
                is_valid = False
        if is_valid == False:
            continue
        answer += 1
    return answer
print(combos())
