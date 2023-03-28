import sys

n = int(input())

nums = []
for i in range(n):
    nums.append(int(input()))

#print(nums)

missing = []
for i in range(1, nums[-1]):
    if i not in nums:
        missing.append(i)

missing = sorted(missing)

if missing:

    for m in missing:
        print(m)
else:
    print("good job")