# 프린터큐 - 큐
import sys

test = int(sys.stdin.readline())
for _ in range(test):
    q = []
    N, M = map(int, sys.stdin.readline().split())
    input = list(map(int, sys.stdin.readline().split()))
    count = 0
    for i in range(len(input)):
        if i == M:
            input[i] = (input[i], 1)
        else:
            input[i] = (input[i], 0)

    while input:
        ## 🚨 max(arr, key=lambda x:x[0]): x[0]을 기준으로 max
        if input[0] == max(input, key=lambda x:x[0]):
            count += 1
            if input[0][1] == 1:
                print(count)
                break
            input = input[1:]
        else:
            top = input[0]
            input = input[1:]+[top]