input = [int(input()) for _ in range(9)]

max = 0
maxIdx = 0

for i in range(9):
    if input[i] > max:
        max = input[i]
        maxIdx = i

print(max)
print(maxIdx + 1)