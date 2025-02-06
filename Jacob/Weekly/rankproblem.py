# Jacob Stephens - February 4, 2025
# https://open.kattis.com/problems/rankproblem

n, m = map(int, input().split())
# rankings = [T1, T2, ..., Tn]
rankings = ["T" + str(i) for i in range(1,n+1)]
# [match] where match is [T_win, T_lose]
matches = [input().split() for _ in range(m)]

for match in matches:
    winnerIndex = rankings.index(match[0])
    loserIndex = rankings.index(match[1])

    # if upset
    if winnerIndex > loserIndex:
        #print(rankings)
        rankings.pop(loserIndex)
        rankings.insert(winnerIndex, match[1])

print(" ".join(rankings))```
