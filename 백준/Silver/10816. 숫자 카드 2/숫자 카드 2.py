# 숫자 카드 2 - 이분 탐색
import sys
from collections import Counter

n = int(sys.stdin.readline())
sanggen = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

## 각 숫자가 몇 개인지 세기(시간초과)
# for i in sanggen:
#     c = 0
#     for j in s:
#         if j[0] == i:
#             j[1] += 1
#             c += 1
#     if c == 0:
#         s.append([i, 1])

## 🚨 counter 함수는 개수를 계산해줌
## 🚨 sorted(counter.items()): 아이템의 이름으로 정렬
s = Counter(sanggen)

## 숫자 이분 탐색 함수(Counter로 구해서 필요없음...)
# def bin_search(f):
#     start = 0
#     end = len(s)-1
#     output.append('0')
#     ## 검색이니까 등호도 포함
#     while start <= end:
#         ## 이분 탐색
#         mid = (start+end) //2
#         if s[mid][0] > f:
#             end -= 1
#         elif s[mid][0] < f:
#             start += 1
#         else:
#             output.pop()
#             output.append(str(s[mid][1]))
#             break

# for i in cards:
#     bin_search(i)

output = []
for i in cards:
    if i in s:
        ## 딕셔너리는 key로 value를 찾아야 함
        output.append(str(s[i]))
    else:
        output.append("0")

print(' '.join(output))