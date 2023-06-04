# 파도반 수열 - DP

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    DP = [0] * N
    for i in range(N):
        if i <= 2:
            DP[i] = 1
        elif 2 < i <= 4:
            DP[i] = 2
        else:
            DP[i] = DP[i-1] + DP[i-5]
    print(DP[-1])
