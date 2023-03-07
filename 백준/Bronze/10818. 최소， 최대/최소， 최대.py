# 최소, 최대
import sys

n = int(sys.stdin.readline())
input = list(map(int, sys.stdin.readline().split()))
input = sorted(input)

print(input[0], input[-1], end=" ")