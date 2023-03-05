# 수 정렬하기
import sys

n = int(sys.stdin.readline())
input = [int(sys.stdin.readline().strip()) for _ in range(n)]

input.sort()
for i in input:
    print(i)