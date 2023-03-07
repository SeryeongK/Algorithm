# 평균
import sys

n = int(sys.stdin.readline())
input = list(map(int, sys.stdin.readline().split()))

m = max(input)
score = []
for i in input:
    score.append(i/m*100)

print(sum(score)/n)