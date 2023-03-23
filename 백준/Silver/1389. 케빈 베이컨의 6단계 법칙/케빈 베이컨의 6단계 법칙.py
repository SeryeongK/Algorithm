# 케빈 베이컨의 6단계 법칙
import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
rel = [[] for _ in range(N+1)]
## 사람들과의 관계 정보
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    rel[a].append(b)
    rel[b].append(a)

## 다익스트라 알고리즘 + BFS
def BFS(start):
    distance = [float("inf") for _ in range(N+1)]
    distance[0] = 0
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        d, s = heapq.heappop(q)
        for i in rel[s]:
            if distance[i] > d:
                distance[i] = d+1
                heapq.heappush(q, (distance[i], i))
    return sum(distance) ## 모든 사람과의 단계

output = [float("inf")]
for i in range(1, N+1):
    output.append(BFS(i))

# print(output) 모든 사람의 케빈 베이컨 수
## 케빈 베이컨의 수가 가장 작은 사람을 찾았으면 출력하고 break
for i in range(N):
    if output[i] == min(output):
        print(i)
        break