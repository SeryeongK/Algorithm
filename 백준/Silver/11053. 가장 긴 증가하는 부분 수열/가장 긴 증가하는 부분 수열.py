# 가장 긴 증가하는 부분 수열 - DP
# 🚨 단순히 큰 것만 찾아나가는 게 아님
import sys
N = int(sys.stdin.readline()) # 수열의 크기
S = list(map(int, sys.stdin.readline().split())) # 수열

DP = [0 for _ in range(N)]
for i in range(N):
    now = S[i] ## 비교하고자 하는 값
    ## 비교하고자 하는 값보다 작은 값만 저장하기 위해서(중복 X)
    count = set()
    for j in range(0, i):
        if now > S[j]:
            ## 🚨 가장 긴 수열에 더하기 위해
            count.add((DP[j], S[j], j))
    # print(count)
    if len(count) > 0:
        DP[i] = max(count)[0]+1

# print(DP)
print(max(DP)+1)