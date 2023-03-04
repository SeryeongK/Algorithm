# 팩토리얼
import sys

n = int(sys.stdin.readline())
output = 1

for i in range(2, n+1):
    output = output*i

print(output)