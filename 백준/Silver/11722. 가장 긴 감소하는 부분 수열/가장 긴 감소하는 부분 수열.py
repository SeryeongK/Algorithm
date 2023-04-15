# 가장 긴 감소하는 부분 수열
import sys
N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
DP = [1] * N

for i in range(N):
    M = 0
    for j in range(i):
        if seq[i] < seq[j]:
            if M <= DP[j]:
                M = DP[j]
    DP[i] += M

print(max(DP))