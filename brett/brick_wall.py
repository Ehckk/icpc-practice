N, c1, c2, c3 = map(int, input().split(" "))

last = list(map(int, input().split(" ")))

def solve(N, c1, c2, c3, last):
    ends = set()
    s = 0
    for l in last[:-1]:
        s += l
        ends.add(s)

    cache = {}

    def can_do(n, c1, c2, c3):
        cached = cache.get((n, c1, c2, c3))

        if cached is not None:
            return cached
        
        #print(n, c1, c2, c3, n in ends)
            
        ret = False

        # check if we have a c1 left
        if n not in ends:
            if c1 > 0 and n >= 1:
                ret = ret or can_do(n - 1, c1 - 1, c2, c3)
            if c2 > 0 and n >= 2:
                ret = ret or can_do(n - 2, c1, c2 - 1, c3)
            if c3 > 0 and n >= 3:
                ret = ret or can_do(n - 3, c1, c2, c3 - 1)

        ret = ret or n == 0
        cache[(n, c1, c2, c3)] = ret

        return ret
    
    return can_do(sum(last), c1, c2, c3)

if solve(N, c1, c2, c3, last):
    print("YES")
else:
    print("NO")