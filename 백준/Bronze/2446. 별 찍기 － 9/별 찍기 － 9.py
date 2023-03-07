# 별 찍기 - 9
import sys

n = int(sys.stdin.readline())

for i in range(n-1, 0, -1):
    print(" "*(n-i-1)+"*"+"*"*2*i)
print(" "*(n-1)+"*")
for i in range(1, n):
    print(" "*(n-i-1)+"*"+"*"*2*i)