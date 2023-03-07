# A+B - 6
import sys

n = int(sys.stdin.readline())
input = [sys.stdin.readline().strip().split(",") for _ in range(n)]

for i in input:
    print(int(i[0])+int(i[1]))