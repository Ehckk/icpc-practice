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
