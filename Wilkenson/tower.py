import sys


def stack_boxes(box_in):
    line: str = box_in.split()
    if len(line) < 8 or len(line) > 8:
        return

    tower_height1 = int(line[-1])
    tower_height2 = int(line[-2])

    num = []  # store the first 6 numbers
    tower_one = []  # store the first 3 boxes
    tower_two = []  # store the last 3 boxes

    if tower_height1 == tower_height2:
        return
    [num.append(int(x)) for x in line[:6] if int(x) <= 100]

    if len(set(num)) < 6:
        return
    num.sort()
    for i in range(len(num)):
        left_pointer = i + 1
        right_pointer = len(num) - 1

        while left_pointer < right_pointer:
            box_sum: int = num[i] + num[left_pointer] + num[right_pointer]

            if tower_height1 == box_sum or tower_height2 == box_sum:
                tower_one.append(num[i])
                tower_one.append(num[left_pointer])
                tower_one.append(num[right_pointer])
                tower_one.sort(reverse=True)
                [tower_two.append(x) for x in num if x not in tower_one]
                tower_two.sort(reverse=True)
                [tower_one.append(x) for x in tower_two if x not in tower_one]
                [tower_two.append(x) for x in tower_one if x not in tower_two]
                if tower_height1 == box_sum:
                    return sys.stdout.writelines(' '.join([str(box) for box in tower_two]))
                else:
                    return sys.stdout.writelines(' '.join([str(box) for box in tower_one]))
            elif tower_height1 > box_sum:
                left_pointer += 1
            else:
                right_pointer -= 1
    return ''


for input_in in sys.stdin:
    stack_boxes(input_in)
    print()
