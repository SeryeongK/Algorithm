# 문자열 폭발 - 스택
import sys

input = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

stk = []
for i in range(len(input)):
    ## 🚨 일단 스택에 넣기
    stk.append(input[i])
    # print(f"{stk[-1]} {''.join(stk[-len(bomb):])}")
    ## 🚨 bomb이 들어갈 길이도 안 된다면
    if len(stk) < len(bomb):
        pass
    ## 🚨 bomb이 있다면
    elif stk[-1] == bomb[-1] and ''.join(stk[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            ## stk에서 제거
            stk.pop()

output = ''.join(stk)
if len(output) == 0:
    print("FRULA")
else:
    print(output)

# ❗️ 스택이면 pop을 잘 이용해보자!!

######################### 시간 초과 #########################
"""
while bomb in input: ## 문자열 안에 폭발 문자열이 있을 때
    input = input.replace(bomb, '') ## 폭발 문자열 제거

if len(input) == 0:
    print("FRULA")
else:
    print(input)
"""