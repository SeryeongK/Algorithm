# 차이를 최대로
import sys
from itertools import permutations

n = int(sys.stdin.readline())
input = list(map(int, sys.stdin.readline().split()))

## 모든 순서의 배열 구하기
ls = list(permutations(input, len(input)))
for i in range(len(ls)):
    ls[i] = list(ls[i])

## 최댓값 구하기
sls = []
for i in ls:
    s = 0
    for j in range(1, len(i)):
        s += (abs(i[j-1]-i[j]))
    sls.append(s)

sls.sort()
print(sls[-1])