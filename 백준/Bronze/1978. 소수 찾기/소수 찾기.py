nums = [input() for _ in range(2)][1]

primeCnt = 0
for i in nums.split():
    i = int(i)

    if i == 1:
        continue
    elif i == 2:
        primeCnt += 1
        continue
    else:
        isPrime = True
        for j in range(2, int(i)):
            if int(i) % j == 0:
                isPrime = False
        if isPrime:
            primeCnt += 1

print(primeCnt)