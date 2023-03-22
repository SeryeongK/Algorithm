# 문제집 - 위상 정렬
import sys
import heapq

N, M  = map(int, sys.stdin.readline().split())
rel = [[] for _ in range(N+1)]
come = [0 for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    rel[a].append(b)
    rel[a].sort()
    come[b] += 1

## 가장 숫자가 작은 것부터 뽑기 위해서 최소 힙 사용
q = []
for i in range(1, N+1):
    if come[i] == 0:
        heapq.heappush(q, i)

output = []
while q or sum(come) > 0:
    now = heapq.heappop(q)
    output.append(str(now))
    for i in rel[now]:
        come[i] -= 1
        if come[i] == 0:
            heapq.heappush(q, i)

print(' '.join(output))