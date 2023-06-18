import sys

N = int(sys.stdin.readline())

numbers = list(range(1, N+1))
index = 0  # numbers 리스트를 추적하는 인덱스
stack = []
result = []  # +와 -를 저장할 리스트

for _ in range(N):
    input = int(sys.stdin.readline())
    # 인덱스가 N을 넘지 않고 input보다 작거나 같을 때
    while index < N and numbers[index] <= input:
        stack.append(numbers[index])
        result.append("+")
        index += 1

    # input이 pop될 수 있는 상황일 때
    if stack and stack[-1] == input:
        stack.pop()
        result.append("-")
    # input이 pop될 수 없는 상황일 떄
    else:
        print("NO")
        exit()

# 결과 출력
for op in result:
    print(op)
