# 가장 긴 바이토닉 부분 수열
import sys
N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
DPUP = [1] * N
DPDOWN = [1] * N

## 오름차순 부분 수열
for i in range(N):
    now = seq[i]
    M = 0
    for j in range(i):
        if now > seq[j]:
            if M <= DPUP[j]:
                M = DPUP[j]
    DPUP[i] += M

## 내림차순 부분 수열
for i in range(N-1, -1, -1):
    now = seq[i]
    M = 0
    for j in range(N-1, i-1, -1):
        if now > seq[j]:
            if M <= DPDOWN[j]:
                M = DPDOWN[j]
    DPDOWN[i] += M

output = 0
for i in range(N):
    ADD = DPUP[i]+DPDOWN[i]
    if output < ADD:
        output = ADD

print(output-1)