# 별 찍기 - 17
import sys

n = int(sys.stdin.readline())

for i in range(1, n):
    if i == 1:
        print(" "*(n-i)+"*")
    else:
        print(" "*(n-i)+"*"+" "+" "*(i-2)*2+"*")
print("*"*(n-1)*2+"*")