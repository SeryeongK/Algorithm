# 단어 정렬
import sys

n = int(sys.stdin.readline())
## 🚨 중복된 단어 제거
input = list(set(sys.stdin.readline().strip() for _ in range(n)))
ls = []

for i in range(len(input)):
    temp = [input[i],len(input[i])]
    ls.append(temp)

## 🚨 리스트를 정렬하는 방법 ==> sorted(arr, key=lambda x: 정렬기준)
output = sorted(ls, key=lambda x: (x[1], x[0]))

for i in range(len(input)):
    print(output[i][0])