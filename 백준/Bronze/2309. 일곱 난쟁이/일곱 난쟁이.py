# 일곱 난쟁이
import sys
from itertools import combinations
input = list(map(int, [sys.stdin.readline().strip() for _ in range(9)]))
ls = list(combinations(input, 7))
nls = []
for i in ls:
    if sum(i) == 100:
        nls.append(sorted(list(i)))

for j in nls[0]:
    print(j)