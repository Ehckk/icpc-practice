'''
Jacob Stephens, ICPC
September 15, 2023
A Different Problem Kattis https://open.kattis.com/problems/different
'''
import sys

# get input into pairs array
pairs = []
for line in sys.stdin.readlines():
    pairs.append(line.rstrip())

# subtract elements of each pair
for pair in pairs:
    current = pair.split()
    print(abs(int(current[0])-int(current[1])))
'''
Jacob Stephens, ICPC
September 15, 2023
A Different Problem Kattis https://open.kattis.com/problems/different
'''
import sys

# get input into pairs array
pairs = []
for line in sys.stdin.readlines():
    pairs.append(line.rstrip())

# subtract elements of each pair
for pair in pairs:
    current = pair.split()
    print(abs(int(current[0])-int(current[1])))
