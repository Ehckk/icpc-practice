import sys


def main():

    input = sys.stdin.readlines()

    p1score = 0
    p2score = 0
    counter = 0

    for scores in input:

        scores = scores.rstrip('\n')
        scores = scores.split(' ')

        if counter == 0:

            p1score = (int(scores[0]) * 3) + int(scores[1])

        if counter == 1:

            p2score = (int(scores[0]) * 3) + int(scores[1])

        counter += 1

    dif = abs(p1score - p2score)

    if p1score > p2score:

        print(1, " ", dif)

    elif p1score < p2score:

        print(1, " ", dif)

    else:
        print("NO SCORE")


main()
