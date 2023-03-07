# 2007년
import sys

days = [[1, 31], [2, 28], [3, 31], [4, 30], [5, 31], [6, 30], [7, 31], [8, 31], [9, 30], [10, 31], [11, 30], [12, 31]]
input = list(map(int, sys.stdin.readline().split()))
days = days[:input[0]]

## 며칠 남았는지 구하기
sum = 0
for i in range(len(days)-1):
    sum += days[i][1]
sum += input[1]-1

## 요일 구하기
d = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
print(d[sum % 7])