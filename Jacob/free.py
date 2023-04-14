'''
combo = ['A', 'R', 'B', 'L']
if len(combo) == 4:
    combo.pop(0)
    if (combo.count('R') == 1) and (combo.count('B') == 1) and (combo.count('L') == 1):
        print('COMBO FOUND')
'''

output = "RRRBL"
output = output[:-3]
output += 'C'

print(output)