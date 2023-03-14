# 요세푸스 문제0 - 큐
import sys
import collections
N, K = map(int, sys.stdin.readline().split())
## 덱에 추가
input = collections.deque([])
for i in range(1, N+1):
    input.append(i)

output = []
while len(input) > 0:
    ## 제거될 사람 앞 사람까지 뒷 순서로 보내기
    for _ in range(K-1):
        popped_left = input.popleft()
        input.append(popped_left)
    ## 제거된 사람
    removed = input.popleft()
    output.append(str(removed))

print("<"+", ".join(output)+">")