# 별 찍기 - 12
import sys

n = int(sys.stdin.readline())

for i in range(1, n):
    print(" "*(n-i)+"*"*i)
print("*"*n)
for i in range(n-1, 0, -1):
    print(" "*(n-i)+"*"*i)