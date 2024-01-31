# https://codeforces.com/contest/433/problem/B

n = int(input())
costs = list(map(int, input().split()))

numQueries = int(input())

# generate prefixSum
prefixSum = [0] + costs[:]
for i in range(1,len(costs)+1):
    prefixSum[i] = prefixSum[i] + prefixSum[i-1]
    
# generate prefixSum from sorted costs
sortedCosts = sorted(costs)
prefixSumOfSorted = [0] + sortedCosts[:]

for i in range(1,len(costs)+1):
    prefixSumOfSorted[i] = prefixSumOfSorted[i] + prefixSumOfSorted[i-1]

ans = []
for _ in range(numQueries):
    typeQuestion, l, r = map(int, input().split())

    # return v of i
    if typeQuestion == 1:
        result = prefixSum[r] - prefixSum[l-1]

    # return u of i
    elif typeQuestion == 2:
        result = prefixSumOfSorted[r] - prefixSumOfSorted[l-1]

    ans.append(result)

[print(i) for i in ans]
