# http://acmgnyr.org/year2023/problems/index.html
# B-apivotalquestion
from sys import stdin


def main():

    input_line = stdin.readline().strip()
    input_numbers = list(map(int, input_line.split()))[1:]
    sorted_numbers = sorted(input_numbers)

    cur_input_max = -float('inf')
    pivots = []

    for input_val, sorted_val in zip(input_numbers, sorted_numbers):
        cur_input_max = max(cur_input_max, input_val)
        if input_val == sorted_val and sorted_val >= cur_input_max:
            pivots.append(input_val)

    print(len(pivots), *pivots[:100])


if __name__ == "__main__":
    main()
