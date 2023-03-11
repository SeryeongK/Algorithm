# 스택
import sys

arr = []
ptr = 0

def push(x):
    global arr, ptr
    arr += [x]
    ptr += 1

def pop():
    global arr
    if len(arr) > 0:
        p = arr[-1]
        arr = arr[:-1]
        return p
    else:
        return -1

def size():
    global arr
    return len(arr)

def empty():
    global arr
    if len(arr) > 0:
        return 0
    else:
        return 1

def top():
    global arr
    if len(arr) > 0:
        return arr[-1]
    else:
        return -1
    
n = int(sys.stdin.readline())
for _ in range(n):
    input = sys.stdin.readline().split()
    if input[0] == 'push':
        push(int(input[1]))
    elif input[0] == 'pop':
        print(pop())
    elif input[0] == 'size':
        print(size())
    elif input[0] == 'empty':
        print(empty())
    else:
        print(top())