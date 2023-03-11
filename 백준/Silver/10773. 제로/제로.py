# 제로
import sys

stk = []

def push(x):
    global stk
    stk.append(x)

def pop():
    global stk
    stk = stk[:-1]

k = int(sys.stdin.readline())
for _ in range(k):
    input = int(sys.stdin.readline())
    if input == 0:
        pop()
    else:
        push(input)

print(sum(stk))