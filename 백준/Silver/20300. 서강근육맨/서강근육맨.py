import sys
N = int(sys.stdin.readline())
loss = list(map(int, sys.stdin.readline().split()))
loss.sort()
maxNum = 0
if len(loss) % 2 != 0:  # 홀수이면
    maxNum = loss[-1]  # 가장 큰 숫자는 한 번의 PT로 분리
    loss = loss[:-1]

for i in range(len(loss)//2):
    if loss[i] + loss[-(i+1)] > maxNum:
        maxNum = loss[i] + loss[-(i+1)]

print(maxNum)