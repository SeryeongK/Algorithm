# 가장 큰 증가하는 부분 수열
import sys

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
## 🚨 그냥 DP = seq를 할 경우에는 메모리 주소값을 복사한 것 => 값이 같이 변경됨
## 해결 방법: 슬라이싱, list(), copy() 등
DP = seq[:]
for i in range(1, N):
    M = 0
    for j in range(i):
        if seq[i] > seq[j]:
            if DP[j] >= M:
                M = DP[j]
    DP[i] += M
print(max(DP))