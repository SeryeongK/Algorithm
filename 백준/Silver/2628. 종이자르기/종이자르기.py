# 종이 자르기
import sys

paper = sys.stdin.readline().split()
num = int(sys.stdin.readline())
input =[sys.stdin.readline().strip() for _ in range(num)]

w =[0]
w.append(int(paper[1]))
h = [0]
h.append(int(paper[0]))

ww =[]
hh =[]

## 가로, 세로 넣고 정렬
for i in input:
    l = i.split()
    if l[0] == '0':
        w.append(int(l[1]))
    else:
        h.append(int(l[1]))

w.sort()
h.sort()

## 길이 넣기
for i in range(1, len(w)):
    ww.append(w[i] - w[i-1])


for i in range(1, len(h)):
    hh.append(h[i] - h[i-1])


wm = max(ww)
hm = max(hh)
print(wm*hm)