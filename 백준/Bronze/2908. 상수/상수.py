import sys

input = sys.stdin.readline().split()
new = []

for i in input:
    num = i[2]+i[1]+i[0]
    new.append(num)

new.sort()
print(new[-1])