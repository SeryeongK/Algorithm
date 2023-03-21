# 토마토 - 2차원 배열 BFS
import sys
import collections
M, N = map(int, sys.stdin.readline().split())
tomato = []
for _ in range(N):
    tomato.append(list(map(int, sys.stdin.readline().split())))

mx = [0, 1, 0, -1]
my = [-1, 0, 1, 0]

q = collections.deque([])
def BFS():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                ## 🚨 토마토가 익은 날짜 세기 => 토마토의 숫자를 세면서 1씩 늘려가면 됨
                tomato[nx][ny] = tomato[x][y] + 1
                q.append([nx, ny])

## 익은 토마토 위치 큐에 추가하기
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append([i, j])

BFS()
days = []
for i in range(N):
    for j in tomato[i]:
        ## 만약 안 익은 토마토가 남아있었다면
        if j == 0:
            print(-1)
            exit()
    days.append(max(tomato[i]))

## 이미 하루차에 익어있는게 1이라고 되어있었으니까
print(max(days)-1)
"""
print(max(max(tomato))-1)
위 코드는 첫번째 원소의 값이 가장 큰 1차원 배열을 반환
"""