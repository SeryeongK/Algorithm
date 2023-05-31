# 회의실 배정 - 그리디

# 회의 길이 기준 => 겹치는 것까지 고려해야 함 => 첫번째 회의만 잘 정하면 됨
# 첫번째 회의 => 빨리 끝나는 회의가 결국 짧은 회의

import sys
N = int(sys.stdin.readline())
meetings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

# 첫번째 회의: 가장 빨리 끝나는 회의
table = []
table.append(meetings[0])
if N > 1:
    for i in range(1, N):
        if meetings[i][0] >= table[-1][1]:
            table.append(meetings[i])

print(len(table))