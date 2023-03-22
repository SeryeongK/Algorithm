# 문제집 - 위상 정렬
import sys
import collections
import heapq
N, M  = map(int, sys.stdin.readline().split())
rel = [[] for _ in range(N+1)]
come = [0 for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    rel[a].append(b)
    rel[a].sort()
    come[b] += 1

q = []
for i in range(1, N+1):
    if come[i] == 0:
        heapq.heappush(q, i)
        # q.append(i)

output = []
while q or sum(come) > 0:
    now = heapq.heappop(q)
    # now = q.popleft()
    output.append(str(now))
    for i in rel[now]:
        come[i] -= 1
        if come[i] == 0:
            heapq.heappush(q, i)
            # q.append(i)

print(' '.join(output))