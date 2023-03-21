# 줄 세우기 - 위상 정렬
import sys
import collections

N, M = map(int, sys.stdin.readline().split())
com = [[] for _ in range(N+1)] ## 연결 리스트
come = [0 for _ in range(N+1)] ## 진입차수 저장

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    com[a].append(b)
    come[b] += 1

q = collections.deque([])
output = []

## 초기에 진입 차수가 0인 것을 넣기
for i in range(1, N+1):
    if come[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for i in com[now]:
        come[i] -= 1
        if come[i] == 0:
            q.append(i)
    output.append(str(now))

print(' '.join(output))