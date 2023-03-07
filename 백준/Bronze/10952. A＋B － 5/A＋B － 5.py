# A+B - 5
import sys

while True:
    input = sys.stdin.readline().split()
    if int(input[0]) != 0 and int(input[1]) != 0:
        print(int(input[0])+int(input[1]))
    else:
        break