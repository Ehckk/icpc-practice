A, B, E, P = map(int, input().split(" ")[:4])

rules = {i: [] for i in range(E)}
inv_rules = {i: [] for i in range(E)}
for rule in range(P):
    e1, e2 = map(int, input().split(" "))
    rules[e1].append(e2)
    inv_rules[e2].append(e1)


def solve(A, B, E, rules, inv_rules):
    deps = {}
    inv_deps = {}

    # update the dict deps
    def get_deps(i, rules, deps):
        if i not in deps:
            deps[i] = {i}
        
            for n in rules[i]:
                for k in get_deps(n, rules, deps):
                    deps[i].add(k)

        return deps[i]
    
    dep_counts = [len(get_deps(i, rules, deps)) for i in range(E)] 
    req_counts  = [len(get_deps(i, inv_rules, inv_deps)) for i in range(E)]

    # number of people who will certainly be promoted with A promotions.
    # So if A promotions, out of N, that means we need
    count_must_be_promoted_with_A = 0
    count_must_be_promoted_with_B = 0
    def_not_promoted_with_B = 0
    for i in range(E):
        if dep_counts[i] > (E-A):
            count_must_be_promoted_with_A += 1
    
        if dep_counts[i] > (E-B):
            count_must_be_promoted_with_B += 1

        if req_counts[i] > B:
            def_not_promoted_with_B += 1

    print(count_must_be_promoted_with_A)
    print(count_must_be_promoted_with_B)
    print(def_not_promoted_with_B)

    return (
        count_must_be_promoted_with_A,
        count_must_be_promoted_with_B,
        def_not_promoted_with_B
    )


map(print, solve(A, B, E, rules, inv_rules))