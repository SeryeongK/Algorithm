# 오르막 수
import sys
N = int(sys.stdin.readline())

DP = [1]*10

if N == 1:
    print(10)
elif N == 2:
    print(55)
else:
    for i in range(1, N+1):
        for j in range(1, 10):
            # 🚨 경우의 수를 구하라고 했으면 경우의 수에서 규칙을 찾아볼 것!
            DP[j] += DP[j-1]
    print(DP[-1]%10007) 