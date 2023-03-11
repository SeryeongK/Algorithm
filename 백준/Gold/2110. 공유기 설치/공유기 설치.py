# 공유기 설치
import sys

n, c = map(int, sys.stdin.readline().split())
arr = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])

start = 1
end = arr[-1] - arr[0]
answer = 0

while start <= end:
    ## 초기화
    mid = (start + end) // 2
    ## 🚨 첫번째 집에 공유기를 설치한다고 가정하고 초기화
    count = 1
    current = arr[0]

    for i in range(1, len(arr)):
        if arr[i] >= current + mid:
            count += 1
            current = arr[i]

    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)