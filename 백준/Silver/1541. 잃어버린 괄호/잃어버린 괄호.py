# 잃어버린 괄호
import sys
# -를 기준으로 분리
input = sys.stdin.readline().strip().split("-")
output = []
for i in input:
    # +를 기준으로 분리(0으로 시작하는 숫자 처리)
    temp = i.split("+")
    add = 0
    for i in temp:
        add += int(i)
    output.append(add)

# -를 기준으로 분리된 숫자 더하기
answer = output[0]
for i in range(1, len(output)):
    answer -= output[i]

print(answer)
