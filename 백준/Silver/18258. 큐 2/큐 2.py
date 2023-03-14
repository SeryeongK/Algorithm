# 큐 2
import sys
import collections

queue = collections.deque([])

def push(x):
    global queue
    queue.append(x)

def pop():
    global queue
    if len(queue) > 0:
        print(queue[0])
        ## 🚨 deque를 사용하지 않을 경우 시간초과
        queue.popleft()
    else:
        print(-1)

def size():
    global queue
    print(len(queue))

def empty():
    global queue
    if len(queue) > 0:
        print(0)
    else:
        print(1)

def front():
    if len(queue) > 0:
        print(queue[0])
    else:
        print(-1)

def back():
    if len(queue) > 0:
        print(queue[-1])
    else:
        print(-1)

n = int(sys.stdin.readline())
for _ in range(n):
    input = sys.stdin.readline().split()
    if input[0] == 'push':
        push(input[1])
    elif input[0] == 'pop':
        pop()
    elif input[0] == 'size':
        size()
    elif input[0] == 'empty':
        empty()
    elif input[0] == 'front':
        front()
    elif input[0] == 'back':
        back()