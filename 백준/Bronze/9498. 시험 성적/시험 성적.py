import sys

input = int(sys.stdin.readline())

def score(s):
    if s >= 90:
        print("A")
    elif s >= 80:
        print("B")
    elif s >= 70:
        print("C")
    elif s >= 60:
        print("D")
    else:
        print("F")

score(input)