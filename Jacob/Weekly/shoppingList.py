
N, M = map(int, input().split())

sets = []
for _ in range(N):
    sets.append(set(input().split()))

favorites = set(sets.pop())
for i in range(len(sets)):  # O(n^2) ?
    favorites = favorites.intersection(sets[i])

print(len(favorites))
{print(item) for item in sorted(favorites)} # O(n lgn)
