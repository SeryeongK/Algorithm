input = [int(input()) for _ in range(3)]

num = list(str(input[0] * input[1] * input[2]))  # list로 한글자씩 쪼개기
numCnt = dict()
# 숫자 채우기
for i in range(10):
    i = str(i)
    if i not in numCnt:
        numCnt[i] = 0

# 해당하는 숫자 카운트
for i in num:
    if i in numCnt:
        numCnt[i] += 1

for i in numCnt.values():
    print(i)