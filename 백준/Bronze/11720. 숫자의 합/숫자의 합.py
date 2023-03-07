# 숫자의 합
import sys

n = int(sys.stdin.readline())
input = sys.stdin.readline()
output = 0
for i in range(n):
    output += int(input[i])

print(output)