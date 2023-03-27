# 회의실 배정
"""
아이디어 블로그 참고
끝나는 시간을 기준으로 정렬, 가장 빠르게 끝나는 회의를 잡음
그 회의 시간에 맞게 다음 회의 잡기
"""
import sys

N = int(sys.stdin.readline())
meetings = []
for _ in range(N):
    meetings.append(list(map(int, sys.stdin.readline().split())))

## 시작 시간에 대해서도 정렬
## 시작 시간과 끝 시간이 같은 회의가 먼저 들어왔을 때 다른 회의를 못 잡게 되는 경우 방지
meetings.sort()
meetings.sort(key=lambda x:x[1])

timetable = [meetings[0]]
for i in range(1, len(meetings)):
    now = meetings[i]
    if timetable[-1][1] <= now[0]:
        timetable.append(meetings[i])

print(len(timetable))