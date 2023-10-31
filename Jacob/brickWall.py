#create graph

from collections import defaultdict
creases = [2,5,6,9]
graph = defaultdict(lambda: [])
memo = defaultdict(lambda: [])
end = 11

# worst case 300 * 4 = 1200 operations
for i in range(end):
    if i not in creases:
        graph[i] = [i+j for j in range(1,4) if (i+j not in creases) and (i+j) <= end]
            
stack = [0]
visited = set(0)
pocket = '2 1 3'
#memo = defaultdict(lambda: [])

def dfs():
    # depth first search
    node = stack.pop()
    pocket[brickUsed-1] -= 1
    if -1 in pocket:
        node = stack.pop()

    visited.add(neighbor)
    for neighbor in graph[node]:
        if neighbor not in visited:

            brickUsed = neighbor - node





            stack.append(neighbor)

    # base cases
    if node == end:
        print('YES')
        exit()

    if len(visited) == len(graph):
        print('NO')
        exit()
    
    dfs()

dfs()
# DP

cache = defaultdict(lambda: [1,2,3])

print(cache)




'''line1 = input().split()
line2 = input().split()

N = line1[0]
creases = []
pocket = [-999] + [int(brick) for brick in line1[1:]]

sum = 0
for brick in line2:
    sum += int(brick)
    creases.append(sum)

# check length
layerString = "".join(line2)
layerSum = sum
pocketSum = pocket[1]*1 + pocket[2]*2 + pocket[3]*3



# impossible
if '11' in layerString[1:-2]:
    print('NO')
    exit()
def findNextCrease(pos, creases):
    for crease in creases:
        if pos < crease:
            return crease


def placeBrick(pos, pocket, creases, nextCrease):

    if pos == layerSum:
        print('YES')
        exit()

    for crease in creases:
        if pos < crease:
            nextCrease = crease
            break
    dtc = nextCrease - pos

    if dtc == 1:
        # place brick 2
        if (pocket[2] > 0) and (pos + 2 not in creases):
            pocket[2] -= 1
            pos += 2
        # place brick 3
        elif (pocket[3] > 0) and (pos + 3 not in creases):
            pocket[3] -= 1
            pos += 3
        # out of options
        else:
            print('NO')
            exit()

    if dtc == 2:
        # place brick 1
        if (pocket[1] > 0) and (pos + 1 not in creases):
            pocket[1] -= 1
            pos += 1
        # place brick 3
        elif (pocket[3] > 0) and (pos + 3 not in creases):
            pocket[3] -= 1
            pos += 3
        # out of options
        else:
            print('NO')
            exit()
    
    placeBrick(pos, pocket, creases, nextCrease)



placeBrick(0, pocket, creases, 0)
#if 
#print('a')
'''