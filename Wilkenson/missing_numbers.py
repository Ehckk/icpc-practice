import sys


def missing_number(list_num):
    x_int = [int(i) for i in list_num]
    expected_length = x_int[0]
    x_int = x_int[1:expected_length+1]

    check = []
    out = []

    for n in range(1, int(list_num[-1]) + 1):
        check.append(n)

    for i in check:
        if i not in x_int:
            out.append(i)

    if len(out) != 0:
        for n in out:
            print(n)
    else:
        print('good job')


arr = []

for n in sys.stdin:

    arr.append(n.strip())

missing_number(arr)
