# 연결 요소의 개수
import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
input = []
for _ in range(M):
    input.append(list(map(int, sys.stdin.readline().split())))

## 연결 리스트 만들기
graph = [[] for _ in range(N+1)]
for i in input:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

for i in input:
    i = sorted(i)

## DFS
el = 0
visited = [0]*(N+1)
## 바이러스에 걸리게 되는 컴퓨터
cnt = []
def DFS(start):
    global el, visited, cnt
    visited[start] += 1
    cnt.append(start)
    for i in graph[start]:
        if visited[i] == 0:
            DFS(i)

DFS(1)
print(len(cnt)-1)