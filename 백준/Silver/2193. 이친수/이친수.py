# 이친수
import sys

N = int(sys.stdin.readline())
DP = [0] * (N+1)

if N == 1:
    print(1)
elif N == 2:
    print(1)
else:
    DP[1] = 1
    DP[2] = 1
    for i in range(3, N+1):
        DP[i] = DP[i-2] + DP[i-1]
    print(DP[-1])