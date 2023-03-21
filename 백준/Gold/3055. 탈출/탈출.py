# 탈출 - BFS
import sys
import collections
R, C = map(int, sys.stdin.readline().split())
m = []
for _ in range(R):
    m.append(list(sys.stdin.readline().strip()))

mx = [0, 1, 0, -1]
my = [-1, 0, 1, 0]

q = collections.deque([])
def BFS(dx, dy):
    while q:
        x, y = q.popleft()
        for i in range(4):
            tx = x + mx[i]
            ty = y + my[i]
            if 0 <= tx < R and 0 <= ty < C:
                ## 지금이 고슴도치이고 인접 칸이 비어있거나 비버 굴이면
                if (m[tx][ty] == "." or m[tx][ty] == "D") and m[x][y] != "*":
                    m[tx][ty] = m[x][y] + 1
                    if tx == dx and ty == dy:
                        return
                    q.append([tx, ty])
                ## 지금이 물이고 인접 칸이 비어있거나 고슴도치(숫자)이면
                if (m[tx][ty] == "." or str(type(m[tx][ty])) == "<class 'int'>") and m[x][y] == "*":
                    m[tx][ty] = "*"
                    q.append([tx, ty])
            
## 비버의 위치를 dx, dy로 설정
## 고슴도치의 위치를 큐에 넣기 
dx = 0
dy = 0
for i in range(R):
    for j in range(C):
        if m[i][j] == "D":
            dx = i
            dy = j
        elif m[i][j] == "S":
            q.append([i, j])
            m[i][j] = 1

## 물의 위치를 큐에 넣기
for i in range(R):
    for j in range(C):
        if m[i][j] == "*":
            q.append([i, j])

BFS(dx, dy)
if m[dx][dy] == "D":
    print("KAKTUS")
else:
    ## 마지막에 D를 숫자로 바꿔주기 위해 한 번 더 더했으므로 1 빼기
    print(m[dx][dy]-1)