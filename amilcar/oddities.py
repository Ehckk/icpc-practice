# https://open.kattis.com/problems/oddities
# Oddities

from sys import stdin


def main():

    input_line = stdin.readline().strip()
    first_number = int(input_line)

    for line in range(first_number):
        input_line = stdin.readline().strip()
        input_number = int(input_line)

        if input_number % 2 == 0:
            print('{:d} is even'.format(input_number))
        else:
            print('{:d} is odd'.format(input_number))


if __name__ == '__main__':
    main()
