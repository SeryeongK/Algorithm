# 막대기
import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    input = int(sys.stdin.readline())
    arr.append(input)
stk = [arr[-1]]
arr = arr[:-1]

for i in range(len(arr)-1, -1, -1):
    if arr[i] > stk[-1]:
        stk.append(arr[i])

print(len(stk))