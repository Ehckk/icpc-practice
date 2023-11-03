'''
Jacob Stephens, ICPC 
September 22, 2023
Greater NY Regionals 2022, Sacred Heart (Practice)
(#2/10) Sum of Remainders
'''
import sys
raw = sys.stdin.read()

# list of all numbers
numbers = [int(i) for i in raw.split()]
numGates = numbers[1] 

# start all k values at infinity
k = [999 for _ in range(numGates)]

for n in range(1,len(numbers)):
    if 999 not in k: # end condition - all values discovered
        break

    # calculate expected and actual value
    actual = numbers[n]
    expected = 0
    for j in range(len(k)):
        expected += (n % k[j])

    # compare values 
    if actual != expected:

        # calculate k's that are equal to n and replace infitities with n
        gatesChanged = int((expected - actual) / n)
        for _ in range(gatesChanged):
            target = k.index(999)
            k.pop(target)
            k.insert(target, n)

# print output
k.insert(0, len(k))
[print(element, end =" ") for element in k]
