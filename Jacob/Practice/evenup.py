''' 
Jacob Stephens, ICPC
September 18, 2023
Even Up Solitaire https://open.kattis.com/problems/evenup
Steven Halim Book pg. 77 (stacks, #1)

AC
'''

input()

main = [int(i) for i in input().split()]
aux = [-500]
moves = 0

while main:
    if main[-1] == aux[-1]:
        main.pop()
        aux.pop()
        moves += 1
    else:
        aux.append(main.pop())
        moves += 1

if len(aux) == 1:
    print(moves)
else:
    print('impossible')

    
input()
cards = input().split()
cards = [int(i) for i in cards]
reserve = []

def solve(cards):
    startLength = len(cards)
    while len(cards) >= 2:
        top = cards.pop()
        peek = cards[-1]
        if (top + peek) % 2 == 0:
            cards.pop()
        else:
            reserve.append(top)
    
    if len(cards) == 1:
        reserve.append(cards.pop())
    # else len == 0

    if len(reserve) != startLength:
        cards = reserve.copy()
        reserve.clear()
        solve(cards)
    # else base case

solve(cards)
print(len(reserve))    
