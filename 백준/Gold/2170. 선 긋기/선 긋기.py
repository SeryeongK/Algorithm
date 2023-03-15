# 선 긋기 - 스위핑
import sys

N = int(sys.stdin.readline())
input = []
for _ in range(N):
    input.append(list(map(int, sys.stdin.readline().split())))

input = sorted(input, key=lambda x:x[0])

length = 0 ## 구하고자 하는 그은 선의 총 길이
start = input[0][0] ## 시작점
end = input[0][1] ## 끝점

for i in range(1, N):
    ## 새 출발(이전 끝점보다 현재 시작점이 더 오른쪽에 있을 때)
    # print(input[i], "start:", start, "end:", end, "length:", length)
    if end < input[i][0]:
        length += (end - start)
        start = input[i][0]
    ## 길이 연장
    if end < input[i][1]:
        end = input[i][1]

## 🚨 마지막에 처리되지 못한 길이
length += (end-start)
print(length)   

## - ❗️ 마지막 길이 처리
## - ❗️ 다음 선이 이전 선에 포함될 경우
## - ❗️ 시작점과 끝점(음수로 시작할 경우)