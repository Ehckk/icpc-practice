'''
Jacob Stephens, ICPC 
September 20, 2023
Greater NY Regionals 2022, Sacred Heart (Practice)
(#1/10) Cornhole
'''

# parse input
H1, B1 = map(int, input().split())
H2, B2 = map(int, input().split())

# calc player totals
p1total = (3 * H1) + B1
p2total = (3 * H2) + B2

# calculate difference and output
if p1total > p2total:
    print(f'1 {p1total - p2total}')

elif p1total < p2total:
    print(f'2 {p2total - p1total}')

else: # equal
    print('NO SCORE')