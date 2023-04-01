# 1로 만들기 - DP
import sys
N = int(sys.stdin.readline())

## DP 테이블 생성
DP = [0 for _ in range(N+1)]
## 초기값 설정
DP[0] = 0
DP[1] = 0

for i in range(2, N+1):
    ## 숫자가 2나 3일 때(초기값)
    if i == 2 or i == 3:
        DP[i] = 1
    else:    
        three = 0
        two = 0
        if i % 3 == 0:
            three = i//3
        if i % 2 == 0:
            two = i//2
        
        if three and two:
            DP[i] = min(DP[i//3], DP[i//2], DP[i-1]) + 1
        elif three:
            DP[i] = min(DP[i//3], DP[i-1]) + 1
        elif two:
            DP[i] = min(DP[i//2], DP[i-1]) + 1
        else:
            DP[i] = DP[i-1] + 1

print(DP[-1])