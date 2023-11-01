from sys import stdin, stdout

def squares_less_than_n(n):
    squares = []
    i = 0
    sqr = 0
    
    while sqr <= n:
        squares.append(sqr)
        i += 1
        sqr = i ** 2
    
    return squares

def foursquares(raw):
    n = int(raw[0])
    squares = squares_less_than_n(n)
    result = 0

    def recur(n, count, idx, combo):
        nonlocal result
        if count == 0:
            if n == 0:
                result += 1
            return
        if idx < 0:
            return
        
        for i in range(idx, -1, -1):
            
            if i == 0 or -i not in combo:
                combo.append(i)
                recur(n-squares[i], count-1, i, combo)
                combo.pop()

            if count == 4 or squares[i] == 0:
                continue

            if i not in combo:
                combo.append(-i)
                recur(n+squares[i], count-1, i, combo)
                combo.pop()

    recur(n, count=4, idx=len(squares)-1, combo=[])
    return str(result) + "\n"

raw = []
line = stdin.readline()

while line:
    raw.append(line.strip())
    line = stdin.readline()

stdout.write(foursquares(raw))
