# 최소비용 구하기 <= 다익스트라 알고리즘 코드 완전 참고
import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
input = []
for _ in range(M):
    input.append(list(map(int, sys.stdin.readline().split())))
bus = [[] for _ in range(N+1)]
for i in input:
    a, b, v = i
    bus[a].append([b, v])
    ## 🚨 문제에서 출발지와 도착지라고 함 => 방향 그래프
    # bus[b].append([a, v])

distance = [float("inf")] * (N+1)
## 책의 다익스트라 알고리즘 코드 참고
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in bus[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

start, end = map(int, sys.stdin.readline().split())
dijkstra(start)
print(distance[end])