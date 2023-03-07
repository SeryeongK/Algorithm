# 나머지
import sys

input = [int(sys.stdin.readline()) for _ in range(10)]

left = []
for i in input:
    left.append(i % 42)

left = list(set(left))
print(len(left))