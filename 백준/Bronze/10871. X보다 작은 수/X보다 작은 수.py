import sys

standard = sys.stdin.readline().split()
n = int(standard[0])
x = int(standard[1])

input = sys.stdin.readline().split()
output = []
for i in range(n):
    if x > int(input[i]):
        output.append(input[i])

print(' '.join(output))