import sys
ex1 = "12 17 36 37 51 63 92 124"


def solve(line_in):
    raw = [int(x) for x in line_in.strip().split(" ")]
    nums = raw[:6]
    height1 = raw[6]
    height2 = raw[7]

    def findit():
        for i in range(6):
            for j in range(i):
                for z in range(j):
                    if nums[i] + nums[j] + nums[z] == height1:
                        return i, j, z
    i, j, z = findit()

    ans = [i, j, z]
    rest = list({0, 1, 2, 3, 4, 5} - set(ans))

    ans_raw = sorted([nums[i] for i in ans], reverse=True)
    rest_raw = sorted([nums[i] for i in rest], reverse=True)

    return " ".join([str(c) for c in (ans_raw + rest_raw)])

for s in sys.stdin:
    print(solve(s))
