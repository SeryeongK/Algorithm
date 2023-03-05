# 수 정렬하기3 (메모리 제한 8MB)
import sys

n = int(sys.stdin.readline())

ls = [0] * 10001
for _ in range(n):
    ls[int(sys.stdin.readline())] += 1
for i in range(10001):
    for n in range(ls[i]):
        print(i)