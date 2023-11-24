''' Jacob Stephens
    March 25, 2023
    ICPC Practice

    ** Given an input of numbers from 1 to n, some will be missing. Calculate and print which are missing. (n <= 100)
'''

# put input into list
inp = []
for _ in range(int(input())):
    inp.append(int(input()))

# create set of all numbers from 1 to highest num
max = inp[-1]
all = set()
for i in range(1,max+1):
    all.add(i) 

# create set of all included numbers
incl = set()
for n in inp:
    incl.add(n)

# create list of all missing (excluded) numbers
excl = list(all - incl)
excl.sort()

# OUTPUT
# if missed any numbers
if len(excl) != 0:
    for n in excl:
        print(n)
# else did not miss any
else:
    print("good job")
