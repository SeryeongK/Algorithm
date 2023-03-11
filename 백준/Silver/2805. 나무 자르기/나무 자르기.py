# 나무 자르기
import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(tree) # 이분탐색 검색 범위 설정

while start <= end:
    mid = (start+end) // 2
    
    # 잘라진 나무 총합
    log = 0 
    for i in tree:
        if i >= mid:
            log += i - mid
    
    # 자를 높이를 이분탐색
    if log >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)