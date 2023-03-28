# 점프 - DP
import sys
N, M = map(int, sys.stdin.readline().split())
rocks = []
for _ in range(M):
    rocks.append(int(sys.stdin.readline()))

DP = [[float("inf") for _ in range(int(((2*N)**0.5)+2))] for _ in range(N+1)]
DP[1][0] = 0

for i in range(2, N+1):
    if i in rocks:
        continue
    for j in range(1, int(((2*N)**0.5)+1)):
        # print(f"i: {i}, j: {j}")
        # print(f"DP[i-j][j]: {DP[i-j][j]}, DP[i-j][j-1]: {DP[i-j][j-1]}, DP[i-j][j+1]: {DP[i-j][j+1]}")
        DP[i][j] = min(DP[i-j][j], DP[i-j][j-1], DP[i-j][j+1]) + 1

if min(DP[-1]) == float("inf"):
    print(-1)
else:
    print(min(DP[-1]))