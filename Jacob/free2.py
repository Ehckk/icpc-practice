cache = {
    0: [[2,1,3], [1,1,4]],
    1: [[2,2,2]]

} 

brickUsed = 3
neighbor = 1
node = 0


    # build cache of neighbors
    for combos in cache[node]:
        cache[neighbor].append([prev] + combos.copy())
        cache[neighbor][-1][neighbor-node] -=1
        # duplicates
        if cache[neighbor].count(cache[neighbor][-1]) > 1:
            cache[neighbor].pop()
        # out of bricks
        elif -1 in cache[neighbor][-1]:
            cache[neighbor].pop()




for combos in cache[node]:
cache[neighbor].append(combos.copy())
cache[neighbor][-1][neighbor-node-1] -=1


for i in range(len(cache))
cache[neighbor][-1][neighbor-node-1] -=1

for combos in cache[neighbor]:
combos[neighbor-node-1] -= 1

print(cache[0])



for pocket in cache[1]:
pocket[brickUsed-1] -= 1
print(cache[1])
# copy of pocket where index X is one less

