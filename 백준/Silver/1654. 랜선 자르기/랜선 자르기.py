# 랜선 자르기 - 이분 탐색
import sys

N, K = map(int, sys.stdin.readline().split())
## input에서 찾는 것이 아니므로 정렬할 필요 없음
input = [int(sys.stdin.readline()) for _ in range(N)]

start = 1
end = max(input)

output = 0
## 랜선 길이 이분탐색
while start <= end:
    mid = (start + end) // 2
    s = 0
    ## 만들 수 있는 랜선 개수
    for i in input:
        s += i // mid
    
    ## 길이 조정
    if s >= K:
        start = mid + 1
    else:
        end = mid - 1

print(end)

## 🚨 mid가 있는 이분탐색과 투포인트를 착각하지 말 것