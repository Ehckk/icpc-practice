''' 
Jacob Stephens, ICPC
September 18, 2023
Pairing Socks https://open.kattis.com/problems/pairingsocks
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

    
