# N과 M(1)
import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
nums = []
for i in range(1, N+1):
    nums.append(str(i))
perms = list(permutations(nums, M))

for i in perms:
    print(" ".join(i))
