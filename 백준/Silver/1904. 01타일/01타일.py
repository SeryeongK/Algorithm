# 01타일 - DP 탑다운
import sys

input = int(sys.stdin.readline())
table = [0 for _ in range(input+1)]
## 🚨 모든 경우를 구하는 것이 아니라 경우의 수를 구하는 것!
## 규칙을 알았으면 적용할 것 => 단순화 작업
for i in range(1, input + 1):
    if i == 1:
        table[i] = 1
    elif i == 2:
        table[i] = 2
    else:
        ## 🚨 메모리 초과 방지
        table[i] = (table[i-1] + table[i-2]) % 15746

print(table[-1])