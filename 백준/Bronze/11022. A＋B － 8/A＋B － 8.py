# A+B - 8
import sys

n = int(sys.stdin.readline())
input = [sys.stdin.readline().strip().split() for _ in range(n)]

for i in range(n):
    print(f"Case #{i+1}: {int(input[i][0])} + {int(input[i][1])} = {int(input[i][0])+int(input[i][1])}")