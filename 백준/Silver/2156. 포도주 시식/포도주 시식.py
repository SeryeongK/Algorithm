# 포도주 시식
import sys

N = int(sys.stdin.readline())
wine = []
for _ in range(N):
    wine.append(int(sys.stdin.readline()))
DP = [0] * (N+1)
if N == 1:
    DP[1] = wine[0]
    print(DP[1])
elif N == 2:
    DP[1] = wine[0]
    DP[2] = DP[1]+wine[1]
    print(DP[2])
else:   
    DP[1] = wine[0]
    DP[2] = DP[1]+wine[1]
    for i in range(3, N+1):
        DP[i] = max(DP[i-1], DP[i-2]+wine[i-1], DP[i-3]+wine[i-2]+wine[i-1])
    print(DP[-1])