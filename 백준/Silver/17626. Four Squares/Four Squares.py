# 17626 Four Squares
import sys

num = int(sys.stdin.readline())
DP = [0] * (num + 1)

i = 1
while i**2 <= num:
    DP[i**2] = 1  # 제곱수는 개수가 1개
    i += 1

for i in range(1, num + 1):
    if DP[i] != 0:  # 제곱수이면 패스(어차피 최소이기 때문에)
        continue

    j = 1
    while j*j <= i:  # 아직 개수를 안 셌을 때
        if DP[i] == 0:
            DP[i] = DP[i - j*j] + DP[j*j]  # 제곱수 개수 합치기
        else:
            DP[i] = min(DP[i], DP[i - j*j] + DP[j*j])  # 최소인 제곱수 개수로 업데이트
        j += 1

print(DP[-1])
