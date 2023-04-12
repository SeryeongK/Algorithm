# 스티커
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    sticker = []
    N = int(sys.stdin.readline())
    sticker.append(list(map(int, sys.stdin.readline().split())))
    sticker.append(list(map(int, sys.stdin.readline().split())))
    ## 스티커 위치를 가로 -> 세로
    DP = [[0]*2 for _ in range(N)]

    ## N == 1일 때
    if N == 1:
        print(max(sticker[1][0], sticker[0][0]))
    ## N == 2일 때
    elif N == 2:
        DP[0][0] = sticker[1][0]
        DP[0][1] = sticker[0][0]
        DP[1][0] = DP[0][1] + sticker[1][1]
        DP[1][1] = DP[0][0] + sticker[0][1]
        print(max(DP[1]))
    else: 
        DP[0][0] = sticker[1][0]
        DP[0][1] = sticker[0][0]
        DP[1][0] = DP[0][1] + sticker[1][1]
        DP[1][1] = DP[0][0] + sticker[0][1]
        for i in range(2, N):
            ## 바로 앞 줄에서 스티커를 선택했을 때와 안 선택했을 때 중 최댓값
            DP[i][0] = max(DP[i-1][1] + sticker[1][i], max(DP[i-2][0], DP[i-2][1])+sticker[1][i])
            DP[i][1] = max(DP[i-1][0] + sticker[0][i], max(DP[i-2][0], DP[i-2][1])+sticker[0][i])
        print(max(DP[-1]))