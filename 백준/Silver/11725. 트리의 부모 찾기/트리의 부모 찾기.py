# 트리의 부모 찾기 - DFS
import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

input = []
for _ in range(N-1):
    input.append(list(map(int, sys.stdin.readline().split())))

ls = [[] for _ in range(N+1)]
for i in input:
    a, b = i
    ls[a].append(b)
    ls[b].append(a)

for i in ls:
    i.sort()

parent = [0]*(N+1)
visited = [0]*(N+1)
## 🚨 DFS는 이전 코드 참고(개념 확실히 익힐 것)
def DFS(start):
    visited[start] = 1
    for i in ls[start]:
        if visited[i] == 0:
            parent[i] = start
            DFS(i)

DFS(1)
for i in range(2, len(parent)):
    print(parent[i])