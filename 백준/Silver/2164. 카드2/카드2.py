# 카드2 - 큐
import sys
import collections

n = int(sys.stdin.readline())
input = collections.deque([])
for i in range(1, n+1):
    input.append(i)

while len(input) > 1:
    input.popleft()
    top = input[0]
    input.popleft()
    input.append(top)

print(input[0])