# 카드 정렬하기 - 힙
import sys
import heapq

## 힙에 추가
N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    input = int(sys.stdin.readline())
    heapq.heappush(heap, input)

## 비교한 횟수
sum = 0
## 마지막에는 최종적으로 다 합해진 카드 묶음만 남기 때문에
while len(heap) > 1:
    s = 0
    ## 🚨 가장 작은 것 2번 더하기
    s += heapq.heappop(heap)
    s += heapq.heappop(heap)
    ## 비교한 횟수에 더하기
    sum += s
    ## 더해진 카드 묶음 힙에 추가
    heapq.heappush(heap, s)

print(sum)