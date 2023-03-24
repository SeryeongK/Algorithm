# 동전 - DP
## 아이디어 & 코드 블로그 참고(https://d-cron.tistory.com/23)
## 2차원은 만들다가 꼬임...
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    price = list(map(int, sys.stdin.readline().split()))
    goal = int(sys.stdin.readline())
    DP = [0] * (goal+1)
    ## 1과 동전 숫자 초기화
    DP[0] = 1
    DP[price[0]] = 1

    ## 첫번째 동전 초기화
    for i in range(1, goal+1):
        if i % price[0] == 0:
            DP[i] = 1
    
    ## 두번째 동전부터 숫자 업뎃
    for i in range(1, N):
        for j in range(1, goal+1):
            ## 🚨 DP[만들고 싶은 수 - 지금 동전 값]의 경우의 수로 업뎃
            if j-price[i] >= 0:
                DP[j]+= DP[j-price[i]]
    
    # print(DP)
    print(DP[-1])