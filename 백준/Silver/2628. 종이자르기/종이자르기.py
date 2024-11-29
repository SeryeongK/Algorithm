a, b = map(int, input().split())
x = [0, a]
y = [0, b]
n = int(input())
input = [input() for _ in range(n)]

# 가로 세로 선 추가
for i in input:
    a, b = map(int, i.split())
    if a == 0:
        y.append(b)
    else:
        x.append(b)

x.sort()
y.sort()

# 가장 차이가 많이 나는 가로 세로 길이
maxX = 0
maxY = 0
for i in range(1, len(x)):
    gapX = x[i]-x[i-1]
    if gapX > maxX:
        maxX = gapX

for i in range(1, len(y)):
    gapY = y[i]-y[i-1]
    if gapY > maxY:
        maxY = gapY

print(maxX * maxY)