# 단어 공부
import sys

input = sys.stdin.readline().strip().upper()
input2 = list(set(input))
ls = []
for i in input2:
    if i in ls:
        continue
    ls.append([i, input.count(i)])

ls = sorted(ls, key=lambda x: x[1])

if len(ls) == 1:
    print(ls[-1][0])
elif ls[-1][1] != ls[-2][1]:
    print(ls[-1][0])
else:
    print("?")