# 피보나치 수 2
import sys

""" 재귀(점화식) f(k) = f(k-1) + f(k-1)
def fibonacci(k):
    if k == 1 or k == 2:
        return 1
    return fibonacci(k-1) + fibonacci(k-2)

print(fibonacci(int(sys.stdin.readline())))
"""

# DP - 이전 계산 내용을 저장
input = int(sys.stdin.readline())

table = [0 for _ in range(input+1)]
for i in range(input+1):
    if i == 1 or i == 2:
        table[i] = 1
    else:
        table[i] = table[i-1] + table[i-2]

print(table[-1])