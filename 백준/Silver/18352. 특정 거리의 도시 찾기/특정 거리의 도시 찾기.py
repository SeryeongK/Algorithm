# 특정 거리의 도시 찾기
import sys
import collections
N, M, K, X = map(int, sys.stdin.readline().split())
roads = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    roads[a].append(b)

output = []

q = collections.deque([])
visited = [0]*(N+1)
## 🚨 거리를 저장(아이디어 블로그 참고)
distance = [0]*(N+1)
def BFS(start):
    visited[start] = 1
    for i in roads[start]:
        q.append(i)
        distance[i] = 1
    while q:
        # print(q)
        now = q.popleft()
        for i in roads[now]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
                ## 아직 인접해본 적 없었던 경우
                if distance[i] == 0:
                    distance[i] = distance[now] + 1

BFS(X)

# print(distance)
count = 0
for i in range(len(distance)):
    if distance[i] == K:
        count += 1
        print(i)
if count == 0:
    print(-1)