# 연속합
import sys
N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
DP = [0] * N
DP[0] = seq[0]

for i in range(1, N):
    if DP[i-1] >= 0:
        DP[i] = DP[i-1] + seq[i]
    else: 
        DP[i] = seq[i]

print(max(DP))