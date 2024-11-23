T = int(input())
input = [list(map(int, input().split())) for _ in range(T)]

for i in input:
    len = i[0]
    avg = (sum(i) - len) / len
    overAvg = 0
    for num in range(1, len + 1):
        if i[num] > avg:
            overAvg += 1
    print(format(round(overAvg / len * 100, 3), '.3f') + '%')  # format: 소수점 표시