# 계단 오르기 - DP
import sys

N = int(sys.stdin.readline())
stairs = []
for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

DP = [0 for _ in range(N)] # 시작 계단은 0번 계단
for i in range(N):
    if i == 0:
        DP[i] = stairs[i] # 0번째 계단
    elif i == 1:
        DP[i] = stairs[i-1] + stairs[i] # 0, 1번째 계단
    elif i == 2:
        DP[i] = max(stairs[i-2] + stairs[i], stairs[i-1] + stairs[i])
    else:
        DP[i] = max(DP[i-3] + stairs[i-1] + stairs[i], DP[i-2] + stairs[i])

print(DP[-1])