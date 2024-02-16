def solve():
    N, M = map(int, input().strip().split())
    cols = []
    counts = 0
    for i in input().strip():
        value = int(i)
        if value == 1:
            counts += 1
        cols.append(value)

    moves = 0
    left = 0
    right = N - 1
    while counts > 0:
        while cols[left] == 0 and left < N - 1: 
            left += 1
        while cols[right] == 0 and right > 0: 
            right -= 1
        # print(left, N - 1 - right)
        if left < N - 1 - right:
            i = left
        else:
            i = right
        cols[i] = 0
        counts -= 1
        if i - 1 > 0:
            if cols[i - 1] == 1:
                cols[i - 1] = 0
                if i - 2 > 0:
                    if cols[i - 2] == 0:
                        cols[i - 2] = 1
                    else:
                        counts -= 1
                else:
                    counts -= 1
        if i + 1 < N - 1:
            if cols[i + 1] == 1:
                cols[i + 1] = 0
                if i + 2 < N - 1:
                    if cols[i + 2] == 0:
                        cols[i + 2] = 1
                    else:
                        counts -= 1
                else:
                    counts -= 1
        moves += 1
        # print(cols)

    print(moves)
    
solve()