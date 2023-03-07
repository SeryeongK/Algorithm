# 검증수
import sys

input = list(map(int, sys.stdin.readline().split()))

s = 0
for i in input:
    s += i**2

print(s % 10)