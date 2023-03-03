import sys

data = []

for i in range(9):
    data.append(int(sys.stdin.readline().strip()))

new = data.copy()
new.sort()
l = new[-1]

print(l)
print(data.index(l)+1)