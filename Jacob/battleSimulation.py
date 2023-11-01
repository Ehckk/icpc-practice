'''
Jacob Stephens, ICPC
April 13, 2023
Battle Simiulation Kattis https://open.kattis.com/problems/battlesimulation
'''

input = input()
output = []

# combo = latest 3 attacks
combo = []

for attack in input:
    combo.append(attack)

    # basic defense
    if attack == 'R':
        output.append('S')

    elif attack == 'B':
        output.append('K')

    else:
        output.append('H')

    # if last 3 attacks are unique (powerful combo move)
    if len(set(combo)) == 3:
        for i in range(3):
            output.pop()

        # add C to output, clear combo
        output.append('C')
        combo.clear()
    
    # keeps combo list only 3 len
    elif len(combo) >= 3:
        combo.pop(0)

pri'''
Jacob Stephens, ICPC
April 13, 2023
Battle Simiulation Kattis https://open.kattis.com/problems/battlesimulation
'''

input = input()
output = []

# combo = latest 3 attacks
combo = []

for attack in input:
    combo.append(attack)

    # basic defense
    if attack == 'R':
        output.append('S')

    elif attack == 'B':
        output.append('K')

    else:
        output.append('H')

    # if last 3 attacks are unique (powerful combo move)
    if len(set(combo)) == 3:
        for i in range(3):
            output.pop()

        # add C to output, clear combo
        output.append('C')
        combo.clear()
    
    # keeps combo list only 3 len
    elif len(combo) >= 3:
        combo.pop(0)

pri