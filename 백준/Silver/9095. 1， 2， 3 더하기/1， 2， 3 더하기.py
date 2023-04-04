# 1, 2, 3 더하기
# 경우의 수 제대로 찾기
import sys
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    DP = [0]*(N+1)
    if N == 1:
        print(1)
    elif N == 2:
        print(2)
    elif N == 3:
        print(4)
    else:
        for i in range(3):
            DP[i] = i
        DP[3] = 4
        
        for i in range(4, N+1):
            DP[i] = DP[i-3] + DP[i-2] + DP[i-1]
        print(DP[-1])