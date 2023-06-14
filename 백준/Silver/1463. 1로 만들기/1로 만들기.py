# 1로 만들기
# 원하는 정수까지의 DP 즉, 연산의 최솟값을 저장
import sys
N = int(sys.stdin.readline())

DP = [0] * (N+1)
if N == 1:
    print(0)
else:
    for i in range(2, N+1):
        # -1 연산을 기본으로 둔다.
        DP[i] = DP[i-1] + 1

        # 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            DP[i] = min(DP[i], DP[i//2] + 1)

        # 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            DP[i] = min(DP[i], DP[i//3] + 1)

    print(DP[-1])
