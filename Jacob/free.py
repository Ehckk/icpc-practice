#create graph

from collections import defaultdict
creases = [2,5,6,9]
graph = defaultdict(lambda: [])

end = 11

# worst case 300 * 4 = 1200 operations
for i in range(end):
    if i not in creases:
        graph[i] = [i+j for j in range(1,4) if (i+j not in creases) and (i+j) <= end]
            
stack = [0]
visited = {0}
pocket = [1,2,3]
cache = defaultdict(lambda: [])
fails = []
cache[0].append([*pocket])

#memo = defaultdict(lambda: [])
visited = []
def dfs(pocket):
    # depth first search

    node = stack.pop()

    for neighbor in graph[node]:

        while neighbor in cache:
            


        # build cache of neighbors
        for combos in cache[node]:

            cache[neighbor].append(combos.copy())
    
            #else:
                #cache[neighbor].append(combos.copy())
                #cache[neighbor][-1][0] = node
            cache[neighbor][-1][neighbor-node-1] -=1
            # duplicates
            if cache[neighbor].count(cache[neighbor][-1]) > 1:
                cache[neighbor].pop()
                print('repeated', node, neighbor)
            # out of bricks
            elif -1 in cache[neighbor][-1]:
                # remove from original
                cache[neighbor][-1][neighbor-node-1] +=1
                target = cache[neighbor][-1]
                
                cache[node].remove(target)
                cache[neighbor].pop()
                fails.append(target)
                

            if end in cache:
                print('YES')
                
        for element in cache[node]: # replaces -1 system
            if element[neighbor - node-1] >= 1:
                stack.append((neighbor))
            else:
                pass
            # add to fail
            # where to check fails?
    dfs(pocket)

dfs(pocket)
# DP

cache = defaultdict(lambda: [1,2,3])

print(cache)