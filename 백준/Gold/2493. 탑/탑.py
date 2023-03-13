# 탑 - 스택
import sys
n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
stk = [[tower[0], 1]]
## 미리 배열의 크기 지정
output = [0]*n

for i in range(1, n):
    while stk:
        ## 현재 비교하고 있는 탑의 높이가 스택의 top보다 클 경우
        if stk[-1][0] < tower[i]:
            stk.pop() ## 스택의 top 제거
        else:
            output[i] = stk[-1][1]
            ## 🚨 현재 비교하고 있는 탑의 높이가 스택의 top보다 작아질 때까지 비교한 후
            ## 작아지면 스택의 top을 추가한 후 break
            break
    stk.append([tower[i], i+1])
    
print(' '.join(str(i) for i in output))