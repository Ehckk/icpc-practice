# https://open.kattis.com/problems/npuzzle
from sys import stdin


def main():
    desiredBoard = {}
    inc = 0
    startingLetter = "A"
    for x in range(4):
        for y in range(4):
            currentLetter = chr(ord(startingLetter) + inc)
            desiredBoard[currentLetter] = (x, y)
            inc = inc + 1
    desiredBoard.pop("P")
    desiredBoard["."] = (3, 3)

    row = 0
    sumDistance = 0
    for line in stdin:
        letters = [l for l in line.strip()]
        column = 0
        for letter in letters:
            if letter != ".":
                (desiredX, desiredY) = desiredBoard[letter]
                distanceX = abs(desiredX - row)
                distanceY = abs(desiredY - column)
                mDistance = distanceX + distanceY
                sumDistance = sumDistance + mDistance
            column = column + 1
        row = row + 1

    print(sumDistance)


if __name__ == "__main__":
    main()
