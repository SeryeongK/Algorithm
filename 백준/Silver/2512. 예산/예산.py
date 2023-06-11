# 예산 - 이분탐색
import sys
N = int(sys.stdin.readline())
regions = list(map(int, sys.stdin.readline().split()))
budget = int(sys.stdin.readline())
start, end = 1, max(regions)
answer = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    # 배정할 예산 정하기
    for i in regions:
        if mid >= i:
            total += i
        else:
            total += mid
    # 배정할 예산이 국가예산 총액 안인지 확인
    if total > budget:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid

print(answer)
