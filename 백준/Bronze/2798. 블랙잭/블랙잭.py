# 블랙잭
import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

## 가능한 값 전부 추가
odds = list(set(combinations(cards, 3)))
nodds = []
for i in odds:
    i = list(i)
    nodds.append(i)

ls = []
## 🚨 remove는 O(N)이므로 시간초과 => 값을 m과 직접 비교하는 방법 사용
for i in nodds:
    if sum(i) <= m:
        ls.append([sum(i), m - sum(i)])
ls = sorted(ls, key=lambda x: x[1])
print(ls[0][0])