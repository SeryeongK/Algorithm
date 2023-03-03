import sys

n = int(sys.stdin.readline())

data = [sys.stdin.readline().strip() for i in range(n)]

for line in data:
    nums = line.split()
    print(int(nums[0]) + int(nums[1]))