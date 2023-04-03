# 2*n 타일링
import sys

N = int(sys.stdin.readline())

## 규칙 찾기
DP = [0] * (N+1)
if N <= 2:
    print(N)
else:
    DP[1] = 1
    DP[2] = 2
    for i in range(3, N+1):
        ## 문제 제대로 읽기
        DP[i] = (DP[i-1] + DP[i-2])%10007
    print(DP[-1])