import sys

n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]

for i in range(n):
    line = data[i].split()
    add = 0
    # 평균 구하기
    for i in range(1, int(line[0])+1):
        add += int(line[i])
    average = add / int(line[0])
    # 평균이랑 비교하기
    st = 0
    for i in range(1, int(line[0])+1):
        if int(line[i]) > average:
            st += 1
    p = st / int(line[0]) * 100
    print(f"{p:.3f}"+"%")