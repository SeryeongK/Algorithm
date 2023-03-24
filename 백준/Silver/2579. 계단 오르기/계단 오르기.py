# 계단 오르기 - DP <== 좀이따 보자...
"""
앞에서부터 생각하지 말고
마지막 칸은 무조건 밟아야 하기 때문에 🚨 마지막 칸을 기준으로 생각하기
"""
import sys

N = int(sys.stdin.readline())
steps = [0]
for _ in range(N):
    steps.append(int(sys.stdin.readline()))
m = [0 for _ in range(N+1)]
for i in range(1, N+1):
    if i == 1:
        m[i] = steps[1]
    elif i == 2:
        m[i] = steps[1] + steps[2]
    elif i == 3:
        m[i] = max(steps[i-1]+steps[i], m[i-2]+steps[i])
    else:
        m[i] = max(m[i-3]+steps[i-1]+steps[i], m[i-2]+steps[i])
# print(m)
print(m[-1])