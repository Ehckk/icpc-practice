# https://open.kattis.com/problems/towering
from sys import stdin
from itertools import combinations


def main():
    for line in stdin:
        inputs = [int(i) for i in line.split()]
        towerHeight1 = inputs[-2]
        towerHeight2 = inputs[-1]
        boxHeightsSet = set(inputs[:6])

        for possibleCombo in combinations(boxHeightsSet, 3):
            comboHeight = sum(possibleCombo)
            if comboHeight == towerHeight1:
                tower1 = list(possibleCombo)
                tower1.sort(reverse=True)
                tower2 = list(boxHeightsSet.difference(tower1))
                tower2.sort(reverse=True)
                print(*(tower1 + tower2))
                break
            elif comboHeight == towerHeight2:
                tower2 = list(possibleCombo)
                tower2.sort(reverse=True)
                tower1 = list(boxHeightsSet.difference(tower2))
                tower1.sort(reverse=True)
                print(*(tower1 + tower2))
                break


if __name__ == "__main__":
    main()
