# 카드 놓기
import sys
import itertools

n = int(sys.stdin.readline())
r = int(sys.stdin.readline())
nums =[sys.stdin.readline().strip() for _ in range(n)]

output = set()

## 🚨 순열을 계산해주는 함수
for i in list(itertools.permutations(nums, r)):
    output.add("".join(i))

print(len(output))