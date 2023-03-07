# 별 찍기 - 8
import sys

n = int(sys.stdin.readline())

for i in range(1, n):
    print("*"*i+" "*(n*2-i*2)+"*"*i)
print("*"*n*2)
for i in range(n-1, 0, -1):
    print("*"*i+" "*(n*2-i*2)+"*"*i)