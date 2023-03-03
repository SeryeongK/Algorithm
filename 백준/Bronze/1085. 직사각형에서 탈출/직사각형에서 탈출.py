import sys

input = sys.stdin.readline().split()

nums = []

def min(i):
    x =int(i[0])
    y = int(i[1])
    w = int(i[2])
    h = int(i[3])
    nums.extend([x, y])
    nums.append(w - x)
    nums.append(h-y)
    nums.sort()
    print(nums[0])

min(input)