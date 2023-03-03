import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

num = a * b * c
for n in range(10):
    count = 0
    for i in range(len(str(num))):
        if str(n) == str(num)[i]:
            count += 1
    print(count)