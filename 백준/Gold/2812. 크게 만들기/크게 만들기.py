# 크게 만들기 - 스택
import sys
n, k = map(int, sys.stdin.readline().split())
input = sys.stdin.readline()

stk = [input[0]]
cnt = 0
for i in range(1, n):
    ## k만큼 숫자를 다 지울 때까지
    while k > cnt:
        if stk and stk[-1] < input[i]:
            ## 숫자 지우기
            stk.pop()
            cnt += 1
        else:
            break
    stk.append(input[i])

## 마지막 항목이나 마지막에 같은 숫자가 반복될 경우 제거
for _ in range(k-cnt):
    stk.pop()

print("".join(stk))