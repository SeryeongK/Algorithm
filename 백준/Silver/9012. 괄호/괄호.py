# 괄호
import sys

def push():
    global arr
    arr.append(0)

def pop():
    global arr
    arr = arr[:-1]

n = int(sys.stdin.readline().strip())
for _ in range(n):
    input = sys.stdin.readline().strip()
    arr = []
    result = 1
    for i in range(len(input)):
        if input[i] == "(":
            push()
        else:
            if len(arr) <= 0:
                print("NO")
                result = 0
                break
            else:
                pop()
    if result == 0:
        continue        
    elif len(arr) > 0:
        print("NO")
    else:
        print("YES")