# 문자열 폭발 - 스택
import sys
input = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

stk = []

for i in range(len(input)):
    stk.append(input[i])
    # print(stk[-1],bomb[-1], "|", ''.join(stk[-len(bomb):]), bomb)
    ## 폭발 문자열 길이가 안 된다면 pass
    if len(stk) < len(bomb):
        pass
    ## 폭발 문자열의 가장 뒷부분이 일치하고, 문자열이 일치하면 pop
    elif stk[-1] == bomb[-1] and ''.join(stk[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            stk.pop()

if len(stk) > 0:
    print(''.join(stk))
else:
    print("FRULA")