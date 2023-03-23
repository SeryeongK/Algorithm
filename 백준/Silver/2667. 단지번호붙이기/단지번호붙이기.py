# 단지번호붙이기
import sys
import collections

N = int(sys.stdin.readline())
m = []
for _ in range(N):
    input = list(sys.stdin.readline().strip())
    ## 분명 더 효율적인 방법이 있음
    ii = []
    for i in input:
        ii.append(int(i))
    m.append(ii)

## 방향키
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

q = collections.deque()
## BFS 알고리즘
def BFS(startx, starty, count):
    ## 단지내 집의 수 카운트
    c = 0
    q.append([startx, starty])
    c += 1
    m[startx][starty] = count
    while q:
        x, y = q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < N and m[tx][ty] == 1:
                m[tx][ty] = count
                q.append([tx, ty])
                c += 1
    return c

## 이미 집이 1로 초기화되어 있기 때문에 2로 변경해 나가기
count  = 2
houses = []
for i in range(N):
    for j in range(N):
        if m[i][j] == 1:
            houses.append(BFS(i, j, count))
            ## 단지가 바뀔 때마다 수 늘리기
            count += 1

print(count-2)
houses.sort()
for i in houses:
    print(i)