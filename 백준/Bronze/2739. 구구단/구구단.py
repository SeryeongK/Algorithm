import sys

input = int(sys.stdin.readline())

def nums(num):
    for i in range(1, 10):
        print(num,"*", i, "=", num * i)

nums(input)