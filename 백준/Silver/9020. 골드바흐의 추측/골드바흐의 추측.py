# 골드바흐의 추측
import sys
import math

n = int(sys.stdin.readline())
nums = [sys.stdin.readline().strip() for i in range(n)]
l = []

for j in range(2, 10000): 
        e = 0 
        ## 소수인지 확인
        for t in range(2, int(j ** 1/2)+1):
            if j % t == 0:  
                e += 1
        if e == 0:
            l.append(j)

for i in nums:
    ## 매 숫자마다 소수인지 판별 <-- 시간 초과
    ## 가장 차이가 작은 파티션 출력
    ## 중간값부터 비교
    middle = math.floor(int(i)/2)
    for s in range(middle, 0,  -1):
        if (s in l) and ((int(i) -s) in l):
            print(s, (int(i) -s))
            break

