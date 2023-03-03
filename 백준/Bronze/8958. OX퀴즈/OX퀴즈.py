import sys

n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
score = 0 
count = 0
output = []

for i in range(n):
    line = data[i]
    for i in range(len(line)):
        if line[i] == "O":
            count += 1
            score += count
        else:
            count = 0
            score += count

    output.append(score)
    count = 0
    score = 0

for i in range(n):
    print(output[i])