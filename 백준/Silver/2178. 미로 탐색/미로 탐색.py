# 미로 탐색 - BFS
import sys
import collections
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
maze = []
for _ in range(N):
    input = sys.stdin.readline().strip()
    line = []
    for i in range(len(input)):
        line.append(int(input[i]))
    maze.append(line)

# 방향 탐지기
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
# print(maze)
q = collections.deque([])
def BFS(starty, startx):
    for i in range(0, 4):
        tempy = starty + dy[i]
        tempx = startx + dx[i]
        if 0 <= tempy < N and 0 <= tempx < M:
            if maze[tempy][tempx] == 1:
                # print(f"maze[tempx][tempy]: {maze[tempy][tempx]}, maze[startx][starty]: {maze[starty][startx]}")
                q.append([tempy, tempx])
                maze[tempy][tempx] += maze[starty][startx]
                # for i in maze:
                #     print(i)
            else: continue
    while q:
        ny, nx = q.popleft()
        BFS(ny, nx)


BFS(0, 0)
# print(maze)
print(maze[N-1][M-1])