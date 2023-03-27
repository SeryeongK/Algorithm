# LCS - DP
import sys

A = [0] + list(sys.stdin.readline().strip())
B = [0] + list(sys.stdin.readline().strip())

DP = [[0 for _ in range(len(A))] for _ in range(len(B))]

for i in range(1, len(B)):
    row = DP[i]
    before = DP[i-1]
    for j in range(1, len(A)):
        # print(f"i: {i}, j: {j}")
        if B[i] == A[j]: ## 가장 마지막이 같을 때
            row[j] = before[j-1] + 1
        else: ## 가장 마지막이 다를 때
            row[j] = max(before[j], row[j-1])

print(DP[-1][-1])