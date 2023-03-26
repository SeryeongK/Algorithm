# 평범한 배낭
import sys
N, K = map(int, sys.stdin.readline().split())
bags = []
for _ in range(N):
    bags.append(list(map(int, sys.stdin.readline().split())))

# print(bags)
table = [[0 for _ in range(K+1)] for _ in range(N)]

## 첫번째 줄 세팅
for i in range(1, K+1):
    if i < bags[0][0]:
        table[0][i] = 0
    else:
        table[0][i] = bags[0][1]

for i in range(1, N):
    row = table[i]
    before = table[i-1]
    for j in range(1, K+1):
        if j < bags[i][0]:
            row[j] = before[j]
        else: ## 블로그 코드 참고
            ## 🚨 한 행씩 진행되므로 바로 위의 값들이 해당 무게에서 담을 수 있는 최댓값!!
            row[j] = max(before[j], bags[i][1]+ table[i-1][j-bags[i][0]])

# for i in table:
#     print(i)

print(table[-1][-1])