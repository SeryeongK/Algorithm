# 한수
import sys
import math

n = int(sys.stdin.readline())

count = 0
## 한수인지 아닌지 판별
## 🚨 마지막 수까지 확인을 해야 하므로 range(n+1)
for j in range(1, n+1):
    j = str(j)
    if len(j) == 1 or (len(j) ==2):
        count += 1
    else:
        if (int(j[1]) - int(j[0]) == int(j[2]) - int(j[1])):
            count += 1

print(count)