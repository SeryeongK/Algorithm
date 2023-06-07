# 나무 자르기
# 가장 낮은 나무 & 가장 높은 나무 사이 길이를 이분 탐색하면서
# 적절한 절단 높이 찾기

import sys
N, H = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start+end) // 2
    cut = 0
    for i in trees:
        if i > mid:
            cut += (i - mid)
    if cut >= H:  # => 절단양이 줄어야 == 절단 높이가 높아져야
        start = mid + 1
    else:
        end = mid - 1

print(end)
